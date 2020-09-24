"""Creates a mesh on a cube.
"""
from helpers import compute_volume

import pygmsh


def test():
    with pygmsh.built_in.Geometry() as geom:
        geom.add_box(0, 1, 0, 1, 0, 1, 1.0)
        mesh = pygmsh.generate_mesh(geom)

    ref = 1.0
    assert abs(compute_volume(mesh) - ref) < 1.0e-2 * ref
    return mesh


if __name__ == "__main__":
    test().write("cube.vtu")
