# import os

# os.environ.clear()
import ansys.meshing.prime as prime
import unittest
from .common import PrimeTestCase, PrimeTextTestRunner
import math


class TestElbow(PrimeTestCase):
    def test_toycar_tutorial(self):
        # downloads pmdat file
        toy_car = prime.examples.download_toy_car_pmdat()
        # reads file
        fileIO = prime.FileIO(model=self._model)
        _ = fileIO.read_pmdat(toy_car, prime.FileReadParams(model=self._model))
        mesher = prime.lucid.Mesh(self._model)

        # several objects are open surfaces (with holes)
        # coarse wrap to close holes and delete originals
        coarse_wrap = {"cabin": 1.5, "exhaust": 0.5, "engine": 1.5}
        for part in coarse_wrap:
            mesher.wrap(
                input_parts=part,
                max_size=coarse_wrap[part],
                remesh_postwrap=False,
                enable_feature_octree_refinement=False,
            )
        diag = prime.SurfaceSearch(self._model)
        diag_params = prime.SurfaceDiagnosticSummaryParams(
            self._model,
            scope=prime.ScopeDefinition(model=self._model, part_expression="*wrap*"),
            compute_free_edges=True,
            compute_multi_edges=True,
            compute_self_intersections=True,
        )
        diag_res = diag.get_surface_diagnostic_summary(diag_params)
        # Validate number of free edges after wrap
        self.assertEqual(diag_res.n_free_edges, 0)

        # wrap full model and extract internal region
        wrap_car = mesher.wrap(
            min_size=0.1,
            max_size=2.0,
            region_extract=prime.WrapRegion.LARGESTINTERNAL,
            create_intersection_loops=True,
            # elements_per_gap=3,
            contact_prevention_size=0.1,
        )
        # validations
        wrapper_part = self._model.get_part_by_name("__wrap__.3")
        diag = prime.SurfaceSearch(self._model)
        diag_params = prime.SurfaceDiagnosticSummaryParams(
            self._model,
            scope=prime.ScopeDefinition(model=self._model, part_expression="__wrap__.3"),
            compute_free_edges=True,
            compute_multi_edges=True,
            compute_self_intersections=True,
        )
        diag_res = diag.get_surface_diagnostic_summary(diag_params)

        # Validate number of free edges
        self.assertEqual(
            diag_res.n_free_edges,
            0,
            msg="Validate number of free edges. Expected value: 0. Actual value: "
            + str(diag_res.n_free_edges),
        )
        # Validate number of multi edges
        self.assertEqual(
            diag_res.n_multi_edges,
            0,
            msg="Validate number of multi edges. Expected value: 0. Actual value: "
            + str(diag_res.n_multi_edges),
        )
        # Validate number of self inter faces
        self.assertEqual(
            diag_res.n_self_intersections,
            0,
            msg="Validate number of self inter faces. Expected value: 0. Actual value: "
            + str(diag_res.n_self_intersections),
        )

        face_quality_measures = prime.FaceQualityMeasure.SKEWNESS
        quality = prime.SurfaceSearch(self._model)
        qual_summary_res = quality.get_surface_quality_summary(
            prime.SurfaceQualitySummaryParams(
                model=self._model,
                scope=prime.ScopeDefinition(model=self._model, part_expression="__wrap__.3"),
                face_quality_measures=[face_quality_measures],
                quality_limit=[0.9],
            )
        )

        for summary_res in qual_summary_res.quality_results:
            print("Max surface skewness : ", summary_res.max_quality)
            print("no.of faces above 0.9 : ", summary_res.n_found)

        part_summary_res = wrapper_part.get_summary(
            prime.PartSummaryParams(model=self._model, print_id=False, print_mesh=True)
        )
        # Validate number of tri faces
        self.assertTrue(math.isclose(178102.0, float(part_summary_res.n_faces), rel_tol=0.02))

        mesher.create_zones_from_labels(
            """tunnel,cabin,outer,component21,component22,component24,component25,
            engine,exhaust,ground,inlet,outlet,wheel_1,wheel_2,wheel_3,wheel_4"""
        )

        # volume mesh
        mesher.compute_volumes()
        mesher.volume_mesh(
            prism_layers=3,
            prism_surface_expression="cabin*,component*,engine,exhaust,ground,outer,wheel*",
            prism_volume_expression="tunnel*",
            # volume_fill_type=prime.VolumeFillType.POLY
        )

        # mesh check
        part = self._model.get_part_by_name("__wrap__.3")
        vtool = prime.VolumeMeshTool(model=self._model)
        result = vtool.check_mesh(part_id=part.id, params=prime.CheckMeshParams(model=self._model))

        # Validate quality check error code
        self.assertTrue(result.error_code == prime.ErrorCode.NOERROR)
        # result.hasNonPositiveVolumes
        self.assertEqual(
            result.has_non_positive_volumes,
            False,
            msg="result.has_non_positive_volumes Expected value: False. Actual value: "
            + str(result.has_non_positive_volumes),
        )
        # result.hasNonPositiveAreas
        self.assertEqual(
            result.has_non_positive_areas,
            False,
            msg="result.has_non_positive_areas Expected value: False. Actual value: "
            + str(result.has_non_positive_areas),
        )
        # result.hasInvalidShape
        self.assertEqual(
            result.has_invalid_shape,
            False,
            msg="result.has_invalid_shape Expected value: False. Actual value: "
            + str(result.has_invalid_shape),
        )
        # result.hasLeftHandedFaces
        self.assertEqual(
            result.has_left_handed_faces,
            False,
            msg="result.hasLeftHandedFaces Expected value: False. Actual value: "
            + str(result.has_left_handed_faces),
        )

        quality = prime.VolumeSearch(self._model)
        qual_summary_res = quality.get_volume_quality_summary(
            prime.VolumeQualitySummaryParams(
                model=self._model,
                scope=prime.ScopeDefinition(model=self._model, part_expression="__wrap__.3"),
                cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS],
                quality_limit=[0.95],
            )
        )

        part_summary_res = wrapper_part.get_summary(
            prime.PartSummaryParams(model=self._model, print_id=False, print_mesh=True)
        )

        # Validate number of cells
        self.assertTrue(
            math.isclose(3384800.0, float(part_summary_res.n_cells), rel_tol=0.10),
            msg="Validate number of cells. Expected value: 3384800, 1% tolerance. Actual value: "
            + str(part_summary_res.n_cells),
        )
        # Volume mesh quality
        self.assertTrue(
            qual_summary_res.quality_results_part[0].max_quality < 1,
            msg="Validate max skewness. Expected value: <1. Actual value: "
            + str(qual_summary_res.quality_results_part[0].max_quality),
        )

        # Validate number of cells violating skewness 0.95
        # if os.name == 'nt':
        #    self.assertTrue(
        #        math.isclose(
        #            106.0, float(qual_summary_res.quality_results_part[0].n_found), rel_tol=0.10
        #        ),
        #        msg="""Validate number of cells violating skewness 0.95.
        #         Expected value: 106, 10% tolerance. Actual value: """
        #        + str(qual_summary_res.quality_results_part[0].n_found),
        #    )
        # elif os.name == 'posix':
        #    self.assertTrue(
        #        math.isclose(
        #            200.0, float(qual_summary_res.quality_results_part[0].n_found), rel_tol=0.10
        #        ),
        #        msg="""Validate number of cells violating skewness 0.95.
        #         Expected value: 200, 10% tolerance. Actual value: """
        #        + str(qual_summary_res.quality_results_part[0].n_found),
        #    )


if __name__ == '__main__':
    unittest.main(testRunner=PrimeTextTestRunner, exit=False, verbosity=2)
