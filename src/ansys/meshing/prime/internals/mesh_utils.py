'''
Copyright 1987-2024 ANSYS, Inc. All Rights Reserved.
**This is a beta API**. **The behavior and implementation may change in future**.
'''

import ansys.meshing.prime as prime
from ansys.meshing.prime.internals.error_handling import PrimeRuntimeError
from ansys.meshing.prime.internals.error_handling import PrimeRuntimeWarning
from ansys.meshing.prime import Model, Part
from ansys.meshing.prime import ScopeDefinition, ScopeEntity
from ansys.meshing.prime import (
    SizingType,
    SizeField,
    VolumetricSizeFieldComputeParams,
    SFPeriodicParams,
)
from typing import List, Iterable
import os


class TolerantConnect:
    """
    Provides methods to user who is new to meshing.
    This class also serves as a tutorial
    for commonly used tolerant connect workflows.
    The ``TolerantConnect`` class provides these functionalities:
    *
    *
    *
    *
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

    def compute_size_field_with_periodic(
        self, size_settings: list, periodic_info: dict = None
    ):
        """Computes size field using the size settings and periodic inputs.
        Parameters
        ----------
        size_settings : list
            List of size settings to create size controls.
        periodic_info : dict, optional
            Dictionary containing angle, axis and center for periodic.
                The default is ``None``.
        """
        size_control_ids = []
        for size_control in size_settings:
            control = self.create_size_control_from_settings(size_control)
            size_control_ids.append(control)

        sizefield = SizeField(self._model)
        sizefield_params = VolumetricSizeFieldComputeParams(self._model)
        if periodic_info:
            periodic_params = SFPeriodicParams(
                model=self._model,
                angle=periodic_info["angle"],
                axis=periodic_info["axis"],
                center=periodic_info["center"],
            )
            sizefield_params.periodic_params = periodic_params
            sizefield_params.enable_periodicity = True

        sizefield_result = sizefield.compute_volumetric(
            size_control_ids=size_control_ids,
            volumetric_sizefield_params=sizefield_params,
        )
        return sizefield_result

    def surface_mesh_with_volumetric_size_field(self):
        """
        Surface mesh all topo faces of all parts
        with the active volumetric size field.
        """
        surface_mesher = prime.Surfer(self._model)
        surface_params = prime.SurferParams(
            model=self._model,
            size_field_type=prime.SizeFieldType.VOLUMETRIC,
            enable_multi_threading=False,
            project_on_geometry=True,
            # alignTriEdgeMesh=True,
        )
        for part in self._model.parts:
            topo_faces = part.get_topo_faces()
            try:
                surface_mesher.mesh_topo_faces(
                    part_id=part.id,
                    topo_faces=topo_faces,
                    params=surface_params,
                )
                n_unmeshed_topo_faces = part.get_summary(
                    prime.PartSummaryParams(model=self._model)
                ).n_unmeshed_topo_faces
                if n_unmeshed_topo_faces:
                    unmeshed_faces = [
                        face
                        for face in topo_faces
                        if not self._model.topo_data.get_mesh_zonelets_of_topo_faces(
                            [face]
                        )
                    ]
                    part.add_labels_on_topo_entities(
                        ["WARNING:Unmeshed_topo_face"], unmeshed_faces
                    )
                    self._logger.warning(
                        "Unmeshed topo face ids "
                        + str(unmeshed_faces)
                        + " on part "
                        + part.name
                    )
            except PrimeRuntimeError as error:
                error_label = (
                    "Error: '{}' on '{}' with code '{}' and message '{}'.".format(
                        error.error_locations,
                        part.name,
                        error.error_code,
                        error.message,
                    )
                )
                part.add_labels_on_topo_entities([error_label], error.error_locations)
            except PrimeRuntimeWarning as warning:
                warning_label = "Warning: '{}' with message '{}'.".format(
                    part.name,
                    warning.message,
                )
                part.add_labels_on_topo_entities([warning_label], [])
        return

    def delete_parts_by_name_pattern(self, name_pattern: str) -> Iterable[int]:
        delete_parts = self.get_parts_of_name_pattern(name_pattern)
        if delete_parts:
            self._model.delete_parts([part.id for part in delete_parts])
        return delete_parts

    def get_parts_of_name_pattern(self, part_name_pattern: str) -> Iterable[Part]:
        matching_parts = []
        for part in self._model.parts:
            utils = prime.lucid.utils
            if utils.check_name_pattern(part_name_pattern, part.name):
                matching_parts.append(part)
        return matching_parts

    def part_get_face_zonelets_without_zone(self, part: Part) -> Iterable[int]:
        patternParams = prime.NamePatternParams(model=self._model)
        zones = part.get_face_zones()
        zonelets_with_zones = []
        for zone in zones:
            zone_name = self._model.get_zone_name(zone)
            zonelets = part.get_face_zonelets_of_zone_name_pattern(
                zone_name, patternParams
            )
            zonelets_with_zones.extend(zonelets)
        zonelets_without_zone = list(
            set(part.get_face_zonelets()) - set(zonelets_with_zones)
        )
        return zonelets_without_zone

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

        return self_inter_res.n_found, all_locations

    def auto_node_movement(
        self,
        part: Part,
        quality_measure: prime.CellQualityMeasure,
        target_quality: float,
        dihedral_angle: float,
        n_iteration_per_node: int,
        attempts: int,
        restrict_boundary=True,
    ):
        perform_anm = prime.VolumeMeshTool(model=self._model)
        anm_param = prime.AutoNodeMoveParams(
            model=self._model,
            quality_measure=quality_measure,
            target_quality=target_quality,
            dihedral_angle=dihedral_angle,
            n_iterations_per_node=n_iteration_per_node,
            restrict_boundary_nodes_along_surface=restrict_boundary,
            n_attempts=attempts,
        )
        result = perform_anm.improve_by_auto_node_move(
            part.id,
            part.get_cell_zonelets(),
            part.get_face_zonelets(),
            anm_param,
        )
        return result

    def evaluation_value(self, input_string):
        value = input_string.lower()
        if value == 'curvature':
            return prime.SizingType.CURVATURE
        if value == 'proximity':
            return prime.SizingType.PROXIMITY
        if value == 'hard':
            return prime.SizingType.HARD
        if value == 'soft':
            return prime.SizingType.SOFT
        if value == 'boi':
            return prime.SizingType.BOI
        if value == 'meshed':
            return prime.SizingType.MESHED
        if value == 'edgezonelets' or value == 'edge_zonelets':
            return prime.ScopeEntity.EDGEZONELETS
        if value == 'facezonelets' or value == 'face_zonelets':
            return prime.ScopeEntity.FACEZONELETS
        if value == 'faceandedgezonelets' or value == 'face_and_edge_zonelets':
            return prime.ScopeEntity.FACEANDEDGEZONELETS
        if value == 'volume':
            return prime.ScopeEntity.VOLUME
        if value == 'labels':
            return prime.ScopeEvaluationType.LABELS
        if value == 'zones':
            return prime.ScopeEvaluationType.ZONES
        if value == 'tet':
            return prime.VolumeFillType.TET
        if value == 'poly':
            return prime.VolumeFillType.POLY
        if value == 'hexcoretet' or value == 'hex_core_tet':
            return prime.VolumeFillType.HEXCORETET
        if value == 'hexcorepoly' or value == 'hex_core_poly':
            return prime.VolumeFillType.HEXCOREPOLY

    def create_size_control_from_settings(self, size_control_setting) -> int:
        min_size_str = "min_size"
        max_size_str = "max_size"
        gr_str = "growth_rate"
        if "type" in size_control_setting:
            type1 = size_control_setting["type"]
            ctrl_type = self.evaluation_value(type1)
        else:
            raise PrimeRuntimeError("type is not specified in size control settings")
        ctrl = self._model.control_data.create_size_control(ctrl_type)
        if "name" in size_control_setting:
            ctrl.set_suggested_name(size_control_setting["name"])
        scope = ScopeDefinition(model=self._model)
        if "part_expression" in size_control_setting:
            scope.part_expression = size_control_setting["part_expression"]
        if "label_expression" in size_control_setting:
            scope.label_expression = size_control_setting["label_expression"]
        if "entity_type" in size_control_setting:
            entity_types = size_control_setting["entity_type"]
            scope.entity_type = self.evaluation_value(entity_types)
        ctrl.set_scope(scope)
        if ctrl_type == SizingType.CURVATURE:
            params = prime.CurvatureSizingParams(
                model=self._model, use_cad_curvature=True
            )
            if min_size_str in size_control_setting:
                params.min = size_control_setting[min_size_str]
            if max_size_str in size_control_setting:
                params.max = size_control_setting[max_size_str]
            if gr_str in size_control_setting:
                params.growth_rate = size_control_setting[gr_str]
            if "normal_angle" in size_control_setting:
                params.normal_angle = size_control_setting["normal_angle"]
            ctrl.set_curvature_sizing_params(params)
        elif ctrl_type == SizingType.PROXIMITY:
            params = prime.ProximitySizingParams(model=self._model)
            if min_size_str in size_control_setting:
                params.min = size_control_setting[min_size_str]
            if max_size_str in size_control_setting:
                params.max = size_control_setting[max_size_str]
            if gr_str in size_control_setting:
                params.growth_rate = size_control_setting[gr_str]
            if "elements_per_gap" in size_control_setting:
                params.elements_per_gap = size_control_setting["elements_per_gap"]
            ctrl.set_proximity_sizing_params(params)
        elif ctrl_type == SizingType.SOFT:
            params = prime.SoftSizingParams(model=self._model)
            if max_size_str in size_control_setting:
                params.max = size_control_setting[max_size_str]
            if gr_str in size_control_setting:
                params.growth_rate = size_control_setting[gr_str]
            ctrl.set_soft_sizing_params(params)
        elif ctrl_type == SizingType.BOI:
            params = prime.BoiSizingParams(model=self._model)
            if max_size_str in size_control_setting:
                params.max = size_control_setting[max_size_str]
            if gr_str in size_control_setting:
                params.growth_rate = size_control_setting[gr_str]
            ctrl.set_boi_sizing_params(params)
        return ctrl.id

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
    ):
        connect = prime.Connect(model=self._model)
        params = prime.FuseParams(
            model=self._model,
            fuse_option=prime.FuseOption.TRIMONESIDE,
        )
        params.use_absolute_tolerance = use_abs_tol
        params.gap_tolerance = tolerance
        params.side_tolerance = side_tolerance
        params.fuse_option = fuseOption
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
                "mesh match is not successful and error code = {}".format(
                    result.error_code
                )
            )
        return result.error_code

    def post_surface_mesh_cleanup_triangles(
        self,
        part_name_exp: str = "*",
        collapse_sliver_faces: bool = True,
        stitch_free_faces: bool = True,
        keep_small_free_surfaces: bool = False,
    ):
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
                    collapse_params.feature_type = (
                        prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
                    )
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
                        checks = surface_search_tool.get_surface_diagnostic_summary(
                            diag_params
                        )
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
                    collapse_params.feature_type = (
                        prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
                    )
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

    def _collapse_thin_strips(
        self,
        surface_search_tool,
        collapse_tool,
        part,
        face_zonelets,
        abs_tol,
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
        trim_small_volumes_from_parts_exp: str = "",
        trim_volume_limit: float = 0.0,
        fluid_volume_mpt_settings: list = [],
        keep_small_free_surfaces: bool = False,
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
            ordered_names = [
                part.name for part in self.get_parts_of_name_pattern(part_name_exp)
            ]
            if not ordered_names:
                failed_part_name_exp.append(part_name_exp)
            else:
                priority_ordered_part_names.extend(ordered_names)
        if priority_ordered_part_names_in and failed_part_name_exp:
            for part_name_exp in failed_part_name_exp:
                self._logger.warning(
                    'No parts found for expression "'
                    + part_name_exp
                    + '" specified in interfering_parts_priority setting'
                )
        if trim_volume_limit > 0 and trim_small_volumes_from_parts_exp != "":
            if not self.get_parts_of_name_pattern(trim_small_volumes_from_parts_exp):
                self._logger.warning(
                    "No parts found for expression"
                    + trim_small_volumes_from_parts_exp
                    + " specified as delete_small_volumes_of_parts_exp setting"
                )
        connect = prime.Connect(self._model)
        join_params = prime.JoinParams(
            model=self._model,
            tolerance=join_tolerance,
            use_absolute_tolerance=use_abs_tol,
            remesh=join_remesh,
        )
        intersect_params = prime.IntersectParams(
            model=self._model, tolerance=intersect_tolerance
        )
        surface_search = prime.SurfaceSearch(model=self._model)
        delete_tool = prime.DeleteTool(model=self._model)
        features = prime.FeatureExtraction(self._model)
        feature_params = prime.ExtractFeatureParams(
            model=self._model,
            feature_angle=40.0,
            label_name="__extracted__features__",
            disconnect_with_faces=False,
            replace=True,
        )
        surface_search_tool = prime.SurfaceSearch(model=self._model)
        collapse_tool = prime.CollapseTool(model=self._model)
        n_parts = len(interfering_parts)
        if n_parts > 1:
            compute_volume_params = prime.ComputeVolumesParams(
                self._model,
                create_zones_type=prime.CreateVolumeZonesType.PERNAMESOURCE,
                volume_naming_type=prime.VolumeNamingType.BYFACELABEL,
                priority_ordered_names=priority_ordered_part_names,
            )
            prev_trim_volumes = []
            if intersect:
                mpt_names = []
                mpt_params = prime.CreateMaterialPointParams(
                    model=self._model,
                    type=prime.MaterialPointType.LIVE,
                )
                for mpt_settings in fluid_volume_mpt_settings:
                    results = self._model.material_point_data.create_material_point(
                        suggested_name=mpt_settings["name"],
                        coords=mpt_settings["location"],
                        params=mpt_params,
                    )
                    mpt_names.append(results.assigned_name)
                    compute_volume_params.material_point_names.append(
                        results.assigned_name
                    )
            merged_part = interfering_parts[0]
            for part_i in range(1, n_parts):
                if merged_part.get_edge_zonelets():
                    merged_part.delete_zonelets(merged_part.get_edge_zonelets())
                part = interfering_parts[part_i]
                join_to_faces = merged_part.get_face_zonelets()
                parts_to_merge = [merged_part.id]
                part_name = part.name
                print("Connecting part ", merged_part.name, " with part ", part.name)
                if merged_part.get_edge_zonelets():
                    merged_part.delete_zonelets(merged_part.get_edge_zonelets())
                if part.get_edge_zonelets():
                    part.delete_zonelets(part.get_edge_zonelets())
                join_faces = part.get_face_zonelets()
                if use_mesh_match:
                    if part_i == 1:
                        self._collapse_thin_strips(
                            surface_search_tool,
                            collapse_tool,
                            merged_part,
                            join_to_faces,
                            join_tolerance * 1.5,
                        )
                    self._collapse_thin_strips(
                        surface_search_tool,
                        collapse_tool,
                        part,
                        join_faces,
                        join_tolerance * 1.5,
                    )
                    features.extract_features_on_face_zonelets(
                        part_id=merged_part.id,
                        face_zonelets=join_to_faces,
                        params=feature_params,
                    )
                    features.extract_features_on_face_zonelets(
                        part_id=part.id,
                        face_zonelets=join_faces,
                        params=feature_params,
                    )
                parts_to_merge.append(part.id)
                merge_part_params = prime.MergePartsParams(
                    model=self._model,
                    merged_part_suggested_name=connected_part_name,
                )
                merge_res = self._model.merge_parts(parts_to_merge, merge_part_params)
                merged_part = self._model.get_part(merge_res.merged_part_id)
                if merged_part is None:
                    print("invalid part returned")
                merged_part.add_labels_on_zonelets([dummy_unique_label1], join_to_faces)
                merged_part.add_labels_on_zonelets([dummy_unique_label2], join_faces)
                if use_mesh_match:
                    self.mesh_match(
                        merged_part,
                        join_to_faces,
                        join_faces,
                        join_tolerance,
                        side_tolerance,
                        use_abs_tol,
                        mesh_match_angle,
                        prime.FuseOption.TRIMONESIDE,
                    )
                else:
                    connect.join_face_zonelets(
                        merge_res.merged_part_id,
                        join_to_faces,
                        join_faces,
                        join_params,
                    )
                if merged_part.get_edge_zonelets():
                    merged_part.delete_zonelets(merged_part.get_edge_zonelets())
                if intersect:
                    intersect_to_faces = (
                        merged_part.get_face_zonelets_of_label_name_pattern(
                            dummy_unique_label1,
                            pattern_params,
                        )
                    )
                    intersect_faces = (
                        merged_part.get_face_zonelets_of_label_name_pattern(
                            dummy_unique_label2,
                            pattern_params,
                        )
                    )
                    intersect_params = prime.IntersectParams(
                        self._model, intersect_tolerance
                    )
                    connect.intersect_face_zonelets(
                        merged_part.id,
                        intersect_faces,
                        intersect_to_faces,
                        intersect_params,
                    )
                register_id = 26
                self_params = prime.SearchBySelfIntersectionParams(model=self._model)
                search_results = surface_search.search_zonelets_by_self_intersections(
                    part_id=merged_part.id,
                    face_zonelets=merged_part.get_face_zonelets(),
                    register_id=register_id,
                    params=self_params,
                )
                if search_results.n_found:
                    intersect_to_faces = (
                        merged_part.get_face_zonelets_of_label_name_pattern(
                            dummy_unique_label1, pattern_params
                        )
                    )
                    intersect_faces = (
                        merged_part.get_face_zonelets_of_label_name_pattern(
                            dummy_unique_label2, pattern_params
                        )
                    )
                    intersect_params = prime.IntersectParams(
                        model=self._model, tolerance=0.1 * intersect_tolerance
                    )
                    connect.intersect_face_zonelets(
                        merged_part.id,
                        intersect_faces,
                        intersect_to_faces,
                        intersect_params,
                    )
                if intersect:
                    diag_params = prime.SurfaceDiagnosticSummaryParams(
                        self._model,
                        scope=ScopeDefinition(
                            self._model, part_expression=merged_part.name
                        ),
                        compute_self_intersections=True,
                        compute_free_edges=True,
                        compute_multi_edges=True,
                        compute_duplicate_faces=True,
                    )
                    checks = surface_search.get_surface_diagnostic_summary(diag_params)
                    if (
                        checks.n_free_edges > 0
                        or checks.n_multi_edges > 0
                        or checks.n_self_intersections > 0
                        or checks.n_duplicate_faces > 0
                    ):
                        # print(
                        #   merged_part.name,
                        #   checks.n_free_edges,
                        #   checks.n_multi_edges,
                        #   checks.n_self_intersections,
                        #   checks.n_duplicate_faces,
                        # )
                        if checks.n_multi_edges > 0 or checks.n_free_edges > 0:
                            zonelets = merged_part.get_face_zonelets()
                            # print(
                            #   "before delete fringes ",
                            #   merged_part.name,
                            #   checks.n_free_edges,
                            #   checks.n_multi_edges,
                            #   checks.n_self_intersections,
                            #   checks.n_duplicate_faces,
                            #   0 if keep_small_free_surfaces else 5,
                            # )
                            delete_fringe_params = prime.DeleteFringesAndOverlapsParams(
                                model=self._model,
                                fringe_element_count=0
                                if keep_small_free_surfaces
                                else 5,
                                overlap_element_count=3,
                                delete_overlaps=True,
                            )
                            delete_tool.delete_fringes_and_overlaps_on_zonelets(
                                merged_part.id, zonelets, delete_fringe_params
                            )
                        checks = surface_search.get_surface_diagnostic_summary(
                            diag_params
                        )
                all_face_zonelets = merged_part.get_face_zonelets()
                merged_part.remove_labels_from_zonelets(
                    [dummy_unique_label1, dummy_unique_label2], all_face_zonelets
                )
                diag_params = prime.SurfaceDiagnosticSummaryParams(
                    self._model,
                    scope=ScopeDefinition(
                        self._model, part_expression=merged_part.name
                    ),
                    compute_self_intersections=True,
                    compute_free_edges=False,
                    compute_multi_edges=False,
                    compute_duplicate_faces=False,
                )
                checks = surface_search.get_surface_diagnostic_summary(diag_params)
                if checks.n_self_intersections:
                    zonelets = merged_part.get_face_zonelets()
                    delete_fringe_params = prime.DeleteFringesAndOverlapsParams(
                        model=self._model,
                        fringe_element_count=0 if keep_small_free_surfaces else 10,
                        overlap_element_count=20,
                        delete_overlaps=True,
                    )
                    delete_tool.delete_fringes_and_overlaps_on_zonelets(
                        merged_part.id, zonelets, delete_fringe_params
                    )
                    checks = self.surface_intersection_results(merged_part)
                    if checks[0] > 20 or (checks[0] > 0 and intersect):
                        # lucid_mesh.write("failed_join_intersect.pmdat")
                        for mpt_name in compute_volume_params.material_point_names:
                            self._model.material_point_data.delete_material_point(
                                mpt_name
                            )
                        err_string = (
                            "failed to connect "
                            + '"'
                            + part_name
                            + '"'
                            + " with other parts.\nCheck the locations at "
                            + str(checks[1])
                            + ".\nTry by enabling refine_at_contacts, "
                            + "use finer sizes or adjust connect_tolerance."
                        )
                        raise PrimeRuntimeError(err_string)
                if intersect:
                    try:
                        results = merged_part.compute_closed_volumes(
                            compute_volume_params
                        )
                    except:
                        zonelets = merged_part.get_face_zonelets()
                        # print(
                        #   "we are deleteting fringes for compute volumes ",
                        #   0 if keep_small_free_surfaces else 10,
                        # )
                        delete_fringe_params = prime.DeleteFringesAndOverlapsParams(
                            model=self._model,
                            fringe_element_count=0 if keep_small_free_surfaces else 10,
                            overlap_element_count=20,
                            delete_overlaps=True,
                        )
                        delete_tool.delete_fringes_and_overlaps_on_zonelets(
                            merged_part.id, zonelets, delete_fringe_params
                        )
                        results = merged_part.compute_closed_volumes(
                            compute_volume_params
                        )
                    # lucid_mesh.write("after_just_connection_with_part_" +  part_name + ".pmdat")
                    if trim_small_volumes_from_parts_exp:
                        name_pattern_params = prime.NamePatternParams(model=self._model)
                        trim_volumes = merged_part.get_volumes_of_zone_name_pattern(
                            zone_name_pattern=trim_small_volumes_from_parts_exp,
                            name_pattern_params=name_pattern_params,
                        )
                        if len(trim_volumes) > len(prev_trim_volumes):
                            delete_volumes_params = prime.DeleteVolumesParams(
                                model=self._model,
                                delete_small_volumes=True,
                                volume_limit=trim_volume_limit,
                            )
                            del_results = merged_part.delete_volumes(
                                volumes=trim_volumes, params=delete_volumes_params
                            )
                            if del_results.deleted_volumes:
                                results = merged_part.compute_closed_volumes(
                                    compute_volume_params
                                )
                                trim_volumes = merged_part.get_volumes_of_zone_name_pattern(
                                    zone_name_pattern=trim_small_volumes_from_parts_exp,
                                    name_pattern_params=name_pattern_params,
                                )
                                delete_volumes_params = prime.DeleteVolumesParams(
                                    model=self._model,
                                    delete_small_volumes=True,
                                    volume_limit=trim_volume_limit,
                                )
                                del_results = merged_part.delete_volumes(
                                    volumes=trim_volumes, params=delete_volumes_params
                                )
                        prev_trim_volumes = trim_volumes
                    part_volumes = merged_part.get_volumes()
                    # lucid_mesh.write("after_delete_volumes_with_part_" +  part_name + ".pmdat")
                    merged_part.merge_volumes(
                        part_volumes, prime.MergeVolumesParams(model=self._model)
                    )
                    # lucid_mesh.write("after_merge_volumes_with_part_" +  part_name + ".pmdat")
            zonelets = merged_part.get_face_zonelets()
            # print("end delete fringes ", 0 if keep_small_free_surfaces else 5)
            delete_fringe_params = prime.DeleteFringesAndOverlapsParams(
                model=self._model,
                fringe_element_count=0 if keep_small_free_surfaces else 5,
                overlap_element_count=3,
                delete_overlaps=True,
            )
            delete_tool.delete_fringes_and_overlaps_on_zonelets(
                merged_part.id, zonelets, delete_fringe_params
            )
            if intersect:
                diag_params = prime.SurfaceDiagnosticSummaryParams(
                    self._model,
                    scope=ScopeDefinition(
                        self._model, part_expression=merged_part.name
                    ),
                    compute_self_intersections=True,
                    compute_free_edges=True,
                    compute_multi_edges=True,
                    compute_duplicate_faces=True,
                )
                checks = surface_search.get_surface_diagnostic_summary(diag_params)
                if checks.n_self_intersections:
                    checks = self.surface_intersection_results(merged_part)
                    for mpt_name in compute_volume_params.material_point_names:
                        self._model.material_point_data.delete_material_point(mpt_name)
                    err_string = (
                        "failed to connect volumetric interfering parts.\nCheck the locations at "
                        + str(checks[1])
                        + ".\nTry by enabling refine_at_contacts, "
                        + "use finer sizes or adjust connect_tolerance."
                    )
                    raise PrimeRuntimeError(err_string)
                for mpt_name in compute_volume_params.material_point_names:
                    self._model.material_point_data.delete_material_point(mpt_name)
                merge_params = prime.MergeZoneletsParams(
                    model=self._model,
                    merge_small_zonelets_with_neighbors=True,
                    element_count_limit=20,
                )
                merged_part.merge_zonelets(
                    merged_part.get_face_zonelets(), params=merge_params
                )
                merge_params = prime.MergeZoneletsParams(
                    model=self._model,
                    merge_small_zonelets_with_neighbors=False,
                    element_count_limit=20,
                )
                merged_part.merge_zonelets(
                    merged_part.get_face_zonelets(), params=merge_params
                )
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
        trim_small_volumes_from_parts_exp: str = "",
        trim_volume_limit: float = 0.0,
        fluid_volume_mpt_settings: list = [],
        connected_part_name: str = "merged_part",
        use_mesh_match: bool = False,
        mesh_match_angle: float = 45,
        keep_small_free_surfaces: bool = False,
    ):
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
            trim_small_volumes_from_parts_exp=trim_small_volumes_from_parts_exp,
            trim_volume_limit=trim_volume_limit,
            fluid_volume_mpt_settings=fluid_volume_mpt_settings,
            keep_small_free_surfaces=keep_small_free_surfaces,
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
        keep_small_free_surfaces: bool = False,
    ):
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
            trim_small_volumes_from_parts_exp="",
            trim_volume_limit=0,
            fluid_volume_mpt_settings=[],
            keep_small_free_surfaces=keep_small_free_surfaces,
        )

    def post_connections_improve_quality(
        self,
        part: Part = None,
        local_remesh_by_size_change: bool = True,
        soft_target_skewness: float = 0.6,
        hard_target_skewness: float = 0.9,
        keep_small_free_surfaces: bool = True,
    ):
        global_sf_params = self._model.get_global_sizing_params()
        register_id = 26
        surface_search = prime.SurfaceSearch(model=self._model)
        quality_params = prime.SearchByQualityParams(
            model=self._model,
            quality_limit=0.95 if soft_target_skewness > 0.95 else soft_target_skewness,
        )
        collapse_tool = prime.CollapseTool(model=self._model)
        collapse_params = prime.CollapseParams(model=self._model)
        split_params = prime.SplitParams(model=self._model)
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
            model=self._model,
            quality_limit=soft_target_skewness,
            strip_height_limit=global_sf_params.min * 0.4,
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
            model=self._model,
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
        surfer = prime.Surfer(model=self._model)
        if local_remesh_by_size_change:
            sc_quality_params = prime.SearchByQualityParams(model=self._model)
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
            local_surfer_params = prime.LocalSurferParams(
                model=self._model, max_angle=179.5
            )
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
                    model=self._model,
                    preserve_quality=True,
                    target_skewness=soft_target_skewness,
                )
                collapse_params.feature_type = (
                    prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
                )
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
                    model=self._model,
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
            params = prime.SearchBySelfIntersectionParams(model=self._model)
            search_results = surface_search.search_zonelets_by_self_intersections(
                part_id=part.id,
                face_zonelets=part.get_face_zonelets(),
                register_id=register_id,
                params=params,
            )
            if search_results.n_found:
                local_surfer_params = prime.LocalSurferParams(
                    model=self._model, growth_rate=1.2, min_angle=180, max_angle=180
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
            collapse_params.feature_type = (
                prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
            )
            split_params.split_ratio = 0.4
            collapse_params = prime.CollapseParams(
                model=self._model,
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
                model=self._model,
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
            collapse_params.feature_type = (
                prime.SurfaceFeatureType.FEATUREORZONEBOUNDARY
            )
            split_params.split_ratio = 0.4
            collapse_params = prime.CollapseParams(
                model=self._model,
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
                model=self._model,
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
            params = prime.SearchBySelfIntersectionParams(model=self._model)
            search_results = surface_search.search_zonelets_by_self_intersections(
                part_id=part.id,
                face_zonelets=part.get_face_zonelets(),
                register_id=register_id,
                params=params,
            )
        delete_tool = prime.DeleteTool(model=self._model)
        zonelets = part.get_face_zonelets()
        delete_fringe_params = prime.DeleteFringesAndOverlapsParams(
            model=self._model,
            fringe_element_count=0 if keep_small_free_surfaces else 5,
            overlap_element_count=3,
            delete_overlaps=True,
        )
        delete_tool.delete_fringes_and_overlaps_on_zonelets(
            part.id, zonelets, delete_fringe_params
        )
        quality_params.quality_limit = hard_target_skewness
        quality_res = surface_search.search_zonelets_by_quality(
            part.id, part.get_face_zonelets(), register_id, quality_params
        )
        params = prime.SearchBySelfIntersectionParams(model=self._model)
        search_results = surface_search.search_zonelets_by_self_intersections(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            register_id=register_id,
            params=params,
        )
        if search_results.n_found > 0:
            local_surfer_params = prime.LocalSurferParams(
                model=self._model, growth_rate=1.2, min_angle=180, max_angle=180
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
            delete_tool.delete_fringes_and_overlaps_on_zonelets(
                part.id, zonelets, delete_fringe_params
            )

    def cap_flow_volumes(
        self,
        part: Part = None,
        flow_volume_end_label_exp: str = "end_*",
        cap_zone_name: str = "fluid_caps",
    ):
        surface_utils = prime.SurfaceUtilities(model=self._model)
        cap_face_zonelets_params = prime.CreateCapParams(model=self._model)
        name_pattern_params = prime.NamePatternParams(model=self._model)
        face_zonelets = part.get_face_zonelets_of_label_name_pattern(
            flow_volume_end_label_exp,
            name_pattern_params=name_pattern_params,
        )
        cap_res = surface_utils.create_cap_on_face_zonelets(
            part_id=part.id,
            face_zonelets=face_zonelets,
            params=cap_face_zonelets_params,
        )
        zone_id = self._model.get_zone_by_name(cap_zone_name)
        if zone_id <= 0:
            create_zone_res = self._model.create_zone(
                cap_zone_name, prime.ZoneType.FACE
            )
            zone_id = create_zone_res.zone_id
        part.add_zonelets_to_zone(zone_id, cap_res.created_face_zonelets)
        return cap_res.created_face_zonelets

    def punch_holes(
        self,
        part: Part = None,
        target_volume_zone_exp: str = "* !solid*",
        cutter_volume_zone_exp: str = "solid*",
        ignore_face_label_exp: str = "periodic*",
    ):
        target_volumes = part.get_volumes_of_zone_name_pattern(
            target_volume_zone_exp, prime.NamePatternParams(self._model)
        )
        cutter_volumes = part.get_volumes_of_zone_name_pattern(
            cutter_volume_zone_exp, prime.NamePatternParams(self._model)
        )
        ignore_faces = part.get_face_zonelets_of_label_name_pattern(
            ignore_face_label_exp, prime.NamePatternParams(self._model)
        )
        volm = prime.Connect(model=self._model)
        params = prime.SubtractVolumesParams(model=self._model, check_cutters=True)
        params.ignore_face_zonelets = ignore_faces
        result = volm.subtract_volumes(
            part_id=part.id,
            target_volumes=target_volumes,
            cutter_volumes=cutter_volumes,
            params=params,
        )
        return result

    def create_face_zones_using_volume_zones(
        self,
        part: Part = None,
        fluid_zones_exp="fluid*",
        solid_solid_shared_suffix: str = ":contact",
        fluid_shared_suffix: str = ":interface",
        exclude_fluid_zones: bool = False,
        force_shared_zone_creation: bool = True,
    ):
        name_pattern_params = prime.NamePatternParams(model=self._model)
        fluid_volume_zones = set([])
        sorted_vol_zone = []
        if not exclude_fluid_zones:
            fluid_volume_zones = set(
                part.get_volume_zones_of_name_pattern(
                    fluid_zones_exp, name_pattern_params
                )
            )
        face_zonelets = part.get_face_zonelets()
        for zonelet in face_zonelets:
            face_zone_of_zonelet = part.get_face_zone_of_zonelet(zonelet)
            if not face_zone_of_zonelet or force_shared_zone_creation:
                volume_for_face_zonelet = part.get_volumes_of_face_zonelet(zonelet)
                face_zone_pattern = ""
                if len(volume_for_face_zonelet) == 1:
                    volume_zone_for_volume = part.get_volume_zone_of_volume(
                        volume_for_face_zonelet[0]
                    )
                    volume_zone_name = self._model.get_zone_name(volume_zone_for_volume)
                    face_zone_pattern = "{}:face_zone".format(volume_zone_name)
                elif len(volume_for_face_zonelet) == 2:
                    first_vol_zone = part.get_volume_zone_of_volume(
                        volume_for_face_zonelet[0]
                    )
                    second_vol_zone = part.get_volume_zone_of_volume(
                        volume_for_face_zonelet[1]
                    )
                    sorted_vol_zone = sorted(
                        [
                            self._model.get_zone_name(first_vol_zone),
                            self._model.get_zone_name(second_vol_zone),
                        ]
                    )
                    suffix = solid_solid_shared_suffix
                    if (
                        first_vol_zone in fluid_volume_zones
                        or second_vol_zone in fluid_volume_zones
                    ):
                        suffix = fluid_shared_suffix
                    face_zone_pattern = (
                        "{}_{}".format(sorted_vol_zone[0], sorted_vol_zone[1]) + suffix
                    )
                name_zones = part.get_face_zones_of_name_pattern(
                    face_zone_pattern, name_pattern_params
                )
                if name_zones:
                    zone_id = name_zones[0]
                else:
                    zone_id = self._model.create_zone(
                        face_zone_pattern, prime.ZoneType.FACE
                    ).zone_id
                part.add_zonelets_to_zone(zone_id, [zonelet])

    def refine_contacts(
        self,
        global_min_size: float,
        connect_tolerance: float,
    ):
        result = None
        part_ids = [part.id for part in self._model.parts]
        if len(part_ids) > 1:
            refine_params = prime.RefineAtContactsParams(model=self._model)
            surface_utils = prime.SurfaceUtilities(model=self._model)
            refine_params.contact_tolerance = 1.3 * connect_tolerance
            refine_params.refine_max_size = global_min_size
            refine_params.project_on_geometry = True
            result = surface_utils.refine_at_contacts(
                part_ids=part_ids, params=refine_params
            )
            size_field_id = result.size_field_id
            self._model.deactivate_volumetric_size_fields([size_field_id])
        else:
            self._logger.info("Less than two parts exist.  No contacts to be refined. ")
        return result

    def delete_topology(self):
        params = prime.DeleteTopoEntitiesParams(
            model=self._model, delete_geom_zonelets=True
        )
        part_ids_to_delete = []
        result = None
        for part in self._model.parts:
            if part.get_topo_faces():
                part.delete_topo_entities(params)
            else:
                part_ids_to_delete.append(part.id)
        if part_ids_to_delete:
            result = self._model.delete_parts(part_ids_to_delete)
        self.post_surface_mesh_cleanup_triangles("*", keep_small_free_surfaces=True)
        return result

    def cusp_removal(
        self,
        cusp_removal_settings: list = [],
    ):
        for cusp_control in cusp_removal_settings:
            if "use_absolute_tolerance" in cusp_control:
                bool_value = cusp_control["use_absolute_tolerance"]
            if "cusp_tolerance" in cusp_control:
                cusp_tol = cusp_control["cusp_tolerance"]
            if "side_tolerance" in cusp_control:
                side_tolerance = cusp_control["side_tolerance"]
            else:
                side_tolerance = 0.00001
            if "cusp_removal_parts_exp" in cusp_control:
                cusp_removal_parts_exp = cusp_control["cusp_removal_parts_exp"]
            if "cusp_removal_source_label_exp" in cusp_control:
                cusp_removal_source_label_exp = cusp_control["cusp_removal_source_label_exp"]
            if "cusp_removal_target_label_exp" in cusp_control:
                cusp_removal_target_label_exp = cusp_control["cusp_removal_target_label_exp"]
            connect = prime.Connect(model=self._model)
            name_pattern_params = prime.NamePatternParams(model=self._model)
            cusp_removal_parts = self.get_parts_of_name_pattern(cusp_removal_parts_exp)
            cusp_results = []
            for source_part in cusp_removal_parts:
                params = prime.FuseParams(model=self._model)
                params.use_absolute_tolerance = bool_value
                params.gap_tolerance = cusp_tol
                params.side_tolerance = side_tolerance
                # params.side_tolerance = cusp_tol
                params.fuse_option = 4
                params.check_interior = False
                params.check_orientation = True
                src_part_zonelets = source_part.get_face_zonelets_of_label_name_pattern(
                    label_name_pattern=cusp_removal_source_label_exp,
                    name_pattern_params=name_pattern_params,
                )
                trg_part_zonelets = source_part.get_face_zonelets_of_label_name_pattern(
                    label_name_pattern=cusp_removal_target_label_exp,
                    name_pattern_params=name_pattern_params,
                )
                cusp_results.append(
                    connect.fuse_face_zonelets(
                        source_part.id, src_part_zonelets, trg_part_zonelets, params
                    )
                )
        self.post_surface_mesh_cleanup_triangles("*", keep_small_free_surfaces=True)
        return cusp_results

    def fuse(
        self,
        connect_tolerance: float,
        side_tolerance: float,
        connect_parts_with_diff_tol: list,
        interfering_parts_exp: str,
        interfering_parts_priority: list,
        delete_small_volumes_of_parts_exp: str,
        small_volume_limit: float,
        material_points_for_flow_volumes: list,
        contact_parts_exp: str,
        part_name: str = "tolerant_connect_part",
        use_absolute_connect_tolerance: bool = True,
        use_mesh_match: bool = True,
        mesh_match_angle: int = 45,
        keep_small_free_surfaces: bool = False,
        refine_at_contacts: bool = True,
    ):
        vol_part_name = ""
        cont_part_name = ""
        mergeParams = prime.MergeZoneletsParams(model=self._model)
        for part in self._model.parts:
            # merge zonelets by zone and labels
            vol_bef_stitch = len(part.get_volumes())
            vol_aft_stitch = len(
                part.compute_closed_volumes(
                    prime.ComputeVolumesParams(self._model)
                ).volumes
            )
            if vol_bef_stitch > vol_aft_stitch:
                raise PrimeRuntimeError(
                    "Topo faces failed to mesh on "
                    + '"'
                    + part.name
                    + '"'
                    + ". Check and restart."
                )
            if not vol_bef_stitch and not vol_aft_stitch:
                part.add_labels_on_zonelets(
                    [part.name + ":cap"], part.get_face_zonelets()
                )
            zonelets = part.get_face_zonelets()
            if len(zonelets) > 1:
                part.merge_zonelets(zonelets=zonelets, params=mergeParams)
            # create zone with part name for default zone zonelets
            default_zone_zonelets = self.part_get_face_zonelets_without_zone(part=part)
            if default_zone_zonelets:
                create_zone_res = self._model.create_zone(
                    part.name + ":face_zone", type=prime.ZoneType.FACE
                )
                part.add_zonelets_to_zone(
                    create_zone_res.zone_id, default_zone_zonelets
                )
            # add label for part with part name
            part.add_labels_on_zonelets([part.name], part.get_face_zonelets())
        # [TODO] following edge deletion code is a workaround to speedup join intersect.
        # Remove it when the slowness is fixed
        if len(self._model.parts) > 1:
            for part in self._model.parts:
                edge_zonelets = part.get_edge_zonelets()
                if edge_zonelets:
                    part.delete_zonelets(edge_zonelets)
            for part_list in connect_parts_with_diff_tol:
                connect_parts = []
                prt_list = part_list["connect_parts_exp"]
                if "*" not in prt_list and "!" not in prt_list:
                    patterns = prt_list.split(",")
                    for pattern in patterns:
                        connect_parts.extend(self.get_parts_of_name_pattern(pattern))
                else:
                    connect_parts = self.get_parts_of_name_pattern(prt_list)
                part_name = connect_parts[0].name
                self.connect_contact_interfering_parts(
                    parts_name_exp=prt_list,
                    join_tolerance=part_list["specific_connect_tolerance"],
                    side_tolerance=part_list["specific_side_tolerance"],
                    use_abs_tol=use_absolute_connect_tolerance,
                    connected_part_name=part_name,
                    use_mesh_match=use_mesh_match,
                    mesh_match_angle=mesh_match_angle,
                    keep_small_free_surfaces=keep_small_free_surfaces,
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
                    trim_small_volumes_from_parts_exp=delete_small_volumes_of_parts_exp,
                    trim_volume_limit=small_volume_limit,
                    fluid_volume_mpt_settings=material_points_for_flow_volumes,
                    connected_part_name=vol_part_name,
                    use_mesh_match=use_mesh_match,
                    mesh_match_angle=mesh_match_angle,
                    keep_small_free_surfaces=keep_small_free_surfaces,
                )
            if self.get_parts_of_name_pattern(contact_parts_exp):
                cont_part_name = (
                    part_name if vol_part_name == "" else "contact_interfering_part"
                )
                self.connect_contact_interfering_parts(
                    parts_name_exp=contact_parts_exp,
                    join_tolerance=connect_tolerance,
                    side_tolerance=side_tolerance,
                    use_abs_tol=use_absolute_connect_tolerance,
                    connected_part_name=cont_part_name,
                    use_mesh_match=use_mesh_match,
                    mesh_match_angle=mesh_match_angle,
                    keep_small_free_surfaces=keep_small_free_surfaces,
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
                    keep_small_free_surfaces=keep_small_free_surfaces,
                )
            tolerant_connect_part = self._model.get_part_by_name(part_name)
            if refine_at_contacts:
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
                    part_id=tolerant_connect_part.id,
                    face_zonelets=tolerant_connect_part.get_face_zonelets(),
                    edge_zonelets=[],
                    params=surfer_params,
                )

    def hole_punching(
        self,
        material_points_for_flow_volumes: list,
        hole_punching_cutter_parts_exp: str,
        hole_punching_target_parts_exp: str,
        hole_punching_keep_face_labels_exp: str,
        part_name: str = "tolerant_connect_part"
    ):
        tolerant_connect_part_name = part_name
        compute_volume_params = prime.ComputeVolumesParams(
                                    self._model,
                                    create_zones_type=prime.CreateVolumeZonesType.PERNAMESOURCE,
                                    volume_naming_type=prime.VolumeNamingType.BYFACEZONE,
                                    )
        part_ids_to_merge = []
        for part in self.get_parts_of_name_pattern(hole_punching_cutter_parts_exp):
            part_ids_to_merge.append(part.id)
            results = part.compute_closed_volumes(compute_volume_params)
        if len(part_ids_to_merge) > 0:
            tolerant_connect_part = self._model.get_part_by_name(tolerant_connect_part_name)
            compute_volume_params = prime.ComputeVolumesParams(
                                    self._model,
                                    create_zones_type=prime.CreateVolumeZonesType.PERNAMESOURCE,
                                    volume_naming_type=prime.VolumeNamingType.BYFACELABEL,
                                    )
            mpt_params = prime.CreateMaterialPointParams(
                            model = self._model,
                            type = prime.MaterialPointType.LIVE,
                            )
            for mpt_settings in material_points_for_flow_volumes:
                results = self._model.material_point_data.create_material_point(
                            suggested_name = mpt_settings["name"],
                            coords = mpt_settings["location"],
                            params=mpt_params,
                            )
                compute_volume_params.material_point_names.append(results.assigned_name)
            results = tolerant_connect_part.compute_closed_volumes(compute_volume_params)
            for mpt_name in compute_volume_params.material_point_names:
                self._model.material_point_data.delete_material_point(mpt_name)
            part_ids_to_merge.append(tolerant_connect_part.id)
            merge_res = self._model.merge_parts(
                            part_ids_to_merge,
                            prime.MergePartsParams(
                                model = self._model,
                                merged_part_suggested_name=tolerant_connect_part_name,
                                )
                            )
            tolerant_connect_part = self._model.get_part_by_name(tolerant_connect_part_name)
            self.punch_holes(
                self._model,
                part = tolerant_connect_part,
                target_volume_zone_exp = hole_punching_target_parts_exp,
                cutter_volume_zone_exp = hole_punching_cutter_parts_exp,
                ignore_face_label_exp = hole_punching_keep_face_labels_exp,
                )

    def improve_surface_mesh(
        self,
        keep_small_free_surfaces: bool = False,
    ):
        for part in self._model.parts:
            self.post_connections_improve_quality(
                part,
                local_remesh_by_size_change=False,
                soft_target_skewness=0.7,
                keep_small_free_surfaces=keep_small_free_surfaces,
            )

    def extract_flow_volume(
        self,
        material_points_for_flow_volumes: list,
        capping_settings: list,
        hole_punching_cutter_parts_exp: str,
        hole_punching_keep_face_labels_exp: str,
        non_simulation_parts_exp: str,
        fix_invalid_normals_on_face_label_exp: str,
        extracting_flow_volume: bool = True,
        fix_invalid_normals: bool = False,
        improve_dihedral_angle: bool = False,
        part_name: str = "tolerant_connect_part",
        fluid_fluid_interface_wall: bool = False,
    ):
        if extracting_flow_volume:
            print(self._model.parts[0].name)
            if self._model.parts[0].name == "tolerant_connect_part":
                tolerant_connect_part = self._model.get_part_by_name(part_name)
            else: tolerant_connect_part = self._model.parts[0]
            surf_inter_res = self.surface_intersection_results(tolerant_connect_part)
            if surf_inter_res[0]:
                err_string = (
                    str(surf_inter_res[0])
                    + " face elements found intersecting. Locations are : "
                    + str(surf_inter_res[1])
                    + "."
                )
                raise PrimeRuntimeError(err_string)
            compute_volume_params = prime.ComputeVolumesParams(
                self._model,
                create_zones_type=prime.CreateVolumeZonesType.PERNAMESOURCE,
                volume_naming_type=prime.VolumeNamingType.BYFACELABEL,
            )
            mpt_params = prime.CreateMaterialPointParams(
                model=self._model, type=prime.MaterialPointType.LIVE
            )
            for mpt_settings in material_points_for_flow_volumes:
                results = self._model.material_point_data.create_material_point(
                    suggested_name=mpt_settings["name"],
                    coords=mpt_settings["location"],
                    params=mpt_params,
                )
                compute_volume_params.material_point_names.append(results.assigned_name)
            results = tolerant_connect_part.compute_closed_volumes(compute_volume_params)
            if (
                len(results.material_point_volumes) < 1
            ) and compute_volume_params.material_point_names:
                err_string = "No flow volume extracted. "
                +"Provide correct material points for flow volume extraction."
                raise PrimeRuntimeError(err_string)
            fluid_vols = results.material_point_volumes.tolist()
            caps_and_vol_zone_map = []
            for cap_info in capping_settings:
                cap_face_zonelets = self.cap_flow_volumes(
                    tolerant_connect_part,
                    flow_volume_end_label_exp=cap_info["source_face_label_exp"],
                    cap_zone_name=cap_info["cap_face_zone_name"],
                )
                caps_and_vol_zone_map.append(
                    [cap_face_zonelets, cap_info["flow_volume_zone_name"]]
                )
            print(caps_and_vol_zone_map)
            extract_volume_params = prime.ExtractVolumesParams(model=self._model)
            extract_volume_params.create_zone = True
            for cap_and_vol_zone in caps_and_vol_zone_map:
                extract_volume_params.suggested_zone_name = cap_and_vol_zone[1]
                try:
                    extract_vol_res = tolerant_connect_part.extract_volumes(
                        cap_and_vol_zone[0], extract_volume_params
                    )
                    for vol in extract_vol_res.volumes.tolist():
                        if vol not in fluid_vols:
                            fluid_vols.append(vol)
                except:
                    print(
                        "Flow volume extraction failed. "
                        + "Check cap settings to ensure all capping surfaces are created, "
                        + "or check for leaks in the model."
                    )
            name_pattern_params = prime.NamePatternParams(model=self._model)
            fluid_zonelets = tolerant_connect_part.get_face_zonelets_of_volumes(fluid_vols)
            if fluid_zonelets and hole_punching_cutter_parts_exp != "":
                periodic_zonelets = (
                    tolerant_connect_part.get_face_zonelets_of_label_name_pattern(
                        hole_punching_keep_face_labels_exp, name_pattern_params
                    )
                )
                periodic_fluid_zonelets = list(set(fluid_zonelets) & set(periodic_zonelets))
                if periodic_fluid_zonelets:
                    merge_params = prime.MergeZoneletsParams(
                        model=self._model,
                        merge_small_zonelets_with_neighbors=True,
                        element_count_limit=20000,
                    )
                    tolerant_connect_part.merge_zonelets(
                        periodic_fluid_zonelets, params=merge_params
                    )
                    periodic_zonelets = (
                        tolerant_connect_part.get_face_zonelets_of_label_name_pattern(
                            hole_punching_keep_face_labels_exp, name_pattern_params
                        )
                    )
                    periodic_fluid_zonelets = list(
                        set(fluid_zonelets) & set(periodic_zonelets)
                    )
            merge_params = prime.MergeZoneletsParams(
                model=self._model,
                merge_small_zonelets_with_neighbors=True,
                element_count_limit=30,
            )
            tolerant_connect_part.merge_zonelets(
                tolerant_connect_part.get_face_zonelets(), params=merge_params
            )
            existing_caps = tolerant_connect_part.get_face_zonelets_of_label_name_pattern(
                "*:cap", prime.NamePatternParams(self._model)
            )
            cap_vols = []
            for face in existing_caps:
                vols = tolerant_connect_part.get_volumes_of_face_zonelet(face)
                for vol in vols:
                    if vol not in cap_vols:
                        cap_vols.append(vol)
            if cap_vols:
                for vol in cap_vols:
                    result = self._model.create_zone("fluid", prime.ZoneType.VOLUME)
                    tolerant_connect_part.add_volumes_to_zone(result.zone_id, [vol])
            self.create_face_zones_using_volume_zones(
                tolerant_connect_part,
                fluid_zones_exp="fluid*",
                solid_solid_shared_suffix=":contact",
                fluid_shared_suffix=":interface",
                exclude_fluid_zones=False,
            )
            compute_volume_params = prime.ComputeVolumesParams(
                self._model,
                create_zones_type=prime.CreateVolumeZonesType.PERNAMESOURCE,
                volume_naming_type=prime.VolumeNamingType.BYFACELABEL,
            )
            mpt_params = prime.CreateMaterialPointParams(
                model=self._model, type=prime.MaterialPointType.LIVE
            )
            print(material_points_for_flow_volumes)
            for mpt_settings in material_points_for_flow_volumes:
                results = self._model.material_point_data.create_material_point(
                    suggested_name=mpt_settings["name"],
                    coords=mpt_settings["location"],
                    params=mpt_params,
                )
                compute_volume_params.material_point_names.append(results.assigned_name)
            results = tolerant_connect_part.compute_closed_volumes(compute_volume_params)
            # print("result = {}".format(results))
            fluid_vols = results.material_point_volumes.tolist()
            extract_volume_params = prime.ExtractVolumesParams(model=self._model)
            extract_volume_params.create_zone = True
            for cap_and_vol_zone in caps_and_vol_zone_map:
                extract_volume_params.suggested_zone_name = cap_and_vol_zone[1]
                extract_vol_res = tolerant_connect_part.extract_volumes(
                    cap_and_vol_zone[0], extract_volume_params
                )
                for vol in extract_vol_res.volumes.tolist():
                    if vol not in fluid_vols:
                        fluid_vols.append(vol)
            # print("fluid_vols = {}".format(fluid_vols))
            name_pattern_params = prime.NamePatternParams(model=self._model)
            delete_volumes = tolerant_connect_part.get_volumes_of_zone_name_pattern(
                zone_name_pattern=non_simulation_parts_exp,
                name_pattern_params=name_pattern_params,
            )
            delete_volumes = list(set(delete_volumes) - set(fluid_vols))
            if delete_volumes:
                delete_volumes_params = prime.DeleteVolumesParams(model=self._model)
                tolerant_connect_part.delete_volumes(
                    volumes=delete_volumes,
                    params=delete_volumes_params,
                )
            if improve_dihedral_angle:
                surface_utils = prime.SurfaceUtilities(model=self._model)
                smooth_params = prime.SmoothDihedralFaceNodesParams(
                    model=self._model,
                    min_dihedral_angle=20.0,
                    tolerance=0.3,
                    type=prime.SmoothType.INFLATE,
                )
                fluid_zonelets = tolerant_connect_part.get_face_zonelets_of_volumes(
                    fluid_vols
                )
                surface_utils.smooth_dihedral_face_nodes(fluid_zonelets, smooth_params)
                smooth_params.type = prime.SmoothType.SMOOTH
                surface_utils.smooth_dihedral_face_nodes(fluid_zonelets, smooth_params)
            if fix_invalid_normals and fluid_vols:
                surface_utils = prime.SurfaceUtilities(model=self._model)
                sphere_params = prime.FixInvalidNormalNodeParams(
                    model=self._model,
                    nugget_size=0.8,
                    label="nuggets_at_invalid_normals",
                )
                fluid_face_zonelets = tolerant_connect_part.get_face_zonelets_of_volumes(
                    fluid_vols
                )
                nugget_zonelets = (
                    tolerant_connect_part.get_face_zonelets_of_label_name_pattern(
                        fix_invalid_normals_on_face_label_exp, name_pattern_params
                    )
                )
                nugget_zonelets = list(set(nugget_zonelets) & set(fluid_face_zonelets))
                if nugget_zonelets:
                    surface_utils.fix_invalid_normal_nodes_of_face_zonelets(
                        tolerant_connect_part.id, fluid_face_zonelets, sphere_params
                    )
            results = tolerant_connect_part.compute_closed_volumes(compute_volume_params)
            fluid_vols = results.material_point_volumes.tolist()
            for cap_and_vol_zone in caps_and_vol_zone_map:
                extract_volume_params.suggested_zone_name = cap_and_vol_zone[1]
                extract_vol_res = tolerant_connect_part.extract_volumes(
                    cap_and_vol_zone[0], extract_volume_params
                )
                for vol in extract_vol_res.volumes.tolist():
                    if vol not in fluid_vols:
                        fluid_vols.append(vol)
            if fix_invalid_normals and fluid_vols:
                invalid_normal_vols = (
                    tolerant_connect_part.get_volumes_of_zone_name_pattern(
                        "nuggets_at_invalid_normals", name_pattern_params
                    )
                )
                delete_volumes_params = prime.DeleteVolumesParams(model=self._model)
                tolerant_connect_part.delete_volumes(
                    volumes=invalid_normal_vols, params=delete_volumes_params
                )
                invalid_normal_vols = (
                    tolerant_connect_part.get_volumes_of_zone_name_pattern(
                        "nuggets_at_invalid_normals", name_pattern_params
                    )
                )
                if invalid_normal_vols:
                    merge_vol_params = prime.MergeVolumesParams(model=self._model)
                    merge_vol_params.merge_to_neighbor_volume = True
                    merge_vol_params.neighbor_volumes = list(
                        set(tolerant_connect_part.get_volumes())
                        - set(invalid_normal_vols)
                        - set(fluid_vols)
                    )
                    tolerant_connect_part.merge_volumes(
                        invalid_normal_vols, merge_vol_params
                    )
                merge_params = prime.MergeZoneletsParams(
                    model=self._model,
                    merge_small_zonelets_with_neighbors=True,
                    element_count_limit=10,
                )
                tolerant_connect_part.merge_zonelets(
                    tolerant_connect_part.get_face_zonelets(), params=merge_params
                )
            for mpt_name in compute_volume_params.material_point_names:
                self._model.material_point_data.delete_material_point(mpt_name)
            for label in tolerant_connect_part.get_labels():
                if not label.endswith(":cap"):
                    faces = tolerant_connect_part.get_face_zonelets_of_label_name_pattern(
                        label, prime.NamePatternParams(self._model)
                    )
                    intersect = list(set(faces).intersection(existing_caps))
                    if intersect:
                        for face in intersect:
                            connected_volumes = (
                                tolerant_connect_part.get_volumes_of_face_zonelet(face)
                            )
                            n_fluids = len(set(connected_volumes))
                            if fluid_fluid_interface_wall and n_fluids == 2:
                                zone_name = label + ":interface"
                            else:
                                zone_name = label
                            result = self._model.create_zone(zone_name, prime.ZoneType.FACE)
                            tolerant_connect_part.add_zonelets_to_zone(
                                result.zone_id, intersect
                            )
                else:
                    if fluid_fluid_interface_wall:
                        faces = (
                            tolerant_connect_part.get_face_zonelets_of_label_name_pattern(
                                label, prime.NamePatternParams(self._model)
                            )
                        )
                        interface_label = label.removesuffix(":cap") + ":interface"
                        tolerant_connect_part.add_labels_on_zonelets(
                            [interface_label], faces
                        )
            cap_vols = []
            for face in existing_caps:
                vols = tolerant_connect_part.get_volumes_of_face_zonelet(face)
                for vol in vols:
                    if vol not in cap_vols:
                        cap_vols.append(vol)
            if cap_vols:
                for vol in cap_vols:
                    result = self._model.create_zone("fluid", prime.ZoneType.VOLUME)
                    tolerant_connect_part.add_volumes_to_zone(result.zone_id, [vol])

    def volume_mesh(
        self,
        volume_fill_type,
        n_procs: int,
        fix_invalid_normals: bool,
        only_solid_mesh: dict = None,
        use_volumetric_size_field_for_volume_mesh: bool = True,
        part_name: str = "tolerant_connect_part",
        generate_thin_volume_mesh: bool = True,
        thin_volume_mesh_settings: list = None,
        generate_prisms: bool = True,
        prism_settings: list = None,
        periodic_labels_exp: str = None,
        periodic_info: dict = None,
        labels_to_delete: list = [],
        labels_to_retain: list = [],
    ):
        if not only_solid_mesh:
            print(self._model.parts[0].name)
            if self._model.parts[0].name == "tolerant_connect_part":
                tolerant_connect_part = self._model.get_part_by_name(part_name)
            else: tolerant_connect_part = self._model.parts[0]
            auto_mesh_params = prime.AutoMeshParams(
                model=self._model
            )
            if generate_thin_volume_mesh:
                thin_vol_ctrls_ids = []
                for (
                    thin_volume_mesh_scope_info
                ) in thin_volume_mesh_settings:  # [TODO] add error handling
                    thin_vol_ctrl = self._model.control_data.create_thin_volume_control()
                    thin_volume_mesh_params = prime.ThinVolumeMeshParams(
                        model=self._model, ignore_unprojected_base=True
                    )
                    if "gap" in thin_volume_mesh_scope_info:
                        # print("the gsp is", thin_volume_mesh_scope_info["gap"])
                        thin_volume_mesh_params = prime.ThinVolumeMeshParams(
                            model=self._model,
                            gap=thin_volume_mesh_scope_info["gap"],
                            ignore_unprojected_base=True,
                        )
                    if "n_layers" in thin_volume_mesh_scope_info:
                        thin_volume_mesh_params.n_layers = thin_volume_mesh_scope_info[
                            "n_layers"
                        ]
                    if "imprint_sides" in thin_volume_mesh_scope_info:
                        thin_volume_mesh_params.imprint_sides = thin_volume_mesh_scope_info[
                            "imprint_sides"
                        ]
                    if "n_ignore_rings" in thin_volume_mesh_scope_info:
                        thin_volume_mesh_params.n_ignore_rings = (
                            thin_volume_mesh_scope_info["n_ignore_rings"]
                        )
                    thin_vol_ctrl.set_thin_volume_mesh_params(thin_volume_mesh_params)
                    if "source_scope" in thin_volume_mesh_scope_info:
                        source_scope = ScopeDefinition(model=self._model)
                        source_scope_dict = thin_volume_mesh_scope_info["source_scope"]
                        if "evaluation_type" in source_scope_dict:
                            source_scope.evaluation_type = self.evaluation_value(
                                        source_scope_dict["evaluation_type"],
                                        )
                        if "label_expression" in source_scope_dict:
                            source_scope.label_expression = source_scope_dict[
                                "label_expression"
                            ]
                        if "zone_expression" in source_scope_dict:
                            source_scope.zone_expression = source_scope_dict[
                                "zone_expression"
                            ]
                        thin_vol_ctrl.set_source_scope(source_scope)
                    if "target_scope" in thin_volume_mesh_scope_info:
                        target_scope = ScopeDefinition(model=self._model)
                        target_scope_dict = thin_volume_mesh_scope_info["target_scope"]
                        if "evaluation_type" in target_scope_dict:
                            target_scope.evaluation_type = self.evaluation_value(
                                                source_scope_dict["evaluation_type"],
                                                )
                        if "label_expression" in target_scope_dict:
                            target_scope.label_expression = target_scope_dict[
                                "label_expression"
                            ]
                        if "zone_expression" in target_scope_dict:
                            target_scope.zone_expression = target_scope_dict[
                                "zone_expression"
                            ]
                        thin_vol_ctrl.set_target_scope(target_scope)
                    if "volume_scope" in thin_volume_mesh_scope_info:
                        volume_scope = ScopeDefinition(model=self._model)
                        volume_scope_dict = thin_volume_mesh_scope_info["volume_scope"]
                        volume_scope.entity_type = ScopeEntity.VOLUME
                        volume_scope.evaluation_type = prime.ScopeEvaluationType.ZONES
                        if "zone_expression" in volume_scope_dict:
                            volume_scope.zone_expression = volume_scope_dict[
                                "zone_expression"
                            ]
                        # print("some", volume_scope)
                        thin_vol_ctrl.set_volume_scope(volume_scope)
                    thin_vol_ctrls_ids.append(thin_vol_ctrl.id)
                auto_mesh_params.thin_volume_control_ids = thin_vol_ctrls_ids
            if generate_prisms:
                prism_ctrl_ids = []
                for prism_scope_info in prism_settings:  # [TODO] add error handling
                    prism_ctrl = self._model.control_data.create_prism_control()
                    prism_params = prime.PrismControlGrowthParams(model=self._model)
                    if "n_layers" in prism_scope_info:
                        prism_params.n_layers = prism_scope_info["n_layers"]
                    if "first_height" in prism_scope_info:
                        prism_params.first_height = prism_scope_info["first_height"]
                    if "last_aspect_ratio" in prism_scope_info:
                        prism_params.last_aspect_ratio = prism_scope_info[
                            "last_aspect_ratio"
                        ]
                        prism_params.offset_type = prime.PrismControlOffsetType.LASTRATIO
                    prism_ctrl.set_growth_params(prism_params)
                    if "surface_scope" in prism_scope_info:
                        surface_scope = ScopeDefinition(model=self._model)
                        surface_scope_dict = prism_scope_info["surface_scope"]
                        if "evaluation_type" in surface_scope_dict:
                            surface_scope.evaluation_type = self.evaluation_value(
                                            surface_scope_dict["evaluation_type"],
                                            )
                        if "label_expression" in surface_scope_dict:
                            surface_scope.label_expression = surface_scope_dict[
                                "label_expression"
                            ]
                        if "zone_expression" in surface_scope_dict:
                            surface_scope.zone_expression = surface_scope_dict[
                                "zone_expression"
                            ]
                        prism_ctrl.set_surface_scope(surface_scope)
                    if "volume_scope" in prism_scope_info:
                        volume_scope = ScopeDefinition(model=self._model)
                        volume_scope.entity_type = ScopeEntity.VOLUME
                        volume_scope.evaluation_type = prime.ScopeEvaluationType.ZONES
                        volume_scope_dict = prism_scope_info["volume_scope"]
                        if "zone_expression" in volume_scope_dict:
                            volume_scope.zone_expression = volume_scope_dict[
                                "zone_expression"
                            ]
                        prism_ctrl.set_volume_scope(volume_scope)
                    prism_ctrl_ids.append(prism_ctrl.id)
                auto_mesh_params.prism_control_ids = prism_ctrl_ids
                stairstep_params = prime.PrismStairStep(
                    model=self._model, check_proximity=False, gap_factor_scale=0.2
                )
                prism_params = prime.PrismParams(
                    model=self._model, stair_step=stairstep_params
                )
                auto_mesh_params.prism = prism_params
            if periodic_labels_exp and periodic_info:
                periodic_control = self._model.control_data.create_periodic_control()
                periodic_control.set_scope(
                    ScopeDefinition(
                        model=self._model,
                        entity_type=ScopeEntity.FACEZONELETS,
                        evaluation_type=prime.ScopeEvaluationType.LABELS,
                        label_expression=periodic_labels_exp,
                    )
                )
                periodic_control.set_params(
                    prime.PeriodicControlParams(
                        model=self._model,
                        angle=periodic_info["angle"],
                        axis=periodic_info["axis"],
                        center=periodic_info["center"],
                    )
                )
                auto_mesh_params.periodic_control_ids = [periodic_control.id]
            if fix_invalid_normals:
                name_pattern_params = prime.NamePatternParams(model=self._model)
                volume_ctrl_ids = []
                nub_vol_zones = tolerant_connect_part.get_volume_zones_of_name_pattern(
                    "nubs_at_invalid_normals*", name_pattern_params=name_pattern_params
                )
                if nub_vol_zones:
                    volume_ctrl = self._model.control_data.create_volume_control()
                    volume_ctrl.set_scope(
                        ScopeDefinition(
                            model=self._model,
                            evaluation_type=prime.ScopeEvaluationType.ZONES,
                            zone_expression="nubs_at_invalid_normals*",
                        )
                    )
                    volume_ctrl.set_params(
                        prime.VolumeControlParams(
                            model=self._model, cell_zonelet_type=prime.CellZoneletType.DEAD
                        )
                    )
                    volume_ctrl_ids.append(volume_ctrl.id)
                auto_mesh_params.volume_control_ids = volume_ctrl_ids
            auto_mesh_params.volume_fill_type = self.evaluation_value(volume_fill_type)
            if use_volumetric_size_field_for_volume_mesh:
                auto_mesh_params.size_field_type = prime.SizeFieldType.VOLUMETRIC
            if n_procs > 1 and thin_volume_mesh_settings:
                self._model.start_distributed_meshing()
            auto_mesher = prime.AutoMesh(model=self._model)
            auto_mesher.mesh(
                part_id=tolerant_connect_part.id, automesh_params=auto_mesh_params
            )
            if labels_to_delete != []:
                tolerant_connect_part.remove_labels_from_zonelets(
                                labels_to_delete,
                                tolerant_connect_part.get_face_zonelets(),
                                )
            if labels_to_retain != []:
                total_labels = tolerant_connect_part.get_labels()
                delete_labels = list(set(total_labels).difference(set(labels_to_retain)))
                tolerant_connect_part.remove_labels_from_zonelets(
                                delete_labels,
                                tolerant_connect_part.get_face_zonelets(),
                                )
            vtool = prime.VolumeMeshTool(model=self._model)
            vtool.check_mesh(
                part_id=tolerant_connect_part.id,
                params=prime.CheckMeshParams(model=self._model),
            )
        if only_solid_mesh:
            self.volume_mesh_solid(only_solid_mesh["quadratic_mesh"])

    def improve_volume_mesh(
        self,
        only_solid_mesh: dict = None,
        volume_fill_type: prime.VolumeFillType = prime.VolumeFillType.TET,
        part_name: str = "tolerant_connect_part",
    ):
        volume_fill_type = self.evaluation_value(volume_fill_type)
        if (
            volume_fill_type == prime.VolumeFillType.TET
            or volume_fill_type == prime.VolumeFillType.HEXCORETET
        ):
            quality_measure_param = prime.CellQualityMeasure.SKEWNESS
        elif (
            volume_fill_type == prime.VolumeFillType.POLY
            or volume_fill_type == prime.VolumeFillType.HEXCOREPOLY
        ):
            quality_measure_param = prime.CellQualityMeasure.INVERSEORTHOGONAL
        else:
            err_string = "Invalid volume_fill_type setting."
            raise PrimeRuntimeError(err_string)
        auto_node_move_sequence = [
            {"target_quality": 0.97, "dihedral_angle": 120, "restrict_boundary": True},
            {"target_quality": 0.99, "dihedral_angle": 120, "restrict_boundary": True},
            {"target_quality": 0.98, "dihedral_angle": 120, "restrict_boundary": True},
            {"target_quality": 0.98, "dihedral_angle": 90, "restrict_boundary": True},
            {"target_quality": 0.98, "dihedral_angle": 60, "restrict_boundary": True},
            {"target_quality": 0.98, "dihedral_angle": 0, "restrict_boundary": True},
            {"target_quality": 0.99, "dihedral_angle": 120, "restrict_boundary": False},
            {"target_quality": 0.98, "dihedral_angle": 70, "restrict_boundary": True},
            {"target_quality": 0.99, "dihedral_angle": 20, "restrict_boundary": False},
            {"target_quality": 0.99, "dihedral_angle": 120, "restrict_boundary": False},
            {"target_quality": 0.99, "dihedral_angle": 70, "restrict_boundary": False},
            {"target_quality": 0.98, "dihedral_angle": 20, "restrict_boundary": True},
            {"target_quality": 0.98, "dihedral_angle": 120, "restrict_boundary": True},
            {"target_quality": 0.98, "dihedral_angle": 70, "restrict_boundary": False},
            {"target_quality": 0.95, "dihedral_angle": 20, "restrict_boundary": True},
            {"target_quality": 0.95, "dihedral_angle": 120, "restrict_boundary": True},
            {"target_quality": 0.95, "dihedral_angle": 70, "restrict_boundary": True},
            {"target_quality": 0.92, "dihedral_angle": 20, "restrict_boundary": True},
            {"target_quality": 0.92, "dihedral_angle": 70, "restrict_boundary": True},
            {"target_quality": 0.92, "dihedral_angle": 20, "restrict_boundary": True},
            {"target_quality": 0.90, "dihedral_angle": 120, "restrict_boundary": True},
            {"target_quality": 0.90, "dihedral_angle": 70, "restrict_boundary": True},
            {"target_quality": 0.90, "dihedral_angle": 20, "restrict_boundary": True},
        ]
        if not only_solid_mesh:
            if self._model.parts[0].name == "tolerant_connect_part":
                tolerant_connect_part = self._model.get_part_by_name(part_name)
            else: tolerant_connect_part = self._model.parts[0]
            for operation in auto_node_move_sequence:
                self.auto_node_movement(
                    part=tolerant_connect_part,
                    quality_measure=quality_measure_param,
                    target_quality=operation["target_quality"],
                    dihedral_angle=operation["dihedral_angle"],
                    n_iteration_per_node=50,
                    attempts=5,
                    restrict_boundary=operation["restrict_boundary"],
                )
        if only_solid_mesh:
            for part in self._model.parts:
                for operation in auto_node_move_sequence:
                    self.auto_node_movement(
                        part=part,
                        quality_measure=prime.CellQualityMeasure.SKEWNESS,
                        target_quality=operation["target_quality"],
                        dihedral_angle=operation["dihedral_angle"],
                        n_iteration_per_node=50,
                        attempts=5,
                        restrict_boundary=operation["restrict_boundary"],
                    )

    def surface_mesh_check(self):
        params = prime.SurfaceDiagnosticSummaryParams(self._model)
        params.compute_self_intersections = True
        params.compute_free_edges = True
        params.compute_duplicate_faces = True
        search = prime.SurfaceSearch(model=self._model)
        result = search.get_surface_diagnostic_summary(params)
        if result.n_self_intersections == 0 and result.n_free_edges == 0:
            print(f"number of self intersecting elements= {result.n_self_intersections}")
            print(f"number of free elements= {result.n_free_edges}")
        if result.n_self_intersections:
            self._logger.error(
                str(result.n_self_intersections) + " self intersecting faces found."
            )
        if result.n_free_edges:
            self._logger.error(str(result.n_free_edges) + " free faces found.")
        if result.n_duplicate_faces:
            self._logger.error(
                str(result.n_duplicate_faces) + " duplicate faces found."
            )
        return result

    def volume_mesh_check(self, volume_fill_type=prime.VolumeFillType.TET):
        for part in self._model.parts:
            params = prime.PartSummaryParams(
                model=self._model, print_id=False, print_mesh=True
            )
            part_summary_res = part.get_summary(params)
            print(f"number of face elements= {part_summary_res.n_faces}")
            print(f"number of cell= {part_summary_res.n_cells}")
            if volume_fill_type == prime.VolumeFillType.TET:
                search = prime.SurfaceSearch(model=self._model)
                params = prime.SurfaceQualitySummaryParams(model=self._model)
                params.scope = prime.ScopeDefinition(
                    model=self._model, part_expression=part.name
                )
                params.face_quality_measures = [prime.FaceQualityMeasure.SKEWNESS]
                params.quality_limit = [0.9]
                face_quality = search.get_surface_quality_summary(params)
                print(f"min face elements quality = {face_quality.quality_results[0].min_quality}")
            search = prime.VolumeSearch(self._model)
            params = prime.VolumeQualitySummaryParams(model=self._model)
            params.scope = prime.ScopeDefinition(
                model=self._model, part_expression=part.name
            )
            if (
                volume_fill_type == prime.VolumeFillType.TET
                or volume_fill_type == prime.VolumeFillType.HEXCORETET
            ):
                params.cell_quality_measures = [prime.CellQualityMeasure.SKEWNESS]
                params.quality_limit = [0.9]
                cell_quality = search.get_volume_quality_summary(params)
                print(f"min cell quality = {cell_quality.quality_results_part[0].min_quality}")
                print("number of cell above criterio = ")
                print(cell_quality.quality_results_part[0].n_found)
            elif (
                volume_fill_type == prime.VolumeFillType.POLY
                or volume_fill_type == prime.VolumeFillType.HEXCOREPOLY
            ):
                params.cell_quality_measures = [
                    prime.CellQualityMeasure.INVERSEORTHOGONAL
                ]
                params.quality_limit = [0.9]
                cell_quality = search.get_volume_quality_summary(params)
                print(f"min cell quality = {cell_quality.quality_results_part[0].min_quality}")
                print("number of cell above criterio = ")
                print(cell_quality.quality_results_part[0].n_found)
            tool = prime.VolumeMeshTool(model=self._model)
            check = tool.check_mesh(
                part_id=part.id, params=prime.CheckMeshParams(model=self._model)
            )
            if (
                check.has_non_positive_volumes
                or check.has_invalid_shape
                or check.has_left_handed_faces
                or check.has_non_positive_areas
            ):
                self._logger.error(check)

    def volume_mesh_solid(self, quadratic: bool= False):
        #compute volumes
        compute_volume_count = 0
        create_zones_type = prime.CreateVolumeZonesType.PERVOLUME
        params = prime.ComputeVolumesParams(self._model, create_zones_type=create_zones_type)
        params.volume_naming_type = prime.VolumeNamingType.BYFACENORMALS
        params.create_zones_type = prime.CreateVolumeZonesType.PERNAMESOURCE
        for part in self._model.parts:
            try:
                if len(part.get_topo_faces()) > 0:
                    result = part.compute_topo_volumes(params=params)
                else:
                    result = part.compute_closed_volumes(params=params)
                compute_volume_count += 1
            except:
                print("compute volume is failed for part: ", part.name)
        print("total computed volumes are: ", compute_volume_count)
        #volume meshing
        name_pattern_params = prime.NamePatternParams(self._model)
        dead_volumes = []
        for part in self._model.parts:
            dead_region = part.get_volumes_of_zone_name_pattern("dead*", name_pattern_params)
            dead_volumes.append(dead_region)
        volume_control_ids = []
        if len(dead_volumes) > 0:
            print( ">>>> dead volumes found ")
            #set the control params
            volume_control_param = prime.VolumeControlParams(self._model)
            volume_control_param.cell_zonelet_type = prime.CellZoneletType.DEAD
            volume_control_scope = prime.ScopeDefinition(self._model,
                                                entity_type=prime.ScopeEntity.VOLUME,
                                                evaluation_type=prime.ScopeEvaluationType.ZONES,
                                                part_expression="*",
                                                zone_expression= "dead*")
            #set the volume control
            volume_control = self._model.control_data.create_volume_control()
            volume_control.set_params(volume_control_params=volume_control_param)
            volume_control.set_scope(scope=volume_control_scope)
            volume_control_ids.append(volume_control.id)
        else:
            print( "<<<< no dead volumes found ")
        automesh = prime.AutoMesh(self._model)
        automesh_params = prime.AutoMeshParams(
                            self._model,
                            volume_fill_type=prime.VolumeFillType.TET,
                            volume_control_ids=volume_control_ids,
                            growth_rate=1.5,
                            cell_quality_measure = prime.CellQualityMeasure.ELEMENTQUALITY,
                            target_quality = 0.1,
                            )
        tet_params = prime.TetParams(
                            self._model,
                            # refine_sliver_quality = 0.99,
                            # refine_target_quality = 0.8,
                            # refine_target_low_quality = 0.8,
                            # remove_sliver_cells = True,
                            # remove_sliver_target_quality = 0.85,
                            # remove_sliver_quality = 0.8,
                            )
        automesh_params.tet = tet_params
        # if quadratic:
            # automesh_params.tet = prime.TetParams(self._model, True)
        for part in self._model.parts:
            try:
                result = automesh.mesh(part.id, automesh_params=automesh_params)
            except:
                print("volume meshing is failed for part: ", part.name)
        ## mid node projection
        # if quadratic:
            # project_mid_node = True
            # if project_mid_node:
                # for part in self._model.parts:
                    # try:
                        # topo_faces = part.get_topo_faces()
                        # surfaceUtils = prime.SurfaceUtilities(self._model)
                        # projectParams = prime.ProjectOnGeometryParams(
                            # model=self._model,
                            # project_on_facets_if_cadnot_found = True,
                            # project_only_mid_nodes = True,
                            # check_quality = True,
                            ## morphMidNodes = True,
                            # )
                        # results = surfaceUtils.project_topo_faces_on_geometry(
                                        # topo_faces,
                                        # projectParams,
                                        # )
                    # except:
                        # print("mid node projection is failed for part: ", part.name)

    def file_read(self, file_name, sf_file_name=""):
        file_io = prime.FileIO(model=self._model)
        filename, fileext = os.path.splitext(file_name)
        if fileext == ".pmdat":
            file_io.read_pmdat(file_name, prime.FileReadParams(model=self._model))
            if sf_file_name != "":
                file_io.read_size_field(sf_file_name, prime.ReadSizeFieldParams(model=self._model))
        elif fileext == ".msh" or fileext == ".cas":
            file_io.import_fluent_case(file_name, prime.ImportFluentCaseParams(model=self._model))
            if sf_file_name != "":
                file_io.import_fluent_meshing_size_field(sf_file_name)
        elif fileext == ".cdb":
            file_io.import_mapdl_cdb(file_name, prime.ImportMapdlCdbParams(model=self._model))
        else:
            params = prime.ImportCadParams(
                        model=self._model,
                        length_unit = prime.LengthUnit.MM,
                        cad_reader_route = prime.CadReaderRoute.PROGRAMCONTROLLED,
                        part_creation_type = prime.PartCreationType.BODY,
                        geometry_transfer = True,
                        )
            file_io.import_cad(file_name=file_name, params=params)
