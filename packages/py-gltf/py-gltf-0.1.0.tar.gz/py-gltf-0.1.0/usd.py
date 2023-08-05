from enum import Enum

import numpy as np


class Field:
    def __init__(self, token, value):
        self.token = token
        self.value = value


class Path:
    def __init__(self, path):
        if not path.startswith('/'):
            raise ValueError('Cannot initialize relative path')
        self._path = path

    def __str__(self):
        return self.path

    @property
    def path(self):
        return self._path

    @property
    def prim(self):
        return self.path.split('.')[0]

    def append(self, path):
        if path.startswith('/'):
            raise ValueError('Cannot append absolute path')
        if self.prim.endswith('/'):
            appended_path = self.prim + path
        else:
            appended_path = self.prim + '/' + path
        return Path(appended_path)


class SpecType(Enum):
    UNKNOWN = 0
    ATTRIBUTE = 1
    CONNECTION = 2
    EXPRESSION = 3
    MAPPER = 4
    MAPPER_ARG = 5
    PRIM = 6
    PSEUDO_ROOT = 7
    RELATIONSHIP = 8
    RELATIONSHIP_TARGET = 9
    VARIANT = 10
    VARIANT_SET = 11


class Spec:
    type = SpecType.UNKNOWN

    def __init__(self, path, spec_type=None, fields=None):
        self.path = path
        self.fields = [] if fields is None else fields
        if spec_type is not None:
            self.type = SpecType(spec_type)


class Xform(Spec):
    type = SpecType.PRIM

    def __init__(self, path):
        fields = [
            Field('specifier', 'SdfSpecifierDef'),
            Field('typeName', 'Xform'),
            Field('primChildren', []),
        ]
        super().__init__(path, fields=fields)


def load_gltf_texture(mesh, path, usd):
    pass


def load_gltf_node(node, path, usd):
    xform = Xform(path)

    if node.mesh:
        for p in node.mesh.primitives:
            pass

    for i, child_node in enumerate(node.children):
        child_path = xform.path.append()
        load_gltf_node()


class USD:
    def __init__(self):
        self.root_children = []
        self.root = Spec(Path('/'), SpecType.PSEUDO_ROOT, [
            Field('primChildren', [])
        ])
        self.specs = [self.root]

    @staticmethod
    def load_file():
        pass

    def export_usda(self):
        pass

    def export_usdc(self):
        pass

    def export_usdz(self):
        pass

    @staticmethod
    def load_gltf(gltf):
        scale = np.diag([100, 100, 100, 1])
        # TODO: copy the gltf before modifying the vertex data?
        gltf.apply_all_transforms(scale)

        usd = USD()
        for i, n in enumerate(gltf.scene.nodes):
            node_path = usd.root.path.append('SceneNode' + str(i))
            load_gltf_node(n, node_path, usd)

    def export_gltf(self):
        pass
