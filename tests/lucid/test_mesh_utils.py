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
    mesh.read(os.path.abspath(str(tmp_path) + "/file_output.msh"))

    mesh.write(os.path.abspath(str(tmp_path) + "/file_output.cas"))
    mesh.read(os.path.abspath(str(tmp_path) + "/file_output.cas"))

    mesh.write(os.path.abspath(str(tmp_path) + "/file_output.cdb"))
    # mesh.read(os.path.abspath(str(tmp_path) + "/file_output.cdb"))

    mesh.write(os.path.abspath(str(tmp_path) + "/file_output.pmdat"))
    mesh.read(os.path.abspath(str(tmp_path) + "/file_output.pmdat"))


def test_create_zones(mesh, get_examples):
    pmdat_path = get_examples["elbow_lucid"]
    mesh.read(pmdat_path)
    mesh.create_zones_from_labels(label_expression="*")
    mesh.create_zones_from_labels(conversion_method=1)
    mesh.read(os.path.abspath("./tests/core/test_files/hex.cas"))
    mesh.create_zones_from_labels(label_expression="*")


def test_merge(mesh):
    mesh.merge_parts()


def test_surface_mesh(mesh):
    mesh.surface_mesh()
    mesh.surface_mesh(max_size=0.1)
    mesh.surface_mesh(min_size=0.1)
    mesh.surface_mesh(min_size=0.1, max_size=0.9)

    mesh.surface_mesh_with_size_controls()


def test_connect_faces(mesh):
    mesh.connect_faces()


def test_compute_volumes(mesh):
    mesh.compute_volumes()


def test_volume_mesh(mesh):
    mesh.volume_mesh(quadratic=True)
    mesh.volume_mesh(prism_layers=True)


def test_wrap(mesh):
    mesh.wrap()
    mesh.wrap(contact_prevention_size=0.01)


def test_delete_topo(mesh):
    mesh.delete_topology()
    mesh.delete_topology(delete_edges=True)


def test_size_control(mesh):
    mesh.create_constant_size_control()
    mesh.create_curvature_size_control(max=1.0, min=2.0)
