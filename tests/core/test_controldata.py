"""Tests for all control modules."""
import pytest

from ansys.meshing.prime.params.primestructs import SizingType


@pytest.mark.skip(reason="Periodic control is broken in Prime server version <= 23.1")
def test_periodic_control(initialized_model_elbow):
    """Tests the methods and properties from ControlData class and control classes."""
    model, _ = initialized_model_elbow
    controldata = model.control_data

    # periodic control tests
    periodic_control_test = model.control_data.get_periodic_control_by_name("test")
    assert periodic_control_test is None

    # TODO: error on server side:
    # ansys.meshing.prime.internals.error_handling.PrimeRuntimeError:
    # Could not find method PrimeMesh::ControlData/CreatePeriodicControl

    periodic_control = controldata.create_periodic_control()
    periodic_control_test = controldata.get_periodic_control_by_name(periodic_control.name)
    assert periodic_control_test.name != ('' or None)
    assert periodic_control.name == periodic_control_test.name

    periodic_control_test.set_suggested_name("foo")
    assert periodic_control_test.name == "foo"

    assert controldata.periodic_controls == [periodic_control]

    # delete controls
    controls_ids = [periodic_control.id]
    controldata.delete_controls(controls_ids)
    assert model.control_data.get_periodic_control_by_name(periodic_control.name) is None


def test_wrapper_control(initialized_model_elbow):
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

    assert controldata.wrapper_controls == [wrapper_control_test]
    controls_ids = [wrapper_control.id]
    controldata.delete_controls(controls_ids)
    assert model.control_data.get_wrapper_control_by_name(wrapper_control.name) is None


def test_size_control(initialized_model_elbow):
    model, _ = initialized_model_elbow
    controldata = model.control_data

    # size control tests
    size_control_test = model.control_data.get_size_control_by_name("test")
    assert size_control_test is None

    size_control = controldata.create_size_control(SizingType.BOI)
    size_control_test = controldata.get_size_control_by_name(size_control.name)
    assert size_control_test.name != ('' or None)
    assert size_control.name == size_control_test.name

    size_control_test.set_suggested_name("foo")
    assert size_control_test.name == "foo"

    assert controldata.size_controls == [size_control]
    controls_ids = [size_control.id]
    controldata.delete_controls(controls_ids)
    assert model.control_data.get_size_control_by_name(size_control.name) is None


def test_prism_control(initialized_model_elbow):
    model, _ = initialized_model_elbow
    controldata = model.control_data
    # prism control tests
    prism_control_test = model.control_data.get_prism_control_by_name("test")
    assert prism_control_test is None

    prism_control = controldata.create_prism_control()
    prism_control_test = controldata.get_prism_control_by_name(prism_control.name)
    assert prism_control_test.name != ('' or None)
    assert prism_control.name == prism_control_test.name

    assert controldata.prism_controls == [prism_control]

    controls_ids = [prism_control.id]
    controldata.delete_controls(controls_ids)
    assert model.control_data.get_prism_control_by_name(prism_control.name) is None


def test_volume_control(initialized_model_elbow):
    model, _ = initialized_model_elbow
    controldata = model.control_data

    # volume control tests
    volume_control_test = model.control_data.get_volume_control_by_name("test")
    assert volume_control_test is None

    volume_control = controldata.create_volume_control()
    volume_control_test = controldata.get_volume_control_by_name(volume_control.name)
    assert volume_control_test.name != ('' or None)
    assert volume_control.name == volume_control_test.name

    volume_control_test.set_suggested_name("bar")
    assert volume_control_test.name == "bar"

    assert controldata.volume_controls == [volume_control]

    controls_ids = [volume_control.id]
    controldata.delete_controls(controls_ids)
    assert model.control_data.get_volume_control_by_name(volume_control.name) is None
