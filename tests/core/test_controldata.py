from ansys.meshing.prime.params.primestructs import SizingType


def test_controldata(initialized_model_elbow):
    model, _ = initialized_model_elbow

    controldata = model.control_data
    wrapper_control = controldata.create_wrapper_control()
    wrapper_control_test = model.control_data.get_wrapper_control_by_name(wrapper_control.name)
    assert wrapper_control_test.name != ('' or None)
    assert wrapper_control_test.name == 'WrapperControl1'

    size_control = controldata.create_size_control(SizingType.BOI)
    size_control_test = controldata.get_size_control_by_name(size_control.name)
    assert size_control_test.name != ('' or None)
    assert size_control.name == size_control_test.name

    prism_control = controldata.create_prism_control()
    prism_control_test = controldata.get_prism_control_by_name(prism_control.name)
    assert prism_control_test.name != ('' or None)
    assert prism_control.name == prism_control_test.name

    volume_control = controldata.create_volume_control()
    volume_control_test = controldata.get_volume_control_by_name(volume_control.name)
    assert volume_control_test.name != ('' or None)
    assert volume_control.name == volume_control_test.name

    # error on server side
    periodic_control = controldata.create_periodic_control()
    periodic_control_test = controldata.get_periodic_control_by_name(periodic_control.name)
    assert periodic_control_test.name != ('' or None)
    assert periodic_control.name == periodic_control_test.name
