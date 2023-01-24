import ansys.meshing.prime as prime


def test_sizecontrol(get_remote_client, get_examples):
    """Test the regular usage of SizeControl Class."""

    # load example from fixture
    elbow_lucid = get_examples["elbow_lucid"]

    # initialize model from fixture
    model = get_remote_client.model

    # init mesher and load the example
    mesher = prime.lucid.Mesh(model)
    mesher.read(file_name=elbow_lucid)

    # create a SizeControl object from the model
    size_control = model.control_data.create_size_control(prime.SizingType.CURVATURE)

    # change the name and check if it is working as intended
    result = size_control.set_suggested_name('bar')
    assert result.assigned_name != ''
    assert result.assigned_name == size_control.name
