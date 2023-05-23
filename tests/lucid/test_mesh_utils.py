import os

import pytest

from ansys.meshing.prime.lucid.mesh_util import Mesh


@pytest.fixture
def mesh(get_remote_client):
    model = get_remote_client.model
    mesh = Mesh(model)
    return mesh


def test_read(mesh):
    mesh.read(os.path.abspath("./tests/core/test_files/hex.msh"))
    mesh.read(os.path.abspath("./tests/core/test_files/hex.cdb"))
    mesh.read(os.path.abspath("./tests/core/test_files/hex.cas"))

    # causes docker error
    # mesh.read(os.path.abspath("./tests/core/test_files/file.pmdat"))
    # missing CAD file


def test_write(mesh, tmp_path):
    mesh.write(os.path.abspath(str(tmp_path) + "/file_output.msh"))
    mesh.write(os.path.abspath(str(tmp_path) + "/file_output.cas"))
    mesh.write(os.path.abspath(str(tmp_path) + "/file_output.cdb"))
    mesh.write(os.path.abspath(str(tmp_path) + "/file_output.pmdat"))


def test_create_zones(mesh):
    mesh.create_zones_from_labels(label_expression=None)


def test_merge(mesh):
    mesh.merge_parts()


def test_surface_mesh(mesh):
    mesh.surface_mesh()


def test_connect_faces(mesh):
    mesh.connect_faces()


def test_compute_volumes(mesh):
    mesh.compute_volumes()


def test_volume_mesh(mesh):
    mesh.volume_mesh(quadratic=True)


def test_wrap(mesh):
    mesh.wrap()


def test_delete_topo(mesh):
    mesh.delete_topology()
    mesh.delete_topology(delete_edges=True)
