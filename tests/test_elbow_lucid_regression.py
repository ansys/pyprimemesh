import ansys.meshing.prime as pyprime
import unittest
import math
from .common import PrimeTestCase, PrimeTextTestRunner


class TestElbow(PrimeTestCase):
    def test_elbow_lucid(self):
        # downloads pmdat file
        elbow_lucid = pyprime.examples.download_elbow_pmdat()
        # reads file
        fileIO = pyprime.FileIO(model=self._model)
        _ = fileIO.read_pmdat(elbow_lucid, pyprime.FileReadParams(model=self._model))
        mesher = pyprime.lucid.Mesh(self._model)
        mesher.create_zones_from_labels("inlet,outlet")
        mesher.surface_mesh(min_size=5, max_size=20)
        result = mesher.volume_mesh(
            prism_layers=3,
            prism_surface_expression="* !inlet !outlet",
            volume_fill_type=pyprime.VolumeFillType.POLY,
        )
        part = self._model.get_part_by_name("flow_volume")
        part_summary_res = part.get_summary(pyprime.PartSummaryParams(model=self._model))
        # validate number of face zones
        self.assertEqual(
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
            math.isclose(7424.0, float(part_summary_res.n_poly_cells), rel_tol=0.02),
            msg="Validate number of poly cells. Expected value: 7424, 2% tolerance. Actual value: "
            + str(part_summary_res.n_poly_cells),
        )


if __name__ == '__main__':
    unittest.main(testRunner=PrimeTextTestRunner, exit=False, verbosity=2)
