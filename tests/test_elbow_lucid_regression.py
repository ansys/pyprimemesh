import math

import ansys.meshing.prime as prime


def test_elbow_lucid(get_remote_client):
    # downloads pmdat file
    elbow_lucid = prime.examples.download_elbow_pmdat()
    # reads file
    model = get_remote_client.model
    fileIO = prime.FileIO(model=model)
    mesher = prime.lucid.Mesh(model)
    mesher.read(file_name=elbow_lucid)
    mesher.create_zones_from_labels("inlet,outlet")
    mesher.surface_mesh(min_size=5, max_size=20)
    result = mesher.volume_mesh(
        prism_layers=3,
        prism_surface_expression="* !inlet !outlet",
        volume_fill_type=prime.VolumeFillType.POLY,
    )
    part = model.get_part_by_name("flow_volume")
    part_summary_res = part.get_summary(prime.PartSummaryParams(model=model))
    # validate number of face zones
    assert part_summary_res.n_face_zones == 2

    # validate number of tri faces
    assert part_summary_res.n_tri_faces == 0

    # validate number of poly faces
    assert math.isclose(1964.0, float(part_summary_res.n_poly_faces), rel_tol=0.02)

    # validate number of poly cells
    assert math.isclose(7613.0, float(part_summary_res.n_poly_cells), rel_tol=0.02)
