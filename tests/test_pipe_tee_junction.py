import math

import ansys.meshing.prime as prime


def test_pipe_tee_junction(get_remote_client):
    # downloads pmdat file
    pipe_tee = prime.examples.download_pipe_tee_pmdat()
    # reads file
    model = get_remote_client.model
    fileIO = prime.FileIO(model=model)
    mesher = prime.lucid.Mesh(model)
    mesher.read(file_name=pipe_tee)
    wrap = mesher.wrap(min_size=6, region_extract=prime.WrapRegion.LARGESTINTERNAL)
    # set global sizing
    params = prime.GlobalSizingParams(model, min=6, max=50)
    model.set_global_sizing_params(params)

    mesher.create_zones_from_labels("outlet_main,in1_inlet,in2_inlet")

    mesher.volume_mesh(
        prism_layers=5,
        prism_surface_expression="* !*inlet* !*outlet*",
        volume_fill_type=prime.VolumeFillType.POLY,
    )
    # Get statistics on the mesh
    part = model.get_part_by_name("__wrap__")
    part_summary_res = part.get_summary(prime.PartSummaryParams(model=model))
    # validate number of tri faces
    assert part_summary_res.n_tri_faces == 0

    # validate number of poly faces
    assert math.isclose(16717, float(part_summary_res.n_poly_faces), rel_tol=0.02)
    # validate number of poly cells
    assert math.isclose(97341, float(part_summary_res.n_poly_cells), rel_tol=0.05)
