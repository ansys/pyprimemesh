import math

import ansys.meshing.prime as prime


def test_elbow_lucid(getRemoteClient):
    # downloads pmdat file
    elbow_lucid = prime.examples.download_elbow_pmdat()
    # elbow_lucid = prime.examples.download_elbow_scdoc()
    # reads file
    model = getRemoteClient.model
    fileIO = prime.FileIO(model=model)
    # _ = fileIO.read_pmdat(elbow_lucid, prime.FileReadParams(model=self._model))
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
    """self.assertEqual(
        part_summary_res.n_face_zones,
        2,
        msg="Validate number of face zones. Expected value: 2. Actual value: "
        + str(part_summary_res.n_face_zones),
    )
    # validate number of tri faces
    self.assertEqual(
        part_summary_res.n_tri_faces,
        0,
        msg="Validate number of tri faces. Expected value: 0. Actual value: "
        + str(part_summary_res.n_tri_faces),
    )
    # validate number of poly faces
    self.assertTrue(
        math.isclose(1964.0, float(part_summary_res.n_poly_faces), rel_tol=0.02),
        msg="Validate number of poly faces. Expected value: 1964, 2% tolerance. Actual value: "
        + str(part_summary_res.n_poly_faces),
    )
    # validate number of poly cells
    self.assertTrue(
        math.isclose(7613.0, float(part_summary_res.n_poly_cells), rel_tol=0.02),
        msg="Validate number of poly cells. Expected value: 7424, 2% tolerance. Actual value: "
        + str(part_summary_res.n_poly_cells),
    )"""
