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

import ansys.meshing.prime.numen.utils.macros as macros
from ansys.meshing import prime
from ansys.meshing.prime.numen.utils import surface_utils, volume_utils
from ansys.meshing.prime.numen.utils.cached_data import CachedData
from ansys.meshing.prime.numen.utils.communicator import call_method


def _str(input: tuple) -> str:
    if isinstance(input, tuple):
        return " ".join(input)
    else:
        return input


def volume_mesh(model: prime.Model, volume_mesh_params: dict, cached_data: CachedData):

    fill_type = volume_mesh_params["volume_fill_type"]

    if (
        evaluation_value(fill_type) == prime.VolumeFillType.TET
        or evaluation_value(fill_type) == prime.VolumeFillType.HEXCORETET
    ):
        quality_measure_param = prime.CellQualityMeasure.SKEWNESS
    elif (
        evaluation_value(fill_type) == prime.VolumeFillType.POLY
        or evaluation_value(fill_type) == prime.VolumeFillType.HEXCOREPOLY
    ):
        quality_measure_param = prime.CellQualityMeasure.INVERSEORTHOGONAL

    part_scope = volume_mesh_params["part_scope"]
    sf_per_part = volume_mesh_params["size_field_computation_per_part"]
    part_ids = macros._get_part_ids(model, part_scope)
    if sf_per_part:
        sf_prefix = volume_mesh_params["size_field_per_part_prefix"]
        size_field_ids = model.get_active_volumetric_size_fields()
        if len(size_field_ids) > 0:
            model.deactivate_volumetric_size_fields(size_field_ids)
        else:
            size_field_ids = model.get_volumetric_size_fields()
    auto_mesh_params = prime.AutoMeshParams(
        model=model, volume_fill_type=evaluation_value(fill_type)
    )
    thin_volume_mesh_settings = volume_mesh_params["thin_volume_mesh_controls"]
    thin_vol_ctrls_ids = []
    for tv_setting in thin_volume_mesh_settings:
        source_face_label = tv_setting["source_face_label"]
        target_face_label = tv_setting["target_face_label"]
        imprint = tv_setting["imprint_sides"]
        n_layers = tv_setting["n_layers"]
        stair_step = tv_setting["stair_step"]
        part_expression = tv_setting["part_expression"]

        thin_vol_ctrls = volume_utils.create_thin_volume_controls(
            model,
            part_expression,
            source_face_label,
            target_face_label,
            imprint,
            n_layers,
            stair_step,
        )
        thin_vol_ctrls_ids.extend(thin_vol_ctrls)

    auto_mesh_params.thin_volume_control_ids = thin_vol_ctrls_ids
    # prism settings
    prism_settings = volume_mesh_params["prism_controls"]
    prism_ctrl_ids = []
    for prism_scope_info in prism_settings:
        n_layers = prism_scope_info["n_layers"]
        first_height = prism_scope_info["first_height"]
        last_aspect_ratio = prism_scope_info["last_aspect_ratio"]
        face_evaluation_type = prism_scope_info["face_evaluation_type"]
        face_expression = prism_scope_info["face_expression"]
        volume_expression = prism_scope_info["volume_expression"]
        part_expression = prism_scope_info["part_expression"]
        prism_ctrl_id = volume_utils.create_prism_control(
            model,
            part_expression,
            face_expression,
            evaluation_value(face_evaluation_type),
            volume_expression,
            n_layers,
            first_height,
            last_aspect_ratio,
        )
        prism_ctrl_ids.append(prism_ctrl_id)
    auto_mesh_params.prism_control_ids = prism_ctrl_ids
    stairstep_params = prime.PrismStairStep(
        model=model, check_proximity=False, gap_factor_scale=0.2
    )
    prism_params = prime.PrismParams(model=model, stair_step=stairstep_params)
    auto_mesh_params.prism = prism_params

    for part_id in part_ids:
        part = model.get_part(part_id)
        if sf_per_part:
            for size_field_id in size_field_ids:
                args = {"size_field_id": size_field_id}
                size_field_name = call_method(
                    model, "PrimeMesh::Model/GetSizeFieldName", model._object_id, args
                )
                if size_field_name.strip() == (sf_prefix + "_" + part.name).strip():
                    model.activate_volumetric_size_fields([size_field_id])
        # periodic settings
        '''
        periodic_labels_exp = volume_mesh_params["periodic_labels_exp"]
        if "periodic_info" in volume_mesh_params:
            periodic_info = volume_mesh_params["periodic_info"]
        else: periodic_info = {}
        if periodic_labels_exp and periodic_info:
            periodic_control = model.control_data.create_periodic_control()
            periodic_control.set_scope(
                prime.ScopeDefinition(
                    model=model,
                    entity_type=prime.ScopeEntity.FACEZONELETS,
                    evaluation_type=prime.ScopeEvaluationType.LABELS,
                    label_expression=periodic_labels_exp,
                )
            )
            periodic_control.set_params(
                prime.PeriodicControlParams(
                    model=model,
                    angle=periodic_info["angle"],
                    axis=periodic_info["axis"],
                    center=periodic_info["center"],
                )
        '''
        auto_mesh_params.size_field_type = prime.SizeFieldType.VOLUMETRIC
        if model.get_num_compute_nodes() > 1:
            model.start_distributed_meshing()
        auto_mesher = prime.AutoMesh(model=model)
        auto_mesher.mesh(part_id=part_id, automesh_params=auto_mesh_params)
        if "labels_to_delete" in volume_mesh_params:
            labels_to_delete = volume_mesh_params["labels_to_delete"]
        else:
            labels_to_delete = []
        if "labels_to_retain" in volume_mesh_params:
            labels_to_retain = volume_mesh_params["labels_to_retain"]
        else:
            labels_to_retain = []
        if labels_to_delete != []:
            part.remove_labels_from_zonelets(labels_to_delete, part.get_face_zonelets())
        if labels_to_retain != []:
            total_labels = part.get_labels()
            delete_labels = list(set(total_labels).difference(set(labels_to_retain)))
            part.remove_labels_from_zonelets(
                delete_labels,
                part.get_face_zonelets(),
            )


def evaluation_value(value: str):
    if value == 'tet':
        return prime.VolumeFillType.TET
    if value == 'poly':
        return prime.VolumeFillType.POLY
    if value == 'tethexcore' or value == 'tet_hexcore':
        return prime.VolumeFillType.HEXCORETET
    if value == 'polyhexcore' or value == 'poly_hexcore':
        return prime.VolumeFillType.HEXCOREPOLY
    if value == 'labels':
        return prime.ScopeEvaluationType.LABELS
    if value == 'zones':
        return prime.ScopeEvaluationType.ZONES


def cell_apportion(model: prime.Model, cell_apportion_params: dict, cached_data: CachedData):
    target_part_name = cell_apportion_params["target_part_name"]
    topo_part_scope = cell_apportion_params["topology_part_scope"]
    volume_scope = cell_apportion_params["volume_expression"]
    topo_part_ids = macros._get_part_ids(model, topo_part_scope)
    mesh_part = model.get_part_by_name(target_part_name)
    args = {
        "zone_name_pattern": "*",
        "name_pattern_params": prime.NamePatternParams(model)._jsonify(),
    }
    zonelets = model._comm.serve(
        model,
        "PrimeMesh::Part/GetCellZoneletsOfZoneNamePattern_Beta",
        mesh_part._object_id,
        args=args,
    )
    # parts = [part.id for part in model.parts if part.id != mesh_part.id]
    '''
    # geom_part_name = "dirtysolids_highpriority"
    geom_part = model.get_part_by_name(geom_part_name)
    args={"target_part_id" : mesh_part.id, "target_cell_zonelets" : zonelets,
    "source_part_ids" : [geom_part.id], "small_regions_volume_fraction" : 0.0001}
    '''
    tool = prime.VolumeMeshTool(model)
    args = {
        "target_part_id": mesh_part.id,
        "target_cell_zonelets": zonelets,
        "source_part_ids": topo_part_ids,
        "small_regions_volume_fraction": 0.0001,
    }
    region_result = model._comm.serve(
        model, "PrimeMesh::VolumeMeshTool/AssignMeshRegions", tool._object_id, args=args
    )
    # print(region_result)

    args = {
        "zone_name_pattern": "*",
        "name_pattern_params": prime.NamePatternParams(model)._jsonify(),
    }
    cell_zonelets = model._comm.serve(
        model,
        "PrimeMesh::Part/GetCellZoneletsOfZoneNamePattern_Beta",
        mesh_part._object_id,
        args=args,
    )
    for cell_zonelet in cell_zonelets:
        mesh_info = prime.MeshInfo(model)
        args = {
            "edge_zonelets": [],
            "face_zonelets": [],
            "cell_zonelets": [cell_zonelet],
            "params": {},
        }
        result = model._comm.serve(
            model, "PrimeMesh::MeshInfo/GetElementCountOfZonelets", mesh_info._object_id, args=args
        )
        # print(result["cellElementCount"])
    model.delete_parts(topo_part_ids)
    name_pattern_params = prime.NamePatternParams(model=model)
    zone_ids = mesh_part.get_face_zones_of_name_pattern(
        "*_boundary, *_contact, *_interface", name_pattern_params
    )
    for zone_id in zone_ids:
        results = model.delete_zone(zone_id)
    if volume_scope:
        fluid_zones_ids = mesh_part.get_volume_zones_of_name_pattern(
            volume_scope, prime.NamePatternParams(model)
        )
        fluid_zones = [model.get_zone_name(zone_id) for zone_id in fluid_zones_ids]
        volume_utils.volume_zone_management(model, mesh_part, fluid_zones)


def extract_flow_volume(
    model: prime.Model, extract_flow_volume_params: dict, cached_data: CachedData
):
    capping_settings = extract_flow_volume_params["capping_params"]
    part_name = extract_flow_volume_params["part_name"]

    # create cap
    cap_face_zonelets = []
    np_params = prime.NamePatternParams(model)
    for part in model.parts:
        for cap_setting in capping_settings:
            face_evaluation_type = cap_setting["face_evaluation_type"]
            face_expression = cap_setting["face_expression"]
            side_face_expression = cap_setting["side_face_expression"]
            flow_volume_zone_name = cap_setting["flow_volume_zone_name"]
            if len(face_expression) > 0 and len(side_face_expression) > 0:
                raise RuntimeError(
                    _str(
                        (
                            "Both \"face_expression\" and",
                            "\"side_face_expression\"",
                            "cannot be defined together",
                        )
                    )
                )
            if len(face_expression) > 0:
                part_cap_z = []
                if face_evaluation_type == "labels":
                    part_cap_z = part.get_face_zonelets_of_label_name_pattern(
                        face_expression, np_params
                    )
                elif face_evaluation_type == "zones":
                    part_cap_z = part.get_face_zonelets_of_zone_name_pattern(
                        face_expression, np_params
                    )
                cap_face_zonelets.extend(part_cap_z)

    # merge all parts
    merge_part_params = prime.MergePartsParams(model, part_name)
    merge_res = model.merge_parts([part.id for part in model.parts], merge_part_params)
    part_name = merge_res.merged_part_assigned_name

    tolerant_connect_part = model.get_part_by_name(part_name)

    # intersect
    if len(cap_face_zonelets) > 0:
        intersect_params = prime.IntersectParams(
            model=model,
            use_absolute_tolerance=False,
            tolerance=0.25,
            remesh=True,
        )
        face_zonelets = tolerant_connect_part.get_face_zonelets()
        connect = prime.Connect(model)
        results = connect.intersect_face_zonelets(
            tolerant_connect_part.id, cap_face_zonelets, face_zonelets, intersect_params
        )

    intersect_results = surface_utils.check_surface_intersection(model, tolerant_connect_part)
    if intersect_results[0]:
        surface_utils.improve_quality(model, tolerant_connect_part, 0.7, 0.9, True, False)

        intersect_results = surface_utils.check_surface_intersection(model, tolerant_connect_part)
        if intersect_results[0]:
            raise RuntimeError(
                _str(
                    (
                        f"{intersect_results[0]} face elements found",
                        "intersecting.\n    Locations are :\n       ",
                        f"{intersect_results[1]}\n   ",
                        "Intersecting face zonelets are:\n       ",
                        f"{intersect_results[2]}",
                    )
                )
            )

    # remove free faces
    mesh_check_results = surface_utils.surface_mesh_check(model)
    if mesh_check_results.n_free_edges != 0:
        model._comm.serve(
            model,
            "PrimeMesh::Model/SetPyPrimeSettings",
            model._object_id,
            args={"settings": "encode_hidden_params"},
        )
        command_name = "PrimeMesh::Connect/StitchFaceZonelets"
        args = {
            "part_id": tolerant_connect_part.id,
            "face_zonelet_ids": tolerant_connect_part.get_face_zonelets(),
            "with_face_zonelet_ids": tolerant_connect_part.get_face_zonelets(),
            "params": {"remesh": True, "tolerance": 0.1, "type": 2},
        }
        connect = prime.Connect(model)
        model._comm.serve(model, command_name, connect._object_id, args=args)

        mesh_check_results = surface_utils.surface_mesh_check(model)
        if mesh_check_results.n_free_edges != 0:
            result = surface_utils.free_elements_results(model, tolerant_connect_part)
            su = prime.SurfaceUtilities(model)
            params = prime.CreateCapParams(model)
            su.create_cap_on_face_zonelets(tolerant_connect_part.id, result[2], params)

            mesh_check_results = surface_utils.surface_mesh_check(model)
            if mesh_check_results.n_free_edges != 0:
                nfree = mesh_check_results.n_free_edges
                raise RuntimeError(f"{nfree} face elements found free edges.")

    # delete extra face labels
    total_labels = tolerant_connect_part.get_labels()
    for label in total_labels:
        if "__attrib_abr_topotype" in label:
            tolerant_connect_part.remove_labels_from_zonelets(
                [label],
                tolerant_connect_part.get_face_zonelets(),
            )
            tolerant_connect_part.remove_labels_from_zonelets(
                [label],
                tolerant_connect_part.get_edge_zonelets(),
            )

    # face label creation
    volume_zone_ids = tolerant_connect_part.get_volume_zones()
    for volume_zone in volume_zone_ids:
        volume_zone_name = model.get_zone_name(volume_zone)
        volumes = tolerant_connect_part.get_volumes_of_zone_name_pattern(
            volume_zone_name,
            np_params,
        )
        face_zonelets = tolerant_connect_part.get_face_zonelets_of_volumes(volumes)
        tolerant_connect_part.add_labels_on_zonelets([volume_zone_name], face_zonelets)

    # check duplicates in cap zonelets
    for zonelet in cap_face_zonelets:
        if cap_face_zonelets.count(zonelet) > 1:
            raise RuntimeError("Duplicate zonelets found")

    # flow volume extraction
    cap_zonelets_with_label = {}
    for cap_setting in capping_settings:
        face_evaluation_type = cap_setting["face_evaluation_type"]
        face_expression = cap_setting["face_expression"]
        side_face_expression = cap_setting["side_face_expression"]
        flow_volume_zone_name = cap_setting["flow_volume_zone_name"]
        if len(side_face_expression) > 0:
            cap_face_zonelets = volume_utils.create_cap(
                model,
                tolerant_connect_part,
                side_face_expression,
                face_evaluation_type,
                "__numen_cap",
            )
            cap_zonelets_with_label[flow_volume_zone_name] = cap_face_zonelets
        else:
            cap_face_zonelets = []
            if face_evaluation_type == "labels":
                cap_face_zonelets = tolerant_connect_part.get_face_zonelets_of_label_name_pattern(
                    face_expression, np_params
                )
            elif face_evaluation_type == "zones":
                cap_face_zonelets = tolerant_connect_part.get_face_zonelets_of_zone_name_pattern(
                    face_expression, np_params
                )
            cap_zonelets_with_label[flow_volume_zone_name] = cap_face_zonelets

    fluid_vols = []
    extract_volume_params = prime.ExtractVolumesParams(model)
    extract_volume_params.create_zone = True
    for volume_zone_name, cap_zonelets in cap_zonelets_with_label.items():
        extract_volume_params.suggested_zone_name = volume_zone_name
        try:
            extract_vol_res = tolerant_connect_part.extract_volumes(
                cap_zonelets, extract_volume_params
            )
            for vol in extract_vol_res.volumes.tolist():
                if vol not in fluid_vols:
                    fluid_vols.append(vol)
        except:
            cached_data._logger.warning(
                "Flow volume extraction failed. "
                + "Check cap settings to ensure all capping surfaces are created, "
                + "or check for leaks in the model."
            )


def prepare_for_volume_meshing(model: prime.Model, improve_params: dict, cached_data: CachedData):
    part_name = improve_params["part_name"]
    volume_scope = improve_params["volume_expression"]
    part = model.get_part_by_name(part_name)
    np_params = prime.NamePatternParams(model)

    # nugget creation
    fluid_zones = part.get_volume_zones_of_name_pattern(volume_scope, np_params)
    volume_zone_ids = part.get_volume_zones()
    for volume_zone in volume_zone_ids:
        volume_zone_name = model.get_zone_name(volume_zone)
        volumes = part.get_volumes_of_zone_name_pattern(
            volume_zone_name,
            np_params,
        )
        face_zonelets = part.get_face_zonelets_of_volumes(volumes)
        part.add_labels_on_zonelets([volume_zone_name], face_zonelets)

    fluid_vols = []
    volume_zone_ids = part.get_volume_zones()
    for i in volume_zone_ids:
        zone_name = model.get_zone_name(i)
        if i in fluid_zones:
            volumes = part.get_volumes_of_zone_name_pattern(zone_name, np_params)
            for volume in volumes:
                fluid_vols.append(volume)
    if fluid_vols:
        surf_utils = prime.SurfaceUtilities(model)
        sphere_params = prime.FixInvalidNormalNodeParams(
            model,
            nugget_size=improve_params["_nugget_size"],
            nugget_mesh_size=improve_params["_nugget_mesh_size"],
            label="__numen_nuggets_at_invalid_normals",
        )
        fluid_face_zonelets = part.get_face_zonelets_of_volumes(fluid_vols)
        fix_invalid_normals_on_face_label_exp = "* !periodic*"
        nugget_zonelets = part.get_face_zonelets_of_label_name_pattern(
            fix_invalid_normals_on_face_label_exp, np_params
        )
        nugget_zonelets = list(set(nugget_zonelets) & set(fluid_face_zonelets))
        if nugget_zonelets:
            surf_utils.fix_invalid_normal_nodes_of_face_zonelets(
                part.id, fluid_face_zonelets, sphere_params
            )

    # compute volumes
    volume_zone_ids = part.get_volume_zones()
    zone_names = [model.get_zone_name(i) for i in volume_zone_ids]
    all_labels = part.get_labels()
    excluded_lables = list(set(all_labels) - set(zone_names))
    compute_volume_params = prime.ComputeVolumesParams(
        model,
        create_zones_type=prime.CreateVolumeZonesType.PERNAMESOURCE,
        priority_ordered_names=zone_names,
        volume_naming_type=prime.VolumeNamingType.BYFACELABEL,
        excludeNames=excluded_lables,
    )
    result = part.compute_closed_volumes(compute_volume_params)
    fluid_vols = []
    volume_zone_ids = part.get_volume_zones()
    for i in volume_zone_ids:
        volume_zone_name = model.get_zone_name(i)
        if "fluid" in volume_zone_name:
            volumes = part.get_volumes_of_zone_name_pattern(
                volume_zone_name,
                np_params,
            )
            for volume in volumes:
                fluid_vols.append(volume)

    # merging the nuggets to neighbor_volumes
    if fluid_vols:
        invalid_normal_vols = part.get_volumes_of_zone_name_pattern(
            "__numen_nuggets_at_invalid_normals*", np_params
        )
        if invalid_normal_vols:
            delete_volumes_params = prime.DeleteVolumesParams(model)
            part.delete_volumes(volumes=invalid_normal_vols, params=delete_volumes_params)
        invalid_normal_vols = part.get_volumes_of_zone_name_pattern(
            "__numen_nuggets_at_invalid_normals*", np_params
        )
        if invalid_normal_vols:
            merge_vol_params = prime.MergeVolumesParams(model)
            merge_vol_params.merge_to_neighbor_volume = True
            neighbour_volumes_of_nugget = list(
                set(part.get_volumes()) - set(invalid_normal_vols) - set(fluid_vols)
            )
            merge_vol_params.neighbor_volumes = neighbour_volumes_of_nugget
            part.merge_volumes(invalid_normal_vols, merge_vol_params)
        merge_params = prime.MergeZoneletsParams(
            model,
            merge_small_zonelets_with_neighbors=True,
            element_count_limit=10,
        )
        part.merge_zonelets(part.get_face_zonelets(), params=merge_params)

    volume_utils.volume_zone_management(model, part, fluid_zones)

    merge_params = prime.MergeZoneletsParams(
        model,
        merge_small_zonelets_with_neighbors=False,
        element_count_limit=5,
    )

    label_fz_map = {}
    fzs = part.get_face_zonelets()
    for fz in fzs:
        face_labels = part.get_labels_on_zonelet(fz)
        sorted_labels = sorted(face_labels)
        unq_lbl = "\"".join(sorted_labels)
        if len(unq_lbl) == 0:
            unq_lbl = "_______"
        if unq_lbl in label_fz_map:
            label_fz_map[unq_lbl].append(fz)
        else:
            label_fz_map[unq_lbl] = [fz]

    for unq_lbl, fzs in label_fz_map.items():
        zone_fz_map = {}
        for fz in fzs:
            zone = part.get_face_zone_of_zonelet(fz)
            if zone in zone_fz_map:
                zone_fz_map[zone].append(fz)
            else:
                zone_fz_map[zone] = [fz]
        for zone, face_zonelets in zone_fz_map.items():
            if len(face_zonelets) > 1:
                part.merge_zonelets(face_zonelets, merge_params)

    surface_utils.smooth_dihedral_faces(model, part, fluid_vols)


def mesh_check(model: prime.Model, mesh_check_params: dict, cached_data: CachedData):
    part_scope = mesh_check_params["part_scope"]
    part_ids = macros._get_part_ids(model, part_scope)
    volume_fill_type = mesh_check_params["volume_fill_type"]
    for part_id in part_ids:
        part = model.get_part(part_id)
        part_name = part.name
        if not part:
            cached_data._logger.error(f"    Part \"{part_name}\" not found.")
            return
        fill_type = evaluation_value(volume_fill_type)

        quality_measure = prime.CellQualityMeasure.SKEWNESS
        if fill_type == prime.VolumeFillType.TET or fill_type == prime.VolumeFillType.HEXCORETET:
            quality_measure = prime.CellQualityMeasure.SKEWNESS
        elif (
            fill_type == prime.VolumeFillType.POLY or fill_type == prime.VolumeFillType.HEXCOREPOLY
        ):
            quality_measure = prime.CellQualityMeasure.INVERSEORTHOGONAL

        params = prime.PartSummaryParams(model, print_id=False, print_mesh=True)
        res = part.get_summary(params)
        cached_data._logger.info(f" Mesh Check for \"{part.name}\" ongo.")
        cached_data._logger.info(f"    Face element count    : {res.n_faces}")
        cached_data._logger.info(f"    Cell element count    : {res.n_cells}")
        cached_data._logger.info(f"    Prism cell count      : {res.n_prism_cells}")
        bl_count = _get_cell_and_face_statistics(model, part.id)["bl_count"]
        cached_data._logger.info(f"    Thin volume cell count: {bl_count}")
        search = prime.VolumeSearch(model)
        params = prime.VolumeQualitySummaryParams(model)
        params.scope = prime.ScopeDefinition(
            model, part_expression=part.name, entity_type=prime.ScopeEntity.VOLUME
        )
        params.quality_limit = [0.99]
        params.cell_quality_measures = [quality_measure]
        cell_quality = search.get_volume_quality_summary(params)
        cached_data._logger.info(f"    Quality measure       : {quality_measure.name}")
        cached_data._logger.info(
            _str(
                (
                    "    Min cell quality      :",
                    f"{cell_quality.quality_results_part[0].min_quality}",
                )
            )
        )
        cached_data._logger.info(
            _str(
                (
                    "    Max cell quality      :",
                    f"{cell_quality.quality_results_part[0].max_quality}",
                )
            )
        )
        cached_data._logger.info(
            _str(("    Cells above criteria  :", f"{cell_quality.quality_results_part[0].n_found}"))
        )
        tool = prime.VolumeMeshTool(model)
        check = tool.check_mesh(part.id, prime.CheckMeshParams(model))
        if check.has_non_positive_volumes:
            cached_data._logger.error(f"    Part \"{part.name}\" has non positive volumes.")
        if check.has_non_positive_areas:
            cached_data._logger.error(f"    Part \"{part.name}\" has non positive areas.")
        if check.has_invalid_shape:
            cached_data._logger.error(f"    Part \"{part.name}\" has invalid shapes.")
        if check.has_left_handed_faces:
            cached_data._logger.error(f"    Part \"{part.name}\" has left handed faces.")
    cached_data._logger.info("    Mesh check done")


def _get_cell_and_face_statistics(model: prime.Model, part_id: int):
    mesh_info = prime.MeshInfo(model)
    result = {}
    face_scope = prime.ScopeDefinition(
        model=model,
        entity_type=prime.ScopeEntity.FACEZONELETS,
        evaluation_type=prime.ScopeEvaluationType.ZONES,
        zone_expression="*",
    )
    volume_scope = prime.ScopeDefinition(
        model=model,
        entity_type=prime.ScopeEntity.VOLUME,
        evaluation_type=prime.ScopeEvaluationType.ZONES,
        zone_expression="*",
    )
    jsonified_face_scope = face_scope._jsonify()
    jsonified_volume_scope = volume_scope._jsonify()
    face_stats_args = {"part_id": part_id, "face_scope": jsonified_face_scope}
    cell_stats_args = {"part_id": part_id, "volume_scope": jsonified_volume_scope}
    face_stats_result = model._comm.serve(
        model,
        "PrimeMesh::MeshInfo/GetStatisticsOfFaceZoneletsByScope_Beta",
        mesh_info._object_id,
        args=face_stats_args,
    )
    cell_stats_result = model._comm.serve(
        model,
        "PrimeMesh::MeshInfo/GetStatisticsOfCellZoneletsByScope_Beta",
        mesh_info._object_id,
        args=cell_stats_args,
    )
    result['face_elem_count'] = face_stats_result["elementCount"]
    result['prism_count'] = cell_stats_result["wedgeElementCount"]
    result['tet_count'] = cell_stats_result["tetElementCount"]
    result['hex_count'] = cell_stats_result["hexElementCount"]
    result['poly_count'] = cell_stats_result["polyElementCount"]
    result['bl_count'] = cell_stats_result["boundaryLayerElementCount"]
    return result
