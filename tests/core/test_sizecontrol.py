import ansys.meshing.prime as prime


def test_sizecontrol(initialized_model_elbow):
    """Test the regular usage of SizeControl Class."""

    # load example from fixture
    model, _ = initialized_model_elbow

    # create a SizeControl object from the model
    size_control = model.control_data.create_size_control(prime.SizingType.CURVATURE)

    # change the name and check if it is working as intended
    result = size_control.set_suggested_name('bar')

    assert str(size_control) == (
        "\nSize Control Summary: \n    Name : bar\n    ID : 1\n    Type : Curvature\n    "
        "Min : 2\n    Max : 20\n    Growth Rate : 1.2\n    Normal Angle : 18\n    Scope "
        "(Used labels to evaluate Face zonelets) : \n"
    )
    assert result.assigned_name != ''
    assert result.assigned_name == size_control.name
