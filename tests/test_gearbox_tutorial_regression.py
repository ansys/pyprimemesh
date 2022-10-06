import ansys.meshing.prime as prime
import unittest
from .common import PrimeTestCase, PrimeTextTestRunner


class TestElbow(PrimeTestCase):
    def test_gearbox_tutorial(self):
        # downloads pmdat file
        wind_turbine = prime.examples.download_wind_turbine_stp()
        # reads file
        fileIO = prime.FileIO(model=self._model)
        _ = fileIO.read_pmdat(wind_turbine, prime.FileReadParams(model=self._model))
        mesher = prime.lucid.Mesh(self._model)
        # mesher.create_zones_from_labels("inlet,outlet")
        # mesher.surface_mesh(min_size=5, max_size=20)
        # result = mesher.volume_mesh(
        #    prism_layers=3,
        #    prism_surface_expression="* !inlet !outlet",
        #    volume_fill_type=pyprime.VolumeFillType.POLY,
        # )

        # copied from arm test
        mp = self._model.material_point_data.create_material_point(
            suggested_name="mp",
            coords=[-52.579027, 7.699242, 26.736631],
            params=prime.CreateMaterialPointParams(
                model=self._model, type=prime.MaterialPointType.DEAD
            ),
        )
        leak_prev = prime.LeakPreventionParams(
            self._model,
            material_points=[mp.assigned_name],
            scope=prime.ScopeDefinition(self._model, part_expression="*"),
            max_hole_size=10.0,
            n_expansion_layers=1,
        )

        gearbox_wrap = mesher.wrap(
            number_of_threads=6, min_size=0.4, max_size=50.0, leak_prevention_controls=[leak_prev]
        )
        part = self._model.get_part_by_name("__wrap__")
        part_summary_res = part.get_summary(prime.PartSummaryParams(model=self._model))

        # Validate number face zones
        self.assertEqual(part_summary_res.n_face_zones, 0)
        # Validate number of tri faces after importing case file
        self.assertTrue(1502912 * 0.95 <= part_summary_res.n_tri_faces <= 1502912 * 1.05)
        # Validate number of poly faces after importing case file
        self.assertTrue(part_summary_res.n_poly_faces, 0)

        # part = self._model.get_part_by_name("flow_volume")
        # part_summary_res = part.get_summary(prime.PartSummaryParams(model=self._model))
        # validate number of face zones
        # self.assertEqual(part_summary_res.n_face_zones, 2)
        # validate number of tri faces
        # self.assertEqual(part_summary_res.n_tri_faces, 0)
        # validate number of poly faces
        # self.assertTrue(1964 * 0.98 <= part_summary_res.n_poly_faces <= 1964 * 1.02)
        # validate number of poly cells
        # self.assertTrue(7424 * 0.98 <= part_summary_res.n_poly_cells <= 7424 * 1.02)


if __name__ == '__main__':
    unittest.main(testRunner=PrimeTextTestRunner, exit=False, verbosity=2)
