import ansys.meshing.prime as prime


def test_sizecontrol(get_remote_client):
    model = get_remote_client.model
    fileIO = prime.FileIO(model=model)

    size_control = prime.SizeControl(model, 0, 0, "foo")
    assert size_control.name == "foo"

    result = size_control.set_suggested_name('bar')
    assert result.assigned_name != ''
    assert result.assigned_name == size_control.name
