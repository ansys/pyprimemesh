# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
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

from logging import Logger
from typing import List

from ansys.meshing import prime


def improve_quality(
    model: prime.Model,
    part: prime.Part,
    soft_target_skewness: float,
    hard_target_skewness: float,
    local_remesh_by_size_change: bool,
    keep_small_free_surfaces: bool,
):
    global_sf_params = model.get_global_sizing_params()
    register_id = 26
    surface_search = prime.SurfaceSearch(model)
    quality_params = prime.SearchByQualityParams(model, quality_limit=soft_target_skewness)
    collapse_tool = prime.CollapseTool(model)
    collapse_params = prime.CollapseParams(model)
    split_params = prime.SplitParams(model)
    quality_res = surface_search.search_zonelets_by_quality(
        part.id,
        part.get_face_zonelets(),
        register_id,
        quality_params,
    )
    if quality_res.n_found:
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )
        collapse_params.feature_type = prime.SurfaceFeatureType.ZONEBOUNDARY
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )
    thin_strip_params = prime.SearchByThinStripParams(
        model, quality_limit=soft_target_skewness, strip_height_limit=global_sf_params.min * 0.4
    )
    thin_strip_results = surface_search.search_zonelets_by_thin_strips(
        part_id=part.id,
        face_zonelets=part.get_face_zonelets(),
        register_id=register_id,
        params=thin_strip_params,
    )
    if thin_strip_results.n_found:
        collapse_params.feature_type = prime.SurfaceFeatureType.ZONEBOUNDARY
        collapse_params.collapse_ratio = 0.4
        split_params.split_ratio = 0.1
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )
    thin_strip_params = prime.SearchByThinStripParams(
        model,
        quality_limit=soft_target_skewness,
        strip_height_limit=global_sf_params.max,
        feature_type=prime.SurfaceFeatureType.FEATURE,
        feature_angle=155,
    )
    thin_strip_results = surface_search.search_zonelets_by_thin_strips(
        part_id=part.id,
        face_zonelets=part.get_face_zonelets(),
        register_id=register_id,
        params=thin_strip_params,
    )
    if thin_strip_results.n_found:
        collapse_params.feature_type = prime.SurfaceFeatureType.ZONEBOUNDARY
        collapse_params.collapse_ratio = 0.6
        split_params.split_ratio = 0.1
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )
    n_size_change_faces_found = 0
    surfer = prime.Surfer(model)
    if local_remesh_by_size_change:
        sc_quality_params = prime.SearchByQualityParams(model)
        sc_quality_params.face_quality_measure = prime.FaceQualityMeasure.SIZECHANGE
        sc_quality_params.quality_limit = 2.5
        quality_res = surface_search.search_zonelets_by_quality(
            part.id,
            part.get_face_zonelets(),
            register_id,
            sc_quality_params,
        )
        n_size_change_faces_found = quality_res.n_found
        if n_size_change_faces_found:
            local_surfer_params = prime.LocalSurferParams(model, max_angle=179.5)
            local_surfer_params.size_field_type = prime.SizeFieldType.VOLUMETRIC
            local_surfer_params.n_rings = 2
            surfer.remesh_face_zonelets_locally(
                part_id=part.id,
                face_zonelets=part.get_face_zonelets(),
                register_id=register_id,
                local_surfer_params=local_surfer_params,
            )
            quality_params.quality_limit = soft_target_skewness
            quality_res = surface_search.search_zonelets_by_quality(
                part.id,
                part.get_face_zonelets(),
                register_id,
                quality_params,
            )
            if quality_res.n_found:
                collapse_params = prime.CollapseParams(
                    model,
                    preserve_quality=True,
                    target_skewness=soft_target_skewness,
                )
                collapse_params.feature_type = prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
                split_params.split_ratio = 0.1
                collapse_tool.split_and_collapse_on_zonelets(
                    part_id=part.id,
                    face_zonelets=part.get_face_zonelets(),
                    register_id=register_id,
                    split_params=split_params,
                    collapse_params=collapse_params,
                )
                collapse_params.collapse_ratio = 0.4
                collapse_tool.split_and_collapse_on_zonelets(
                    part_id=part.id,
                    face_zonelets=part.get_face_zonelets(),
                    register_id=register_id,
                    split_params=split_params,
                    collapse_params=collapse_params,
                )
                collapse_params = prime.CollapseParams(
                    model,
                    preserve_quality=True,
                    target_skewness=hard_target_skewness,
                )
                collapse_params.feature_type = prime.SurfaceFeatureType.ZONEBOUNDARY
                collapse_tool.split_and_collapse_on_zonelets(
                    part_id=part.id,
                    face_zonelets=part.get_face_zonelets(),
                    register_id=register_id,
                    split_params=split_params,
                    collapse_params=collapse_params,
                )
                collapse_params.feature_type = prime.SurfaceFeatureType.NONE
                collapse_tool.split_and_collapse_on_zonelets(
                    part_id=part.id,
                    face_zonelets=part.get_face_zonelets(),
                    register_id=register_id,
                    split_params=split_params,
                    collapse_params=collapse_params,
                )
            params = prime.SearchBySelfIntersectionParams(model)
            search_results = surface_search.search_zonelets_by_self_intersections(
                part_id=part.id,
                face_zonelets=part.get_face_zonelets(),
                register_id=register_id,
                params=params,
            )
            if search_results.n_found:
                local_surfer_params = prime.LocalSurferParams(
                    model, growth_rate=1.2, min_angle=180, max_angle=180
                )
                local_surfer_params.size_field_type = prime.SizeFieldType.VOLUMETRIC
                local_surfer_params.n_rings = 1
                surfer.remesh_face_zonelets_locally(
                    part_id=part.id,
                    face_zonelets=part.get_face_zonelets(),
                    register_id=register_id,
                    local_surfer_params=local_surfer_params,
                )
    quality_params.quality_limit = soft_target_skewness
    quality_res = surface_search.search_zonelets_by_quality(
        part.id, part.get_face_zonelets(), register_id, quality_params
    )
    if quality_res.n_found > 0:
        collapse_params.feature_type = prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
        split_params.split_ratio = 0.4
        collapse_params = prime.CollapseParams(
            model,
            preserve_quality=True,
            target_skewness=soft_target_skewness,
        )
        collapse_params.collapse_ratio = 0.4
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )
        split_params.split_ratio = 0.1
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )
        collapse_params = prime.CollapseParams(
            model,
            preserve_quality=True,
            target_skewness=hard_target_skewness,
        )
        collapse_params.feature_type = prime.SurfaceFeatureType.ZONEBOUNDARY
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )
        collapse_params.feature_type = prime.SurfaceFeatureType.NONE
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )

    quality_res = surface_search.search_zonelets_by_quality(
        part.id, part.get_face_zonelets(), register_id, quality_params
    )
    if quality_res.n_found > 0:
        collapse_params.feature_type = prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
        split_params.split_ratio = 0.4
        collapse_params = prime.CollapseParams(
            model,
            preserve_quality=True,
            target_skewness=soft_target_skewness,
        )
        collapse_params.collapse_ratio = 0.4
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )
        split_params.split_ratio = 0.1
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )
        collapse_params = prime.CollapseParams(
            model,
            preserve_quality=True,
            target_skewness=hard_target_skewness,
        )
        collapse_params.feature_type = prime.SurfaceFeatureType.ZONEBOUNDARY
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )
        collapse_params.feature_type = prime.SurfaceFeatureType.NONE
        collapse_tool.split_and_collapse_on_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            split_params=split_params,
            collapse_params=collapse_params,
        )
        params = prime.SearchBySelfIntersectionParams(model)
        search_results = surface_search.search_zonelets_by_self_intersections(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            params=params,
        )
    delete_tool = prime.DeleteTool(model)
    zonelets = part.get_face_zonelets()
    delete_fringe_params = prime.DeleteFringesAndOverlapsParams(
        model,
        fringe_element_count=0 if keep_small_free_surfaces else 5,
        overlap_element_count=3,
        delete_overlaps=True,
    )
    delete_tool.delete_fringes_and_overlaps_on_zonelets(part.id, zonelets, delete_fringe_params)
    quality_params.quality_limit = hard_target_skewness
    quality_res = surface_search.search_zonelets_by_quality(
        part.id, part.get_face_zonelets(), register_id, quality_params
    )
    params = prime.SearchBySelfIntersectionParams(model)
    search_results = surface_search.search_zonelets_by_self_intersections(
        part_id=part.id,
        face_zonelets=part.get_face_zonelets(),
        register_id=register_id,
        params=params,
    )
    gs_params = model.get_global_sizing_params()
    if search_results.n_found > 0:
        if len(model.get_active_volumetric_size_fields()) == 0:
            local_surfer_params = prime.LocalSurferParams(
                model,
                min_size=gs_params.min,
                max_size=gs_params.max,
                growth_rate=1.2,
                min_angle=180,
                max_angle=180,
            )
            local_surfer_params.size_field_type = prime.SizeFieldType.MESHEDGEODESIC
        else:
            local_surfer_params = prime.LocalSurferParams(
                model, growth_rate=1.2, min_angle=180, max_angle=180
            )
            local_surfer_params.size_field_type = prime.SizeFieldType.VOLUMETRIC
        local_surfer_params.n_rings = 1
        surfer.remesh_face_zonelets_locally(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            local_surfer_params=local_surfer_params,
        )
        zonelets = part.get_face_zonelets()
        delete_tool.delete_fringes_and_overlaps_on_zonelets(part.id, zonelets, delete_fringe_params)


def cleanup_tri_mesh(
    model: prime.Model,
    part: prime.Part,
    collapse_sliver_faces: bool,
    stitch_free_faces: bool,
    keep_small_free_surfaces: bool,
    logger: Logger,
):
    quality_reg_id = 26
    surface_search_tool = prime.SurfaceSearch(model)
    collapse_tool = prime.CollapseTool(model)
    quality_params = prime.SearchByQualityParams(
        model=model, quality_limit=0.98, face_quality_measure=prime.FaceQualityMeasure.SKEWNESS
    )
    collapse_params = prime.CollapseParams(model)
    split_params = prime.SplitParams(model)

    if not part.get_face_zonelets():
        logger.warning(f"Mesh cleanup skipped for topology part {part.name}.")
        return
    if collapse_sliver_faces:
        quality_res = surface_search_tool.search_zonelets_by_quality(
            part.id, part.get_face_zonelets(), quality_reg_id, quality_params
        )
        if quality_res.n_found:
            collapse_params.feature_type = prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
            collapse_tool.split_and_collapse_on_zonelets(
                part_id=part.id,
                face_zonelets=part.get_face_zonelets(),
                register_id=quality_reg_id,
                split_params=split_params,
                collapse_params=collapse_params,
            )
            collapse_params.feature_type = prime.SurfaceFeatureType.ZONEBOUNDARY
            collapse_tool.split_and_collapse_on_zonelets(
                part_id=part.id,
                face_zonelets=part.get_face_zonelets(),
                register_id=quality_reg_id,
                split_params=split_params,
                collapse_params=collapse_params,
            )
    diag_params = prime.SurfaceDiagnosticSummaryParams(
        model,
        scope=prime.ScopeDefinition(model, part_expression=part.name),
        compute_self_intersections=False,
        compute_free_edges=True,
        compute_multi_edges=False,
        compute_duplicate_faces=False,
    )
    if stitch_free_faces:
        checks = surface_search_tool.get_surface_diagnostic_summary(diag_params)
        if checks.n_free_edges:
            part_zonelets = part.get_face_zonelets()
            connect = prime.Connect(model)
            connect_params = prime.StitchParams(
                model=model,
                enable_multi_threading=True,
                type=prime.StitchType.FREEFREE,
                remesh=False,
            )
            connect_params.tolerance = 0.2
            connect_params.use_absolute_tolerance = False
            connect.stitch_face_zonelets(
                part.id,
                part_zonelets,
                part_zonelets,
                connect_params,
            )
            tols = [1.5, 2]
            for tol in tols:
                checks = surface_search_tool.get_surface_diagnostic_summary(diag_params)
                if checks.n_free_edges == 0:
                    break
                connect_params.tolerance = 0.2 * tol * tol
                connect.stitch_face_zonelets(
                    part.id,
                    part.get_face_zonelets(),
                    part.get_face_zonelets(),
                    connect_params,
                )
            quality_params.quality_limit = 0.98
            quality_res = surface_search_tool.search_zonelets_by_quality(
                part.id,
                part_zonelets,
                quality_reg_id,
                quality_params,
            )
            collapse_params.feature_type = prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
            collapse_tool.split_and_collapse_on_zonelets(
                part_id=part.id,
                face_zonelets=part_zonelets,
                register_id=quality_reg_id,
                split_params=split_params,
                collapse_params=collapse_params,
            )
    if not keep_small_free_surfaces:
        delete_tool = prime.DeleteTool(model)
        delete_fringe_params = prime.DeleteFringesAndOverlapsParams(
            model=model,
            fringe_element_count=5,
            overlap_element_count=1,
            delete_overlaps=True,
        )
        delete_tool.delete_fringes_and_overlaps_on_zonelets(
            part.id,
            part.get_face_zonelets(),
            delete_fringe_params,
        )


def check_surface_intersection(model: prime.Model, part: prime.Part):
    diag = prime.SurfaceSearch(model)
    register_id = 1
    self_inter_params = prime.SearchBySelfIntersectionParams(model)
    self_inter_res = diag.search_zonelets_by_self_intersections(
        part_id=part.id,
        face_zonelets=part.get_face_zonelets(),
        register_id=register_id,
        params=self_inter_params,
    )
    results = diag.get_search_info_by_register_id(
        part.get_face_zonelets(),
        register_id,
        prime.SearchInfoByRegisterIdParams(model),
    )
    all_locations = []
    for i in range(int(len(results.locations_found) / 3)):
        location = [
            results.locations_found[i * 3],
            results.locations_found[i * 3 + 1],
            results.locations_found[i * 3 + 2],
        ]
        all_locations.append(location)
    face_zonelets = results.face_zonelets_found
    return self_inter_res.n_found, all_locations, face_zonelets


def surface_mesh_check(model: prime.Model):
    params = prime.SurfaceDiagnosticSummaryParams(model)
    params.compute_self_intersections = True
    params.compute_free_edges = True
    params.compute_duplicate_faces = True
    search = prime.SurfaceSearch(model)
    result = search.get_surface_diagnostic_summary(params)
    return result


def free_elements_results(model: prime.Model, part: prime.Part):
    diag = prime.SurfaceSearch(model)
    register_id = 2
    command_name = "PrimeMesh::SurfaceSearch/SearchZoneletsByFreeEdges"
    params = {"minFreeEdges": 0}
    args = {
        "part_id": part.id,
        "face_zonelets": part.get_face_zonelets(),
        "register_id": register_id,
        "params": params,
    }
    free_element_res = model._comm.serve(
        model,
        command_name,
        diag._object_id,
        args=args,
    )
    results = diag.get_search_info_by_register_id(
        part.get_face_zonelets(),
        register_id,
        prime.SearchInfoByRegisterIdParams(model),
    )
    all_locations = []
    for i in range(int(len(results.locations_found) / 3)):
        location = [
            results.locations_found[i * 3],
            results.locations_found[i * 3 + 1],
            results.locations_found[i * 3 + 2],
        ]
        all_locations.append(location)
    face_zonelets = results.face_zonelets_found
    return free_element_res["nFound"], all_locations, face_zonelets


def smooth_dihedral_faces(model: prime.Model, part: prime.Part, fluid_volumes: List[int]):
    fluid_zonelets = part.get_face_zonelets_of_volumes(fluid_volumes)
    if len(fluid_zonelets) > 0:
        result = diahedral_angle_results(model, part, fluid_zonelets)
        if result[0] > 0:
            surface_utils = prime.SurfaceUtilities(model)
            smooth_params = prime.SmoothDihedralFaceNodesParams(
                model,
                min_dihedral_angle=20.0,
                tolerance=0.3,
                type=prime.SmoothType.INFLATE,
            )
            fluid_zonelets = part.get_face_zonelets_of_volumes(fluid_volumes)
            surface_utils.smooth_dihedral_face_nodes(fluid_zonelets, smooth_params)
            smooth_params.type = prime.SmoothType.SMOOTH
            surface_utils.smooth_dihedral_face_nodes(fluid_zonelets, smooth_params)
        surf_inter_res = check_surface_intersection(model, part)
        if surf_inter_res[0]:
            improve_quality(model, part, 0.9, 0.95, False, True)
        surf_inter_res = check_surface_intersection(model, part)
        if surf_inter_res[0]:
            raise RuntimeError("Face elements found intersecting")


def diahedral_angle_results(model: prime.Model, part: prime.Part, face_zonelets: List[int]):
    diag = prime.SurfaceSearch(model)
    register_id = 3
    command_name = "PrimeMesh::SurfaceSearch/SearchZoneletsByDihedralAngle"
    params = {"minAngle": 5, "faceOrientationCorrectionType": 2}
    args = {
        "part_id": part.id,
        "face_zonelets": face_zonelets,
        "register_id": register_id,
        "params": params,
    }
    diahedral_angle_results = model._comm.serve(
        model,
        command_name,
        diag._object_id,
        args=args,
    )
    results = diag.get_search_info_by_register_id(
        part.get_face_zonelets(),
        register_id,
        prime.SearchInfoByRegisterIdParams(model),
    )
    all_locations = []
    for i in range(int(len(results.locations_found) / 3)):
        location = [
            results.locations_found[i * 3],
            results.locations_found[i * 3 + 1],
            results.locations_found[i * 3 + 2],
        ]
        all_locations.append(location)
    diahedral_angle_face_zonelets = results.face_zonelets_found
    return diahedral_angle_results["nFound"], all_locations, diahedral_angle_face_zonelets
