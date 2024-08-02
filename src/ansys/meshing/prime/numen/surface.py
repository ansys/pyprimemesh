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

"""Module for surface mesh."""
import logging
import time

import ansys.meshing.prime.numen.controls as controls
import ansys.meshing.prime.numen.utils.macros as macros
from ansys.meshing import prime
from ansys.meshing.prime.internals.error_handling import (
    PrimeRuntimeError,
    PrimeRuntimeWarning,
)
from ansys.meshing.prime.numen.utils import surface_utils
from ansys.meshing.prime.numen.utils.cached_data import CachedData, create_size_control
from ansys.meshing.prime.numen.utils.communicator import call_method


def mesh(model: prime.Model, mesh_params: dict, cached_data: CachedData):
    """Perform surface mesh based on sizing type."""
    size_field_names = mesh_params["size_field_names"]
    part_scope = mesh_params["part_expression"]
    part_ids = macros._get_part_ids(model, part_scope)
    sizing_type_mapping = {
        "volumetric": prime.SizeFieldType.VOLUMETRIC,
        "constant": prime.SizeFieldType.CONSTANT,
    }
    sizing_type = sizing_type_mapping[mesh_params["sizing_type"]]
    for name in size_field_names:
        cached_data.create_cached_object(name)
    if len(part_ids) == 0:
        part_ids = [part.id for part in model.parts]

    if mesh_params["mesh_type"] == "quadratic":
        generate_quads_param = True
    else:
        generate_quads_param = False
    surfer_params = prime.SurferParams(
        model=model, size_field_type=sizing_type, generate_quads=generate_quads_param
    )
    if sizing_type == prime.SizeFieldType.CONSTANT:
        surfer_params.constant_size = mesh_params.get("constant_size")
    sufer = prime.Surfer(model)
    for part_id in part_ids:
        part = model.get_part(part_id)
        topo_faces = part.get_topo_faces()
        surfer_result = sufer.mesh_topo_faces(part_id, topo_faces, surfer_params)

    for name in size_field_names:
        cached_data.destroy_cached_object(name)


def mesh_with_sizing(model: prime.Model, mesh_params: dict, cached_data: CachedData):
    min_s = mesh_params["min_size"]
    max_s = mesh_params["max_size"]
    gr = mesh_params["growth_rate"]
    part_scope = mesh_params["part_expression"]
    retain_generated_size_field = mesh_params["retain_generated_size_field"]
    sf_per_part = mesh_params["size_field_computation_per_part"]
    robust_mode = mesh_params["robust_mode"]
    robust_rbf = mesh_params["_rbf_interpolation"]
    robust_stitch = mesh_params["_stitch_failed_sliver_topofaces"]
    threaded_surfer = mesh_params["_threaded_surfer"]
    threaded_sf = mesh_params["_threaded_size_field_compute"]
    active_size_fields = model.get_active_volumetric_size_fields()
    sf_time = 0
    meshing_time = 0
    if len(active_size_fields) > 0:
        model.deactivate_volumetric_size_fields(active_size_fields)
    model.set_global_sizing_params(prime.GlobalSizingParams(model, min_s, max_s, gr))
    part_ids = macros._get_part_ids(model, part_scope)

    size_field = prime.SizeField(model)
    periodic_params = prime.SFPeriodicParams(model, angle=0.0)
    size_field_params = prime.VolumetricSizeFieldComputeParams(
        model, periodic_params=periodic_params, enable_multi_threading=threaded_sf
    )
    size_controls = mesh_params["size_controls"]
    if not sf_per_part:
        sf_time_start = time.time()
        size_control_ids = []
        for size_control in size_controls:
            size_control_params = {
                "sizing_type": controls._get_size_control_type(size_control),
                "sizing_params": controls._get_size_control_params(model, size_control),
                "scope": controls._get_scope(model, size_control),
            }
            size_control_id = create_size_control(model, size_control_params, cached_data)
            size_control_ids.append(size_control_id)

        size_field_res = size_field.compute_volumetric(size_control_ids, size_field_params)
        sf_time = time.time() - sf_time_start

    model.logger.python_logger.disabled = True
    surfer_params = prime.SurferParams(
        model=model,
        size_field_type=prime.SizeFieldType.VOLUMETRIC,
        project_on_geometry=True,
        enable_multi_threading=threaded_surfer,
        enableRobustMode=robust_mode,
        robustModeParams={
            "retryWithRBFInterpolation": robust_rbf,
            "stitchFailedSliverTopoFaces": robust_stitch,
        },
    )
    model.logger.python_logger.disabled = False
    surfer = prime.Surfer(model)
    for part_id in part_ids:
        part = model.get_part(part_id)
        topo_faces = part.get_topo_faces()
        if len(topo_faces) > 0:
            cached_data._logger.info(f"    Meshing part \"{part.name}\"")
            if sf_per_part:
                sf_time_start = time.time()
                try:
                    size_control_ids = []
                    for size_control in size_controls:
                        if size_control["control_type"] == 'boi':
                            size_control_params = {
                                "sizing_type": controls._get_size_control_type(size_control),
                                "sizing_params": controls._get_size_control_params(
                                    model, size_control
                                ),
                                "scope": controls._get_scope(model, size_control),
                            }
                            size_control_id = create_size_control(
                                model, size_control_params, cached_data
                            )
                            size_control_ids.append(size_control_id)
                        elif macros._check_size_control_scope(
                            model,
                            part_id,
                            size_control["entity_type"],
                            size_control["entity_scope"],
                            size_control["scope_evaluation_type"],
                        ):
                            sc_part_scope = size_control["part_expression"]
                            sc_part_ids = macros._get_part_ids(model, sc_part_scope)
                            if part_id in sc_part_ids:
                                sc_scope = controls._get_scope(model, size_control)
                                sc_scope.part_expression = part.name
                                size_control_params = {
                                    "sizing_type": controls._get_size_control_type(size_control),
                                    "sizing_params": controls._get_size_control_params(
                                        model, size_control
                                    ),
                                    "scope": sc_scope,
                                }
                                size_control_id = create_size_control(
                                    model, size_control_params, cached_data
                                )
                                size_control_ids.append(size_control_id)
                    size_field_res = size_field.compute_volumetric(
                        size_control_ids, size_field_params
                    )
                    size_field_name = mesh_params["size_field_per_part_prefix"] + "_" + part.name
                    args = {"size_field_id": size_field_res.size_field_id, "name": size_field_name}
                    call_method(model, "PrimeMesh::Model/SetSizeFieldName", model._object_id, args)
                except Exception as e:
                    cached_data._logger.info(f"    Failed to compute SizeField on {part.name}")
                    continue
                finally:
                    sf_time = sf_time + (time.time() - sf_time_start)
            model.logger.python_logger.disabled = True
            model.topo_data.delete_mesh_on_topo_faces(
                topo_faces, prime.DeleteMeshParams(model, True)
            )
            model.logger.python_logger.disabled = False
            try:
                mesh_time_start = time.time()
                surfer.mesh_topo_faces(part_id, topo_faces, surfer_params)
                n_unmeshed_topo_faces = part.get_summary(
                    prime.PartSummaryParams(model)
                ).n_unmeshed_topo_faces
                if n_unmeshed_topo_faces:
                    unmeshed_faces = [
                        face
                        for face in topo_faces
                        if not model.topo_data.get_mesh_zonelets_of_topo_faces([face])
                    ]
                    cached_data._logger.warning(
                        "    Unmeshed topo face ids "
                        + str(unmeshed_faces)
                        + " on part "
                        + part.name
                    )
            except PrimeRuntimeError as error:
                cached_data._logger.warning(
                    "    Error with code '{}' on '{}' with message '{}'".format(
                        error.error_code,
                        part.name,
                        error.message,
                    )
                )
                if mesh_params["stop_on_failure"] == True:
                    break
            except PrimeRuntimeWarning as warning:
                cached_data._logger.warning(
                    "    Warning: '{}' with message '{}'.".format(
                        part.name,
                        warning.message,
                    )
                )
            finally:
                meshing_time = meshing_time + (time.time() - mesh_time_start)
        else:
            cached_data._logger.warning(f"    No topoface was found in part \"{part.name}\"")
        if sf_per_part and retain_generated_size_field:
            model.deactivate_volumetric_size_fields([size_field_res.size_field_id])
        if not retain_generated_size_field:
            model.delete_volumetric_size_fields([size_field_res.size_field_id])
            model.control_data.delete_controls(size_control_ids)
            size_control_ids = []

    if not retain_generated_size_field and not sf_per_part:
        model.delete_volumetric_size_fields([size_field_res.size_field_id])
    if len(size_control_ids) > 0:
        model.control_data.delete_controls(size_control_ids)
    if len(active_size_fields) > 0:
        model.activate_volumetric_size_fields(active_size_fields)

    _log_time("SizeField computation time ", sf_time, cached_data._logger)
    _log_time("Surface meshing time       ", meshing_time, cached_data._logger)


def mesh_with_size_controls(model: prime.Model, mesh_params: dict, cached_data: CachedData):
    part_scope = mesh_params["part_expression"]
    part_ids = macros._get_part_ids(model, part_scope)

    size_control_ids = []
    size_controls = mesh_params["size_controls"]

    for size_control in size_controls:
        size_control_ids.append(cached_data.create_cached_object(size_control))

    size_field = prime.SizeField(model)
    periodic_params = prime.SFPeriodicParams(model, angle=0.0)
    size_field_params = prime.VolumetricSizeFieldComputeParams(
        model, periodic_params=periodic_params
    )
    size_field_res = size_field.compute_volumetric(size_control_ids, size_field_params)

    surfer_params = prime.SurferParams(model=model, size_field_type=prime.SizeFieldType.VOLUMETRIC)
    surfer = prime.Surfer(model)
    for part_id in part_ids:
        part = model.get_part(part_id)
        topo_faces = part.get_topo_faces()
        surfer.mesh_topo_faces(part_id, topo_faces, surfer_params)

    model.delete_volumetric_size_fields([size_field_res.size_field_id])
    for size_control in size_controls:
        cached_data.destroy_cached_object(size_control)


def post_mesh_cleanup(model: prime.Model, improve_quality_params: dict, cached_data: CachedData):
    part_scope = improve_quality_params["part_expression"]
    soft_target_skewness = improve_quality_params["soft_target_skewness"]
    hard_target_skewness = improve_quality_params["hard_target_skewness"]
    local_remesh_by_size_change = improve_quality_params["local_remesh_by_size_change"]
    keep_small_free_surfaces = improve_quality_params["keep_small_free_surfaces"]
    collapse_sliver_faces = improve_quality_params["collapse_sliver_faces"]
    stitch_free_faces = improve_quality_params["stitch_free_faces"]

    part_ids = macros._get_part_ids(model, part_scope)
    for part_id in part_ids:
        part = model.get_part(part_id)
        if stitch_free_faces or collapse_sliver_faces:
            surface_utils.cleanup_tri_mesh(
                model,
                part,
                collapse_sliver_faces,
                stitch_free_faces,
                keep_small_free_surfaces,
                cached_data._logger,
            )
        surface_utils.improve_quality(
            model,
            part,
            soft_target_skewness,
            hard_target_skewness,
            local_remesh_by_size_change,
            keep_small_free_surfaces,
        )

def clean_up_topo_mesh_triangles(
    model: prime.Model, part: prime.Part, clean_up_triangles_params: dict, cached_data: CachedData
):
    stitch_free_faces = True
    stitch_tolerance = 0.2
    stitch_tolerance_absolute = False
    surface_search_tool = prime.SurfaceSearch(model=model)
    part_id = part.id
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
        if checks.n_free_edges > 0:
            if checks.n_free_edges > 0:
                part_topofaces = part.get_topo_faces()
                connect = prime.Connect(model)
                connect_params = prime.StitchParams(
                    model=model,
                    enable_multi_threading=True,
                    type=prime.StitchType.FREEFREE,
                    remesh=False,
                )
                connect_params.tolerance = stitch_tolerance
                connect_params.use_absolute_tolerance = stitch_tolerance_absolute
                # [TODO] implement code to get zonelets with free edges only
                # and get one or two layers around them and pass as input
                args = {
                    "part_id": part.id,
                    "topo_faces": part_topofaces,
                    "with_topo_faces": part_topofaces,
                    "params": connect_params._jsonify(),
                }
                command_name = "PrimeMesh::Connect/StitchMeshOfTopoFaces"
                result = connect._comm.serve(model, command_name, connect._object_id, args=args)
                tols = [1.5, 2]
                for tol in tols:
                    checks = surface_search_tool.get_surface_diagnostic_summary(diag_params)
                    if checks.n_free_edges == 0:
                        break
                    connect_params.tolerance = stitch_tolerance * tol * tol
                    args = {
                        "part_id": part.id,
                        "topo_faces": part_topofaces,
                        "with_topo_faces": part_topofaces,
                        "params": connect_params._jsonify(),
                    }
                    command_name = "PrimeMesh::Connect/StitchMeshOfTopoFaces"
                    results = connect._comm.serve(
                        model, command_name, connect._object_id, args=args
                    )
    diag_params = prime.SurfaceDiagnosticSummaryParams(
        model,
        scope=prime.ScopeDefinition(model, part_expression=part.name),
        compute_self_intersections=True,
        compute_free_edges=True,
        compute_multi_edges=True,
        compute_duplicate_faces=True,
    )
    checks = surface_search_tool.get_surface_diagnostic_summary(diag_params)
    if (
        checks.n_free_edges > 0
        or checks.n_multi_edges > 0
        or checks.n_self_intersections > 0
        or checks.n_duplicate_faces > 0
    ):
        info1 = f"{part.name} : {checks.n_free_edges} {checks.n_multi_edges}"
        info2 = f" {checks.n_self_intersections} {checks.n_duplicate_faces}"
        cached_data._logger.info(info1 + info2)


def clean_up_non_topo_mesh_triangles(
    model: prime.Model, part: prime.Part, clean_up_triangles_params: dict, cached_data: CachedData
):
    collapse_sliver_faces = True
    stitch_free_faces = True
    stitch_tolerance = 0.2
    stitch_tolerance_absolute = False
    keep_small_free_surfaces = False
    quality_reg_id = 26
    surface_search_tool = prime.SurfaceSearch(model=model)
    collapse_tool = prime.CollapseTool(model=model)
    quality_params = prime.SearchByQualityParams(
        model=model, quality_limit=0.98, face_quality_measure=prime.FaceQualityMeasure.SKEWNESS
    )
    collapse_params = prime.CollapseParams(model=model)
    split_params = prime.SplitParams(model=model)
    part_id = part.id
    if collapse_sliver_faces:
        quality_res = surface_search_tool.search_zonelets_by_quality(
            part_id, part.get_face_zonelets(), quality_reg_id, quality_params
        )
        if quality_res.n_found > 0:
            collapse_params.feature_type = prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
            collapse_tool.split_and_collapse_on_zonelets(
                part_id=part_id,
                face_zonelets=part.get_face_zonelets(),
                register_id=quality_reg_id,
                split_params=split_params,
                collapse_params=collapse_params,
            )
            collapse_params.feature_type = prime.SurfaceFeatureType.ZONEBOUNDARY
            collapse_tool.split_and_collapse_on_zonelets(
                part_id=part_id,
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
        if checks.n_free_edges > 0:
            if checks.n_free_edges > 0:
                part_zonelets = part.get_face_zonelets()
                connect = prime.Connect(model)
                connect_params = prime.StitchParams(
                    model=model,
                    enable_multi_threading=True,
                    type=prime.StitchType.FREEFREE,
                    remesh=False,
                )
                connect_params.tolerance = stitch_tolerance
                connect_params.use_absolute_tolerance = stitch_tolerance_absolute
                results = connect.stitch_face_zonelets(
                    part_id, part_zonelets, part_zonelets, connect_params
                )
                tols = [1.5, 2]
                for tol in tols:
                    checks = surface_search_tool.get_surface_diagnostic_summary(diag_params)
                    if checks.n_free_edges == 0:
                        break
                    connect_params.tolerance = stitch_tolerance * tol * tol
                    results = connect.stitch_face_zonelets(
                        part_id, part.get_face_zonelets(), part.get_face_zonelets(), connect_params
                    )
                quality_params.quality_limit = 0.98
                quality_res = surface_search_tool.search_zonelets_by_quality(
                    part_id, part_zonelets, quality_reg_id, quality_params
                )
                collapse_params.feature_type = prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
                collapse_tool.split_and_collapse_on_zonelets(
                    part_id=part_id,
                    face_zonelets=part_zonelets,
                    register_id=quality_reg_id,
                    split_params=split_params,
                    collapse_params=collapse_params,
                )
    if not keep_small_free_surfaces:
        delete_tool = prime.DeleteTool(model=model)
        delete_fringe_params = prime.DeleteFringesAndOverlapsParams(
            model=model, fringe_element_count=5, overlap_element_count=1, delete_overlaps=True
        )
        delete_tool.delete_fringes_and_overlaps_on_zonelets(
            part_id, part.get_face_zonelets(), delete_fringe_params
        )
    diag_params = prime.SurfaceDiagnosticSummaryParams(
        model,
        scope=prime.ScopeDefinition(model, part_expression=part.name),
        compute_self_intersections=True,
        compute_free_edges=True,
        compute_multi_edges=True,
        compute_duplicate_faces=True,
    )
    checks = surface_search_tool.get_surface_diagnostic_summary(diag_params)
    if (
        checks.n_free_edges > 0
        or checks.n_multi_edges > 0
        or checks.n_self_intersections > 0
        or checks.n_duplicate_faces > 0
    ):
        info1 = f"{part.name} : {checks.n_free_edges} {checks.n_multi_edges}"
        info2 = f" {checks.n_self_intersections} {checks.n_duplicate_faces}"
        cached_data._logger.info(info1 + info2)


def clean_up_triangles(
    model: prime.Model, clean_up_triangles_params: dict, cached_data: CachedData
):
    part_scope = clean_up_triangles_params["part_expression"]
    part_ids = macros._get_part_ids(model, part_scope)
    for part_id in part_ids:
        part = model.get_part(part_id)
        if len(part.get_topo_faces()) > 0:
            clean_up_topo_mesh_triangles(model, part, clean_up_triangles_params, cached_data)
        elif len(part.get_face_zonelets()) > 0:
            clean_up_non_topo_mesh_triangles(model, part, clean_up_triangles_params, cached_data)


def _log_time(message: str, measured_time: float, logger: logging.Logger):
    time_mins = int(measured_time) // 60
    time_secs = int(measured_time) % 60
    if time_mins:
        logger.info(f"    {message}: {time_mins} mins {time_secs} seconds")
    else:
        logger.info(f"    {message}: {time_secs} seconds")

