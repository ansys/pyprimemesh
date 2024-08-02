from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.cached_data import CachedData, create_size_control
import ansys.meshing.prime.numen.controls as controls
from ansys.meshing.prime.internals.error_handling import PrimeRuntimeError, PrimeRuntimeWarning
import ansys.meshing.prime.numen.utils.macros as macros
from ansys.meshing.prime.numen.utils import surface_utils

def mesh(model: prime.Model, mesh_params: dict, cached_data: CachedData):
    size_field_names = mesh_params["size_field_names"]
    part_scope = mesh_params["part_scope"]
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
    surfer_params = prime.SurferParams( model = model,
                                        size_field_type = sizing_type,
                                        generate_quads = generate_quads_param)
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
    part_scope = mesh_params["part_scope"]
    retain_generated_size_field = mesh_params["retain_generated_size_field"]
    sf_per_part = mesh_params["size_field_computation_per_part"]
    model.set_global_sizing_params(prime.GlobalSizingParams(model,
                                                            mesh_params["min_size"],
                                                            mesh_params["max_size"],
                                                            mesh_params["growth_rate"]))
    part_ids = macros._get_part_ids(model, part_scope)

    size_field = prime.SizeField(model)
    periodic_params = prime.SFPeriodicParams(model, angle = 0.0)
    size_field_params = prime.VolumetricSizeFieldComputeParams(model,
                                                        periodic_params = periodic_params)
    size_controls = mesh_params["size_controls"]
    if not sf_per_part:
        size_control_ids = []
        for size_control in size_controls:
            size_control_params = {
                "sizing_type": controls._get_size_control_type(size_control),
                "sizing_params": controls._get_size_control_params(model, size_control),
                "scope": controls._get_scope(model, size_control)
            }
            size_control_id = create_size_control(model, size_control_params, cached_data)
            size_control_ids.append(size_control_id)

        size_field_res = size_field.compute_volumetric(size_control_ids, size_field_params)

    surfer_params = prime.SurferParams(model=model, size_field_type=prime.SizeFieldType.VOLUMETRIC,
                                       project_on_geometry=True, enable_multi_threading=False)
    surfer = prime.Surfer(model)
    for part_id in part_ids:
        part = model.get_part(part_id)
        print("inprogress=======================\n")
        print(part.name)
        if sf_per_part:
            size_control_ids = []
            for size_control in size_controls:
                if(macros._check_size_control_scope(model, part_id, size_control["entity_type"],
                                                    size_control["entity_scope"],
                                                    size_control["scope_evaluation_type"])):
                    sc_part_scope = size_control["part_scope"]
                    sc_part_ids = macros._get_part_ids(model, sc_part_scope)
                    if part_id in sc_part_ids:
                        sc_scope = controls._get_scope(model, size_control)
                        sc_scope.part_expression = part.name
                        size_control_params = {
                            "sizing_type": controls._get_size_control_type(size_control),
                            "sizing_params": controls._get_size_control_params(model, size_control),
                            "scope": sc_scope
                        }
                        size_control_id = create_size_control(model, size_control_params,
                                                              cached_data)
                        size_control_ids.append(size_control_id)
            size_field_res = size_field.compute_volumetric(size_control_ids, size_field_params)
        part = model.get_part(part_id)
        topo_faces = part.get_topo_faces()
        if len(topo_faces) > 0:
            model.logger.python_logger.disabled = True
            model.topo_data.delete_mesh_on_topo_faces(topo_faces,
                                                        prime.DeleteMeshParams(model, True))
            model.logger.python_logger.disabled = False
            try:
                surfer.mesh_topo_faces(part_id, topo_faces, surfer_params)
                n_unmeshed_topo_faces = part.get_summary(
                    prime.PartSummaryParams(model)
                    ).n_unmeshed_topo_faces
                if n_unmeshed_topo_faces:
                    unmeshed_faces = [
                            face for face in topo_faces
                                if not model.topo_data.get_mesh_zonelets_of_topo_faces([face])
                        ]
                    print(
                        "Unmeshed topo face ids "
                        + str(unmeshed_faces)
                        + " on part "
                        + part.name
                        )
            except PrimeRuntimeError as error:
                print(
                    "Error with code '{}' on '{}' with message '{}'".format(
                        error.error_code,
                        part.name,
                        error.message,
                        )
                    )
                if mesh_params["stop_on_failure"] == True:
                    break
            except PrimeRuntimeWarning as warning:
                print(
                    "Warning: '{}' with message '{}'.".format(
                        part.name,
                        warning.message,
                        )
                    )
        else:
            cached_data._logger.warning(f"No topoface was found in part \"{part.name}\"")
        if sf_per_part:
            model.delete_volumetric_size_fields([size_field_res.size_field_id])
            model.control_data.delete_controls(size_control_ids)
            size_control_ids = []
            retain_generated_size_field = True

    if not retain_generated_size_field:
        model.delete_volumetric_size_fields([size_field_res.size_field_id])
    model.control_data.delete_controls(size_control_ids)


def mesh_with_size_controls(model: prime.Model, mesh_params: dict, cached_data: CachedData):
    part_scope = mesh_params["part_scope"]
    part_ids = macros._get_part_ids(model, part_scope)

    size_control_ids = []
    size_controls = mesh_params["size_controls"]

    for size_control in size_controls:
        size_control_ids.append(cached_data.create_cached_object(size_control))

    size_field = prime.SizeField(model)
    periodic_params = prime.SFPeriodicParams(model, angle = 0.0)
    size_field_params = prime.VolumetricSizeFieldComputeParams(model,
                                                               periodic_params = periodic_params)
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


def improve_quality(model: prime.Model, improve_quality_params: dict, cached_data: CachedData):
    part_scope = improve_quality_params["part_scope"]
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
            surface_utils.cleanup_tri_mesh(model, part, collapse_sliver_faces, stitch_free_faces,
                                           keep_small_free_surfaces, cached_data._logger)
        surface_utils.improve_quality(model, part, soft_target_skewness,
                                      hard_target_skewness, local_remesh_by_size_change,
                                      keep_small_free_surfaces)

def clean_up_triangles(model: prime.Model, clean_up_triangles_params: dict,
                       cached_data: CachedData):
    part_scope = clean_up_triangles_params["part_scope"]
    collapse_sliver_faces = True
    stitch_free_faces = True
    keep_small_free_surfaces = False
    part_ids = macros._get_part_ids(model, part_scope)
    quality_reg_id = 26
    surface_search_tool = prime.SurfaceSearch(model= model)
    collapse_tool = prime.CollapseTool(model= model)
    for part_id in part_ids:
        part = model.get_part(part_id)
        quality_params = prime.SearchByQualityParams(model= model, quality_limit=0.98,
                                            face_quality_measure=prime.FaceQualityMeasure.SKEWNESS)
        collapse_params = prime.CollapseParams(model= model)
        split_params = prime.SplitParams(model= model)
        if len(part.get_face_zonelets()) == 0:
            continue
        if collapse_sliver_faces:
            quality_res = surface_search_tool.search_zonelets_by_quality(part_id,
                                                                         part.get_face_zonelets(),
                                                                         quality_reg_id,
                                                                         quality_params)
            if quality_res.n_found > 0:
                collapse_params.feature_type = prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
                collapse_tool.split_and_collapse_on_zonelets(part_id= part_id,
                                                             face_zonelets=part.get_face_zonelets(),
                                                             register_id=quality_reg_id,
                                                             split_params=split_params,
                                                             collapse_params=collapse_params)
                collapse_params.feature_type = prime.SurfaceFeatureType.ZONEBOUNDARY
                collapse_tool.split_and_collapse_on_zonelets(part_id= part_id,
                                                             face_zonelets=part.get_face_zonelets(),
                                                             register_id=quality_reg_id,
                                                             split_params=split_params,
                                                             collapse_params=collapse_params)
        diag_params = prime.SurfaceDiagnosticSummaryParams(model,
                                                            scope=prime.ScopeDefinition(model,
                                                            part_expression= part.name),
                                                            compute_self_intersections=False,
                                                            compute_free_edges=True,
                                                            compute_multi_edges=False,
                                                            compute_duplicate_faces=False)
        if stitch_free_faces:
            checks = surface_search_tool.get_surface_diagnostic_summary(diag_params)
            if (checks.n_free_edges > 0):
                if (checks.n_free_edges > 0):
                    part_zonelets = part.get_face_zonelets()
                    connect = prime.Connect(model)
                    connect_params = prime.StitchParams(model=model, enable_multi_threading = True,
                                                        type = prime.StitchType.FREEFREE,
                                                        remesh = False)
                    connect_params.tolerance = 0.2
                    connect_params.use_absolute_tolerance = False
                    results = connect.stitch_face_zonelets(part_id, part_zonelets, part_zonelets,
                                                           connect_params)
                    tols = [1.5, 2]
                    for tol in tols:
                        checks = surface_search_tool.get_surface_diagnostic_summary(diag_params)
                        if (checks.n_free_edges == 0):
                            break
                        connect_params.tolerance = 0.2 * tol * tol
                        results = connect.stitch_face_zonelets(part_id, part.get_face_zonelets(),
                                                               part.get_face_zonelets(),
                                                               connect_params)
                    quality_params.quality_limit = 0.98
                    quality_res = surface_search_tool.search_zonelets_by_quality(part_id,
                                                                                 part_zonelets,
                                                                                 quality_reg_id,
                                                                                 quality_params)
                    collapse_params.feature_type = prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
                    collapse_tool.split_and_collapse_on_zonelets(part_id = part_id,
                                                                 face_zonelets=part_zonelets,
                                                                 register_id=quality_reg_id,
                                                                 split_params=split_params,
                                                                 collapse_params=collapse_params)
        if not keep_small_free_surfaces:
            delete_tool = prime.DeleteTool(model = model)
            delete_fringe_params = prime.DeleteFringesAndOverlapsParams(model = model,
                                                                        fringe_element_count=5,
                                                                        overlap_element_count=1,
                                                                        delete_overlaps=True)
            delete_tool.delete_fringes_and_overlaps_on_zonelets(part_id, part.get_face_zonelets(),
                                                                delete_fringe_params)
        diag_params = prime.SurfaceDiagnosticSummaryParams(model,
                                                           scope=prime.ScopeDefinition(model,
                                                                    part_expression = part.name),
                                                           compute_self_intersections=True,
                                                           compute_free_edges=True,
                                                           compute_multi_edges=True,
                                                           compute_duplicate_faces=True)
        checks = surface_search_tool.get_surface_diagnostic_summary(diag_params)
        if (checks.n_free_edges > 0 or checks.n_multi_edges > 0 or
            checks.n_self_intersections > 0 or checks.n_duplicate_faces > 0):
            print(part.name, checks.n_free_edges, checks.n_multi_edges, checks.n_self_intersections,
                  checks.n_duplicate_faces)