# Copyright 2025 ANSYS, Inc. Unauthorized use, distribution, or duplication is prohibited.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Integration test for the toy car example."""
import math

import ansys.meshing.prime as prime


def test_toycar_tutorial(get_remote_client, get_examples):
    """Tests an use case with the toy car example."""

    toy_car = get_examples["toy_car"]
    model = get_remote_client.model

    # reads file
    _ = prime.FileIO(model=model).read_pmdat(toy_car, prime.FileReadParams(model=model))
    mesher = prime.lucid.Mesh(model)

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
    diag = prime.SurfaceSearch(model)
    diag_params = prime.SurfaceDiagnosticSummaryParams(
        model,
        scope=prime.ScopeDefinition(model=model, part_expression="*wrap*"),
        compute_free_edges=True,
        compute_multi_edges=True,
        compute_self_intersections=True,
    )
    diag_res = diag.get_surface_diagnostic_summary(diag_params)
    # Validate number of free edges after wrap
    assert diag_res.n_free_edges == 0

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
    wrapper_part = model.get_part_by_name("__wrap__.3")
    diag = prime.SurfaceSearch(model)
    diag_params = prime.SurfaceDiagnosticSummaryParams(
        model,
        scope=prime.ScopeDefinition(model=model, part_expression="__wrap__.3"),
        compute_free_edges=True,
        compute_multi_edges=True,
        compute_self_intersections=True,
    )
    diag_res = diag.get_surface_diagnostic_summary(diag_params)

    # Validate number of free edges
    assert diag_res.n_free_edges == 0

    # Validate number of multi edges
    assert diag_res.n_multi_edges == 0

    # Validate number of self inter faces
    assert diag_res.n_self_intersections == 0

    face_quality_measures = prime.FaceQualityMeasure.SKEWNESS
    quality = prime.SurfaceSearch(model)
    qual_summary_res = quality.get_surface_quality_summary(
        prime.SurfaceQualitySummaryParams(
            model=model,
            scope=prime.ScopeDefinition(model=model, part_expression="__wrap__.3"),
            face_quality_measures=[face_quality_measures],
            quality_limit=[0.9],
        )
    )

    part_summary_res = wrapper_part.get_summary(
        prime.PartSummaryParams(model=model, print_id=False, print_mesh=True)
    )
    # Validate number of tri faces
    assert math.isclose(178102.0, float(part_summary_res.n_faces), rel_tol=0.02)

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
    part = model.get_part_by_name("__wrap__.3")
    vtool = prime.VolumeMeshTool(model=model)
    result = vtool.check_mesh(part_id=part.id, params=prime.CheckMeshParams(model=model))

    # Validate quality check error code
    assert result.error_code is prime.ErrorCode.NOERROR
    # result.hasNonPositiveVolumes
    assert not result.has_non_positive_volumes

    # result.hasNonPositiveAreas
    assert not result.has_non_positive_areas

    # result.hasInvalidShape
    assert not result.has_invalid_shape

    # result.hasLeftHandedFaces
    assert not result.has_left_handed_faces

    quality = prime.VolumeSearch(model)
    qual_summary_res = quality.get_volume_quality_summary(
        prime.VolumeQualitySummaryParams(
            model=model,
            scope=prime.ScopeDefinition(model=model, part_expression="__wrap__.3"),
            cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS],
            quality_limit=[0.95],
        )
    )

    part_summary_res = wrapper_part.get_summary(
        prime.PartSummaryParams(model=model, print_id=False, print_mesh=True)
    )

    # Validate number of cells
    assert math.isclose(3384800.0, float(part_summary_res.n_cells), rel_tol=0.10)

    # Volume mesh quality
    assert qual_summary_res.quality_results_part[0].max_quality < 1

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
