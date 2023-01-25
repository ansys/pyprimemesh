import ansys.meshing.prime as prime
from ansys.meshing.prime.autogen.primeconfig import ErrorCode


def test_surface_utilities(initialized_model_elbow):
    """Tests the SurfaceUtilities class initialization and methods."""
    model, mesher = initialized_model_elbow
    surf_utils = prime.SurfaceUtilities(model)

    # get the zonelets from one of the parts
    face_zonelets = model.parts[0].get_face_zonelets()

    # add some thickness to the selected face zonelets
    surf_utils_params = prime.AddThicknessParams(model, 0.3, False)
    result = surf_utils.add_thickness(face_zonelets, surf_utils_params)
    assert result.error_code == ErrorCode.NOERROR
