"""This module tests the different methods in Surfer class."""
import ansys.meshing.prime as prime


def test_mesh_topo_faces(initialized_model_elbow):
    """Test the meshing for topo faces."""
    # load example from fixture
    model: prime.Model
    mesher: prime.lucid.Mesh
    model, mesher = initialized_model_elbow
    mesher.surface_mesh(min_size=1, max_size=200)

    topo_faces = model.parts[0].get_topo_faces()

    surfer = prime.Surfer(model)
    surfer_params = prime.SurferParams(model)
    results = surfer.mesh_topo_faces(2, topo_faces, surfer_params)
    assert results.error_code is prime.ErrorCode.NOERROR


def test_remesh_face_zonelets_locally(initialized_model_elbow):
    """Test the remeshing of face zonelets locally."""
    # load example from fixture
    model: prime.Model
    mesher: prime.lucid.Mesh
    model, mesher = initialized_model_elbow
    mesher.surface_mesh(min_size=1, max_size=200)

    surfer = prime.Surfer(model)
    local_surfer_params = prime.LocalSurferParams(model)

    part = model.parts[0]
    part.delete_topo_entities(
        prime.DeleteTopoEntitiesParams(model, delete_geom_zonelets=False, delete_mesh_zonelets=True)
    )
    face_zonelets = part.get_face_zonelets()
    results = surfer.remesh_face_zonelets_locally(part.id, face_zonelets, 1, local_surfer_params)
    assert results.error_code is prime.ErrorCode.NOERROR


def test_remesh_face_zonelets(initialized_model_elbow):
    """Test the remeshing of face zonelets."""
    # load example from fixture
    model: prime.Model
    mesher: prime.lucid.Mesh
    model, mesher = initialized_model_elbow
    mesher.surface_mesh(min_size=1, max_size=200)

    surfer = prime.Surfer(model)
    surfer_params = prime.SurferParams(model)
    part = model.parts[0]
    part.delete_topo_entities(
        prime.DeleteTopoEntitiesParams(model, delete_geom_zonelets=False, delete_mesh_zonelets=True)
    )
    face_zonelets = part.get_face_zonelets()
    edge_zonelets = part.get_edge_zonelets()

    results = surfer.remesh_face_zonelets(part.id, face_zonelets, edge_zonelets, surfer_params)
    assert results.error_code is prime.ErrorCode.NOERROR


def test_initialize_surfer_params_for_wrapper(initialized_model_elbow):
    """Test the initialization of surfer parameters."""
    model: prime.Model
    model, _ = initialized_model_elbow
    surfer = prime.Surfer(model)
    surfer_params = surfer.initialize_surfer_params_for_wrapper()
    assert surfer_params != None
