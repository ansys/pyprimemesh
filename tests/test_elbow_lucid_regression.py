import ansys.meshing.prime as pyprime
import unittest
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
        self.assertEqual(part_summary_res.n_face_zones, 2)
        # validate number of tri faces
        self.assertEqual(part_summary_res.n_tri_faces, 0)
        # validate number of poly faces
        self.assertTrue(1964 * 0.98 <= part_summary_res.n_poly_faces <= 1964 * 1.02)
        # validate number of poly cells
        self.assertTrue(7424 * 0.98 <= part_summary_res.n_poly_cells <= 7424 * 1.02)


if __name__ == '__main__':
    unittest.main(testRunner=PrimeTextTestRunner, exit=False, verbosity=2)
