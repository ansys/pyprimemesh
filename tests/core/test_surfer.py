import ansys.meshing.prime as prime
from ansys.meshing.prime.autogen.primeconfig import ErrorCode


def test_mesh_topo_faces(initialized_model_elbow):

    # load example from fixture
    model, mesher = initialized_model_elbow
    mesher.surface_mesh(min_size=1, max_size=200)

    topo_faces = model.parts[0].get_topo_faces()

    surfer = prime.Surfer(model)
    surfer_params = prime.SurferParams(model)
    results = surfer.mesh_topo_faces(2, topo_faces, surfer_params)
    assert results.error_code == ErrorCode.NOERROR


def test_remesh_face_zonelets_locally(initialized_model_elbow):
    # load example from fixture
    model, mesher = initialized_model_elbow
    mesher.surface_mesh(min_size=1, max_size=200)

    surfer = prime.Surfer(model)
    local_surfer_params = prime.LocalSurferParams(model)

    # TODO: returns empty list
    face_zonelets = model.parts[0].get_face_zonelets()
    part_id = model.parts[0].id
    results = surfer.remesh_face_zonelets_locally(part_id, face_zonelets, 4, local_surfer_params)
    assert results.error_code == ErrorCode.NOERROR


def test_remesh_face_zonelets(initialized_model_elbow):
    # load example from fixture
    model, mesher = initialized_model_elbow
    mesher.surface_mesh(min_size=1, max_size=200)

    surfer = prime.Surfer(model)
    surfer_params = prime.SurferParams(model)
    part_id = model.parts[0].id
    # TODO: returns empty list
    face_zonelets = model.parts[0].get_face_zonelets()
    edge_zonelets = model.parts[0].get_edge_zonelets()
    # Error: Not supported for part with topology data
    # results = surfer.remesh_face_zonelets(part_id,
    #                        face_zonelets, edge_zonelets, surfer_params)
    # assert results.error_code == ErrorCode.NOERROR


def test_initialize_surfer_params_for_wrapper(initialized_model_elbow):
    model, _ = initialized_model_elbow
    surfer = prime.Surfer(model)
    surfer_params = surfer.initialize_surfer_params_for_wrapper()
    assert surfer_params != None
