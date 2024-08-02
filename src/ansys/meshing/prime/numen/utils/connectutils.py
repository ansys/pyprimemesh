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

"""Module for connect utils."""
import re
from typing import List

import ansys.meshing.prime as prime
from ansys.meshing.prime import Model, Part, ScopeDefinition
from ansys.meshing.prime.internals.error_handling import PrimeRuntimeError


class TolerantConnect:
    """
    Provides methods to user who is new to meshing.

    This class also serves as a tutorial
    for commonly used tolerant connect workflows.
    The ``TolerantConnect`` class provides these functionalities:
    """

    def __init__(self, model: Model):
        """Initialize using a model.

        Parameters
        ----------
        model : Model
            Model that the methods are to work on.
        """
        self._model = model
        self._logger = model.python_logger

    def match_pattern(self, pattern: str, name: str) -> bool:
        """Evaluate pattern."""
        pattern = "^" + pattern.replace("*", ".*").replace("?", ".") + "$"
        x = re.search(pattern, name)
        if x:
            return True
        else:
            return False

    def eval_name_pattern(self, name: str, pattern: str) -> bool:
        """Evaluate name pattern."""
        bb = pattern.split("!")
        if self.match_pattern(bb[0].strip(), name):
            if len(bb) > 1:
                nv = False
                for nvbb in bb[1:]:
                    if self.match_pattern(nvbb.strip(), name):
                        nv = True
                        break
                if not nv:
                    return True
            else:
                return True

    def get_parts_of_name_pattern(self, name_pattern: str):
        """Get parts of name pattern."""
        patterns = name_pattern.split(",")

        part_names = []
        for part in self._model.parts:
            part_names.append(part.name)

        # can loop over parts instead of part names and then append the part names but unclear
        # about duplicate removal
        ordered_names = []
        for pattern in patterns:
            for name in part_names:
                chk = self.eval_name_pattern(name, pattern)
                if chk == True:
                    ordered_names.append(name)

        # if multiple regex expressions evaluate true for a part, the ordering will retain the
        # first instance only
        ordered_names = list(dict.fromkeys(ordered_names))
        ordered_parts = []
        for name in ordered_names:
            ordered_parts.append(self._model.get_part_by_name(name))

        return ordered_parts

    def getfailedfuseordering(
        self,
        part_id: int,
        results: prime.FuseResults,
        part_labels: list = [],
    ):
        """Get failed fuse ordering."""
        model = self._model
        pairs = []
        part = model.get_part(part_id)
        set_part_labels = set(part_labels)
        for item in results.intersecting_zonelet_pairs:
            labels_1 = part.get_labels_on_zonelet(item.zone_id0)
            labels_2 = part.get_labels_on_zonelet(item.zone_id1)
            parts_1 = list(set(labels_1).intersection(set_part_labels))
            parts_2 = list(set(labels_2).intersection(set_part_labels))
            pairs.append([parts_1, parts_2])

        spairs = sorted(pairs)
        noduppairs = [spairs[0]]
        for i in range(1, len(spairs)):
            if spairs[i][0] != spairs[i - 1][0] or spairs[i][1] != spairs[i - 1][1]:
                noduppairs.append(spairs[i])

        print("Part1   vs   Part2")
        for a, b in noduppairs:
            print(a, "vs", b)

    def mesh_match(
        self,
        part: Part,
        join_to_faces: List[int],
        join_faces: List[int],
        tolerance: float,
        side_tolerance: float,
        use_abs_tol: float,
        max_angle: float,
        fuseOption: prime.FuseOption,
        fuse_edges_only: bool = False,
        separate: bool = True,
    ):
        """Perform mesh match."""
        connect = prime.Connect(model=self._model)
        params = prime.FuseParams(
            model=self._model,
            fuse_option=prime.FuseOption.TRIMONESIDE,
        )
        params.use_absolute_tolerance = use_abs_tol
        params.gap_tolerance = tolerance
        params.side_tolerance = side_tolerance
        params.fuse_option = fuseOption
        params.fuse_edges_only = fuse_edges_only
        params.check_interior = True
        params.check_orientation = False
        params.local_remesh = True
        params.separate = True
        params.dump_mesh = False
        params.n_layers = 2
        params.angle = max_angle
        sourceFaces = join_to_faces
        targetFaces = join_faces
        try:
            result = connect.fuse_face_zonelets(part.id, sourceFaces, targetFaces, params)
            return result
        except Exception as e:
            print(e)
            result = prime.FuseResults(self._model)
            result.warning_codes = [prime.WarningCode.FUSEOVERLAPREMOVALINCOMPLETE]
            return result

    def _resolve_conflicts(
        self,
        name: str = "",
        all_labels_in: List[str] = [],
        priority_ordered_part_names_in: List[str] = [],
        new_vol_zone_name: str = "unclaimed_vol_zone",
    ):
        model = self._model
        connect = prime.Connect(model)
        merged_part = model.get_part_by_name(name)
        hidden = model._comm.serve(
            model,
            "PrimeMesh::Model/SetPyPrimeSettings",
            model._object_id,
            args={"settings": "encode_hidden_params"},
        )
        results = model._comm.serve(
            model,
            "PrimeMesh::Connect/ResolveConflictVolumes",
            connect._object_id,
            args={
                "part_id": merged_part.id,
                "labels": all_labels_in,
                "priority": priority_ordered_part_names_in,
                "params": {"zoneName": new_vol_zone_name},
            },
        )

    def _collapse_thin_strips(
        self, surface_search_tool, collapse_tool, part, face_zonelets, abs_tol
    ):
        quality_reg_id = 26
        thin_strip_params = prime.SearchByThinStripParams(
            model=self._model,
            quality_limit=0.6,
            strip_height_limit=abs_tol,
            feature_type=prime.SurfaceFeatureType.FEATURE,
            feature_angle=60,
        )
        thin_strip_results = surface_search_tool.search_zonelets_by_thin_strips(
            part_id=part.id,
            face_zonelets=face_zonelets,
            register_id=quality_reg_id,
            params=thin_strip_params,
        )
        collapse_params = prime.CollapseParams(model=self._model)
        split_params = prime.SplitParams(model=self._model)
        if thin_strip_results.n_found:
            collapse_params.feature_type = prime.SurfaceFeatureType.ZONEBOUNDARY
            collapse_params.collapse_ratio = 0.4
            split_params.split_ratio = 0.1
            collapse_tool.split_and_collapse_on_zonelets(
                part_id=part.id,
                face_zonelets=face_zonelets,
                register_id=quality_reg_id,
                split_params=split_params,
                collapse_params=collapse_params,
            )
        thin_strip_params.strip_height_limit = abs_tol
        thin_strip_results = surface_search_tool.search_zonelets_by_thin_strips(
            part_id=part.id,
            face_zonelets=face_zonelets,
            register_id=quality_reg_id,
            params=thin_strip_params,
        )
        if thin_strip_results.n_found:
            collapse_params.feature_type = prime.SurfaceFeatureType.ZONEBOUNDARY
            collapse_params.collapse_ratio = 0.6
            split_params.split_ratio = 0.1
            collapse_tool.split_and_collapse_on_zonelets(
                part_id=part.id,
                face_zonelets=face_zonelets,
                register_id=quality_reg_id,
                split_params=split_params,
                collapse_params=collapse_params,
            )

    def _collapse_within_parts(self, list_parts_to_connect: list, tolerance: float = 0.05):
        model = self._model
        surface_search_tool = prime.SurfaceSearch(model=model)
        collapse_tool = prime.CollapseTool(model=model)
        # maybe the loop is not required?
        for part in list_parts_to_connect:
            faces = part.get_face_zonelets()
            self._collapse_thin_strips(surface_search_tool, collapse_tool, part, faces, tolerance)

    def surface_intersection_results(self, part: Part):
        diag = prime.SurfaceSearch(model=self._model)
        register_id = 1
        self_inter_params = prime.SearchBySelfIntersectionParams(model=self._model)
        self_inter_res = diag.search_zonelets_by_self_intersections(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            params=self_inter_params,
        )
        results = diag.get_search_info_by_register_id(
            part.get_face_zonelets(),
            register_id,
            prime.SearchInfoByRegisterIdParams(model=self._model),
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

    def _connect_interfering_volumes(
        self,
        parts_name_exp: str = "*",
        join_tolerance: float = 0.05,
        side_tolerance: float = 0.05,
        use_abs_tol: bool = False,
        intersect_tolerance: float = 0.05,
        join_remesh: bool = True,
        connected_part_name: str = "merged_part",
        mesh_match_angle: float = 45,
        priority_ordered_part_names_in: List[str] = [],
        intersect: bool = True,
        part_labels: list = [],
        fuse_edges_only: bool = False,
        debug: bool = False,
    ):
        dummy_unique_label1 = "___dummy_unique_label_to_join_intersect_one_by_one1___"
        dummy_unique_label2 = "___dummy_unique_label_to_join_intersect_one_by_one2___"
        pattern_params = prime.NamePatternParams(model=self._model)
        interfering_parts = []
        if "*" not in parts_name_exp and "!" not in parts_name_exp:
            patterns = parts_name_exp.split(",")
            for pattern in patterns:
                interfering_parts.extend(self.get_parts_of_name_pattern(pattern))
        else:
            interfering_parts = self.get_parts_of_name_pattern(parts_name_exp)
        priority_ordered_part_names = []
        failed_part_name_exp = []
        for part_name_exp in priority_ordered_part_names_in:
            ordered_names = [part.name for part in self.get_parts_of_name_pattern(part_name_exp)]
            if len(ordered_names) == 0:
                failed_part_name_exp.append(part_name_exp)
            else:
                priority_ordered_part_names.extend(ordered_names)
        if len(priority_ordered_part_names_in) > 0 and len(failed_part_name_exp) > 0:
            for part_name_exp in failed_part_name_exp:
                self._logger.warning(
                    'No parts found for expression "'
                    + part_name_exp
                    + '" specified in interfering_parts_priority setting'
                )
        connect = prime.Connect(self._model)
        intersect_params = prime.IntersectParams(
            model=self._model,
            tolerance=intersect_tolerance,
        )
        merged_part = self._model.parts[0]
        # merged_part.delete_zonelets(merged_part.get_edge_zonelets())
        volumes = merged_part.get_volumes()
        merged_part.get_face_zonelets_of_volumes([])
        n_parts = len(interfering_parts)
        if n_parts == 1:
            print("volumes found = ", len(volumes))
            join_to_faces = merged_part.get_face_zonelets_of_volumes([volumes[0]])
            for ind in range(1, len(volumes)):
                print("connecting with volume ", ind)
                join_faces = merged_part.get_face_zonelets_of_volumes([volumes[ind]])
                # self.write("before_matching_with_volume_" + ind.__str__() + ".pmdat")
                merged_part.add_labels_on_zonelets([dummy_unique_label1], join_to_faces)
                merged_part.add_labels_on_zonelets([dummy_unique_label2], join_faces)
                check_self_intersections = False
                result = self.mesh_match(
                    merged_part,
                    join_to_faces,
                    join_faces,
                    join_tolerance,
                    side_tolerance,
                    use_abs_tol,
                    mesh_match_angle,
                    prime.FuseOption.TRIMONESIDE,
                    fuse_edges_only,
                )
                if prime.WarningCode.FUSEOVERLAPREMOVALINCOMPLETE in result.warning_codes:
                    self.getfailedfuseordering(merged_part.id, result, part_labels)
                    check_self_intersections = True
                if prime.WarningCode.REMOVEOVERLAPWITHINTERSECT in result.warning_codes:
                    check_self_intersections = True
                if intersect:
                    intersect_to_faces = merged_part.get_face_zonelets_of_label_name_pattern(
                        dummy_unique_label1,
                        pattern_params,
                    )
                    intersect_faces = merged_part.get_face_zonelets_of_label_name_pattern(
                        dummy_unique_label2,
                        pattern_params,
                    )
                    intersect_params = prime.IntersectParams(
                        model=self._model,
                        tolerance=intersect_tolerance,
                    )
                    inter_res = connect.intersect_face_zonelets(
                        merged_part.id,
                        intersect_faces,
                        intersect_to_faces,
                        intersect_params,
                    )
                if check_self_intersections == True:
                    checks = self.surface_intersection_results(merged_part)
                    if checks[0] > 0:
                        # self.write("with_self_intersections.pmdat")
                        err_string = "Failed to connect " " with " + volumes[
                            ind
                        ].__str__ + ".\nCheck the locations at " + str(checks[1])
                        raise PrimeRuntimeError(err_string)
                fz1 = merged_part.get_face_zonelets_of_label_name_pattern(
                    dummy_unique_label1,
                    pattern_params,
                )
                fz2 = merged_part.get_face_zonelets_of_label_name_pattern(
                    dummy_unique_label2,
                    pattern_params,
                )
                join_faces = list(set(fz1).union(set(fz2)))
                merged_part.remove_labels_from_zonelets(
                    [dummy_unique_label1, dummy_unique_label2], join_faces
                )
                # self._lucid_mesh.write("after_just_connection_with_part_" +  part_name + ".pmdat")
            # merged_part.delete_zonelets(merged_part.get_edge_zonelets())
        elif n_parts == 1:
            merged_part = interfering_parts[0]
            merged_part.set_suggested_name(connected_part_name)

    def _connect_interfering_parts_multi_tol(
        self,
        interfering_parts: list,
        join_tolerances: list,
        side_tolerance: float = 0.05,
        use_abs_tol: bool = False,
        connected_part_name: str = "merged_part",
        mesh_match_angle: float = 45,
        part_labels: list = [],
        fuse_edges_only: bool = False,
        debug: bool = False,
    ):
        features = prime.FeatureExtraction(self._model)
        feature_params = prime.ExtractFeatureParams(
            model=self._model,
            feature_angle=40.0,
            label_name="__extracted__features__",
            disconnect_with_faces=False,
            replace=True,
        )
        dummy_unique_label1 = "___dummy_unique_label_to_join_intersect_one_by_one1___"
        dummy_unique_label2 = "___dummy_unique_label_to_join_intersect_one_by_one2___"
        n_parts = len(interfering_parts)
        if n_parts > 1:
            for part_i in range(n_parts):
                part = interfering_parts[part_i]
            merged_part = interfering_parts[0]
            start_index = 1
            if debug:
                merged_part = self._model.get_part_by_name(connected_part_name)
                start_index = 0
            for part_i in range(start_index, n_parts):
                part = interfering_parts[part_i]
                join_to_faces = merged_part.get_face_zonelets()
                parts_to_merge = [merged_part.id]
                if part.id == merged_part.id:
                    continue
                part_name = part.name
                print("Connecting part ", merged_part.name, " with part ", part.name)
                # self.write("before_mesh_matchin_with_part_" +  part_name + ".pmdat")
                join_faces = part.get_face_zonelets()
                parts_to_merge.append(part.id)
                if False:
                    res = features.extract_features_on_face_zonelets(
                        part_id=merged_part.id, face_zonelets=join_to_faces, params=feature_params
                    )
                    res = features.extract_features_on_face_zonelets(
                        part_id=merged_part.id, face_zonelets=join_faces, params=feature_params
                    )
                merge_res = self._model.merge_parts(
                    parts_to_merge,
                    prime.MergePartsParams(
                        model=self._model, merged_part_suggested_name=connected_part_name
                    ),
                )
                merged_part = self._model.get_part(merge_res.merged_part_id)
                if merged_part == None:
                    print("invalid part returned")
                merged_part.add_labels_on_zonelets([dummy_unique_label1], join_to_faces)
                merged_part.add_labels_on_zonelets([dummy_unique_label2], join_faces)
                check_self_intersections = False
                result = self.mesh_match(
                    merged_part,
                    join_to_faces,
                    join_faces,
                    join_tolerances[0],
                    side_tolerance,
                    use_abs_tol,
                    mesh_match_angle,
                    prime.FuseOption.TRIMONESIDE,
                    fuse_edges_only,
                )
                repeat = False
                if prime.WarningCode.FUSEOVERLAPREMOVALINCOMPLETE in result.warning_codes:
                    self.getfailedfuseordering(merged_part.id, result, part_labels)
                    check_self_intersections = True
                    repeat = True
                if prime.WarningCode.REMOVEOVERLAPWITHINTERSECT in result.warning_codes:
                    repeat = True
                if repeat:
                    all = []
                    zids1 = []
                    zids2 = []
                    for pair in result.intersecting_zonelet_pairs:
                        zids1.append(pair.zone_id0)
                        zids2.append(pair.zone_id1)
                        all.append(pair.zone_id0)
                        all.append(pair.zone_id1)
                    all = list(set(all))
                    zids1 = list(set(zids1))
                    zids2 = list(set(zids2))
                    print(zids1)
                    print(zids2)
                    labelsource = "connect_topology_source"
                    labeltarget = "connect_topology_target"
                    merged_part.remove_labels_from_zonelets(
                        [labelsource, labeltarget], merged_part.get_face_zonelets()
                    )
                    merged_part.add_labels_on_zonelets([labelsource], zids1)
                    merged_part.add_labels_on_zonelets([labeltarget], zids2)
                    # self.write("before_mesh_matchin_with_part_" +  part_name + "_labels.pmdat")
                    for index in range(1, len(join_tolerances)):
                        tol2 = join_tolerances[index]
                        result = self.mesh_match(
                            merged_part,
                            zids1,
                            zids2,
                            tol2,
                            side_tolerance,
                            use_abs_tol,
                            mesh_match_angle,
                            prime.FuseOption.TRIMONESIDE,
                            fuse_edges_only,
                        )
                        if len(result.warning_codes) == 0:
                            merged_part.remove_labels_from_zonelets(
                                [labelsource, labeltarget], merged_part.get_face_zonelets()
                            )
                            break
                if check_self_intersections == True:
                    checks = self.surface_intersection_results(merged_part)
                    if checks[0] > 0:
                        # self.write("with_self_intersections.pmdat")
                        err_string = (
                            "Failed to connect "
                            + '"'
                            + part_name
                            + '"'
                            + " with other parts.\nCheck the locations at "
                            + str(checks[1])
                        )
                        raise PrimeRuntimeError(err_string)
                all_face_zonelets = merged_part.get_face_zonelets()
                merged_part.remove_labels_from_zonelets(
                    [dummy_unique_label1, dummy_unique_label2], all_face_zonelets
                )
                # self.write("after_just_connection_with_part_" +  part_name + ".pmdat")
            # merged_part.delete_zonelets(merged_part.get_edge_zonelets())
        elif n_parts == 1:
            merged_part = interfering_parts[0]
            merged_part.set_suggested_name(connected_part_name)

    def zone_management(self, part_list: list):
        """Zone management."""
        label_list = []
        mergeParams = prime.MergeZoneletsParams(model=self._model)
        for part in part_list:
            # merge zonelets by zone and labels
            vol_bef_stitch = len(part.get_volumes())
            vol_aft_stitch = len(
                part.compute_closed_volumes(prime.ComputeVolumesParams(self._model)).volumes
            )
            zonelets = part.get_face_zonelets()
            if len(zonelets) > 1:
                part.merge_zonelets(zonelets=zonelets, params=mergeParams)
            # add label for part with part name
            part.add_labels_on_zonelets([part.name], part.get_face_zonelets())
            label_list.append(part.name)
        return label_list

    def post_surface_mesh_cleanup_triangles(
        self,
        parts: list,
        collapse_sliver_faces: bool = True,
        stitch_free_faces: bool = True,
        keep_small_free_surfaces: bool = False,
    ):
        """Clean up triangles post surface mesh."""
        parts = self.get_parts_of_name_pattern(part_name_exp)
        quality_reg_id = 26
        surface_search_tool = prime.SurfaceSearch(model=self._model)
        collapse_tool = prime.CollapseTool(model=self._model)
        quality_params = prime.SearchByQualityParams(
            model=self._model,
            quality_limit=0.98,
            face_quality_measure=prime.FaceQualityMeasure.SKEWNESS,
        )
        collapse_params = prime.CollapseParams(model=self._model)
        split_params = prime.SplitParams(model=self._model)
        for part in parts:
            if not part.get_face_zonelets():
                continue
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
                self._model,
                scope=ScopeDefinition(self._model, part_expression=part.name),
                compute_self_intersections=False,
                compute_free_edges=True,
                compute_multi_edges=False,
                compute_duplicate_faces=False,
            )
            if stitch_free_faces:
                checks = surface_search_tool.get_surface_diagnostic_summary(diag_params)
                if checks.n_free_edges:
                    part_zonelets = part.get_face_zonelets()
                    connect = prime.Connect(self._model)
                    connect_params = prime.StitchParams(
                        model=self._model,
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
                delete_tool = prime.DeleteTool(model=self._model)
                delete_fringe_params = prime.DeleteFringesAndOverlapsParams(
                    model=self._model,
                    fringe_element_count=5,
                    overlap_element_count=1,
                    delete_overlaps=True,
                )
                delete_tool.delete_fringes_and_overlaps_on_zonelets(
                    part.id,
                    part.get_face_zonelets(),
                    delete_fringe_params,
                )
            diag_params = prime.SurfaceDiagnosticSummaryParams(
                self._model,
                scope=ScopeDefinition(self._model, part_expression=part.name),
                compute_self_intersections=True,
                compute_free_edges=True,
                compute_multi_edges=True,
                compute_duplicate_faces=True,
            )
            checks = surface_search_tool.get_surface_diagnostic_summary(diag_params)

    def surface_mesh_coarsening(self, part: Part = None):
        """Coarsen the surface mesh."""
        surfer = prime.Surfer(self._model)
        surfer_params = prime.SurferParams(
            self._model,
            size_field_type=prime.SizeFieldType.VOLUMETRIC,
            max_angle=179,
            enable_multi_threading=False,
            check_non_manifolds=True,
            avoid_corner_triangles=True,
        )
        surfer.remesh_face_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            edge_zonelets=[],
            params=surfer_params,
        )

    def delete_topology(
        self,
        part_list: list,
        write_intermediate_files: bool = False,
    ):
        """Delete topology."""
        params = prime.DeleteTopoEntitiesParams(model=self._model, delete_geom_zonelets=True)
        part_ids_to_delete = []
        result = None
        for part in part_list:
            if part.get_topo_faces():
                part.delete_topo_entities(params)
            else:
                self._logger.info("No topology to delete in part: " + part.name)
                part_ids_to_delete.append(part.id)
        self.post_surface_mesh_cleanup_triangles(part_list, keep_small_free_surfaces=False)
        if write_intermediate_files:
            self.write("after_delete_topology.pmdat")
        return result

    def refine_contacts(
        self,
        connect_tolerance: float,
        part_list: list,
    ):
        """Refine contacts."""
        result = None
        global_min_size = self._model.get_global_sizing_params().min
        part_ids = [part.id for part in part_list]
        if len(part_ids) > 1:
            refine_params = prime.RefineAtContactsParams(model=self._model)
            surface_utils = prime.SurfaceUtilities(model=self._model)
            refine_params.contact_tolerance = 1.3 * connect_tolerance
            refine_params.refine_max_size = global_min_size
            refine_params.project_on_geometry = True
            result = surface_utils.refine_at_contacts(part_ids=part_ids, params=refine_params)
            size_field_id = result.size_field_id
        else:
            self._logger.info("Less than two parts exist.  No contacts to be refined. ")
        return result

    def stfailure1(
        self,
        parts,
        connect_tolerances,
        side_tolerance,
        use_absolute_connect_tolerance,
        mesh_match_angle,
    ):
        features = prime.FeatureExtraction(self._model)
        feature_params = prime.ExtractFeatureParams(
            model=self._model,
            feature_angle=40.0,
            label_name="__extracted__features__",
            disconnect_with_faces=False,
            replace=True,
        )
        for part in parts:
            total_labels = part.get_labels()
            name_pattern_params = prime.NamePatternParams(model=self._model)
            source = []
            target = []
            for label in total_labels:
                source = part.get_face_zonelets_of_label_name_pattern(
                    "connect_topology_source", name_pattern_params
                )
                target = part.get_face_zonelets_of_label_name_pattern(
                    "connect_topology_target", name_pattern_params
                )
            if len(source) > 0 and len(target) > 0:
                print(source)
                print(target)
                resolved = False
                for tol in connect_tolerances:
                    result = self.mesh_match(
                        part=part,
                        join_to_faces=source,
                        join_faces=target,
                        tolerance=tol,
                        side_tolerance=side_tolerance,
                        use_abs_tol=use_absolute_connect_tolerance,
                        max_angle=mesh_match_angle,
                        fuseOption=prime.FuseOption.TRIMONESIDE,
                    )
                    num_warn_codes = len(result.warning_codes)
                    if num_warn_codes == 0 and result.error_code == prime.ErrorCode.NOERROR:
                        resolved = True
                        break
                    if len(result.warning_codes):
                        self._logger.warning('Failed to remove overlaps in part' + part.name)
                if resolved:
                    part.remove_labels_from_zonelets(
                        ["connect_topology_source", "connect_topology_target"],
                        part.get_face_zonelets(),
                    )
                else:
                    checks = self.surface_intersection_results(part)
                    if checks[0] > 0:
                        err_string = "Found self intersections at" + str(checks[1])
                        print(err_string)

    def stfailure2(
        self,
        connect_tolerance,
        side_tolerance,
        use_absolute_connect_tolerance,
        part_name,
        use_mesh_match,
        mesh_match_angle,
        interfering_parts_priority,
        debug,
    ):
        if len(self._model.parts) == 1:
            self._connect_interfering_volumes(
                parts_name_exp="*",
                join_tolerance=connect_tolerance,
                side_tolerance=side_tolerance,
                use_abs_tol=use_absolute_connect_tolerance,
                intersect_tolerance=0.05,
                join_remesh=True,
                connected_part_name=part_name,
                use_mesh_match=use_mesh_match,
                mesh_match_angle=mesh_match_angle,
                priority_ordered_part_names_in=interfering_parts_priority,
                intersect=False,
                part_labels=[],
                debug=debug,
            )

    def cusp_removal(
        self,
        connect_tolerances: list,
        side_tolerance: float,
        part_expression: str,
        source_labels: str,
        target_labels: str,
        mesh_match_angle: float = 45,
        debug: bool = False,
    ):
        list_parts_to_connect = self.get_parts_of_name_pattern(part_expression)
        pattern_params = prime.NamePatternParams(model=self._model)
        for part in list_parts_to_connect:
            source = part.get_face_zonelets_of_label_name_pattern(source_labels, pattern_params)
            target = part.get_face_zonelets_of_label_name_pattern(target_labels, pattern_params)
            for tol in connect_tolerances:
                result = self.mesh_match(
                    part=part,
                    join_to_faces=source,
                    join_faces=target,
                    tolerance=tol,
                    side_tolerance=side_tolerance,
                    use_abs_tol=True,
                    max_angle=mesh_match_angle,
                    fuseOption=prime.FuseOption.TRIMTWOSIDES,
                    separate=False,
                )

    def _recompute_vol_preserve_names(self, part_name: str):
        part = self._model.get_part_by_name(part_name)
        volume_zone_ids = part.get_volume_zones()
        zone_names = [self._model.get_zone_name(i) for i in volume_zone_ids]
        for zone_name in zone_names:
            fz = part.get_face_zonelets_of_volumes(
                part.get_volumes_of_zone_name_pattern(
                    zone_name, prime.NamePatternParams(self._model)
                )
            )
            part.add_labels_on_zonelets([zone_name], fz)
        all_labels = part.get_labels()
        excluded_lables = list(set(all_labels) - set(zone_names))
        compute_volume_params = prime.ComputeVolumesParams(
            model=self._model,
            create_zones_type=prime.CreateVolumeZonesType.PERVOLUME,
            priority_ordered_names=zone_names,
            exclude_names=excluded_lables,
            volume_naming_type=prime.VolumeNamingType.BYFACELABEL,
        )
        result = part.compute_closed_volumes(compute_volume_params)

    def fuse(
        self,
        connect_tolerance: list,
        side_tolerance: float,
        part_expression: str,
        part_name: str = "tolerant_connect_part",
        delete_topology: bool = False,
        refine_at_contacts: bool = False,
        use_absolute_connect_tolerance: bool = True,
        mesh_match_angle: int = 45,
        write_intermediate_files: bool = False,
        debug: bool = False,
    ):
        """Fuse."""
        list_parts_to_connect = self.get_parts_of_name_pattern(part_expression)
        connected_part = self._model.get_part_by_name(part_name)
        if connected_part != None:
            skip = False
            for p in list_parts_to_connect:
                if p.id == connected_part.id:
                    skip = True
                    break
            if skip == False:
                # print("inserting final part into list")
                list_parts_to_connect.insert(0, connected_part)
        if refine_at_contacts:
            rc_results = self.refine_contacts(min(connect_tolerance), list_parts_to_connect)
        if delete_topology:
            self.delete_topology(list_parts_to_connect)
            # self.write("after_delete_topology.pmdat",)
        # extra face label deletion
        for part in list_parts_to_connect:
            total_labels = part.get_labels()
            for label in total_labels:
                if "__attrib_abr_topotype" in label:
                    part.remove_labels_from_zonelets(
                        [label],
                        part.get_face_zonelets(),
                    )
                    part.remove_labels_from_zonelets(
                        [label],
                        part.get_edge_zonelets(),
                    )
        # mesh match within part in case of shared topology failure
        self.stfailure1(
            list_parts_to_connect,
            connect_tolerance,
            side_tolerance,
            use_absolute_connect_tolerance,
            mesh_match_angle,
        )
        # self.stfailure2(
        #     connect_tolerance,
        #     side_tolerance,
        #     use_absolute_connect_tolerance,
        #     part_name,
        #     mesh_match_angle,
        #     interfering_parts_priority,
        #     debug
        # )
        vol_part_name = ""
        cont_part_name = ""
        part_labels = []
        # [TODO] following edge deletion code is a workaround to speedup join intersect.
        # Remove it when the slowness is fixed
        if len(list_parts_to_connect) > 1:
            if not debug:
                part_labels = self.zone_management(list_parts_to_connect)
                self._collapse_within_parts(list_parts_to_connect, 1.2 * max(connect_tolerance))
            self._connect_interfering_parts_multi_tol(
                interfering_parts=list_parts_to_connect,
                join_tolerances=connect_tolerance,
                side_tolerance=side_tolerance,
                use_abs_tol=use_absolute_connect_tolerance,
                connected_part_name=part_name,
                mesh_match_angle=mesh_match_angle,
                part_labels=part_labels,
                debug=debug,
            )
            part = self._model.get_part_by_name(part_name)
            part.remove_labels_from_zonelets(part_labels, part.get_face_zonelets())
            self._recompute_vol_preserve_names(part_name)
            if refine_at_contacts:
                self._model.deactivate_volumetric_size_fields([rc_results.size_field_id])
                self.surface_mesh_coarsening(part)
                self.post_surface_mesh_cleanup_triangles(part, keep_small_free_surfaces=True)
        if write_intermediate_files:
            self.write("after_fuse.pmdat")

    def write(self, filename: str):
        prime.FileIO(self._model).write_pmdat(filename, prime.FileWriteParams(self._model))

