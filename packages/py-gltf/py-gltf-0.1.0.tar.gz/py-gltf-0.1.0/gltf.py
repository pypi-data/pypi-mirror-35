import base64
import imghdr
import shutil
import json
import os
import logging
import math
import copy
from enum import Enum
from uuid import uuid4
from io import BytesIO

import numpy as np
from PIL import Image as PImage
from pyquaternion import Quaternion

logger = logging.getLogger(__name__)


def binary_to_uri(b, mime_type='application/octet-stream'):
    return 'data:{};base64,{}'.format(mime_type, base64.b64encode(b).decode('utf-8'))


def load_uri(s, folder=None):
    if s.startswith('data:'):
        return base64.b64decode(s[s.index(',') + 1:])

    if folder:
        s = os.path.join(folder, s)
    with open(s, 'rb') as f:
        return f.read()


class BaseGLTFStructure:
    name = None

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False

        # self_data = self.__dict__.copy()
        # self_data.pop('name', None)
        # other_data = other.__dict__.copy()
        # other_data.pop('name', None)
        # return self_data == other_data
        return self.__dict__ == other.__dict__

    # def __hash__(self):
    #     self_data = self.__dict__.copy()
    #     self_data.pop('name', None)
    #     return hash(frozenset(self_data.items()))


class BufferView:
    class BufferTarget(Enum):
        ARRAY_BUFFER = 34962
        ELEMENT_ARRAY_BUFFER = 34963

    target = None
    name = None
    offset = 0
    component_size = 4

    def __init__(self, buffer_view=None, gltf=None,
                 target=None, byte_stride=None, component_size=None, buffer=None):
        if target:
            self.target = self.BufferTarget(target)
        self.byte_stride = byte_stride
        self.component_size = component_size
        self.data = bytearray()
        self.buffer = buffer
        if buffer_view:
            self.name = buffer_view.get('name')
            self.buffer = gltf.buffers[buffer_view['buffer']]
            offset = buffer_view.get('byteOffset', 0)
            self.data = self.buffer.data[offset:offset + buffer_view['byteLength']]

    def __repr__(self):
        return self.name or super().__repr__()

    @property
    def byte_length(self):
        return len(self.data)

    def write(self, data):
        offset = self.byte_length
        self.data += data
        return offset

    def write_to_buffer(self):
        self.offset = self.buffer.write(self.data, alignment=self.component_size)

    def render(self, gltf):
        buffer_view = {
            'buffer': gltf.index('buffers', self.buffer),
            'byteLength': self.byte_length,
        }
        if self.offset:
            buffer_view['byteOffset'] = self.offset
        if self.name:
            buffer_view['name'] = self.name
        if self.target:
            buffer_view['target'] = self.target.value
        if self.byte_stride:
            buffer_view['byteStride'] = self.byte_stride
        return buffer_view


class Buffer:
    name = None

    def __init__(self, buffer=None, gltf=None):
        self.buffer_views = {}
        self.data = bytearray()

        if buffer:
            self.name = buffer.get('name')
            if 'data' in buffer:
                self.data = bytearray(buffer['data'])
            else:
                self.data = load_uri(buffer['uri'], folder=gltf.folder)
            if self.byte_length != buffer['byteLength']:
                raise ValueError('Buffer length does not match')

    def __repr__(self):
        return self.name or super().__repr__()

    @property
    def byte_length(self):
        return len(self.data)

    def write(self, data, alignment=None):
        offset = self.byte_length
        if alignment and offset % alignment:
            self.data += bytes([0x00] * (alignment - offset % alignment))
            offset = self.byte_length
        self.data += data
        return offset

    def render(self):
        buffer = {
            'data': self.data,
            'byteLength': self.byte_length
        }
        if self.name:
            buffer['name'] = self.name
        return buffer

    def get_view(self, target=None, byte_stride=None, component_size=None, image=None):
        view_type = image or (target, byte_stride, component_size)
        if view_type not in self.buffer_views:
            self.buffer_views[view_type] = BufferView(target=target,
                                                      byte_stride=byte_stride,
                                                      component_size=component_size,
                                                      buffer=self)
        return self.buffer_views[view_type]


class Accessor(BaseGLTFStructure):
    class ComponentType(Enum):
        int8 = 5120
        uint8 = 5121
        int16 = 5122
        uint16 = 5123
        uint32 = 5125
        float32 = 5126

    _valid_component_types = list(ComponentType)
    _data = None
    component_type = None
    type = str()
    target = BufferView.BufferTarget.ARRAY_BUFFER
    byte_stride = None
    size = 1

    def __init__(self, data=None, gltf=None):
        if type(data) is dict:
            self.name = data.get('name')
            component_type = data.get('componentType')
            if component_type is not None:
                self.component_type = self.ComponentType(component_type)
            else:
                logger.warning('Accessor has no component type')

            buffer_view = data.get('bufferView')
            if buffer_view is not None:
                bv = gltf.buffer_views[buffer_view]
            else:
                logger.warning('Accessor has no buffer view')
                return

            arr = np.frombuffer(bv.data,
                                dtype=self.component_type.name,
                                count=data['count'] * self.size,
                                offset=data.get('byteOffset', 0))
            if self.size != 1:
                arr = arr.reshape(len(arr) // self.size, self.size)
            self.data = arr

            if data['count'] != self.count:
                raise ValueError('Accessor count does not match! Expected {}, got {}'
                                 ''.format(data['count'], self.count))

            if 'min' in data and not all(
                    math.isclose(a, b, rel_tol=1e-07)
                    for a, b in zip(data['min'], self.min)):
                logger.warning('Accessor minimum did not match! Expected {}, got {}'
                               ''.format(data['min'], self.min))

            if 'max' in data and not all(
                    math.isclose(a, b, rel_tol=1e-07)
                    for a, b in zip(data['max'], self.max)):
                logger.warning('Accessor maximum did not match! Expected {}, got {}'
                               ''.format(data['max'], self.max))
        else:
            self.data = [] if data is None else data

    def __repr__(self):
        return self.name or super().__repr__()

    def __eq__(self, other):
        if not ((isinstance(other, type(self))
                and (self.component_type, self.type, self.target, self.byte_stride, self.size, self.name) ==
                (other.component_type, other.type, other.target, other.byte_stride, other.size, other.name))):
            return False

        return np.array_equal(self._data, other._data)

    def check_component_type(self, dtype):
        if self.ComponentType[dtype] not in self._valid_component_types:
            raise TypeError(dtype + ' is an invalid data type for accessor of type ' + self.type)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if isinstance(data, np.ndarray):
            self.check_component_type(str(data.dtype))
            self._data = data.copy()
        else:
            self._data = np.array(data, dtype=self.component_type.name)

    def render(self, buffer, gltf):
        view = buffer.get_view(self.target, self.byte_stride, self.data.itemsize)
        offset = view.write(self.data.tobytes())
        acc = {
            'componentType': self.component_type.value,
            'type': self.type,
            'count': self.count,
            'min': self.min,
            'max': self.max,
            'bufferView': gltf.index('buffer_views', view),
        }
        if self.name:
            acc['name'] = self.name
        if offset:
            acc['byteOffset'] = offset
        return acc

    @property
    def min(self):
        return np.min(self.data, axis=0).tolist()

    @property
    def max(self):
        return np.max(self.data, axis=0).tolist()

    @property
    def count(self):
        return len(self.data)


class ScalarArray(Accessor):
    type = 'SCALAR'
    component_type = Accessor.ComponentType.uint16
    target = BufferView.BufferTarget.ELEMENT_ARRAY_BUFFER
    _valid_component_types = [
        Accessor.ComponentType.uint8,
        Accessor.ComponentType.uint16,
        Accessor.ComponentType.uint32,
        Accessor.ComponentType.float32,
    ]

    @property
    def min(self):
        return [int(np.min(self.data))]

    @property
    def max(self):
        return [int(np.max(self.data))]

    @property
    def count(self):
        return self.data.size


class Vec2Array(Accessor):
    type = 'VEC2'
    size = 2
    byte_stride = size * 4
    component_type = Accessor.ComponentType.float32
    _valid_component_types = [Accessor.ComponentType.float32]


class Vec3Array(Accessor):
    type = 'VEC3'
    size = 3
    byte_stride = size * 4
    component_type = Accessor.ComponentType.float32
    _valid_component_types = [Accessor.ComponentType.float32]


class Vec4Array(Accessor):
    type = 'VEC4'
    size = 4
    component_type = Accessor.ComponentType.float32
    _valid_component_types = [
        Accessor.ComponentType.uint8,
        Accessor.ComponentType.uint16,
        Accessor.ComponentType.float32,
    ]

    @property
    def byte_stride(self):
        if self.component_type == Accessor.ComponentType.float32:
            return self.size * 4
        if self.component_type == Accessor.ComponentType.uint16:
            return self.size * 2
        return self.size


class Mat4Array(Accessor):
    type = 'MAT4'
    size = 16
    byte_stride = size * 4
    component_type = Accessor.ComponentType.float32
    _valid_component_types = [Accessor.ComponentType.float32]


class Image:
    name = ''
    _data = None
    mime_type = None
    gltf = None

    def __init__(self, image, gltf=None):
        if gltf:
            self.gltf = gltf

        if type(image) == dict:
            self.name = image.get('name', '')
            try:
                if 'bufferView' in image:
                    bv = gltf.buffer_views[image['bufferView']]
                    self.data = bv.data
                else:
                    self.data = image['uri']
            except KeyError:
                logger.warning('Image has no bufferView or uri')
        else:
            self.data = image

    def __repr__(self):
        return self.name or super().__repr__()

    def __eq__(self, other):
        if not isinstance(other, type(self)) or self.is_uri != other.is_uri:
            return False
        return self.data == other.data

    def __hash__(self):
        return hash(self.path or id(self))

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        mime_type = None
        if type(data) is str:
            if data.startswith('data:'):
                data = load_uri(data)
            else:
                data = data.replace('\\', '/')
                if os.path.isabs(data):
                    logger.warning('Image uri is an absolute path: ' + data)
                path = (os.path.join(self.gltf.folder, data)
                        if self.gltf and self.gltf.folder
                        else data)
                if os.path.exists(path):
                    mime_type = imghdr.what(path)
                else:
                    logger.warning('Image uri does not exist: ' + path)

        # Check type again in case a data uri was loaded above
        if type(data) is not str:
            mime_type = imghdr.what(None, data)

        if not mime_type:
            raise TypeError('Image format not recognized')
        self._data = data
        self.mime_type = 'image/' + mime_type

    @property
    def is_uri(self):
        return type(self._data) is str

    @property
    def path(self):
        if not self.is_uri:
            return
        if self.gltf and self.gltf.folder:
            return os.path.join(self.gltf.folder, self.data)
        return self.data

    def get_fp(self):
        if self.is_uri:
            with open(self.path, 'rb') as f:
                return BytesIO(f.read())

        return BytesIO(self.data)

    def write_to(self, path):
        if self.is_uri:
            filename = self.data.split('/')[-1]
            shutil.copy(self.path, os.path.join(path, filename))
            return filename

        filename = self.name or str(uuid4())[:8]
        if '.' not in filename:
            filename += '.'
            if self.mime_type == 'image/jpeg':
                filename += 'jpg'
            else:
                filename += self.mime_type.split('/')[-1]

        with open(os.path.join(path, filename), 'wb') as f:
            f.write(self.data)

        return filename

    def render(self, buffer, gltf, embed=False):
        image = {}
        if self.name:
            image['name'] = self.name

        data = self.data

        if not data:
            return image
        image['mimeType'] = self.mime_type
        if self.is_uri:
            if embed:
                data = load_uri(self.data, folder=gltf.folder)
            else:
                image['uri'] = self.data
                return image

        view = buffer.get_view(image=self)
        if view.data:
            if view.byte_length != len(data):
                raise ValueError('Buffer view already exists for this image, '
                                 'but the byte_length does not match')
        else:
            view.write(data)
        image['bufferView'] = gltf.index('buffer_views', view)
        return image


class Sampler(BaseGLTFStructure):
    mag_filter = None
    min_filter = None
    wrap_s = None
    wrap_t = None

    class MagFilter(Enum):
        NEAREST = 9728
        LINEAR = 9729

    class MinFilter(Enum):
        NEAREST = 9728
        LINEAR = 9729
        NEAREST_MIPMAP_NEAREST = 9984
        LINEAR_MIPMAP_NEAREST = 9985
        NEAREST_MIPMAP_LINEAR = 9986
        LINEAR_MIPMAP_LINEAR = 9987

    class WrapMode(Enum):
        CLAMP_TO_EDGE = 33071
        MIRRORED_REPEAT = 33648
        REPEAT = 10497

    def __init__(self, sampler=None, name=None,
                 mag_filter=None, min_filter=None, wrap_s=None, wrap_t=None):
        if sampler:
            mag_filter = sampler.get('magFilter', mag_filter)
            if mag_filter:
                self.mag_filter = self.MagFilter(mag_filter)
            min_filter = sampler.get('minFilter', min_filter)
            if min_filter:
                self.min_filter = self.MinFilter(min_filter)
            wrap_s = sampler.get('wrapS', wrap_s)
            if wrap_s:
                self.wrap_s = self.WrapMode(wrap_s)
            wrap_t = sampler.get('wrapT', wrap_t)
            if wrap_t:
                self.wrap_t = self.WrapMode(wrap_t)
            self.name = sampler.get('name')
        else:
            self.name = name
            self.mag_filter = mag_filter
            self.min_filter = min_filter
            self.wrap_s = wrap_s
            self.wrap_t = wrap_t

    def __repr__(self):
        return self.name or super().__repr__()

    def render(self):
        sampler = {}
        if self.name:
            sampler['name'] = self.name
        if self.mag_filter:
            sampler['magFilter'] = self.mag_filter.value
        if self.min_filter:
            sampler['minFilter'] = self.min_filter.value
        if self.wrap_s:
            sampler['wrapS'] = self.wrap_s.value
        if self.wrap_t:
            sampler['wrapT'] = self.wrap_t.value
        return sampler

    @staticmethod
    def wrap(val, wrap_mode):
        if 0 < val < 1:
            return val
        if wrap_mode == Sampler.WrapMode.CLAMP_TO_EDGE:
            return 1.0 if val > 1 else 0.0
        if wrap_mode == Sampler.WrapMode.REPEAT:
            portion, _ = math.modf(val)
            return portion if val > 0 else 1.0 - portion
        if wrap_mode == Sampler.WrapMode.MIRRORED_REPEAT:
            portion, whole = math.modf(abs(val))
            if val < 0:
                whole += 1
            if whole % 2:
                return portion
            return 1.0 - portion
        raise TypeError('Invalid WrapMode')

    def wrap_point(self, point):
        return (
            self.wrap(point[0], self.wrap_s or self.WrapMode.REPEAT),
            self.wrap(point[1], self.wrap_t or self.WrapMode.REPEAT)
        )


class Texture(BaseGLTFStructure):
    sampler = None
    source = None

    def __init__(self, texture=None, gltf=None, name=None,
                 image=None, sampler=None, mirrored_repeat=False, repeat=False):
        if texture:
            sam = texture.get('sampler')
            if sam is not None:
                self.sampler = sam if isinstance(sam, Sampler) else gltf.samplers[sam]
            img = texture.get('source')
            if img is not None:
                self.source = img if isinstance(img, Image) else gltf.images[img]
            self.name = texture.get('name')
        else:
            self.name = name
            self.sampler = sampler
            if mirrored_repeat:
                self.sampler = Sampler(wrap_s=Sampler.WrapMode.MIRRORED_REPEAT,
                                       wrap_t=Sampler.WrapMode.MIRRORED_REPEAT)
            if repeat:
                self.sampler = Sampler(wrap_s=Sampler.WrapMode.REPEAT,
                                       wrap_t=Sampler.WrapMode.REPEAT)
            if image:
                self.source = image if isinstance(image, Image) else Image(image)

    def __repr__(self):
        return self.name or super().__repr__()

    def render(self, gltf):
        texture = {'source': gltf.index('images', self.source)}
        if self.name:
            texture['name'] = self.name
        if self.sampler:
            texture['sampler'] = gltf.index('samplers', self.sampler)
        return texture


class Material(BaseGLTFStructure):
    alpha_mode = None
    double_sided = None
    base_color_factor = None
    color_texture = None
    color_uv = None
    rough_metal_texture = None
    rough_uv = None
    normal_texture = None
    normal_uv = None
    normal_scale = None
    occlusion_texture = None
    occlusion_uv = None
    occlusion_strength = None
    emissive_texture = None
    emissive_factor = None
    emissive_uv = None
    metallic_factor = None
    roughness_factor = None

    diffuse_factor = None
    specular_factor = None
    glossiness_factor = None
    diffuse_texture = None
    spec_gloss_texture = None

    class AlphaMode(Enum):
        OPAQUE = 'OPAQUE'
        MASK = 'MASK'
        BLEND = 'BLEND'

    def __init__(self, material=None, gltf=None, name=None, image=None,
                 base_color_factor=None, double_sided=None,
                 color_texture=None, color_uv=None,
                 normal_texture=None, normal_uv=None,
                 occlusion_texture=None, occlusion_uv=None,
                 emissive_texture=None, emissive_uv=None,
                 rough_metal_texture=None, rough_uv=None,
                 alpha_mode=None, metallic_factor=0, roughness_factor=None, emissive_factor=None,
                 diffuse_factor=None, specular_factor=None, glossiness_factor=None,
                 diffuse_texture=None, spec_gloss_texture=None):
        if material:
            self.name = material.get('name')
            if material.get('alphaMode'):
                self.alpha_mode = self.AlphaMode(material.get('alphaMode'))
            if material.get('doubleSided'):
                self.double_sided = material.get('doubleSided')
            self.emissive_factor = material.get('emissiveFactor')
            pbr = material.get('pbrMetallicRoughness')
            if pbr:
                self.base_color_factor = pbr.get('baseColorFactor')
                self.metallic_factor = pbr.get('metallicFactor')
                self.roughness_factor = pbr.get('roughnessFactor')

                base_color_texture = pbr.get('baseColorTexture')
                if base_color_texture:
                    self.color_texture = gltf.textures[base_color_texture['index']]
                    if 'texCoord' in base_color_texture:
                        self.color_uv = gltf.accessors[base_color_texture['texCoord']]

                metallic_roughness_tex = pbr.get('metallicRoughnessTexture')
                if metallic_roughness_tex:
                    self.rough_metal_texture = gltf.textures[metallic_roughness_tex['index']]
                    if 'texCoord' in metallic_roughness_tex:
                        self.rough_uv = gltf.accessors[metallic_roughness_tex['texCoord']]

            normal = material.get('normalTexture')
            if normal:
                if 'index' in normal:
                    self.normal_texture = gltf.textures[normal['index']]
                if 'texCoord' in normal:
                    self.normal_uv = gltf.accessors[normal['texCoord']]
                if 'scale' in normal:
                    self.normal_scale = normal['scale']

            occlusion = material.get('occlusionTexture')
            if occlusion:
                if 'index' in occlusion:
                    self.occlusion_texture = gltf.textures[occlusion['index']]
                if 'texCoord' in occlusion:
                    self.occlusion_uv = gltf.accessors[occlusion['texCoord']]
                if 'strength' in occlusion:
                    self.occlusion_strength = occlusion['strength']

            emissive = material.get('emissiveTexture')
            if emissive:
                if 'index' in emissive:
                    self.emissive_texture = gltf.textures[emissive['index']]
                if 'texCoord' in emissive:
                    self.emissive_uv = gltf.accessors[emissive['texCoord']]

            extensions = material.get('extensions')
            if extensions:
                spec_gloss = extensions.get('KHR_materials_pbrSpecularGlossiness')
                if spec_gloss:
                    self.diffuse_factor = spec_gloss.get('diffuseFactor')
                    self.specular_factor = spec_gloss.get('specularFactor')
                    self.glossiness_factor = spec_gloss.get('glossinessFactor')
                    diffuse_texture = spec_gloss.get('diffuseTexture')
                    if diffuse_texture and diffuse_texture.get('index') is not None:
                        self.diffuse_texture = gltf.textures[diffuse_texture['index']]
                    spec_gloss_texture = spec_gloss.get('specularGlossinessTexture')
                    if spec_gloss_texture and spec_gloss_texture.get('index') is not None:
                        self.spec_gloss_texture = gltf.textures[spec_gloss_texture['index']]
        else:
            self.name = name
            self.double_sided = double_sided
            self.base_color_factor = base_color_factor
            self.color_texture = color_texture
            self.color_uv = color_uv
            self.normal_texture = normal_texture
            self.normal_uv = normal_uv
            self.occlusion_texture = occlusion_texture
            self.occlusion_uv = occlusion_uv
            self.rough_metal_texture = rough_metal_texture
            self.rough_uv = rough_uv
            self.emissive_texture = emissive_texture
            self.emissive_uv = emissive_uv
            self.metallic_factor = metallic_factor
            self.roughness_factor = roughness_factor
            self.emissive_factor = emissive_factor
            self.diffuse_factor = diffuse_factor
            self.specular_factor = specular_factor
            self.glossiness_factor = glossiness_factor
            self.diffuse_texture = diffuse_texture
            self.spec_gloss_texture = spec_gloss_texture
            if alpha_mode:
                self.alpha_mode = self.AlphaMode(alpha_mode)
            if image:
                self.color_texture = Texture(image=image)

    def __repr__(self):
        return self.name or super().__repr__()

    def __contains__(self, item):
        return (self.color_texture == item or
                self.rough_metal_texture == item or
                self.normal_texture == item or
                self.emissive_texture == item or
                self.diffuse_texture == item or
                self.spec_gloss_texture == item)

    def render(self, gltf):
        material = {'pbrMetallicRoughness': {}}

        if self.color_texture:
            color_texture = {
                'index': gltf.index('textures', self.color_texture)
            }
            if self.color_uv:
                color_texture['texCoord'] = gltf.index('accessors', self.color_uv)
            material['pbrMetallicRoughness']['baseColorTexture'] = color_texture

        if self.rough_metal_texture:
            rough_metal_texture = {
                'index': gltf.index('textures', self.rough_metal_texture)
            }
            if self.rough_uv:
                rough_metal_texture['texCoord'] = gltf.index('accessors', self.rough_uv)
            material['pbrMetallicRoughness']['metallicRoughnessTexture'] = rough_metal_texture

        if self.normal_texture:
            normal_texture = {
                'index': gltf.index('textures', self.normal_texture)
            }
            if self.normal_uv:
                normal_texture['texCoord'] = gltf.index('accessors', self.normal_uv)
            if self.normal_scale is not None:
                normal_texture['scale'] = self.normal_scale
            material['normalTexture'] = normal_texture

        if self.occlusion_texture:
            occlusion_texture = {
                'index': gltf.index('textures', self.occlusion_texture)
            }
            if self.occlusion_uv:
                occlusion_texture['texCoord'] = gltf.index('accessors', self.occlusion_uv)
            if self.occlusion_strength is not None:
                occlusion_texture['strength'] = self.occlusion_strength
            material['occlusionTexture'] = occlusion_texture

        if self.emissive_texture:
            emissive_texture = {
                'index': gltf.index('textures', self.emissive_texture)
            }
            if self.emissive_uv:
                emissive_texture['texCoord'] = gltf.index('accessors', self.emissive_uv)
            material['emissiveTexture'] = emissive_texture

        if self.name:
            material['name'] = self.name
        if self.alpha_mode:
            material['alphaMode'] = self.alpha_mode.value
        if self.double_sided:
            material['doubleSided'] = self.double_sided
        if self.emissive_factor:
            material['emissiveFactor'] = self.emissive_factor
        if self.metallic_factor is not None:
            material['pbrMetallicRoughness']['metallicFactor'] = self.metallic_factor
        if self.roughness_factor is not None:
            material['pbrMetallicRoughness']['roughnessFactor'] = self.roughness_factor
        if self.base_color_factor:
            material['pbrMetallicRoughness']['baseColorFactor'] = self.base_color_factor

        spec_gloss = {}
        if self.diffuse_texture:
            spec_gloss['diffuseTexture'] = {'index': gltf.index('textures', self.diffuse_texture)}
        if self.spec_gloss_texture:
            spec_gloss['specularGlossinessTexture'] = {
                'index': gltf.index('textures', self.spec_gloss_texture)
            }
        if self.glossiness_factor is not None:
            spec_gloss['glossinessFactor'] = self.glossiness_factor
        if self.diffuse_factor:
            spec_gloss['diffuseFactor'] = self.diffuse_factor
        if self.specular_factor:
            spec_gloss['specularFactor'] = self.specular_factor
        if spec_gloss:
            material['extensions'] = {'KHR_materials_pbrSpecularGlossiness': spec_gloss}
            if 'KHR_materials_pbrSpecularGlossiness' not in gltf.extensions_used:
                gltf.extensions_used.append('KHR_materials_pbrSpecularGlossiness')

        if not material['pbrMetallicRoughness']:
            material.pop('pbrMetallicRoughness')
        return material


class Primitive(BaseGLTFStructure):
    _positions = None
    _normals = None
    _texcoords = None
    _indices = None
    _tangents = None
    mode = None
    material = None

    class Mode(Enum):
        POINTS = 0
        LINES = 1
        LINE_LOOP = 2
        LINE_STRIP = 3
        TRIANGLES = 4
        TRIANGLE_STRIP = 5
        TRIANGLE_FAN = 6

    def __init__(self, prim=None, gltf=None, name=None,
                 positions=None, normals=None, indices=None, texcoords=None, tangents=None,
                 material=None, image=None, texture=None, mode=None):
        self.name = name
        if prim:
            if 'name' in prim:
                self.name = name
            if 'material' in prim:
                self.material = gltf.materials[prim.get('material')]
            if 'indices' in prim:
                self.indices = gltf.accessors[prim.get('indices')]
            if 'mode' in prim:
                self.mode = self.Mode(prim.get('mode'))
            attributes = prim.get('attributes')
            if attributes:
                if 'POSITION' in attributes:
                    self.positions = gltf.accessors[attributes.get('POSITION')]
                if 'NORMAL' in attributes:
                    self.normals = gltf.accessors[attributes.get('NORMAL')]
                if 'TANGENT' in attributes:
                    self.tangents = gltf.accessors[attributes.get('TANGENT')]
                if 'TEXCOORD_0' in attributes:
                    self.texcoords = gltf.accessors[attributes.get('TEXCOORD_0')]
        else:
            self.positions = positions
            self.normals = normals
            self.indices = indices
            self.tangents = tangents
            self.texcoords = texcoords
            self.material = material
            self.mode = mode and self.Mode[mode]
            if image:
                self.material = Material(image=image)
            if texture:
                self.material = Material(color_texture=texture)

    def __repr__(self):
        return self.name or super().__repr__()

    def __contains__(self, item):
        return (self._positions == item or
                self._normals == item or
                self._texcoords == item or
                self._indices == item or
                self._tangents == item)

    def split_transparency(self, alpha_mode=Material.AlphaMode.BLEND):
        if self.mode and self.mode != self.Mode.TRIANGLES:
            raise NotImplementedError('Prim splitting only implemented for triangles')

        if not self.material or not self.texcoords or (
                self.material.alpha_mode == Material.AlphaMode.OPAQUE):
            raise ValueError('Can\'t split prim: no material or texcoords, or material '
                             'is opaque, or material has no color_texture or diffuse_texture.')

        tex = self.material.color_texture or self.material.diffuse_texture
        sampler = tex.sampler or Sampler()
        img = PImage.open(tex.source.get_fp())
        if len(img.getbands()) != 4:
            return
        alpha = img.getdata(3)
        min_alpha, max_alpha = alpha.getextrema()

        # return if all or none of the image is transparent
        if min_alpha == 255 or max_alpha < 255:
            return

        if self.indices:
            indices_iter = (self.indices.data[pos:pos + 3]
                            for pos in
                            range(0, self.indices.count, 3))
        else:
            indices_iter = ((i, i + 1, i + 2)
                            for i in
                            range(0, self.texcoords.count, 3))
        t_indices = []
        o_indices = []
        for indices in indices_iter:
            for point in [self.texcoords.data[i] for i in indices]:
                point = sampler.wrap_point(point)
                x = math.floor(alpha.size[0] * point[0])
                y = math.floor(alpha.size[1] * point[1])
                alpha_val = alpha.getpixel((x, y))
                if alpha_val < 255:
                    break
            else:
                o_indices.extend(indices)
                continue
            t_indices.extend(indices)

        # return if there are no opaque vertices
        if not len(o_indices):
            return

        t_material = copy.copy(self.material)
        t_material.alpha_mode = alpha_mode
        # Copy own material in case something else is using it
        self.material = copy.copy(self.material)
        self.material.alpha_mode = Material.AlphaMode.OPAQUE
        self.indices = o_indices

        return Primitive(positions=self.positions, normals=self.normals,
                         texcoords=self.texcoords, tangents=self.tangents,
                         indices=t_indices, material=t_material)

    def render(self, gltf):
        primitive = {'attributes': {}}
        if self.mode:
            primitive['mode'] = self.mode.value
        if self.material:
            primitive['material'] = gltf.index('materials', self.material)
        if self.indices and self.indices.count:
            primitive['indices'] = gltf.index('accessors', self.indices)
        if self.positions and self.positions.count:
            primitive['attributes']['POSITION'] = gltf.index('accessors', self.positions)
        if self.normals and self.normals.count:
            primitive['attributes']['NORMAL'] = gltf.index('accessors', self.normals)
        if self.tangents and self.tangents.count:
            primitive['attributes']['TANGENT'] = gltf.index('accessors', self.tangents)
        if self.texcoords and self.texcoords.count:
            primitive['attributes']['TEXCOORD_0'] = gltf.index('accessors', self.texcoords)
        return primitive

    @property
    def positions(self):
        return self._positions

    @positions.setter
    def positions(self, positions):
        if positions is None:
            self._positions = None
            return
        self._positions = positions if isinstance(positions, Vec3Array) else Vec3Array(positions)

    @property
    def normals(self):
        return self._normals

    @normals.setter
    def normals(self, normals):
        if normals is None:
            self._normals = None
            return
        self._normals = normals if isinstance(normals, Vec3Array) else Vec3Array(normals)

    @property
    def tangents(self):
        return self._tangents

    @tangents.setter
    def tangents(self, tangents):
        if tangents is None:
            self._tangents = None
            return
        self._tangents = tangents if isinstance(tangents, Vec4Array) else Vec4Array(tangents)

    @property
    def texcoords(self):
        return self._texcoords

    @texcoords.setter
    def texcoords(self, texcoords):
        if texcoords is None:
            self._texcoords = None
            return
        self._texcoords = texcoords if isinstance(texcoords, Vec2Array) else Vec2Array(texcoords)

    @property
    def indices(self):
        return self._indices

    @indices.setter
    def indices(self, indices):
        if indices is None:
            self._indices = None
            return
        self._indices = indices if isinstance(indices, ScalarArray) else ScalarArray(indices)


class Mesh(BaseGLTFStructure):

    def __init__(self, mesh=None, gltf=None, name=None):
        self.primitives = []
        if mesh:
            self.name = mesh.get('name')
            for prim in mesh['primitives']:
                self.primitives.append(Primitive(prim, gltf))
        else:
            self.name = name

    def __repr__(self):
        return self.name or super().__repr__()

    def add_primitive(self, **kwargs):
        self.primitives.append(Primitive(**kwargs))
        return len(self.primitives) - 1

    def render(self, gltf):
        mesh = {
            'primitives': [primitive.render(gltf) for primitive in self.primitives]
        }
        if self.name:
            mesh['name'] = self.name

        return mesh


class Node(BaseGLTFStructure):
    mesh = None
    translation = None
    rotation = None
    scale = None
    matrix = None

    def __init__(self, node=None, gltf=None, name=None, mesh=None, children=None):
        if node:
            self.children = []
            self.name = node.get('name')
            mesh_idx = node.get('mesh')
            if mesh_idx is not None:
                self.mesh = gltf.meshes[mesh_idx]

            translation = node.get('translation')
            if translation:
                self.translation = np.array(translation, dtype='float32')

            rotation = node.get('rotation')
            if rotation:
                self.rotation = Quaternion(rotation[3], *rotation[:3])

            scale = node.get('scale')
            if scale:
                self.scale = np.array(scale, dtype='float32')

            matrix = node.get('matrix')
            if matrix:
                self.matrix = np.array(matrix, dtype='float32')

            if matrix and (scale or rotation or translation):
                logger.warning('Node defined both matrix and at least one other transform.')
        else:
            self.name = name
            self.mesh = mesh
            self.children = children or []

    def __repr__(self):
        return self.name or super().__repr__()

    def __eq__(self, other):
        if not (isinstance(other, type(self))
                and (self.mesh, self.name) ==
                (other.mesh, other.name)):
            return False

        # quaternions seem to blow up if they're compared to None
        if (self.rotation is None) != (other.rotation is None) or self.rotation != other.rotation:
            return False

        return (np.array_equal(self.translation, other.translation) and
                np.array_equal(self.scale, other.scale) and
                np.array_equal(self.matrix, other.matrix) and
                self.children == other.children)

    def find_children(self, child_indices, gltf):
        for child_idx in child_indices:
            self.children.append(gltf.nodes[child_idx])

    def apply_transforms(self, parent_transformation=None, parent_rotation=None):

        transformation = np.identity(4)
        rotation_matrix = parent_rotation
        if self.scale is not None:
            transformation = transformation.dot(
                np.diag(np.append(self.scale, [1]))
            )
        if self.rotation is not None:
            rotation_matrix = (
                self.rotation.inverse.rotation_matrix.dot(rotation_matrix)
                if rotation_matrix is not None
                else self.rotation.inverse.rotation_matrix
            )
            transformation = transformation.dot(
                self.rotation.inverse.transformation_matrix
            )
        if self.translation is not None:
            translation = np.identity(4)
            translation[3, :] += np.append(self.translation, [0])
            transformation = transformation.dot(translation)

        # Only use self.matrix if there is no other transform
        if self.matrix is not None and np.allclose(transformation, np.identity(4)):
            transformation = self.matrix

        if parent_transformation is not None:
            transformation = transformation.dot(parent_transformation)

        if self.mesh and not np.allclose(transformation, np.identity(4)):
            for p in self.mesh.primitives:
                if not p.positions:
                    continue
                vertices = p.positions.data
                vertices = np.append(vertices, np.ones([len(vertices), 1]), 1)
                p.positions.data = vertices.dot(transformation)[:, :3].astype('float32')
                if p.normals and rotation_matrix is not None:
                    p.normals.data = p.normals.data.dot(rotation_matrix).astype('float32')

        for child in self.children:
            child.apply_transforms(transformation, rotation_matrix)

        self.translation = None
        self.rotation = None
        self.scale = None

    def render(self, gltf):
        node = {}
        if self.mesh:
            node['mesh'] = gltf.index('meshes', self.mesh)
        if self.name:
            node['name'] = self.name
        if self.children:
            node['children'] = [gltf.index('nodes', n) for n in self.children]
        if self.translation is not None:
            node['translation'] = self.translation.tolist()
        if self.rotation is not None:
            node['rotation'] = self.rotation.elements.tolist()
            node['rotation'].append(node['rotation'].pop(0))
        if self.scale is not None:
            node['scale'] = self.scale.tolist()
        if self.matrix is not None:
            node['matrix'] = self.matrix.tolist()
        return node


class Scene:
    name = None
    nodes = None

    def __init__(self, scene=None, gltf=None, nodes=None, name=None):
        if scene:
            self.name = scene.get('name')
            self.nodes = [gltf.nodes[i] for i in scene.get('nodes', [])]
        else:
            self.nodes = nodes or []
            self.name = name

    def __repr__(self):
        return self.name or super().__repr__()

    def render(self, gltf):
        scene = {}
        if self.name:
            scene['name'] = self.name
        if self.nodes:
            scene['nodes'] = [gltf.index('nodes', n) for n in self.nodes]
        return scene


class GLTF:
    MAGIC = 0x46546C67
    JSON_CHUNK = 0x4E4F534A
    BINARY_CHUNK = 0x004E4942
    scene = None

    def __init__(self, folder=None, filename=None):
        self.scenes = []
        self.meshes = []
        self.nodes = []
        self.materials = []
        self.textures = []
        self.samplers = []
        self.accessors = []
        self.images = []
        self.buffer_views = []
        self.buffers = []
        self.extensions_used = []
        self.folder = folder
        self.filename = filename
        self.asset = {
            'version': '2.0',
            'generator': 'Seek GLTF Generator',
        }

    def index(self, component, obj):
        if not hasattr(self, component):
            raise AttributeError(component)
        arr = getattr(self, component)
        if obj not in arr:
            arr.append(obj)
        return arr.index(obj)

    @staticmethod
    def simple_model(name, folder=None):
        gltf = GLTF(folder)
        gltf.scene = Scene()
        mesh = Mesh()
        gltf.meshes.append(mesh)
        node = Node(mesh=mesh, name=name)
        gltf.nodes.append(node)
        gltf.scene.nodes.append(node)

        return gltf, mesh

    @staticmethod
    def load(data_or_path, folder=None, filename=None, repair=False):
        if type(data_or_path) is dict:
            data = data_or_path
        else:
            parts = data_or_path.split('/')
            filename = '.'.join(parts[-1].split('.')[:-1])
            folder = '/'.join(parts[:-1])
            data = None
            with open(data_or_path, 'rb') as f:
                magic, glb_version, file_size = np.frombuffer(f.read(12), dtype='uint32')
                if magic == GLTF.MAGIC:
                    if glb_version != 2:
                        raise NotImplementedError('Only glb version 2 is supported!')
                    total_bytes_read = 12
                    while True:
                        header_bytes = f.read(8)
                        if not header_bytes:
                            if total_bytes_read != file_size:
                                raise ValueError('Expected ' + file_size + ' bytes' +
                                                 ' but only read ' + total_bytes_read)
                            break
                        total_bytes_read += 8
                        chunk_size, chunk_type = np.frombuffer(header_bytes, dtype='uint32')
                        chunk = f.read(chunk_size)
                        total_bytes_read += chunk_size
                        if chunk_type == GLTF.JSON_CHUNK:
                            data = json.loads(chunk.decode('utf-8'))
                        elif chunk_type == GLTF.BINARY_CHUNK:
                            buffer = data['buffers'][0]
                            buffer['data'] = bytearray(chunk)[:buffer['byteLength']]
                        else:
                            raise TypeError('Invalid chunk type: ' + chunk_type)

                else:
                    f.seek(0)
                    data = json.loads(f.read().decode('utf-8'))

        gltf = GLTF(folder, filename)

        asset = data.get('asset', {})
        gltf.asset.update(extras=asset.get('extras', {}))

        extensions = data.get('extensionsUsed')
        if extensions:
            gltf.extensions_used = extensions

        for buf in data.get('buffers', []):
            gltf.buffers.append(Buffer(buf, gltf))

        for bv in data.get('bufferViews', []):
            gltf.buffer_views.append(BufferView(bv, gltf))

        for img in data.get('images', []):
            gltf.images.append(Image(img, gltf))

        for acc in data.get('accessors', []):
            if acc['type'] == 'SCALAR':
                acc = ScalarArray(acc, gltf)
            elif acc['type'] == 'VEC3':
                acc = Vec3Array(acc, gltf)
            elif acc['type'] == 'VEC2':
                acc = Vec2Array(acc, gltf)
            elif acc['type'] == 'VEC4':
                acc = Vec4Array(acc, gltf)
            elif acc['type'] == 'MAT4':
                acc = Mat4Array(acc, gltf)
            else:
                raise NotImplementedError('Accessor of type ' + acc['type'] + ' not implemented')
            gltf.accessors.append(acc)

        for sam in data.get('samplers', []):
            gltf.samplers.append(Sampler(sam))

        for tex in data.get('textures', []):
            gltf.textures.append(Texture(tex, gltf))

        for mat in data.get('materials', []):
            gltf.materials.append(Material(mat, gltf))

        for mesh in data.get('meshes', []):
            gltf.meshes.append(Mesh(mesh, gltf))

        nodes = data.get('nodes', [])
        for node in nodes:
            gltf.nodes.append(Node(node, gltf))
        for node, node_dict in zip(gltf.nodes, nodes):
            children = node_dict.get('children', [])
            node.find_children(children, gltf)

        for scene in data.get('scenes', []):
            gltf.scenes.append(Scene(scene, gltf))

        scene_idx = data.get('scene')
        if scene_idx is not None:
            gltf.scene = gltf.scenes[scene_idx]

        if repair:
            gltf.repair()

        return gltf

    def center(self):
        min_x = min_y = min_z = float('inf')
        max_x = max_z = float('-inf')
        for n in [n for n in self.nodes if n.mesh]:
            for p in n.mesh.primitives:
                x, y, z = p.positions.min
                if x < min_x:
                    min_x = x
                if z < min_z:
                    min_z = z
                if y < min_y:
                    min_y = y

                x, _, z = p.positions.max
                if x > max_x:
                    max_x = x
                if z > max_z:
                    max_z = z
        translation = [-(min_x + (max_x - min_x) / 2),
                       -min_y,
                       -(min_z + (max_z - min_z) / 2)]

        transformation = np.identity(4)
        transformation[3, :3] += translation
        if not np.allclose(transformation, np.identity(4)):
            logger.info('Centering model using translation: '
                        '' + ', '.join(map(str, translation)))
            for n in self.scene.nodes:
                n.apply_transforms(transformation)

    def render(self, binary=False, embed=False):
        self.buffers = []
        self.buffer_views = []

        data = {
            'asset': self.asset,
            'nodes': [n.render(self) for n in self.nodes],
            'meshes': [m.render(self) for m in self.meshes],
            'scene': self.index('scenes', self.scene),
            'scenes': [s.render(self) for s in self.scenes],
            'buffers': [],
            'bufferViews': [],
        }

        if self.extensions_used:
            data['extensionsUsed'] = self.extensions_used

        if self.materials:
            data['materials'] = [mat.render(self) for mat in self.materials]

        if self.textures:
            data['textures'] = [tex.render(self) for tex in self.textures]

        if self.samplers:
            data['samplers'] = [sampler.render() for sampler in self.samplers]

        buffer = Buffer()

        if self.accessors:
            data['accessors'] = [acc.render(buffer, self) for acc in self.accessors]

        if self.images:
            data['images'] = [img.render(buffer, self, embed) for img in self.images]

        for bv in self.buffer_views:
            bv.write_to_buffer()
            data['bufferViews'].append(bv.render(self))

        data['buffers'].append(buffer.render())

        if binary:
            if len([b for b in data['buffers'] if not b.get('uri')]) > 1:
                raise ValueError('GLB only supports one embedded buffer')

            total_size = 0

            binary_chunk = b''
            if data['buffers']:
                binary_chunk = bytearray(data['buffers'][0].pop('data', b''))

            json_chunk = bytearray(json.dumps(data).encode())
            if len(json_chunk) % 4:
                # pad to 4 bytes with spaces
                json_chunk.extend(bytes([0x20] * (4 - len(json_chunk) % 4)))

            json_header = np.array([
                len(json_chunk),
                self.JSON_CHUNK,
            ], dtype='uint32').tobytes()

            total_size += len(json_header) + len(json_chunk)

            binary_header = b''
            if binary_chunk:
                if len(binary_chunk) % 4:
                    # pad to 4 bytes with zeroes
                    binary_chunk.extend(bytes([0x00] * (4 - len(binary_chunk) % 4)))
                binary_header = np.array([
                    len(binary_chunk),
                    self.BINARY_CHUNK,
                ], dtype='uint32').tobytes()

            total_size += len(binary_header) + len(binary_chunk)

            file_header = np.array([
                self.MAGIC,
                2,  # GLB container version
                total_size + 12,  # size of entire file (total_size + file_header length)
            ], dtype='uint32').tobytes()

            return bytearray(
                file_header +
                json_header +
                json_chunk +
                binary_header +
                binary_chunk
            )

        for buffer in data['buffers']:
            buffer['uri'] = binary_to_uri(buffer.pop('data'))

        return data

    def split_transparent_prims(self):
        for n in self.nodes:
            if not n.mesh:
                continue
            new_prims = []
            for prim in n.mesh.primitives:
                if prim.material \
                        and prim.material.alpha_mode != Material.AlphaMode.OPAQUE \
                        and prim.texcoords:
                    new_prim = prim.split_transparency()
                    if new_prim:
                        new_prims.append(new_prim)
            n.mesh.primitives.extend(new_prims)

    def duplicate_shared_meshes(self):
        existing_meshes = []
        existing_accessors = []
        for n in self.nodes:
            if not n.mesh:
                continue
            if n.mesh in existing_meshes:
                n.mesh = Mesh(n.mesh.render(self), gltf=self)
                for p in n.mesh.primitives:
                    if p.positions:
                        p.positions = Vec3Array(p.positions.data)
                        self.accessors.append(p.positions)
                    if p.normals:
                        p.normals = Vec3Array(p.normals.data)
                        self.accessors.append(p.normals)
                self.meshes.append(n.mesh)
            else:
                for p in n.mesh.primitives:
                    if p.positions:
                        if p.positions in existing_accessors:
                            p.positions = Vec3Array(p.positions.data)
                            self.accessors.append(p.positions)
                        else:
                            existing_accessors.append(p.positions)
                    if p.normals:
                        if p.normals in existing_accessors:
                            p.normals = Vec3Array(p.normals.data)
                            self.accessors.append(p.normals)
                        else:
                            existing_accessors.append(p.normals)

            existing_meshes.append(n.mesh)

    def apply_all_transforms(self, transform=None, rotation=None):
        self.duplicate_shared_meshes()
        for n in self.scene.nodes:
            n.apply_transforms(transform, rotation)
        self.repair()

    @staticmethod
    def remove_duplicates(input_list):
        trimmed_list = []
        for item in input_list:
            if item not in trimmed_list:
                trimmed_list.append(item)
        return trimmed_list

    def repair(self, trim_to_scene=True):
        countable_attrs = ['scenes', 'nodes', 'meshes', 'accessors',
                           'materials', 'textures', 'images', 'samplers']
        counts = {
            attr: len(getattr(self, attr)) for attr in countable_attrs
        }

        # remove any nodes (from both the gltf and the scenes) that don't have a mesh or children
        def recurse_nodes(node, valid_nodes=None):
            valid_children = []
            for cn in node.children:
                if recurse_nodes(cn, valid_nodes):
                    valid_children.append(cn)
            node.children = valid_children

            if node.mesh or node.children:
                if valid_nodes is not None and node not in valid_nodes:
                    valid_nodes.append(node)
                return True

        for scene in self.scenes:
            valid_scene_nodes = []
            for n in scene.nodes:
                if recurse_nodes(n):
                    valid_scene_nodes.append(n)
            scene.nodes = valid_scene_nodes

        if trim_to_scene:
            # remove all but the root scene, and keep only nodes descended from that scene
            if not self.scene:
                raise ValueError('Cannot trim to scene if there is no scene!')
            self.scenes = [self.scene]
            self.nodes = []
            for n in self.scene.nodes:
                recurse_nodes(n, self.nodes)
        else:
            nodes = self.nodes
            self.nodes = []
            for n in nodes:
                recurse_nodes(n, self.nodes)

        # remove duplicate meshes
        meshes = self.remove_duplicates(self.meshes)
        self.meshes = []

        # populate the used meshes
        for mesh in meshes:
            for node in self.nodes:
                if node.mesh == mesh and mesh not in self.meshes:
                    self.meshes.append(mesh)
                    break

        # get rid of duplicate materials and accessors
        materials = self.remove_duplicates(self.materials)
        self.materials = []
        accessors = self.remove_duplicates(self.accessors)
        self.accessors = []

        # go through all meshes and prims and find what materials and accessors are actually used
        for mesh in self.meshes:
            for primitive in mesh.primitives:

                # get all used materials
                for material in materials:
                    if primitive.material == material and material not in self.materials:
                        self.materials.append(material)
                        break

                # get all used accessors
                for accessor in accessors:
                    if accessor in primitive and accessor not in self.accessors:
                        self.accessors.append(accessor)
                        # don't break here, there can be multiple accessors in a prim

        # remove dupe textures
        textures = self.remove_duplicates(self.textures)
        self.textures = []

        # find which textures are used
        for texture in textures:
            for material in self.materials:
                if texture in material and texture not in self.textures:
                    self.textures.append(texture)
                    break

        # remove dupe images and samplers
        images = self.remove_duplicates(self.images)
        self.images = []
        samplers = self.remove_duplicates(self.samplers)
        self.samplers = []

        # find which images and samplers are used
        for texture in self.textures:
            for image in images:
                if texture.source == image and image not in self.images:
                    self.images.append(image)
                    break

            for sampler in samplers:
                if texture.sampler == sampler and sampler not in self.samplers:
                    self.samplers.append(sampler)
                    break

        for attr, count in counts.items():
            diff = len(getattr(self, attr)) - count
            if not diff:
                continue
            logger.info('{} {} {}'.format('Added' if diff > 0 else 'Removed',
                                          str(abs(diff)),
                                          attr))

    def save(self, path_or_filename=None, binary=None, **kwargs):
        folder = (self.folder or '.') + '/'
        filename = None
        if path_or_filename:
            if path_or_filename.endswith('.glb') and binary is None:
                binary = True
            if os.path.dirname(path_or_filename):
                folder = os.path.dirname(path_or_filename)
                if os.path.basename(path_or_filename):
                    filename = os.path.basename(path_or_filename)
            else:
                filename = path_or_filename

        if not filename:
            if not self.filename:
                raise ValueError('Filename required to save')
            filename = self.filename + ('.glb' if binary else '.gltf')

        data = self.render(binary=binary, **kwargs)
        path = os.path.join(folder, filename)
        if binary:
            with open(path, 'wb') as f:
                f.write(data)
        else:
            with open(path, 'w') as f:
                json.dump(data, f)
        return path
