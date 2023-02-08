"""Tests for all control modules."""
from ansys.meshing.prime.params.primestructs import SizingType


def test_periodic_control(initialized_model_elbow):
    """Tests the methods and properties in periodic control."""
    model, _ = initialized_model_elbow
    test_control_data = model.control_data

    # periodic control tests
    periodic_control_test = test_control_data.get_periodic_control_by_name("test")
    assert periodic_control_test is None

    # TODO: error on server side:
    # ansys.meshing.prime.internals.error_handling.PrimeRuntimeError:
    # Could not find method PrimeMesh::controldata/CreatePeriodicControl

    periodic_control = test_control_data.create_periodic_control()
    periodic_control_test = test_control_data.get_periodic_control_by_name(periodic_control.name)
    assert periodic_control_test.name != ('' or None)
    assert periodic_control.name == periodic_control_test.name

    periodic_control_test.set_suggested_name("foo")
    assert periodic_control_test.name == "foo"

    assert test_control_data.periodic_controls == [periodic_control]

    # delete controls
    controls_ids = [periodic_control.id]
    test_control_data.delete_controls(controls_ids)
    assert model.control_data.get_periodic_control_by_name(periodic_control.name) is None


def test_wrapper_control(initialized_model_elbow):
    """Tests the methods and properties in wrapper control."""
    model, _ = initialized_model_elbow
    test_control_data = model.control_data

    # wrapper control tests
    wrapper_control_test = test_control_data.get_wrapper_control_by_name("test")
    assert wrapper_control_test is None

    wrapper_control = test_control_data.create_wrapper_control()
    wrapper_control_test = test_control_data.get_wrapper_control_by_name(wrapper_control.name)
    assert wrapper_control_test.name != ('' or None)
    assert wrapper_control_test.name == 'WrapperControl1'

    wrapper_control_test.set_suggested_name("foo")
    assert wrapper_control_test.name == "foo"

    assert test_control_data.wrapper_controls == [wrapper_control_test]
    controls_ids = [wrapper_control.id]
    test_control_data.delete_controls(controls_ids)
    assert model.control_data.get_wrapper_control_by_name(wrapper_control.name) is None


def test_size_control(initialized_model_elbow):
    """Tests the methods and properties in size control."""
    model, _ = initialized_model_elbow
    test_control_data = model.control_data

    # size control tests
    size_control_test = test_control_data.get_size_control_by_name("test")
    assert size_control_test is None

    size_control = test_control_data.create_size_control(SizingType.BOI)
    size_control_test = test_control_data.get_size_control_by_name(size_control.name)
    assert size_control_test.name != ('' or None)
    assert size_control.name == size_control_test.name

    size_control_test.set_suggested_name("foo")
    assert size_control_test.name == "foo"

    assert test_control_data.size_controls == [size_control]
    controls_ids = [size_control.id]
    test_control_data.delete_controls(controls_ids)
    assert model.control_data.get_size_control_by_name(size_control.name) is None


def test_prism_control(initialized_model_elbow):
    """Tests the methods and properties in prism control."""
    model, _ = initialized_model_elbow
    test_control_data = model.control_data
    # prism control tests
    prism_control_test = test_control_data.get_prism_control_by_name("test")
    assert prism_control_test is None

    prism_control = test_control_data.create_prism_control()
    prism_control_test = test_control_data.get_prism_control_by_name(prism_control.name)
    assert prism_control_test.name != ('' or None)
    assert prism_control.name == prism_control_test.name

    assert test_control_data.prism_controls == [prism_control]

    controls_ids = [prism_control.id]
    test_control_data.delete_controls(controls_ids)
    assert model.control_data.get_prism_control_by_name(prism_control.name) is None


def test_volume_control(initialized_model_elbow):
    """Tests the methods and properties in volume control."""
    model, _ = initialized_model_elbow
    test_control_data = model.control_data

    # volume control tests
    volume_control_test = test_control_data.get_volume_control_by_name("test")
    assert volume_control_test is None

    volume_control = test_control_data.create_volume_control()
    volume_control_test = test_control_data.get_volume_control_by_name(volume_control.name)
    assert volume_control_test.name != ('' or None)
    assert volume_control.name == volume_control_test.name

    volume_control_test.set_suggested_name("bar")
    assert volume_control_test.name == "bar"

    assert test_control_data.volume_controls == [volume_control]

    controls_ids = [volume_control.id]
    test_control_data.delete_controls(controls_ids)
    assert model.control_data.get_volume_control_by_name(volume_control.name) is None
