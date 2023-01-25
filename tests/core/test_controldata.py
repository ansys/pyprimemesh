from ansys.meshing.prime.params.primestructs import SizingType


def test_controldata(initialized_model_elbow):
    """Tests the methods and properties from ControlData class and control classes."""
    model, _ = initialized_model_elbow
    controldata = model.control_data

    # wrapper control tests
    wrapper_control_test = model.control_data.get_wrapper_control_by_name("test")
    assert wrapper_control_test is None

    wrapper_control = controldata.create_wrapper_control()
    wrapper_control_test = model.control_data.get_wrapper_control_by_name(wrapper_control.name)
    assert wrapper_control_test.name != ('' or None)
    assert wrapper_control_test.name == 'WrapperControl1'

    wrapper_control_test.set_suggested_name("foo")
    assert wrapper_control_test.name == "foo"

    # size control tests
    size_control_test = model.control_data.get_size_control_by_name("test")
    assert size_control_test is None

    size_control = controldata.create_size_control(SizingType.BOI)
    size_control_test = controldata.get_size_control_by_name(size_control.name)
    assert size_control_test.name != ('' or None)
    assert size_control.name == size_control_test.name

    size_control_test.set_suggested_name("foo")
    assert size_control_test.name == "foo.1"

    # prism control tests
    prism_control_test = model.control_data.get_prism_control_by_name("test")
    assert prism_control_test is None

    prism_control = controldata.create_prism_control()
    prism_control_test = controldata.get_prism_control_by_name(prism_control.name)
    assert prism_control_test.name != ('' or None)
    assert prism_control.name == prism_control_test.name

    # volume control tests
    volume_control_test = model.control_data.get_volume_control_by_name("test")
    assert volume_control_test is None

    volume_control = controldata.create_volume_control()
    volume_control_test = controldata.get_volume_control_by_name(volume_control.name)
    assert volume_control_test.name != ('' or None)
    assert volume_control.name == volume_control_test.name

    volume_control_test.set_suggested_name("bar")
    assert volume_control_test.name == "bar"

    # periodic control tests
    periodic_control_test = model.control_data.get_periodic_control_by_name("test")
    assert periodic_control_test is None

    # error on server side:
    # ansys.meshing.prime.internals.error_handling.PrimeRuntimeError:
    # Could not find method PrimeMesh::ControlData/CreatePeriodicControl

    # periodic_control = controldata.create_periodic_control()
    # periodic_control_test = controldata.get_periodic_control_by_name(periodic_control.name)
    # assert periodic_control_test.name != ('' or None)
    # assert periodic_control.name == periodic_control_test.name

    assert controldata.wrapper_controls == [wrapper_control]
    assert controldata.size_controls == [size_control]
    assert controldata.volume_controls == [volume_control]
    assert controldata.prism_controls == [prism_control]
    # assert controldata.periodic_controls == [periodic_control]

    # delete controls
    controls_ids = [wrapper_control.id, size_control.id, volume_control.id, prism_control.id]
    controldata.delete_controls(controls_ids)
    assert model.control_data.get_wrapper_control_by_name(wrapper_control.name) is None
    assert model.control_data.get_size_control_by_name(size_control.name) is None
    assert model.control_data.get_volume_control_by_name(volume_control.name) is None
    assert model.control_data.get_prism_control_by_name(prism_control.name) is None
