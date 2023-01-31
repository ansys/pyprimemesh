import enum
import os
from typing import Iterable, List

import ansys.meshing.prime as prime

from .scope import SurfaceScope, VolumeScope
from .utils import check_name_pattern


class LabelToZoneMethod(enum.IntEnum):
    """Method to create zones from labels."""

    SIMPLE = 0
    """
    Simple method to create zones from labels.
    Entities are queried using labels and zones created.
    """


class Mesh:
    """Mesh is one of the classes in Lucid API.

    This class is meant for beginners to meshing.
    It also serves as a tutorial for commonly used meshing workflows.

    The following functionalities are provided by this class:
    * Surface meshing with constant and variable sizing with triangle or quad dominant mesh.
    * Volume meshing with prism, tetrahedral and polyhedral elements.
    * Surface wrapping.
    * Helper method to create zones from labels.
    * Helper methods for reading and writing files.
    """

    def __init__(self, model: prime.Model):
        """Initialize mesher using model.

        Parameters
        ----------
        model : prime.Model
            Model on which the methods work.
        """
        self._model = model
        self._logger = model.python_logger

    def read(
        self, file_name: str, append: bool = False, cad_reader_route: prime.CadReaderRoute = None
    ):
        """Read or import files of different formats based on file extension.

        PyPrimeMesh's native file format has extension pmdat.
        The method supports the following:
        * Reading PyPrimeMesh's native file format.
        * Importing various CAD Formats.
        * Importing Fluent Meshing's msh file.
        * Importing Fluent cas file.
        * Importing MAPDL cdb files.

        Parameters
        ----------
        file_name : str
            Path to file to be read or imported.

        append : bool
            Set it to True to append instead of overwrite.

        cad_reader_route : prime.CadReaderRoute
            Route of CadReader.

        """
        filename, fileext = os.path.splitext(file_name)
        if fileext == ".msh" or file_name[-7:] == ".msh.gz":
            prime.FileIO(self._model).import_fluent_meshing_meshes(
                [file_name], prime.ImportFluentMeshingMeshParams(self._model, append=append)
            )
        elif fileext == ".cas":
            prime.FileIO(self._model).import_fluent_case(
                file_name, prime.ImportFluentCaseParams(self._model, append=append)
            )
        elif fileext == ".cdb":
            prime.FileIO(self._model).import_mapdl_cdb(
                file_name, prime.ImportMapdlCdbParams(self._model, append=append)
            )
        elif fileext == ".pmdat":
            prime.FileIO(self._model).read_pmdat(
                file_name, prime.FileReadParams(self._model, append=append)
            )
        else:
            prime.FileIO(self._model).import_cad(
                file_name,
                prime.ImportCadParams(
                    self._model, append=append, cad_reader_route=cad_reader_route
                ),
            )

    def write(self, file_name: str):
        """Write or export files of different formats based on file extension.

        PyPrimeMesh's native file format has extension pmdat.
        The method supports the following:
        * Writing PyPrimeMesh's native file format.
        * Exporting Fluent Meshing's msh file.
        * Exporting Fluent cas file.
        * Exporting MAPDL cdb files.

        Parameters
        ----------
        file_name : str
            Path of file to be written or exported.

        """
        filename, fileext = os.path.splitext(file_name)
        if fileext == ".cdb":
            prime.FileIO(self._model).export_mapdl_cdb(
                file_name, prime.ExportMapdlCdbParams(self._model)
            )
        elif fileext == ".cas":
            prime.FileIO(self._model).export_fluent_case(
                file_name, prime.ExportFluentCaseParams(self._model)
            )
        elif fileext == ".msh" or file_name[-7:] == ".msh.gz":
            prime.FileIO(self._model).export_fluent_meshing_mesh(
                file_name, prime.ExportFluentMeshingMeshParams(self._model)
            )
        else:
            prime.FileIO(self._model).write_pmdat(file_name, prime.FileWriteParams(self._model))

    def create_zones_from_labels(
        self,
        label_expression: str = None,
        conversion_method: LabelToZoneMethod = LabelToZoneMethod.SIMPLE,
    ):
        """Create zones from labels.

        When exporting to various solvers, zones play a very important role.
        Zones are where material properties and boundary conditions
        can be set in respective solvers.

        Zones allow downstream setting of
        boundary conditions or material properties.

        Zone names in PyPrimeMesh are translated into equivalent concepts in solver.
        Currently, only one method is available to convert zone to label.
        Currently, only face zones are created.

        The method finds the entities by labels and then adds them to the
        zone with the same name as label.

        If no label_expression is provided then all labels will be flattened to
        create zones.  Label names will be combined if overlaps occur and
        separate zones created.

        For example, if "LabelA" and "LabelB" had overlapping TopoFaces then
        the following three zones would be created;
        "LabelA", "LabelB" and "LabelA_LabelB" for the overlap.

        Parameters
        ----------
        label_expression : str
            Expression for labels to be converted to zones.

        conversion_method : LabelToZoneMethod
            Method used to convert label to zones.

        Examples
        --------
        >>> from ansys.meshing.prime import lucid
        >>> mesh_util = lucid.Mesh(model)
        >>> mesh_util.create_zones_from_labels()

        """
        if conversion_method != LabelToZoneMethod.SIMPLE:
            self._logger.error("Invalid label to zone conversion method")

        if label_expression:
            labels = []
            for part in self._model.parts:
                lbls = part.get_labels()
                for l in lbls:
                    if l not in labels and check_name_pattern(label_expression, l):
                        labels.append(l)

            for label in labels:
                face_zone = None
                for part in self._model.parts:
                    topo_faces = part.get_topo_faces()
                    if len(topo_faces) > 0:
                        in_topo_faces = part.get_topo_faces_of_label_name_pattern(
                            label, prime.NamePatternParams(model=self._model)
                        )
                        if len(in_topo_faces) > 0:
                            if face_zone == None:
                                face_zone = self._model.create_zone(label, prime.ZoneType.FACE)
                            part.add_topo_entities_to_zone(face_zone.zone_id, in_topo_faces)
                    else:
                        in_face_zonelets = part.get_face_zonelets_of_label_name_pattern(
                            label, prime.NamePatternParams(model=self._model)
                        )
                        if len(in_face_zonelets) > 0:
                            if face_zone == None:
                                face_zone = self._model.create_zone(label, prime.ZoneType.FACE)
                            part.add_zonelets_to_zone(face_zone.zone_id, in_face_zonelets)
        else:
            labels = []
            for part in self._model.parts:
                labels += part.get_labels()
            faces_of_label = {}
            labels_of_face = {}
            label_zone_definitions = {}
            face_zones = []
            all_topo = []
            for part in self._model.parts:
                for face in part.get_topo_faces():
                    labels_of_face[face] = []
                for face in part.get_face_zonelets():
                    labels_of_face[face] = []
            for label in labels:
                faces = []
                faces_of_label[label] = []
                for part in self._model.parts:
                    for zone in part.get_face_zones():
                        face_zones.append(self._model.get_zone_name(zone))
                    topo_faces = part.get_topo_faces()
                    all_topo += topo_faces
                    if topo_faces:
                        faces += part.get_topo_faces_of_label_name_pattern(
                            label_name_pattern=label,
                            name_pattern_params=prime.NamePatternParams(self._model),
                        )
                    else:
                        faces += part.get_face_zonelets_of_label_name_pattern(
                            label_name_pattern=label,
                            name_pattern_params=prime.NamePatternParams(self._model),
                        )
                if faces:
                    faces_of_label[label] += faces
                    [labels_of_face[face].append(label) for face in faces]
            for face in labels_of_face:
                name_exists = False
                for zone_name in label_zone_definitions:
                    if set(zone_name) == set(labels_of_face[face]):
                        name_exists = True
                        label_zone_definitions[zone_name].append(face)
                if not name_exists:
                    label_zone_definitions['_'.join(labels_of_face[face])] = [face]
            # remove empty labels
            if "" in label_zone_definitions:
                label_zone_definitions.pop("")
            self._logger.info("Labels to zones: " + str(label_zone_definitions))
            for zone_name in label_zone_definitions:
                if zone_name not in face_zones:
                    self._model.create_zone(zone_name, prime.ZoneType.FACE)
                for face in label_zone_definitions[zone_name]:
                    for part in self._model.parts:
                        if face in all_topo and face in part.get_topo_faces():
                            part.add_topo_entities_to_zone(
                                topo_entities=[face],
                                zone_id=self._model.get_zone_by_name(zone_name=zone_name),
                            )
                        elif face not in all_topo and face in part.get_face_zonelets():
                            part.add_zonelets_to_zone(
                                zonelets=[face],
                                zone_id=self._model.get_zone_by_name(zone_name=zone_name),
                            )

    def merge_parts(self, parts_expression: str = "*", new_name: str = "merged_part"):
        """Merges given parts into one.

        Parameters
        ----------
        parts_expression : str
            Expression of parts to be merged.
        new_name : str
            New part name for the merged part.

        """
        part_ids = []
        for part in self._model.parts:
            if check_name_pattern(parts_expression, part.get_name()):
                part_ids.append(part.id)

        self._model.merge_parts(
            part_ids=part_ids,
            params=prime.MergePartsParams(self._model, merged_part_suggested_name=new_name),
        )

    def delete_topology(self, parts_expression: str = "*", delete_edges: bool = True):
        """Delete topoentities of part.

        Parameters
        ----------
        parts_expression : str
            Expression of parts whose topology needs to be deleted.
        delete_edges : bool
            Check whether to delete the edges or not.

        """
        for part in self._model.parts:
            if check_name_pattern(parts_expression, part.get_name()):
                part.delete_topo_entities(
                    prime.DeleteTopoEntitiesParams(
                        self._model, delete_geom_zonelets=True, delete_mesh_zonelets=False
                    )
                )
                if delete_edges:
                    part.delete_zonelets(part.get_edge_zonelets())

    def __surface_mesh_on_active_sf(self, generate_quads: bool, scope: SurfaceScope):
        part_ids = scope.get_parts(self._model)
        for part_id in part_ids:
            topofaces = scope.get_topo_faces(self._model, part_id)
            surfer = prime.Surfer(self._model)
            params = prime.SurferParams(
                self._model,
                size_field_type=prime.SizeFieldType.VOLUMETRIC,
                generate_quads=generate_quads,
            )
            if len(topofaces) > 0:
                surfer.mesh_topo_faces(part_id=part_id, topo_faces=topofaces, params=params)
            else:
                tf = scope.get_face_zonelets(self._model, part_id)
                if len(tf) > 0:
                    te = []
                    surfer.remesh_face_zonelets(part_id, tf, te, params)

    def __variable_size_surface_mesh(
        self, min_size: float, max_size: float, generate_quads: bool, scope: SurfaceScope
    ):
        self._model.set_global_sizing_params(
            prime.GlobalSizingParams(model=self._model, min=min_size, max=max_size, growth_rate=1.2)
        )
        surfer = prime.Surfer(self._model)
        params = prime.SurferParams(
            self._model,
            size_field_type=prime.SizeFieldType.VOLUMETRIC,
            generate_quads=generate_quads,
        )
        part_ids = scope.get_parts(self._model)
        for part_id in part_ids:
            part = self._model.get_part(part_id)
            topofaces = scope.get_topo_faces(self._model, part_id)
            if len(topofaces) > 0:
                sizecontrol1 = self._model.control_data.create_size_control(
                    prime.SizingType.CURVATURE
                )
                sizecontrol1.set_curvature_sizing_params(
                    prime.CurvatureSizingParams(
                        model=self._model, min=min_size, max=max_size, growth_rate=1.2
                    )
                )
                sizecontrol1.set_scope(
                    prime.ScopeDefinition(
                        model=self._model,
                        entity_type=prime.ScopeEntity.FACEANDEDGEZONELETS,
                        part_expression=part.name,
                    )
                )
                sizefield = prime.SizeField(model=self._model)
                res = sizefield.compute_volumetric(
                    size_control_ids=[sizecontrol1.id],
                    volumetric_sizefield_params=prime.VolumetricSizeFieldComputeParams(
                        model=self._model, enable_multi_threading=False
                    ),
                )
                surfer.mesh_topo_faces(part_id=part.id, topo_faces=topofaces, params=params)
                self._model.delete_volumetric_size_fields([res.size_field_id])
            else:
                tf = scope.get_face_zonelets(self._model, part_id)
                if len(tf) > 0:
                    te = []
                    sizecontrol1 = self._model.control_data.create_size_control(
                        prime.SizingType.CURVATURE
                    )
                    sizecontrol1.set_curvature_sizing_params(
                        prime.CurvatureSizingParams(
                            model=self._model, min=min_size, max=max_size, growth_rate=1.2
                        )
                    )
                    sizecontrol1.set_scope(
                        prime.ScopeDefinition(
                            model=self._model,
                            entity_type=prime.ScopeEntity.FACEANDEDGEZONELETS,
                            part_expression=part.name,
                        )
                    )
                    sizefield = prime.SizeField(model=self._model)
                    res = sizefield.compute_volumetric(
                        size_control_ids=[sizecontrol1.id],
                        volumetric_sizefield_params=prime.VolumetricSizeFieldComputeParams(
                            model=self._model, enable_multi_threading=False
                        ),
                    )
                    surfer.remesh_face_zonelets(part.id, tf, te, params)
                    self._model.delete_volumetric_size_fields([res.size_field_id])

    def __constant_size_surface_mesh(
        self, min_size: float, generate_quads: bool, scope: SurfaceScope
    ):
        part_ids = scope.get_parts(self._model)
        surfer = prime.Surfer(self._model)
        for part_id in part_ids:
            topofaces = scope.get_topo_faces(self._model, part_id)
            params = prime.SurferParams(
                self._model, constant_size=min_size, generate_quads=generate_quads
            )
            if len(topofaces) > 0:
                surfer.mesh_topo_faces(part_id=part_id, topo_faces=topofaces, params=params)
            else:
                tf = scope.get_face_zonelets(self._model, part_id)
                te = []
                surfer.remesh_face_zonelets(part_id, tf, te, params)

    def surface_mesh(
        self,
        min_size: float = None,
        max_size: float = None,
        generate_quads: bool = False,
        scope: SurfaceScope = SurfaceScope(),
    ):
        """Generate Surface mesh on the given scope.

        This method generates surface mesh on the given scope.
        The method is used to generate constant or variable size surface mesh.
        The method supports generating quad dominant or triangular elements.

        If min size and max size are provided, variable size mesh is generated
        between min size and max size by applying sizes based on curvature.

        If either of min size or max size is provided, constant size mesh
        will be generated with the provided size.

        If neither of min size or max size is provided, global max setting is used to
        generate a constant size mesh.

        Parameters
        ----------
        min_size : float
            Minimum edge length of the mesh.

        max_size : float
            Maximum edge length of the mesh.

        generate_quads : bool
            Generate quad dominant mesh or all triangular mesh.

        scope : SurfaceScope
            Scope for generating surface mesh.

        """
        if min_size == None and max_size == None:
            global_sizing = self._model.get_global_sizing_params()
            self._logger.warning(
                "Min and Max size not provided. Using max global size "
                + str(global_sizing.max)
                + " and min global size "
                + str(global_sizing.min)
            )
            self.__variable_size_surface_mesh(
                min_size=global_sizing.min,
                max_size=global_sizing.max,
                generate_quads=generate_quads,
                scope=scope,
            )
        elif min_size == None or max_size == None:
            if min_size is None:
                self.__constant_size_surface_mesh(
                    min_size=max_size, generate_quads=generate_quads, scope=scope
                )
            else:
                self.__constant_size_surface_mesh(
                    min_size=min_size, generate_quads=generate_quads, scope=scope
                )
        else:
            self.__variable_size_surface_mesh(
                min_size=min_size, max_size=max_size, generate_quads=generate_quads, scope=scope
            )

    def create_constant_size_control(
        self,
        control_name: str = "size_control",
        size: float = 1.0,
        scope: SurfaceScope = SurfaceScope(),
    ):
        """Generate constant size control on the given scope.

        This method generates constant size control on the given scope.

        Parameters
        ----------
        control_name : str
            Name of the control.

        size : float
            Constant edge length of the mesh.

        scope : SurfaceScope
            Scope for creating size control.

        """
        global_sizes = self._model.get_global_sizing_params()
        if global_sizes.max < size:
            global_sizes.max = size
        if global_sizes.min > size or global_sizes.min <= 0:
            global_sizes.min = size
        self._model.set_global_sizing_params(global_sizes)
        sizecontrol = self._model.control_data.create_size_control(prime.SizingType.SOFT)
        sizecontrol.set_soft_sizing_params(
            prime.SoftSizingParams(
                model=self._model, max=size, growth_rate=global_sizes.growth_rate
            )
        )
        sizecontrol.set_scope(scope.get_scope_definition(self._model))
        sizecontrol.set_suggested_name(control_name)

    def create_curvature_size_control(
        self,
        control_name: str = "size_control",
        min: float = 1.0,
        max: float = 2.0,
        scope: SurfaceScope = SurfaceScope(),
    ):
        """Generate curvature size control on the given scope.

        This method generates curvature size control on the given scope.

        Parameters
        ----------
        control_name : str
            Name of the control.

        min : float
            Min edge length of the mesh.

        max : float
            Max edge length of the mesh.

        scope : SurfaceScope
            Scope for creating size control.

        """
        global_sizes = self._model.get_global_sizing_params()
        if max < min:
            t = max
            max = min
            min = t
        if global_sizes.max < max:
            global_sizes.max = max
        if global_sizes.min > min or global_sizes.min <= 0:
            global_sizes.min = min
        self._model.set_global_sizing_params(global_sizes)
        sizecontrol = self._model.control_data.create_size_control(prime.SizingType.CURVATURE)
        sizecontrol.set_curvature_sizing_params(
            prime.CurvatureSizingParams(
                model=self._model, min=min, max=max, growth_rate=global_sizes.growth_rate
            )
        )
        sizecontrol.set_scope(scope.get_scope_definition(self._model))
        sizecontrol.set_suggested_name(control_name)

    def surface_mesh_with_size_controls(
        self,
        size_control_names: str = "*",
        generate_quads: bool = False,
        scope: SurfaceScope = SurfaceScope(),
    ):
        """Generate Surface mesh on the given scope with the given size controls.

        This method generates surface mesh on the given scope.
        The method is used to generate surface mesh using the given size controls.
        The method supports generating quad dominant or triangular elements.

        Parameters
        ----------
        size_control_names : str
            Name pattern for the size controls.

        generate_quads : bool
            Generate quad dominant mesh or all triangular mesh.

        scope : SurfaceScope
            Scope for generating surface mesh.

        """
        sizefield = prime.SizeField(model=self._model)
        s_control_ids = []
        s_controls = self._model.control_data.size_controls
        for control in s_controls:
            if check_name_pattern(size_control_names, control.name):
                s_control_ids.append(control.id)
        if len(s_control_ids) > 0:
            size_field_res = sizefield.compute_volumetric(
                size_control_ids=s_control_ids,
                volumetric_sizefield_params=prime.VolumetricSizeFieldComputeParams(
                    model=self._model, enable_multi_threading=False
                ),
            )
            self.__surface_mesh_on_active_sf(generate_quads=generate_quads, scope=scope)
            self._model.delete_volumetric_size_fields([size_field_res.size_field_id])

    def connect_faces(
        self,
        part_expression: str = "*",
        face_labels: str = "*",
        target_face_labels: str = "*",
        tolerance: float = 0.05,
    ):
        """Connect face zonelets with given label name pattern within the given tolerance.

        This method is used to connect face zonelets of given label name pattern to the
        face zonelets given by target face labels within a given tolerance. Connect happens within
        part. Face zonelets of a part are connected with face zonelets of the same part only.

        Parameters
        ----------
        part_expression: str
            Name pattern of parts used for connecting.
        face_labels: str
            Name pattern of face labels used for connecting.
        target_face_labels: str
            Name pattern of face labels with which you want to connect.
        tolerance: float
            Tolerance used for connection.

        """
        name_pattern_param = prime.NamePatternParams(self._model)
        connect = prime.Connect(self._model)
        for part in self._model.parts:
            if check_name_pattern(part_expression, part.name):
                join_faces_source = part.get_face_zonelets_of_label_name_pattern(
                    face_labels, name_pattern_param
                )
                join_faces_target = part.get_face_zonelets_of_label_name_pattern(
                    target_face_labels, name_pattern_param
                )
                if len(join_faces_source) > 0 and len(join_faces_target) > 0:
                    connect.intersect_face_zonelets(
                        part.id,
                        face_zonelet_ids=join_faces_source,
                        with_face_zonelet_ids=join_faces_target,
                        params=prime.IntersectParams(self._model, tolerance=tolerance),
                    )
                    connect.join_face_zonelets(
                        part.id,
                        face_zonelet_ids=join_faces_source,
                        with_face_zonelet_ids=join_faces_target,
                        params=prime.JoinParams(self._model, tolerance=tolerance),
                    )

    def compute_volumes(self, part_expression: str = "*", create_zones_per_volume: bool = True):
        """
        Computes volumes in the parts defined by the part expression

        Parameters
        ----------
        part_expression : str
            Expression of parts where topology needs to be deleted.

        create_zones_per_volume : bool
            Creates volume zones for each volume when True.

        """
        create_zones_type = prime.CreateVolumeZonesType.NONE
        if create_zones_per_volume:
            create_zones_type = prime.CreateVolumeZonesType.PERVOLUME
        params = prime.ComputeVolumesParams(model=self._model, create_zones_type=create_zones_type)
        for part in self._model.parts:
            if check_name_pattern(part_expression, part.name):
                if len(part.get_topo_faces()) > 0:
                    part.compute_topo_volumes(params=params)
                else:
                    part.compute_closed_volumes(params=params)

    def delete_topology(self, part_expression: str = "*", delete_edges: bool = True):
        """
        Deletes topology in the given part.

        This method can be used to delete topology in the parts defined by the part expression.
        If delete_edges is set to True, edge zonelets will be deleted.

        Parameters
        ----------
        part_expression : str
            Expression of parts where topology needs to be deleted.

        delete_edges : bool
            Edge zonelets are deleted when true.

        """
        for part in self._model.parts:
            if check_name_pattern(part_expression, part.name):
                part.delete_topo_entities(
                    prime.DeleteTopoEntitiesParams(
                        model=self._model, delete_geom_zonelets=True, delete_mesh_zonelets=False
                    )
                )
                if delete_edges:
                    part.delete_zonelets(part.get_edge_zonelets())

    def __create_cap(self, part_id: int, face_zonelets: Iterable[int]):
        su = prime.SurfaceUtilities(model=self._model)
        res = su.create_cap_on_face_zonelets(
            part_id=part_id,
            face_zonelets=face_zonelets,
            params=prime.CreateCapParams(model=self._model),
        )
        return res.created_face_zonelets

    def __compute_flow_volume(
        self, part_id: int, face_zonelets: Iterable[int], flow_volume_zone_name: str = "flow_volume"
    ):
        part = self._model.get_part(part_id)
        if part:
            params = prime.ExtractVolumesParams(
                model=self._model, create_zone=True, suggested_zone_name=flow_volume_zone_name
            )
            res = part.extract_volumes(face_zonelets=face_zonelets, params=params)

    def create_flow_volume(
        self, flow_volume_zone_name: str = "flow_volume", cap_scope: SurfaceScope = SurfaceScope()
    ):
        """Create flow volume by the given face labels defining the boundary of the volume.

        This method creates flow volumes for the given faces defining the boundary of the volume.

        Parameters
        ----------
        flow_volume_zone_name: str
            Suggested name for the volume zone of the created flow volume.
        cap_scope: SurfaceScope
            Scope defining the face zonelets where cap for flow volume needs to be created.

        """
        parts = cap_scope.get_parts(self._model)
        for part in parts:
            caps = self.__create_cap(part, cap_scope.get_face_zonelets(self._model, part))
            if len(caps) > 0:
                self.__compute_flow_volume(part, caps, flow_volume_zone_name)

    def __create_volume_controls(self, part: prime.Part, scope: VolumeScope) -> Iterable[int]:
        volume_control_ids = []
        if scope._evaluation_type == prime.ScopeEvaluationType.ZONES:
            volume_zones_all = part.get_volume_zones()
            volume_zones_to_mesh = []
            for volume_zone in volume_zones_all:
                if check_name_pattern(
                    scope._entity_expression, self._model.get_zone_name(volume_zone)
                ):
                    volume_zones_to_mesh.append(volume_zone)

            volume_zones_to_avoid = [v for v in volume_zones_all if v not in volume_zones_to_mesh]
            scope_str = ", ".join([self._model.get_zone_name(v) for v in volume_zones_to_avoid])

            if len(scope_str) > 0:
                volume_control_param_dead = prime.VolumeControlParams(
                    model=self._model, cell_zonelet_type=prime.CellZoneletType.DEAD
                )
                volume_control_scope_dead = prime.ScopeDefinition(
                    model=self._model,
                    part_expression=part.name,
                    label_expression="",
                    zone_expression=scope_str,
                    entity_type=prime.ScopeEntity.VOLUME,
                    evaluation_type=prime.ScopeEvaluationType.ZONES,
                )
                volume_control_dead = self._model.control_data.create_volume_control()
                volume_control_dead.set_params(volume_control_params=volume_control_param_dead)
                volume_control_dead.set_scope(scope=volume_control_scope_dead)
                volume_control_ids.append(volume_control_dead.id)

            volume_control_param_fluid = prime.VolumeControlParams(
                model=self._model, cell_zonelet_type=prime.CellZoneletType.FLUID
            )
            volume_control_scope_fluid = prime.ScopeDefinition(
                model=self._model,
                part_expression=part.name,
                label_expression="",
                zone_expression=scope._entity_expression,
                entity_type=prime.ScopeEntity.VOLUME,
                evaluation_type=prime.ScopeEvaluationType.ZONES,
            )
            volume_control_fluid = self._model.control_data.create_volume_control()
            volume_control_fluid.set_params(volume_control_params=volume_control_param_fluid)
            volume_control_fluid.set_scope(scope=volume_control_scope_fluid)
            volume_control_ids.append(volume_control_fluid.id)

        return volume_control_ids

    def volume_mesh(
        self,
        volume_fill_type: prime.VolumeFillType = prime.VolumeFillType.TET,
        quadratic: bool = False,
        prism_layers: int = None,
        prism_surface_expression: str = "*",
        prism_volume_expression: str = "*",
        growth_rate: float = 1.2,
        scope: VolumeScope = VolumeScope(),
    ):
        """Generate Volume mesh on the model.

        This method can be used to generate volume mesh on the entire model.
        If prism layers parameter is set, prism layers are generated.

        Parameters
        ----------
        volume_fill_type : prime.VolumeFillType
            Type of volume elements to be generated.

        quadratic : bool
            Option to generate quadratic mesh. It is not supported with parallel meshing.
            It is only supported with pure tetrahedral mesh.

        prism_layers : int
            Number of prism layers to grow.

        prism_label_expression : str
            Labels on surfaces from where prisms are grown.
            Default is to grow from all surfaces.

        prism_volume_expression : str
            Volumes or topovolumes into which prisms are grown.
            The expression evaluates to zone names and volumes
            or topovolumes are queried based on zones evaluated.

        growth_rate : float
            Prism growth rate.

        scope : VolumeScope
            Scope of volumes to be meshed.

        """
        automesh_params = prime.AutoMeshParams(model=self._model)
        automesh_params.volume_fill_type = volume_fill_type
        if quadratic:
            automesh_params.tet = prime.TetParams(self._model, True)
        automesh = prime.AutoMesh(self._model)
        for part in self._model.parts:
            if check_name_pattern(scope._part_expression, part.name):
                try:
                    prism_control = None
                    volume_control_ids = self.__create_volume_controls(part, scope)
                    if len(volume_control_ids) > 0:
                        automesh_params.volume_control_ids = volume_control_ids
                    if prism_layers:
                        prism_control = self._model.control_data.create_prism_control()
                        prism_control.set_surface_scope(
                            prime.ScopeDefinition(
                                self._model,
                                part_expression=part.name,
                                label_expression=prism_surface_expression,
                            )
                        )
                        prism_control.set_growth_params(
                            prime.PrismControlGrowthParams(
                                self._model, n_layers=prism_layers, growth_rate=growth_rate
                            )
                        )
                        prism_control.set_volume_scope(
                            prime.ScopeDefinition(
                                self._model,
                                entity_type=prime.ScopeEntity.VOLUME,
                                evaluation_type=prime.ScopeEvaluationType.ZONES,
                                part_expression=part.name,
                                zone_expression=prism_volume_expression,
                            )
                        )
                        automesh_params.prism_control_ids = [prism_control.id]

                    automesh.mesh(part.id, automesh_params=automesh_params)
                    if prism_control:
                        self._model.control_data.delete_controls([prism_control.id])
                    if len(volume_control_ids) > 0:
                        self._model.control_data.delete_controls(volume_control_ids)
                except:
                    self._logger.info(part.name + " not volume meshed.")

    def __setup_sizing_for_wrapper(
        self,
        min_size: float,
        max_size: float,
        growth_rate: float,
        normal_angle: float,
        elements_per_gap: float,
        global_size_controls: List,
        geodesic_global_size_controls: List,
        scope: prime.ScopeDefinition,
        global_sf: prime.GlobalSizingParams,
        wrap_size_controls: List[prime.SizeControl],
    ):
        constant_size = None
        if min_size and not max_size:
            max_size = min_size
            constant_size = min_size
        elif max_size and not min_size:
            min_size = max_size
            constant_size = max_size

        if not max_size and not min_size:
            max_size = global_sf.max
            min_size = global_sf.min
        if not growth_rate:
            growth_rate = global_sf.growth_rate
        self._model.set_global_sizing_params(
            prime.GlobalSizingParams(
                self._model, min=min_size, max=max_size, growth_rate=growth_rate
            )
        )
        self._logger.info(
            "Min size: "
            + str(min_size)
            + ", Max size: "
            + str(max_size)
            + ", Growth rate: "
            + str(growth_rate)
        )

        is_geodesic = self.__is_size_field_type_geodesic(wrap_size_controls)
        if not constant_size:
            if normal_angle:
                curv_size_control = self._model.control_data.create_size_control(
                    sizing_type=prime.SizingType.CURVATURE
                )
                curv_size_control.set_curvature_sizing_params(
                    prime.CurvatureSizingParams(
                        model=self._model,
                        max=max_size,
                        min=min_size,
                        growth_rate=growth_rate,
                        normal_angle=normal_angle,
                    )
                )
                curv_size_control.set_scope(scope)
                global_size_controls.append(curv_size_control)
                if is_geodesic or elements_per_gap:
                    curv_size_control = self._model.control_data.create_size_control(
                        sizing_type=prime.SizingType.CURVATURE
                    )
                    curv_size_control.set_curvature_sizing_params(
                        prime.CurvatureSizingParams(
                            model=self._model,
                            max=max_size,
                            min=min_size,
                            growth_rate=growth_rate,
                            normal_angle=normal_angle,
                        )
                    )
                    curv_size_control.set_scope(scope)
                    geodesic_global_size_controls.append(curv_size_control)
            else:
                if elements_per_gap == None and not wrap_size_controls:
                    prime.PrimeRuntimeError(
                        "Error: No size functions or settings provided.\
                        No wrap done."
                    )
                    return
            if elements_per_gap:
                prox_size_control = self._model.control_data.create_size_control(
                    sizing_type=prime.SizingType.PROXIMITY
                )
                prox_size_control.set_proximity_sizing_params(
                    prime.ProximitySizingParams(
                        model=self._model,
                        elements_per_gap=elements_per_gap,
                        max=max_size,
                        min=min_size,
                        growth_rate=growth_rate,
                        ignore_orientation=True,
                        ignore_self_proximity=False,
                    )
                )
                prox_size_control.set_scope(scope)
                global_size_controls.append(prox_size_control)
        else:
            const_size_control = self._model.control_data.create_size_control(
                sizing_type=prime.SizingType.CURVATURE
            )
            const_size_control.set_curvature_sizing_params(
                prime.CurvatureSizingParams(
                    model=self._model,
                    max=constant_size,
                    min=constant_size,
                    growth_rate=growth_rate,
                    normal_angle=normal_angle,
                )
            )
            const_size_control.set_scope(scope)
            global_size_controls.append(const_size_control)
            if is_geodesic or elements_per_gap:
                const_size_control = self._model.control_data.create_size_control(
                    sizing_type=prime.SizingType.CURVATURE
                )
                const_size_control.set_curvature_sizing_params(
                    prime.CurvatureSizingParams(
                        model=self._model,
                        max=constant_size,
                        min=constant_size,
                        growth_rate=growth_rate,
                        normal_angle=normal_angle,
                    )
                )
                const_size_control.set_scope(scope)
                geodesic_global_size_controls.append(const_size_control)

        return min_size, max_size

    def __is_size_field_type_geodesic(self, controls: List[prime.SizeControl]):
        """
        Checks if the size field type is geodesic.
        """
        geodesic = True
        geodesic_types = ["Curvature", "Soft"]
        self._logger.info("Size controls: " + str([control.name for control in controls]))
        for control in controls:
            result = control.get_summary(prime.SizeControlSummaryParams(self._model))
            message = str(result.message)
            ctrl_type = message.split("Type : ")[1]
            ctrl_type = ctrl_type.split("\n")[0]
            self._logger.info("Name: '" + control.name + "' Type: '" + ctrl_type + "'")
            if ctrl_type not in geodesic_types:
                geodesic = False
                self._logger.info("Please note: VOLUMETRIC method used.")
                return geodesic
        return geodesic

    def __compute_size_field(
        self, size_controls: List[prime.SizeControl], field: prime.SizeField
    ) -> int:
        """
        Helper method to compute size field.
        """
        self._model.delete_volumetric_size_fields(self._model.get_volumetric_size_fields())
        result = field.compute_volumetric(
            [size_control.id for size_control in size_controls],
            prime.VolumetricSizeFieldComputeParams(model=self._model, enable_multi_threading=False),
        )
        return result.size_field_id

    def __remesh_after_wrap(self, part: prime.Part):
        """
        Surface mesh after wrapping.
        """
        surfer = prime.Surfer(self._model)
        feature_edges = part.get_edge_zonelets_of_label_name_pattern(
            label_name_pattern="___wrapper_feature_path___",
            name_pattern_params=prime.NamePatternParams(model=self._model),
        )
        surf_params = surfer.initialize_surfer_params_for_wrapper()
        surf_params.size_field_type = prime.SizeFieldType.VOLUMETRIC
        surfer.remesh_face_zonelets(
            part_id=part.id,
            face_zonelets=part.get_face_zonelets(),
            edge_zonelets=feature_edges,
            params=surf_params,
        )

    def __create_contact_preventions(
        self,
        contact_prevention_params: List,
        contact_prevention_size: float,
        min_size: float,
        max_size: float,
        growth_rate: float,
        geodesic_global_size_controls: List,
        scope: str,
    ):
        """
        Creates contact prevention controls for all parts.
        Proximity size control created for remeshing.
        """
        all_parts_labels = len(self._model.parts)
        all_parts_labels += sum([len(part.get_labels()) for part in self._model.parts])
        if contact_prevention_size < min_size:
            prime.PrimeRuntimeError("Contact_prevention_size is less than min_size.")
            return
        self._logger.info(
            "Contact prevention enabled for:"
            + str([part.name for part in self._model.parts])
            + str([part.get_labels() for part in self._model.parts if part.get_labels()])
        )

        if all_parts_labels > 1:
            geo_prox_size_control = self._model.control_data.create_size_control(
                sizing_type=prime.SizingType.PROXIMITY
            )
            geo_prox_size_control.set_proximity_sizing_params(
                prime.ProximitySizingParams(
                    model=self._model,
                    elements_per_gap=3.0,
                    max=max_size,
                    min=min_size,
                    growth_rate=growth_rate,
                    ignore_orientation=False,
                )
            )
            geo_prox_size_control.set_scope(scope)
            geodesic_global_size_controls.append(geo_prox_size_control)
            for part in self._model.parts:
                source = prime.ScopeDefinition(model=self._model, part_expression=part.name)
                contact_prevention_params.append(
                    prime.ContactPreventionParams(
                        model=self._model, source_scope=source, size=contact_prevention_size
                    )
                )
                for label in part.get_labels():
                    if part.get_face_zonelets_of_label_name_pattern(
                        label_name_pattern=label,
                        name_pattern_params=prime.NamePatternParams(self._model),
                    ):
                        source = prime.ScopeDefinition(model=self._model, label_expression=label)
                        contact_prevention_params.append(
                            prime.ContactPreventionParams(
                                model=self._model, source_scope=source, size=contact_prevention_size
                            )
                        )
        else:
            self._logger.warning(
                "Contact prevention size specified but \
                insufficient parts and labels identified to define contact."
            )

    def __create_feature_recovery_params(
        self,
        feature_recovery_params: List[prime.FeatureRecoveryParams],
        extract_features: bool,
        create_intersection_loops: bool,
        use_existing_features: bool,
        feature_angle: float,
        enable_feature_octree_refinement: bool,
        scope: prime.ScopeDefinition,
    ):
        features = prime.FeatureExtraction(self._model)
        extracted_features = dict()
        if extract_features:
            face_zonelets_prime_array = self._model.control_data.get_part_zonelets(scope=scope)
            for item in face_zonelets_prime_array:
                res = features.extract_features_on_face_zonelets(
                    part_id=item.part_id,
                    face_zonelets=item.face_zonelets,
                    params=prime.ExtractFeatureParams(
                        model=self._model,
                        feature_angle=feature_angle,
                        separation_angle=20,
                        replace=True,
                        label_name="__extracted__features__",
                    ),
                )
                extracted_features[item.part_id] = res.new_edge_zonelets
            feature_scope = scope
            feature_scope.label_expression = "__extracted__features__"
            extracted_feature_params = prime.FeatureRecoveryParams(
                model=self._model,
                enable_feature_octree_refinement=enable_feature_octree_refinement,
                scope=feature_scope,
            )
            feature_recovery_params.append(extracted_feature_params)
        if create_intersection_loops:
            for part in self._model.parts:
                others = [item.name for item in self._model.parts if item.name != part.name]
                scope1 = prime.ScopeDefinition(self._model, part_expression=part.name)
                scope2 = prime.ScopeDefinition(self._model, part_expression=','.join(others))
                scope1_zonelets_array = self._model.control_data.get_part_zonelets(scope=scope1)
                scope2_zonelets_array = self._model.control_data.get_part_zonelets(scope=scope2)
                intersect_loops_params = prime.CreateIntersectionEdgeLoopsParams(
                    model=self._model, label_name="__intersect_loops__"
                )
                features.create_intersection_edge_loops(
                    part_face_zonelets=scope1_zonelets_array,
                    intersecting_part_face_zonelets=scope2_zonelets_array,
                    params=intersect_loops_params,
                )
            intersect_feature_params = prime.FeatureRecoveryParams(
                model=self._model,
                enable_feature_octree_refinement=enable_feature_octree_refinement,
                scope=prime.ScopeDefinition(
                    model=self._model, part_expression="*", label_expression="__intersect_loops__"
                ),
            )
            feature_recovery_params.append(intersect_feature_params)
        if use_existing_features:
            existing_feature_params = prime.FeatureRecoveryParams(
                model=self._model,
                enable_feature_octree_refinement=enable_feature_octree_refinement,
                scope=scope,
            )
            feature_recovery_params.append(existing_feature_params)
        return extracted_features

    def __process_size_fields(
        self,
        global_size_controls: List[prime.SizeControl],
        wrap_size_controls: List[prime.SizeControl],
        geodesic_global_size_controls: List[prime.SizeControl],
        remesh_postwrap: bool,
        use_existing_size_fields: bool,
        recompute_remesh_sizes: bool,
        wrap_params: prime.WrapParams,
        size_fields: List[int],
    ) -> List[int]:

        created_size_fields = []
        field = prime.SizeField(self._model)
        is_geodesic = self.__is_size_field_type_geodesic(global_size_controls + wrap_size_controls)
        if (
            is_geodesic
            and remesh_postwrap
            and not recompute_remesh_sizes
            and not use_existing_size_fields
        ):
            created_size_fields.append(
                self.__compute_size_field(geodesic_global_size_controls + wrap_size_controls, field)
            )

        if not use_existing_size_fields and (global_size_controls + wrap_size_controls):
            if is_geodesic:
                size_control_ids = [i.id for i in (global_size_controls + wrap_size_controls)]
                self._logger.info("Geodesic size controls used for wrap:" + str(size_control_ids))
                wrap_params.sizing_method = prime.SizeFieldType.GEODESIC
                wrap_params.size_control_ids = size_control_ids
            else:
                self._logger.info(
                    "Volumetric size controls used for wrap:"
                    + str([i.name for i in (global_size_controls + wrap_size_controls)])
                )
                field_id = self.__compute_size_field(
                    global_size_controls + wrap_size_controls, field
                )
                wrap_params.sizing_method = prime.SizeFieldType.VOLUMETRIC
                wrap_params.size_field_ids = [field_id]
                created_size_fields.append(field_id)
        else:
            if size_fields:
                self._logger.info(
                    "Using size fields provided for wrap:" + str([i for i in size_fields])
                )
                wrap_params.sizing_method = prime.SizeFieldType.VOLUMETRIC
                wrap_params.size_field_ids = size_fields
            else:
                size_field_ids = self._model.get_active_volumetric_size_fields()
                if size_field_ids:
                    self._logger.info("Existing size field used for wrap:" + str(size_field_ids))
                    wrap_params.sizing_method = prime.SizeFieldType.VOLUMETRIC
                    wrap_params.size_field_ids = size_field_ids
                else:
                    prime.PrimeRuntimeError("Invalid size fields")
        return created_size_fields

    def __process_after_wrap(
        self,
        remesh_postwrap: bool,
        wrapped_part: prime.Part,
        use_existing_size_fields: bool,
        global_size_controls: List[prime.SizeControl],
        remesh_size_controls: List[prime.SizeControl],
        geodesic_global_size_controls: List[prime.SizeControl],
        wrap_size_controls: List[prime.SizeControl],
        remesh_scope: str,
        recompute_remesh_sizes: bool,
        feature_angle: float,
        wrapper: prime.Wrapper,
    ) -> List[int]:

        created_size_fields = []
        field = prime.SizeField(self._model)
        is_geodesic = self.__is_size_field_type_geodesic(global_size_controls + wrap_size_controls)
        features = prime.FeatureExtraction(self._model)
        if remesh_postwrap and wrapped_part:
            if not use_existing_size_fields and (global_size_controls + remesh_size_controls):
                if recompute_remesh_sizes:

                    if is_geodesic:
                        self._logger.info(
                            "Recomputing sizing after geodesic wrap:"
                            + str(
                                [
                                    i.name
                                    for i in (geodesic_global_size_controls + remesh_size_controls)
                                ]
                            )
                        )
                        for i in range(len(geodesic_global_size_controls)):
                            control = geodesic_global_size_controls[i]
                            control.set_scope(remesh_scope)
                            geodesic_global_size_controls[i] = control
                        created_size_fields.append(
                            self.__compute_size_field(
                                geodesic_global_size_controls + remesh_size_controls, field
                            )
                        )
                    else:
                        self._logger.info(
                            "Recomputing sizing for remesh after volumetric wrap:"
                            + str([i.name for i in (global_size_controls + remesh_size_controls)])
                        )
                        for i in range(len(global_size_controls)):
                            control = global_size_controls[i]
                            control.set_scope(remesh_scope)
                            global_size_controls[i] = control
                        self.__compute_size_field(
                            global_size_controls + remesh_size_controls, field
                        )
                else:
                    if is_geodesic:
                        self._logger.info(
                            "Using geodesic size controls for remesh after geodesic wrap \
                            (consider using recompute_remesh_sizes):"
                            + str(
                                [
                                    i.name
                                    for i in (geodesic_global_size_controls + wrap_size_controls)
                                ]
                            )
                        )

            self.__remesh_after_wrap(wrapped_part)
            wrapper.improve_quality(
                part_id=wrapped_part.id,
                params=prime.WrapperImproveQualityParams(
                    model=self._model, island_count=20, target_skewness=0.9
                ),
            )
            return created_size_fields

    def wrap(
        self,
        min_size: float = None,
        max_size: float = None,
        growth_rate: float = 1.2,
        elements_per_gap: float = None,
        normal_angle: float = 18.0,
        input_parts: str = "*",
        input_labels: str = "*",
        keep_inputs: bool = False,
        region_extract: prime.WrapRegion = prime.WrapRegion.EXTERNAL,
        material_point: List[float] = None,
        extract_features: bool = True,
        create_intersection_loops: bool = False,
        use_existing_features: bool = False,
        enable_feature_octree_refinement: bool = True,
        feature_angle: float = 40.0,
        contact_prevention_size: float = None,
        number_of_threads: int = None,
        remesh_postwrap: bool = True,
        recompute_remesh_sizes: bool = False,
        use_existing_size_fields: bool = False,
        size_fields: List[prime.SizeField] = None,
        wrap_size_controls: List[prime.SizeControl] = None,
        remesh_size_controls: List[prime.SizeControl] = None,
        feature_recovery_params: List[prime.FeatureRecoveryParams] = None,
        contact_prevention_params: List[prime.ContactPreventionParams] = None,
        leak_prevention_params: List[prime.LeakPreventionParams] = None,
    ):
        """Wrap and remesh input.

        Default behaviour is to perform an external wrap of all parts in the model
        using curvature sizing and extracting features.
        The wrap is then remeshed to give a surface mesh for the extracted region.

        Geodesic sizing is used if only soft and curvature controls are set.
        If contact prevention size is set and geodesic sizing is available then contact detection
        is used globally.

        If min_size and max_size is provided, variable size mesh is generated
        between min_size and max_size by applying sizes based on curvature.

        If either of min_size or max_size is provided, constant size mesh
        will be generated with the provided size.

        If neither of min_size or max_size is provided, global min and max settings are used to
        generate a variable size mesh based on curvature.


        Parameters
        ----------
        input_parts : str
            Parts to be wrapped.
            Default = "*"

        input_labels : str
            Labels to be wrapped.
            Default = "*"

        keep_inputs : bool
            Retain inputs.
            Default = False

        region_extract : prime.WrapRegion
            Set region to wrap.
            Default = prime.WrapRegion.EXTERNAL

        material_point : List[float], optional
            Material point needed if region extraction method set to material point.

        min_size: float, optional
            Minimum edge length of the mesh.

        max_size: float, optional
            Maximum edge length of the mesh.

        growth_rate : float
            Default = 1.2

        elements_per_gap : float, optional
            Global proximity size control elements per gap with self proximity.

        normal_angle : float
            Global curvature size control normal angle.
            Default = 18.0

        create_intersection_loops: bool
            Create intersection loops between all parts.
            Default = False

        use_existing_features: bool
            Maintain existing features on parts.
            Default = False

        extract_features: bool
            Extract feature edges using feature angle.
            Default = True

        feature_angle: float
            Angle used to extract features.
            Default = 40.0

        enable_feature_octree_refinement: bool
            Apply refinement to feature edges during wrap.
            Default = True

        contact_prevention_size: float, optional
            Global proximity size controls between all parts.

        number_of_threads: int, optional

        remesh_postwrap : bool
            Remesh wrap.
            Default = True

        recompute_remesh_sizes : bool
            Recompute sizes from global controls using the wrap surface.
            Default = False

        use_existing_size_fields : bool
            Use precomputed size fields.
            Default = False

        size_fields : List[prime.SizeField], optional
            Set size fields to use.

        wrap_size_controls : List[prime.SizeControl], optional
            Set wrap size controls to use.

        remesh_size_controls : List[prime.SizeControl], optional
            Set remesh size controls to use.

        feature_recovery_params : List[prime.FeatureRecoveryParams], optional
            Set feature recovery parameters to use.

        contact_prevention_params : List[prime.ContactPreventionParams], optional
            Set contact prevention parameters to use.

        leak_prevention_params : List[prime.LeakPreventionParams], optional
            Set leak prevention parameters to use.

        Returns
        -------
        Wrapped part
                Returns Part.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> from ansys.meshing.prime import lucid
        >>> prime_client = prime.launch_prime()
        >>> model = prime_client.model
        >>> mesh = lucid.Mesh(model)
        >>> mesh.read("/my_geometry.stl")
        >>> mesh.wrap(min_size=1, max_size=20, create_intersection_loops=True)
        >>> mesh.write("/mesh_output.pmdat")
        >>> prime_client.exit()

        """
        if size_fields is None:
            size_fields = []
        if wrap_size_controls is None:
            wrap_size_controls = []
        if remesh_size_controls is None:
            remesh_size_controls = []
        if feature_recovery_params is None:
            feature_recovery_params = []
        if contact_prevention_params is None:
            contact_prevention_params = []
        if leak_prevention_params is None:
            leak_prevention_params = []

        global_sf = prime.GlobalSizingParams(model=self._model)
        scope = prime.ScopeDefinition(
            model=self._model,
            part_expression=input_parts,
            label_expression=input_labels,
            entity_type=prime.ScopeEntity.FACEANDEDGEZONELETS,
        )

        # Delete topology and work only only on zonelets for now
        for part in self._model.parts:
            if len(part.get_topo_faces()) > 0:
                part.delete_topo_entities(
                    prime.DeleteTopoEntitiesParams(
                        self._model, delete_geom_zonelets=False, delete_mesh_zonelets=True
                    )
                )

        params = prime.ScopeZoneletParams(model=self._model)
        zonelets = self._model.control_data.get_scope_face_zonelets(scope=scope, params=params)
        part_ids = self._model.control_data.get_scope_parts(scope=scope)

        global_size_controls = []
        geodesic_global_size_controls = []
        computed_size_fields = []

        min_size, max_size = self.__setup_sizing_for_wrapper(
            min_size=min_size,
            max_size=max_size,
            growth_rate=growth_rate,
            normal_angle=normal_angle,
            elements_per_gap=elements_per_gap,
            global_size_controls=global_size_controls,
            geodesic_global_size_controls=geodesic_global_size_controls,
            scope=scope,
            global_sf=global_sf,
            wrap_size_controls=wrap_size_controls,
        )

        wrapper_control = self._model.control_data.create_wrapper_control()
        wrap_params = prime.WrapParams(model=self._model, wrap_region=region_extract)
        if region_extract == prime.WrapRegion.MATERIALPOINT:
            if material_point:
                mp_result = self._model.material_point_data.create_material_point(
                    suggested_name="USER_MP",
                    coords=material_point,
                    params=prime.CreateMaterialPointParams(
                        model=self._model, type=prime.MaterialPointType.LIVE
                    ),
                )
                mp_name = mp_result.assigned_name
                wrapper_control.set_live_material_points([mp_name])
            else:
                prime.PrimeRuntimeError("Error: No material point provided. No wrap done.")
                return None

        wrapper_control.set_geometry_scope(scope)

        # Add contact preventions
        if contact_prevention_size:
            self.__create_contact_preventions(
                contact_prevention_params,
                contact_prevention_size,
                min_size,
                max_size,
                growth_rate,
                geodesic_global_size_controls,
                scope,
            )
        if contact_prevention_params:
            wrapper_control.set_contact_preventions(contact_prevention_params)

        # Add feature recoveries
        extracted_features = self.__create_feature_recovery_params(
            feature_recovery_params=feature_recovery_params,
            extract_features=extract_features,
            create_intersection_loops=create_intersection_loops,
            use_existing_features=use_existing_features,
            feature_angle=feature_angle,
            enable_feature_octree_refinement=enable_feature_octree_refinement,
            scope=scope,
        )
        if feature_recovery_params:
            wrapper_control.set_feature_recoveries(feature_recovery_params)

        # Add leak preventions
        if leak_prevention_params:
            wrapper_control.set_leak_preventions(leak_prevention_params)

        computed_size_fields += self.__process_size_fields(
            global_size_controls=global_size_controls,
            wrap_size_controls=wrap_size_controls,
            geodesic_global_size_controls=geodesic_global_size_controls,
            remesh_postwrap=remesh_postwrap,
            use_existing_size_fields=use_existing_size_fields,
            recompute_remesh_sizes=recompute_remesh_sizes,
            wrap_params=wrap_params,
            size_fields=size_fields,
        )

        # Wrap
        wrapper = prime.Wrapper(model=self._model)
        if number_of_threads:
            wrap_params.number_of_threads = number_of_threads
        res = wrapper.wrap(wrapper_control_id=wrapper_control.id, params=wrap_params)
        wrapped_part = self._model.get_part(res.id)
        remesh_scope = prime.ScopeDefinition(model=self._model, part_expression=wrapped_part.name)

        # Post Wrap Processing
        self.__process_after_wrap(
            remesh_postwrap,
            wrapped_part,
            use_existing_size_fields,
            global_size_controls,
            remesh_size_controls,
            geodesic_global_size_controls,
            wrap_size_controls,
            remesh_scope,
            recompute_remesh_sizes,
            feature_angle,
            wrapper,
        )

        volume_results = wrapped_part.compute_closed_volumes(
            prime.ComputeVolumesParams(
                model=self._model, create_zones_type=prime.CreateVolumeZonesType.PERVOLUME
            )
        )
        self._logger.info(str(volume_results.volumes) + " volumes found.")

        self._model.set_global_sizing_params(
            prime.GlobalSizingParams(
                self._model, min=global_sf.min, max=global_sf.max, growth_rate=global_sf.growth_rate
            )
        )
        self._model.control_data.delete_controls(
            [
                control.id
                for control in [wrapper_control]
                + global_size_controls
                + geodesic_global_size_controls
            ]
        )

        # delete extracted features
        for part_id, zonelets_to_delete in extracted_features.items():
            part = self._model.get_part(part_id)
            part.delete_zonelets(zonelets_to_delete)

        # delete size fields
        if len(computed_size_fields) > 0:
            self._model.delete_volumetric_size_fields(computed_size_fields)

        # retain or delete inputs
        if not keep_inputs:
            self._logger.info("Deleting inputs to wrap.")
            if zonelets:
                for part_id in part_ids:
                    part = self._model.get_part(part_id)
                    [
                        part.delete_zonelets([face])
                        for face in zonelets
                        if face in part.get_face_zonelets()
                    ]
            if part_ids:
                self._model.delete_parts(part_ids)

        self._logger.info("Wrap done.")
        return wrapped_part
