import ansys.meshing.prime as prime


def test_sizecontrol(get_remote_client, get_examples):
    elbow_lucid = get_examples["elbow_lucid"]
    model = get_remote_client.model
    fileIO = prime.FileIO(model=model)
    mesher = prime.lucid.Mesh(model)
    mesher.read(file_name=elbow_lucid)
    size_control = model.control_data.create_size_control(prime.SizingType.CURVATURE)
    result = size_control.set_suggested_name('bar')
    assert result.assigned_name != ''
    assert result.assigned_name == size_control.name
