import ansys.meshing.prime as prime


def test_mesh_topo_faces(get_remote_client, get_examples):
    """Test the regular usage of SizeControl Class."""

    # load example from fixture
    elbow_lucid = get_examples["elbow_lucid"]

    # initialize model from fixture
    model = get_remote_client.model
    surfer_params = prime.SurferParams(model)
