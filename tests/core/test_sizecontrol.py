import ansys.meshing.prime as prime


def test_sizecontrol(get_remote_client):
    model = get_remote_client.model
    util = prime.lucid.Mesh(model)
    util.read(prime.examples.download_elbow_pmdat())
    size_control = model.control_data.create_size_control(prime.SizingType.CURVATURE)
    result = size_control.set_suggested_name('bar')
    assert result.assigned_name != ''
    assert result.assigned_name == size_control.name
