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

from itertools import combinations
from typing import List

import ansys.meshing.prime.numen.utils.macros as macros
from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.communicator import PrimeObj


def create_cap(
    model: prime.Model,
    part: prime.Part,
    side_face_exp: str,
    side_face_evaluation_type: str,
    cap_zone_name: str,
):
    surface_utils = prime.SurfaceUtilities(model)
    cap_face_zonelets_params = prime.CreateCapParams(model)
    name_pattern_params = prime.NamePatternParams(model)
    face_zonelets = []
    if side_face_evaluation_type == "labels":
        face_zonelets = part.get_face_zonelets_of_label_name_pattern(
            side_face_exp,
            name_pattern_params,
        )
    elif side_face_evaluation_type == "zones":
        face_zonelets = part.get_face_zonelets_of_zone_name_pattern(
            side_face_exp,
            name_pattern_params,
        )
    cap_res: prime.CreateCapResults = surface_utils.create_cap_on_face_zonelets(
        part_id=part.id,
        face_zonelets=face_zonelets,
        params=cap_face_zonelets_params,
    )
    zone_id = model.get_zone_by_name(cap_zone_name)
    if zone_id <= 0:
        create_zone_res = model.create_zone(cap_zone_name, prime.ZoneType.FACE)
        zone_id = create_zone_res.zone_id
    part.add_zonelets_to_zone(zone_id, cap_res.created_face_zonelets)
    return cap_res.created_face_zonelets


def merge_parts(model: prime.Model, parts: List[prime.Part], suggested_part_name: str):
    merge_part_params = prime.MergePartsParams(
        model,
        merged_part_suggested_name=suggested_part_name,
    )
    merge_res = model.merge_parts([part.id for part in model.parts], merge_part_params)
    return merge_res.merged_part_assigned_name


def detect_thin_volumes(
    model: prime.Model,
    part: prime.Part,
    thickness: float,
    volume_zone_exp: str,
    source_face_label: str,
    target_face_label: str,
    use_mesh_zonelets: bool,
):
    vt = PrimeObj(model, "VTFeatureRecognition", part.id)
    command_name = "PrimeMesh::Part/GetTopoVolumesOfZoneNamePattern_Beta"
    args = {
        "zone_name_pattern": volume_zone_exp,
        "name_pattern_params": prime.NamePatternParams(model)._jsonify(),
    }
    topo_vols = model._comm.serve(model, command_name, part._object_id, args=args)
    params_vt = {
        "maxThickness": thickness,
        "useMeshZonelets": use_mesh_zonelets,
        "labelScope": {
            "sourceLabelPrefix": f"{source_face_label}_{thickness}",
            "targetLabelPrefix": f"{target_face_label}_{thickness}",
            "addTopoVolumeIdSuffix": True,
            "addThicknessRangeSuffix": False,
            "numOfThicknessRanges": 1,
        },
    }
    args = {
        "part_id": part.id,
        "topo_volumes": topo_vols,
        "params": params_vt,
    }
    vt.call_method("DetectThinVolumes", args)
    vt.destruct()


def volume_zone_management(model: prime.Model, part: prime.Part, fluid_zones: List[str]):
    boundary_suffix = "_boundary"
    solid_solid_shared_suffix = "_contact"
    fluid_shared_suffix = "_interface"
    name_pattern_params = prime.NamePatternParams(model)
    volume_zone_ids = part.get_volume_zones()
    for i, j in combinations(volume_zone_ids, 2):
        volume_zone_name1 = model.get_zone_name(i)
        volumes = part.get_volumes_of_zone_name_pattern(
            volume_zone_name1,
            name_pattern_params,
        )
        face_zonelets1 = part.get_face_zonelets_of_volumes(volumes)
        volume_zone_name2 = model.get_zone_name(j)
        volumes = part.get_volumes_of_zone_name_pattern(
            volume_zone_name2,
            name_pattern_params,
        )
        face_zonelets2 = part.get_face_zonelets_of_volumes(volumes)
        difference_zonelets = list(set(face_zonelets1).intersection(set(face_zonelets2)))
        if len(difference_zonelets) > 0:
            zone_name_1 = model.get_zone_name(i)
            zone_name_2 = model.get_zone_name(j)
            new_zone_name = ""
            if zone_name_1 in fluid_zones or zone_name_2 in fluid_zones:
                new_zone_name = f"{zone_name_1}_{zone_name_2}{fluid_shared_suffix}"
            else:
                new_zone_name = f"{zone_name_1}_{zone_name_2}{solid_solid_shared_suffix}"
            face_zone = model.create_zone(new_zone_name, prime.ZoneType.FACE)
            part.add_zonelets_to_zone(face_zone.zone_id, difference_zonelets)
    face_zone_zonelets = []
    face_zones = part.get_face_zones()
    for i in face_zones:
        zone_face_zonelets = part.get_face_zonelets_of_zone_name_pattern(
            model.get_zone_name(i), name_pattern_params
        )
        for zonelet in zone_face_zonelets:
            face_zone_zonelets.append(zonelet)
    for volume_zone in volume_zone_ids:
        volume_zone_name = model.get_zone_name(volume_zone)
        volumes = part.get_volumes_of_zone_name_pattern(
            volume_zone_name,
            prime.NamePatternParams(model),
        )
        volume_zone_face_zonelets = part.get_face_zonelets_of_volumes(volumes)
        volume_zone_boundary_zonelets = [
            item for item in volume_zone_face_zonelets if item not in face_zone_zonelets
        ]
        face_zone = model.create_zone(volume_zone_name + boundary_suffix, prime.ZoneType.FACE)
        part.add_zonelets_to_zone(face_zone.zone_id, volume_zone_boundary_zonelets)


def create_thin_volume_controls(
    model: prime.Model,
    part_expression: str,
    source_face_label_prefix: str,
    target_face_label_prefix: str,
    imprint_sides: bool,
    n_layers: int,
    stair_step: bool,
):
    thin_volume_controls = []
    np_params = prime.NamePatternParams(model)
    part_ids = macros._get_part_ids(model, part_expression)
    for part_id in part_ids:
        part = model.get_part(part_id)
        labels = part.get_labels()
        for src_label in labels:
            if src_label.startswith(source_face_label_prefix):
                volume_zone_id = src_label.split('_')[-1]
                thickness = src_label.split('_')[-2]
                trg_label = f"{target_face_label_prefix}_{thickness}_{volume_zone_id}"
                src_faces = part.get_face_zonelets_of_label_name_pattern(src_label, np_params)
                trg_faces = part.get_face_zonelets_of_label_name_pattern(trg_label, np_params)
                volumes = []
                for face_z1 in src_faces:
                    faces_volumes = part.get_volumes_of_face_zonelet(face_z1)
                    for v in faces_volumes:
                        fzs = part.get_face_zonelets_of_volumes([v])
                        for fz in fzs:
                            if fz in trg_faces:
                                volumes.append(v)
                                break
                volume_zones = [part.get_volume_zone_of_volume(vid) for vid in volumes]
                volume_zone_names = [model.get_zone_name(vzid) for vzid in volume_zones]
                volume_zone_names = list(set(volume_zone_names))
                if len(volume_zone_names) > 0:
                    source_scope = prime.ScopeDefinition(
                        model=model,
                        entity_type=prime.ScopeEntity.FACEZONELETS,
                        evaluation_type=prime.ScopeEvaluationType.LABELS,
                        part_expression=part.name,
                        label_expression=src_label,
                    )
                    target_scope = prime.ScopeDefinition(
                        model=model,
                        entity_type=prime.ScopeEntity.FACEZONELETS,
                        evaluation_type=prime.ScopeEvaluationType.LABELS,
                        part_expression=part.name,
                        label_expression=trg_label,
                    )
                    volume_scope = prime.ScopeDefinition(
                        model=model,
                        entity_type=prime.ScopeEntity.VOLUME,
                        evaluation_type=prime.ScopeEvaluationType.ZONES,
                        part_expression=part.name,
                        zone_expression=",".join(volume_zone_names),
                    )
                    thin_volume_params = prime.ThinVolumeMeshParams(
                        model=model,
                        n_layers=n_layers,
                        imprint_sides=imprint_sides,
                        stairStep=stair_step,
                        gap=float(thickness),
                    )
                    thin_vol_ctrl = model.control_data.create_thin_volume_control()
                    thin_vol_ctrl.set_source_scope(source_scope)
                    thin_vol_ctrl.set_target_scope(target_scope)
                    thin_vol_ctrl.set_volume_scope(volume_scope)
                    thin_vol_ctrl.set_thin_volume_mesh_params(thin_volume_params)
                    thin_volume_controls.append(thin_vol_ctrl.id)
    return thin_volume_controls


def create_prism_control(
    model: prime.Model,
    part_scope: str,
    face_expression: str,
    face_evaluation_type: prime.ScopeEvaluationType,
    volume_expression: str,
    n_layers: int,
    first_height: float,
    last_aspect_ratio: float,
):
    prism_ctrl = model.control_data.create_prism_control()
    prism_params = prime.PrismControlGrowthParams(
        model=model,
        n_layers=n_layers,
        first_height=first_height,
        last_aspect_ratio=last_aspect_ratio,
        offset_type=prime.PrismControlOffsetType.LASTRATIO,
    )
    prism_ctrl.set_growth_params(prism_params)

    surface_scope = prime.ScopeDefinition(
        model=model,
        entity_type=prime.ScopeEntity.FACEZONELETS,
        evaluation_type=face_evaluation_type,
        part_expression=part_scope,
        label_expression=face_expression,
        zone_expression=face_expression,
    )
    prism_ctrl.set_surface_scope(surface_scope)

    volume_scope = prime.ScopeDefinition(
        model=model,
        entity_type=prime.ScopeEntity.VOLUME,
        evaluation_type=prime.ScopeEvaluationType.ZONES,
        part_expression=part_scope,
        zone_expression=volume_expression,
    )
    prism_ctrl.set_volume_scope(volume_scope)
    return prism_ctrl.id
