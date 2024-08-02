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
        result = connect.fuse_face_zonelets(part.id, sourceFaces, targetFaces, params)
        if not result.error_code:
            prime.PrimeRuntimeError(
                "mesh match is not successful and error code = {}".format(result.error_code)
            )
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

    def _collapse_within_parts(
        self, collapse_within_parts_name_exp: str = "", tolerance: float = 0.05
    ):
        model = self._model
        parts_to_collapse = self.get_parts_of_name_pattern(collapse_within_parts_name_exp)
        surface_search_tool = prime.SurfaceSearch(model=model)
        collapse_tool = prime.CollapseTool(model=model)
        # maybe the loop is not required?
        for part in parts_to_collapse:
            faces = part.get_face_zonelets()
            self._collapse_thin_strips(surface_search_tool, collapse_tool, part, faces, tolerance)

    def _connect_interfering_parts(
        self,
        parts_name_exp: str = "*",
        join_tolerance: float = 0.05,
        side_tolerance: float = 0.05,
        use_abs_tol: bool = False,
        intersect_tolerance: float = 0.05,
        join_remesh: bool = True,
        connected_part_name: str = "merged_part",
        use_mesh_match: bool = False,
        mesh_match_angle: float = 45,
        priority_ordered_part_names_in: List[str] = [],
        intersect: bool = True,
        part_labels: list = [],
        fuse_edges_only: bool = False,
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
        join_params = prime.JoinParams(
            model=self._model,
            tolerance=join_tolerance,
            use_absolute_tolerance=use_abs_tol,
            remesh=join_remesh,
        )
        intersect_params = prime.IntersectParams(
            model=self._model,
            tolerance=intersect_tolerance,
        )
        features = prime.FeatureExtraction(self._model)
        feature_params = prime.ExtractFeatureParams(
            model=self._model,
            feature_angle=40.0,
            label_name="__extracted__features__",
            disconnect_with_faces=False,
            replace=True,
        )
        n_parts = len(interfering_parts)
        if n_parts > 1:
            for part_i in range(n_parts):
                part = interfering_parts[part_i]
                part.delete_zonelets(part.get_edge_zonelets())
            # merged_part = model.get_part_by_name(connected_part_name)
            # for part_i in range(n_parts):
            merged_part = interfering_parts[0]
            for part_i in range(1, n_parts):
                part = interfering_parts[part_i]
                join_to_faces = merged_part.get_face_zonelets()
                parts_to_merge = [merged_part.id]
                if part.id == merged_part.id:
                    continue
                part_name = part.name
                print("Connecting part ", merged_part.name, " with part ", part.name)
                # self.write("before_mesh_matchin_with_part_" +  part_name + ".pmdat")
                join_faces = part.get_face_zonelets()
                if use_mesh_match:
                    if part_i == 1:
                        res = features.extract_features_on_face_zonelets(
                            part_id=merged_part.id,
                            face_zonelets=join_to_faces,
                            params=feature_params,
                        )
                    res = features.extract_features_on_face_zonelets(
                        part_id=part.id, face_zonelets=join_faces, params=feature_params
                    )
                parts_to_merge.append(part.id)
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
                if use_mesh_match:
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
                else:
                    joinres = connect.join_face_zonelets(
                        merge_res.merged_part_id,
                        join_to_faces,
                        join_faces,
                        join_params,
                    )
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
                # self._lucid_mesh.write("after_just_connection_with_part_" +  part_name + ".pmdat")
            merged_part.delete_zonelets(merged_part.get_edge_zonelets())
        elif n_parts == 1:
            merged_part = interfering_parts[0]
            merged_part.set_suggested_name(connected_part_name)

    def connect_volumetric_interfering_parts(
        self,
        parts_name_exp: str = "*",
        join_tolerance: float = 0.05,
        side_tolerance: float = 0.05,
        use_abs_tol: bool = False,
        intersect_tolerance: float = 0.05,
        join_remesh: bool = True,
        priority_ordered_part_names: List[str] = [],
        connected_part_name: str = "merged_part",
        use_mesh_match: bool = False,
        mesh_match_angle: float = 45,
        part_labels: list = [],
    ):
        """Connect volumetric interfering parts."""
        return self._connect_interfering_parts(
            parts_name_exp=parts_name_exp,
            join_tolerance=join_tolerance,
            side_tolerance=side_tolerance,
            use_abs_tol=use_abs_tol,
            intersect_tolerance=intersect_tolerance,
            join_remesh=join_remesh,
            connected_part_name=connected_part_name,
            use_mesh_match=use_mesh_match,
            mesh_match_angle=mesh_match_angle,
            priority_ordered_part_names_in=priority_ordered_part_names,
            intersect=True,
            part_labels=part_labels,
        )

    def connect_contact_interfering_parts(
        self,
        parts_name_exp: str = "*",
        join_tolerance: float = 0.05,
        side_tolerance: float = 0.05,
        use_abs_tol: bool = False,
        join_remesh: bool = True,
        connected_part_name: str = "merged_part",
        use_mesh_match: bool = False,
        mesh_match_angle: float = 45,
        part_labels: list = [],
        fuse_edges_only: bool = False,
    ):
        """Connect contact interfering parts."""
        return self._connect_interfering_parts(
            parts_name_exp=parts_name_exp,
            join_tolerance=join_tolerance,
            side_tolerance=side_tolerance,
            use_abs_tol=use_abs_tol,
            intersect_tolerance=0.05,
            join_remesh=join_remesh,
            connected_part_name=connected_part_name,
            use_mesh_match=use_mesh_match,
            mesh_match_angle=mesh_match_angle,
            priority_ordered_part_names_in=[],
            intersect=False,
            part_labels=part_labels,
            fuse_edges_only=fuse_edges_only,
        )

    def zone_management(self):
        """Zone management."""
        label_list = []
        mergeParams = prime.MergeZoneletsParams(model=self._model)
        for part in self._model.parts:
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
        part_name_exp: str = "*",
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
        write_intermediate_files: bool = False,
    ):
        """Delete topology."""
        params = prime.DeleteTopoEntitiesParams(model=self._model, delete_geom_zonelets=True)
        part_ids_to_delete = []
        result = None
        for part in self._model.parts:
            if part.get_topo_faces():
                part.delete_topo_entities(params)
            else:
                self._logger.info("No topology to delete in part: " + part.name)
                part_ids_to_delete.append(part.id)
        self.post_surface_mesh_cleanup_triangles("*", keep_small_free_surfaces=True)
        if write_intermediate_files:
            self.write("after_delete_topology.pmdat")
        return result

    def refine_contacts(
        self,
        connect_tolerance: float,
    ):
        """Refine contacts."""
        result = None
        global_min_size = self._model.get_global_sizing_params().min
        part_ids = [part.id for part in self._model.parts]
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

    def fuse(
        self,
        connect_tolerance: float,
        side_tolerance: float,
        connect_parts_with_diff_tol: list,
        interfering_parts_exp: str,
        interfering_parts_priority: list,
        contact_parts_exp: str,
        part_name: str = "tolerant_connect_part",
        delete_topology: bool = False,
        refine_at_contacts: bool = False,
        use_absolute_connect_tolerance: bool = True,
        use_mesh_match: bool = True,
        mesh_match_angle: int = 45,
        write_intermediate_files: bool = False,
    ):
        """Fuse."""
        if refine_at_contacts:
            refine_contact_results = self.refine_contacts(connect_tolerance)
        if delete_topology:
            self.delete_topology()
        # mesh match within part in case of shared topology failure
        for part in self._model.parts:
            non_share_labels = []
            total_labels = part.get_labels()
            for label in total_labels:
                if "connect_topology" in label:
                    non_share_labels.append(label)
            for non_share_label in non_share_labels:
                name_pattern_params = prime.NamePatternParams(model=self._model)
                face_zonelets = part.get_face_zonelets_of_label_name_pattern(
                    non_share_label, name_pattern_params
                )
                result = self.mesh_match(
                    part=part,
                    join_to_faces=face_zonelets,
                    join_faces=face_zonelets,
                    tolerance=connect_tolerance,
                    side_tolerance=side_tolerance,
                    use_abs_tol=use_absolute_connect_tolerance,
                    max_angle=mesh_match_angle,
                    fuseOption=prime.FuseOption.TRIMONESIDE,
                )
                if prime.WarningCode.FUSEOVERLAPREMOVALINCOMPLETE in result.warning_codes:
                    self._logger.warning('Failed to remove overlaps in part' + part.name)
                if prime.WarningCode.REMOVEOVERLAPWITHINTERSECT in result.warning_codes:
                    self._logger.warning(
                        'Intersections found when removing overlaps in part' + part.name
                    )
        vol_part_name = ""
        cont_part_name = ""
        part_labels = self.zone_management()
        # [TODO] following edge deletion code is a workaround to speedup join intersect.
        # Remove it when the slowness is fixed
        if len(self._model.parts) > 1:
            self._collapse_within_parts("*", 1.5 * connect_tolerance)
            for part in self._model.parts:
                edge_zonelets = part.get_edge_zonelets()
                if edge_zonelets:
                    part.delete_zonelets(edge_zonelets)
            for part_list in connect_parts_with_diff_tol:
                connect_parts = []
                prt_list = part_list["part_expression"]
                if "*" not in prt_list and "!" not in prt_list:
                    patterns = prt_list.split(",")
                    for pattern in patterns:
                        connect_parts.extend(self.get_parts_of_name_pattern(pattern))
                else:
                    connect_parts = self.get_parts_of_name_pattern(prt_list)
                part_name1 = connect_parts[0].name
                self.connect_volumetric_interfering_parts(
                    parts_name_exp=prt_list,
                    join_tolerance=part_list["local_connect_tolerance"],
                    side_tolerance=part_list["local_side_tolerance"],
                    priority_ordered_part_names="",
                    use_abs_tol=use_absolute_connect_tolerance,
                    connected_part_name=part_name1,
                    use_mesh_match=use_mesh_match,
                    mesh_match_angle=mesh_match_angle,
                    part_labels=part_labels,
                )
            if self.get_parts_of_name_pattern(interfering_parts_exp):
                vol_part_name = part_name
                self.connect_volumetric_interfering_parts(
                    parts_name_exp=interfering_parts_exp,
                    join_tolerance=connect_tolerance,
                    side_tolerance=side_tolerance,
                    use_abs_tol=use_absolute_connect_tolerance,
                    intersect_tolerance=0.05,
                    priority_ordered_part_names=interfering_parts_priority,
                    connected_part_name=vol_part_name,
                    use_mesh_match=use_mesh_match,
                    mesh_match_angle=mesh_match_angle,
                    part_labels=part_labels,
                )
            if self.get_parts_of_name_pattern(contact_parts_exp):
                cont_part_name = part_name if vol_part_name == "" else "contact_interfering_part"
                self.connect_contact_interfering_parts(
                    parts_name_exp=contact_parts_exp,
                    join_tolerance=connect_tolerance,
                    side_tolerance=side_tolerance,
                    use_abs_tol=use_absolute_connect_tolerance,
                    connected_part_name=cont_part_name,
                    use_mesh_match=use_mesh_match,
                    mesh_match_angle=mesh_match_angle,
                    part_labels=part_labels,
                )
            if vol_part_name != "" and cont_part_name != "":
                connect_part_exp = vol_part_name + ", " + cont_part_name
                self.connect_contact_interfering_parts(
                    parts_name_exp=connect_part_exp,
                    join_tolerance=connect_tolerance,
                    side_tolerance=side_tolerance,
                    use_abs_tol=use_absolute_connect_tolerance,
                    join_remesh=True,
                    connected_part_name=part_name,
                    use_mesh_match=use_mesh_match,
                    mesh_match_angle=mesh_match_angle,
                    part_labels=part_labels,
                )
            tolerant_connect_part = self._model.get_part_by_name(part_name)
            # if not interferences, no conflict volumes to resolve
            if len(interfering_parts_exp) > 0:
                self.write("before_resolve_conflict.pmdat")
                self._resolve_conflicts(
                    name=part_name,
                    all_labels_in=part_labels,
                    priority_ordered_part_names_in=interfering_parts_priority,
                    new_vol_zone_name="unclaimed_vol_zone",
                )
            tolerant_connect_part.remove_labels_from_zonelets(
                part_labels, tolerant_connect_part.get_face_zonelets()
            )
            if refine_at_contacts:
                self._model.deactivate_volumetric_size_fields(
                    [refine_contact_results.size_field_id]
                )
                for part in self._model.parts:
                    self.surface_mesh_coarsening(part)
                self.post_surface_mesh_cleanup_triangles("*", keep_small_free_surfaces=True)

        if write_intermediate_files:
            self.write("after_fuse.pmdat")
