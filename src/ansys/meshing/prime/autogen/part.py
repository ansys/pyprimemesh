# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import Dict, Any, Union, List, Iterable

class Part(CoreObject):
    """Part contains zonelets and topoentities.

    Parameters
    ----------
    model : Model
        Server model to create Part object.
    id : int
        Id of the Part.
    object_id : int
        Object id of the Part.
    name : str
        Name of the Part.

    Notes
    -----
    Each Part is assigned with an id. Each Part id is unique. The value cannot be zero or negative.
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize Part """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def get_name(self) -> str:
        """ Gets the name of the Part.


        Returns
        -------
        str
            Returns part name.


        Examples
        --------
        >>> part_name = part.get_name()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetName"
        self._model._print_logs_before_command("get_name", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_name")
        return result

    def set_suggested_name(self, name : str) -> SetNameResults:
        """ Sets the unique name for the part based on the suggested name.


        Parameters
        ----------
        name : str
            Suggested name for the part.

        Returns
        -------
        SetNameResults
            Returns the results of the set name operation.


        Examples
        --------
        >>> part.set_suggested_name("part1")

        """
        if not isinstance(name, str):
            raise TypeError("Invalid argument type passed for 'name'. Valid argument type is str.")
        args = {"name" : name}
        command_name = "PrimeMesh::Part/SetSuggestedName"
        self._model._print_logs_before_command("set_suggested_name", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_suggested_name", SetNameResults(model = self._model, json_data = result))
        return SetNameResults(model = self._model, json_data = result)

    def get_face_zonelets(self) -> Iterable[int]:
        """ Gets the face zonelets of a part.


        Returns
        -------
        Iterable[int]
            Returns the ids of face zonelets or an empty list for a topology part.


        Examples
        --------
        >>> face_zonelets = part.get_face_zonelets()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetFaceZonelets"
        self._model._print_logs_before_command("get_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zonelets")
        return result

    def get_cell_zonelets(self) -> Iterable[int]:
        """ Gets the cell zonelet ids in the part.


        Returns
        -------
        Iterable[int]
            Returns the ids of cell zonelets or an empty list for a topology part.


        Examples
        --------
        >>> from ansys.meshing.prime import Part
        >>> cell_zonelet_ids = part.get_cell_zonelets()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetCellZonelets"
        self._model._print_logs_before_command("get_cell_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_cell_zonelets")
        return result

    def get_edge_zonelets(self) -> Iterable[int]:
        """ Gets the edge zonelets of a part.


        Returns
        -------
        Iterable[int]
            Returns the ids of edge zonelets or an empty list for a topology part.


        Examples
        --------
        >>> edge_zonelets = part.get_edge_zonelets()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetEdgeZonelets"
        self._model._print_logs_before_command("get_edge_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_edge_zonelets")
        return result

    def add_labels_on_zonelets(self, labels : List[str], zonelets : Iterable[int]) -> AddLabelResults:
        """ Adds the given labels on the provided zonelets.


        Parameters
        ----------
        labels : List[str]
            Labels to be added on zonelets.
        zonelets : Iterable[int]
            Ids of zonelets.

        Returns
        -------
        AddLabelResults
            Returns the results of the add label operation.


        Examples
        --------
        >>> labels = ["wall", "outer"]
        >>> part.add_labels_on_zonelets(labels, zonelets)

        """
        if not isinstance(labels, List):
            raise TypeError("Invalid argument type passed for 'labels'. Valid argument type is List[str].")
        if not isinstance(zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'zonelets'. Valid argument type is Iterable[int].")
        args = {"labels" : labels,
        "zonelets" : zonelets}
        command_name = "PrimeMesh::Part/AddLabelsOnZonelets"
        self._model._print_logs_before_command("add_labels_on_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("add_labels_on_zonelets", AddLabelResults(model = self._model, json_data = result))
        return AddLabelResults(model = self._model, json_data = result)

    def remove_labels_from_zonelets(self, labels : List[str], zonelets : Iterable[int]) -> RemoveLabelResults:
        """ Removes the given labels from the provided zonelets.


        Parameters
        ----------
        labels : List[str]
            Labels to be removed from zonelets.
        zonelets : Iterable[int]
            Ids of zonelets.

        Returns
        -------
        RemoveLabelResults
            Returns the results of the remove label operation.


        Examples
        --------
        >>> labels = ["wall", "outer"]
        >>> part.remove_labels_from_zonelets(labels, zonelets)

        """
        if not isinstance(labels, List):
            raise TypeError("Invalid argument type passed for 'labels'. Valid argument type is List[str].")
        if not isinstance(zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'zonelets'. Valid argument type is Iterable[int].")
        args = {"labels" : labels,
        "zonelets" : zonelets}
        command_name = "PrimeMesh::Part/RemoveLabelsFromZonelets"
        self._model._print_logs_before_command("remove_labels_from_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("remove_labels_from_zonelets", RemoveLabelResults(model = self._model, json_data = result))
        return RemoveLabelResults(model = self._model, json_data = result)

    def add_labels_on_topo_entities(self, labels : List[str], topo_entities : Iterable[int]) -> AddLabelResults:
        """ Adds the given labels on the provided topoentities.


        Parameters
        ----------
        labels : List[str]
            Labels to be added on topoentities.
        topo_entities : Iterable[int]
            Ids of topoentities.

        Returns
        -------
        AddLabelResults
            Returns the results of the add label operation.


        Examples
        --------
        >>> labels = ["wall", "outer"]
        >>> part.add_labels_on_topo_entities(labels, topo_entities)

        """
        if not isinstance(labels, List):
            raise TypeError("Invalid argument type passed for 'labels'. Valid argument type is List[str].")
        if not isinstance(topo_entities, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_entities'. Valid argument type is Iterable[int].")
        args = {"labels" : labels,
        "topo_entities" : topo_entities}
        command_name = "PrimeMesh::Part/AddLabelsOnTopoEntities"
        self._model._print_logs_before_command("add_labels_on_topo_entities", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("add_labels_on_topo_entities", AddLabelResults(model = self._model, json_data = result))
        return AddLabelResults(model = self._model, json_data = result)

    def remove_labels_from_topo_entities(self, labels : List[str], topo_entities : Iterable[int]) -> RemoveLabelResults:
        """ Removes the given labels from the provided topoentities.


        Parameters
        ----------
        labels : List[str]
            Labels to be removed from topoentities.
        topo_entities : Iterable[int]
            Ids of topoentities.

        Returns
        -------
        RemoveLabelResults
            Returns the results of the remove label operation.


        Examples
        --------
        >>> labels = ["wall", "outer"]
        >>> part.remove_labels_from_topo_entities(labels, topo_entities)

        """
        if not isinstance(labels, List):
            raise TypeError("Invalid argument type passed for 'labels'. Valid argument type is List[str].")
        if not isinstance(topo_entities, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_entities'. Valid argument type is Iterable[int].")
        args = {"labels" : labels,
        "topo_entities" : topo_entities}
        command_name = "PrimeMesh::Part/RemoveLabelsFromTopoEntities"
        self._model._print_logs_before_command("remove_labels_from_topo_entities", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("remove_labels_from_topo_entities", RemoveLabelResults(model = self._model, json_data = result))
        return RemoveLabelResults(model = self._model, json_data = result)

    def get_face_zones_of_name_pattern(self, zone_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets ids of face zones with name matching the given name pattern.


        Parameters
        ----------
        zone_name_pattern : str
            Name pattern to be matched with zone name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match zone name pattern.

        Returns
        -------
        Iterable[int]
            Returns list of face zone ids matching the zone name pattern.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> zones = part.get_face_zones_of_name_pattern("wall*", name_pattern_params)

        """
        if not isinstance(zone_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'zone_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"zone_name_pattern" : zone_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetFaceZonesOfNamePattern"
        self._model._print_logs_before_command("get_face_zones_of_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zones_of_name_pattern")
        return result

    def get_volume_zones_of_name_pattern(self, zone_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets ids of volume zones with name matching the given name pattern.


        Parameters
        ----------
        zone_name_pattern : str
            Name pattern to be matched with zone name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match zone name pattern.

        Returns
        -------
        Iterable[int]
            Returns a list of volume zone ids matching the zone name pattern.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> zones = part.get_volume_zones_of_name_pattern("solid*", name_pattern_params)

        """
        if not isinstance(zone_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'zone_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"zone_name_pattern" : zone_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetVolumeZonesOfNamePattern"
        self._model._print_logs_before_command("get_volume_zones_of_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volume_zones_of_name_pattern")
        return result

    def get_face_zonelets_of_zone_name_pattern(self, zone_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets ids of face zonelets of zones with name matching the given name pattern.


        Parameters
        ----------
        zone_name_pattern : str
            Name pattern to be matched with zone name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match zone name pattern.

        Returns
        -------
        Iterable[int]
            Returns face zonelet ids of zones with name matching the name pattern or an empty list for a topology part.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> face_zonelets = part.get_face_zonelets_of_zone_name_pattern("wall*", name_pattern_params)

        """
        if not isinstance(zone_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'zone_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"zone_name_pattern" : zone_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetFaceZoneletsOfZoneNamePattern"
        self._model._print_logs_before_command("get_face_zonelets_of_zone_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zonelets_of_zone_name_pattern")
        return result

    def get_volumes_of_zone_name_pattern(self, zone_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets volume ids of zones with name matching the given name pattern.


        Parameters
        ----------
        zone_name_pattern : str
            Name pattern to be matched with zone name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match zone name pattern.

        Returns
        -------
        Iterable[int]
            Returns volume ids of zones with name matching the name pattern or an empty list for a topology part.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> volumes = part.get_volumes_of_zone_name_pattern("body*", name_pattern_params)

        """
        if not isinstance(zone_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'zone_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"zone_name_pattern" : zone_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetVolumesOfZoneNamePattern"
        self._model._print_logs_before_command("get_volumes_of_zone_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volumes_of_zone_name_pattern")
        return result

    def get_volumes_of_label_name_pattern(self, label_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets ids of volumes with label matching the given name pattern.


        Parameters
        ----------
        label_name_pattern : str
            Name pattern to be matched with label.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match label name pattern.

        Returns
        -------
        Iterable[int]
            Returns ids of volumes with label matching the name pattern or an empty list for a topology part.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> volumes = part.get_volumes_of_label_name_pattern("body*", name_pattern_params)

        """
        if not isinstance(label_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'label_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"label_name_pattern" : label_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetVolumesOfLabelNamePattern"
        self._model._print_beta_api_warning("get_volumes_of_label_name_pattern")
        self._model._print_logs_before_command("get_volumes_of_label_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volumes_of_label_name_pattern")
        return result

    def get_topo_faces_of_zone_name_pattern(self, zone_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets topoface ids of zones with name matching the given name pattern.


        Parameters
        ----------
        zone_name_pattern : str
            Name pattern to be matched with zone name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match zone name pattern.

        Returns
        -------
        Iterable[int]
            Returns topoface ids of zones with name matching the name pattern.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> topo_faces = part.get_topo_faces_of_zone_name_pattern("wall*", name_pattern_params)

        """
        if not isinstance(zone_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'zone_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"zone_name_pattern" : zone_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetTopoFacesOfZoneNamePattern"
        self._model._print_logs_before_command("get_topo_faces_of_zone_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_faces_of_zone_name_pattern")
        return result

    def get_topo_volumes_of_zone_name_pattern(self, zone_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets the topovolume ids of zones with name matching the given name pattern.


        Parameters
        ----------
        zone_name_pattern : str
            Name pattern to be matched with zone name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match zone name pattern.

        Returns
        -------
        Iterable[int]
            Returns topovolume ids of zones with name matching the name pattern.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> topo_volumes = part.get_topo_volumes_of_zone_name_pattern(zone_name_pattern = "solid*",
        name_pattern_params = prime.NamePatternParams(model = model))

        """
        if not isinstance(zone_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'zone_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"zone_name_pattern" : zone_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetTopoVolumesOfZoneNamePattern"
        self._model._print_beta_api_warning("get_topo_volumes_of_zone_name_pattern")
        self._model._print_logs_before_command("get_topo_volumes_of_zone_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_volumes_of_zone_name_pattern")
        return result

    def get_topo_faces_of_topo_volumes(self, volumes : Iterable[int]) -> Iterable[int]:
        """ Gets the topofaces of given topovolumes.


        Parameters
        ----------
        volumes : Iterable[int]
            Ids of topovolumes.

        Returns
        -------
        Iterable[int]
            Returns the ids of topofaces.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> topo_faces = part.get_topo_faces_of_topo_volumes(volumes)

        """
        if not isinstance(volumes, Iterable):
            raise TypeError("Invalid argument type passed for 'volumes'. Valid argument type is Iterable[int].")
        args = {"volumes" : volumes}
        command_name = "PrimeMesh::Part/GetTopoFacesOfTopoVolumes"
        self._model._print_beta_api_warning("get_topo_faces_of_topo_volumes")
        self._model._print_logs_before_command("get_topo_faces_of_topo_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_faces_of_topo_volumes")
        return result

    def get_edge_zonelets_of_label_name_pattern(self, label_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets edge zonelet ids of labels with name matching the given name pattern.


        Parameters
        ----------
        label_name_pattern : str
            Name pattern to be matched with label name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match label name pattern.

        Returns
        -------
        Iterable[int]
            Returns edge zonelet ids of labels with name matching the name pattern or an empty list for a topology part.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> edge_zonelets = part.get_edge_zonelets_of_label_name_pattern("wall*", name_pattern_params)

        """
        if not isinstance(label_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'label_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"label_name_pattern" : label_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetEdgeZoneletsOfLabelNamePattern"
        self._model._print_logs_before_command("get_edge_zonelets_of_label_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_edge_zonelets_of_label_name_pattern")
        return result

    def get_face_zonelets_of_label_name_pattern(self, label_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets face zonelet ids of labels with name matching the given name pattern.


        Parameters
        ----------
        label_name_pattern : str
            Name pattern to be matched with label name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match label name pattern.

        Returns
        -------
        Iterable[int]
            Returns face zonelet ids of labels with name matching the name pattern or an empty list for a topology part.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> face_zonelets = part.get_face_zonelets_of_label_name_pattern("wall*", name_pattern_params)

        """
        if not isinstance(label_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'label_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"label_name_pattern" : label_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetFaceZoneletsOfLabelNamePattern"
        self._model._print_logs_before_command("get_face_zonelets_of_label_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zonelets_of_label_name_pattern")
        return result

    def get_face_zonelets_of_component_body_name_pattern(self, component_body_name_pattern : str, body_query_type : BodyQueryType, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets face zonelet ids belonging to components or bodies with name matching the given name pattern.


        Parameters
        ----------
        component_body_name_pattern : str
            Name pattern to be matched with component or body names.
        body_query_type : BodyQueryType
            Type of query used to match component or body name pattern.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match component or body name pattern.

        Returns
        -------
        Iterable[int]
            Returns face zonelet ids belonging to components or bodies with names matching the name pattern or an empty list for a topology part.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> face_zonelets = part.get_face_zonelets_of_component_body_pattern("/body*", body_query_type, name_pattern_params)

        """
        if not isinstance(component_body_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'component_body_name_pattern'. Valid argument type is str.")
        if type(body_query_type).__name__ != 'BodyQueryType':
            raise TypeError("Invalid argument type passed for 'body_query_type'. Valid argument type is BodyQueryType.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"component_body_name_pattern" : component_body_name_pattern,
        "body_query_type" : body_query_type,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetFaceZoneletsOfComponentBodyNamePattern"
        self._model._print_beta_api_warning("get_face_zonelets_of_component_body_name_pattern")
        self._model._print_logs_before_command("get_face_zonelets_of_component_body_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zonelets_of_component_body_name_pattern")
        return result

    def get_topo_edges_of_label_name_pattern(self, label_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets topoedge ids of labels with name matching the given name pattern.


        Parameters
        ----------
        label_name_pattern : str
            Name pattern to be matched with label name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match label name pattern.

        Returns
        -------
        Iterable[int]
            Returns the ids of topoedges.


        Examples
        --------
        >>> topo_edges = part.get_topo_edges_of_label_name_pattern(
        >>>                   label_name_pattern = "edge_label",
        >>>                   params = prime.NamePatternParams(model=model))

        """
        if not isinstance(label_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'label_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"label_name_pattern" : label_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetTopoEdgesOfLabelNamePattern"
        self._model._print_logs_before_command("get_topo_edges_of_label_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_edges_of_label_name_pattern")
        return result

    def get_topo_faces_of_label_name_pattern(self, label_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets topoface ids of labels with name matching the given name pattern.


        Parameters
        ----------
        label_name_pattern : str
            Name pattern to be matched with label name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match label name pattern.

        Returns
        -------
        Iterable[int]
            Returns the ids of topofaces.


        Examples
        --------
        >>> topo_faces = part.get_topo_faces_of_label_name_pattern(
        >>>                   label_name_pattern = "face_label",
        >>>                   params = prime.NamePatternParams(model=model))

        """
        if not isinstance(label_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'label_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"label_name_pattern" : label_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetTopoFacesOfLabelNamePattern"
        self._model._print_logs_before_command("get_topo_faces_of_label_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_faces_of_label_name_pattern")
        return result

    def get_topo_faces_of_component_body_name_pattern(self, component_body_name_pattern : str, body_query_type : BodyQueryType, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets topoface ids of component or bodies with name matching the given name pattern.


        Parameters
        ----------
        component_body_name_pattern : str
            Name pattern to be matched with component or body name.
        body_query_type : BodyQueryType
            Type of query used to match component or body name pattern.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match component or body name pattern.

        Returns
        -------
        Iterable[int]
            Returns the ids of topofaces.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> topo_faces = part.get_topo_faces_of_component_body_name_pattern(
        >>>                   component_body_name_pattern = "body*",
        >>>                   body_query_type = BodyQueryType_All,
        >>>                   params = prime.NamePatternParams(model=model))

        """
        if not isinstance(component_body_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'component_body_name_pattern'. Valid argument type is str.")
        if type(body_query_type).__name__ != 'BodyQueryType':
            raise TypeError("Invalid argument type passed for 'body_query_type'. Valid argument type is BodyQueryType.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"component_body_name_pattern" : component_body_name_pattern,
        "body_query_type" : body_query_type,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetTopoFacesOfComponentBodyNamePattern"
        self._model._print_beta_api_warning("get_topo_faces_of_component_body_name_pattern")
        self._model._print_logs_before_command("get_topo_faces_of_component_body_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_faces_of_component_body_name_pattern")
        return result

    def get_topo_volumes_of_label_name_pattern(self, label_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets the topovolumes of labels of the given label name expression.


        Parameters
        ----------
        label_name_pattern : str
            Name pattern to be matched with topovolume name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match topovolume name pattern.

        Returns
        -------
        Iterable[int]
            Returns the ids of the topovolumes.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> topo_volumes = prime.get_topo_volumes_of_label_name_pattern(
        >>>                      label_name_pattern = "solid*",
        >>>                      params = prime.NamePatternParams(model=model))

        """
        if not isinstance(label_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'label_name_pattern'. Valid argument type is str.")
        if type(name_pattern_params).__name__ != 'NamePatternParams':
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"label_name_pattern" : label_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetTopoVolumesOfLabelNamePattern"
        self._model._print_beta_api_warning("get_topo_volumes_of_label_name_pattern")
        self._model._print_logs_before_command("get_topo_volumes_of_label_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_volumes_of_label_name_pattern")
        return result

    def merge_zonelets(self, zonelets : Iterable[int], params : MergeZoneletsParams) -> MergeZoneletsResults:
        """ Merges zonelets.


        Parameters
        ----------
        zonelets : Iterable[int]
            Ids of zonelets to be merged.
        params : MergeZoneletsParams
            Parameters to merge zonelets.

        Returns
        -------
        MergeZoneletsResults
            Returns the results of the merge operation including merged zonelet information.


        Examples
        --------
        >>> params = prime.MergeZoneletsParams(model = model)
        >>> results = part.merge_zonelets(zonelets, params)

        """
        if not isinstance(zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'zonelets'. Valid argument type is Iterable[int].")
        if type(params).__name__ != 'MergeZoneletsParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is MergeZoneletsParams.")
        args = {"zonelets" : zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/MergeZonelets"
        self._model._print_logs_before_command("merge_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("merge_zonelets", MergeZoneletsResults(model = self._model, json_data = result))
        return MergeZoneletsResults(model = self._model, json_data = result)

    def merge_volumes(self, volumes : Iterable[int], params : MergeVolumesParams) -> MergeVolumesResults:
        """ Merges volumes by removing shared face zonelets.


        Parameters
        ----------
        volumes : Iterable[int]
            Ids of volumes to be merged.
        params : MergeVolumesParams
            Parameters to merge volumes.

        Returns
        -------
        MergeVolumesResults
            Returns the results of the merge operation including merged volume information.


        Examples
        --------
        >>> params = prime.MergeVolumesParams(model = model)
        >>> results = part.merge_volumes(volumes, params)

        """
        if not isinstance(volumes, Iterable):
            raise TypeError("Invalid argument type passed for 'volumes'. Valid argument type is Iterable[int].")
        if type(params).__name__ != 'MergeVolumesParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is MergeVolumesParams.")
        args = {"volumes" : volumes,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/MergeVolumes"
        self._model._print_logs_before_command("merge_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("merge_volumes", MergeVolumesResults(model = self._model, json_data = result))
        return MergeVolumesResults(model = self._model, json_data = result)

    def delete_volumes(self, volumes : Iterable[int], params : DeleteVolumesParams) -> DeleteVolumesResults:
        """ Deletes volumes by deleting their face zonelets.


        Parameters
        ----------
        volumes : Iterable[int]
            Ids of volumes to be deleted.
        params : DeleteVolumesParams
            Parameters to delete volumes.

        Returns
        -------
        DeleteVolumesResults
            Returns the results of the delete operation.


        Examples
        --------
        >>> params = prime.DeleteVolumesParams(model = model)
        >>> results = part.delete_volumes(volumes, params)

        """
        if not isinstance(volumes, Iterable):
            raise TypeError("Invalid argument type passed for 'volumes'. Valid argument type is Iterable[int].")
        if type(params).__name__ != 'DeleteVolumesParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is DeleteVolumesParams.")
        args = {"volumes" : volumes,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/DeleteVolumes"
        self._model._print_logs_before_command("delete_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("delete_volumes", DeleteVolumesResults(model = self._model, json_data = result))
        return DeleteVolumesResults(model = self._model, json_data = result)

    def get_face_zonelets_of_volumes(self, volumes : Iterable[int]) -> Iterable[int]:
        """ Gets the face zonelets of given volumes.


        Parameters
        ----------
        volumes : Iterable[int]
            Ids of volumes.

        Returns
        -------
        Iterable[int]
            Returns the ids of face zonelets.


        Examples
        --------
        >>> face_zonelets = part.get_face_zonelets_of_volumes(volumes)

        """
        if not isinstance(volumes, Iterable):
            raise TypeError("Invalid argument type passed for 'volumes'. Valid argument type is Iterable[int].")
        args = {"volumes" : volumes}
        command_name = "PrimeMesh::Part/GetFaceZoneletsOfVolumes"
        self._model._print_logs_before_command("get_face_zonelets_of_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zonelets_of_volumes")
        return result

    def compute_closed_volumes(self, params : ComputeVolumesParams) -> ComputeVolumesResults:
        """ Computes volume by identifying closed volumes defined by face zonelets of the part.


        Parameters
        ----------
        params : ComputeVolumesParams
            Parameters to compute volumes.

        Returns
        -------
        ComputeVolumesResults
            Returns the results of volume computation including created volume ids.


        Examples
        --------
        >>> params = prime.ComputeVolumesParams(model = model, create_zones_type = prime.CreateVolumeZonesType.PERVOLUME)
        >>> results = part.compute_closed_volumes(params)

        """
        if type(params).__name__ != 'ComputeVolumesParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ComputeVolumesParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::Part/ComputeClosedVolumes"
        self._model._print_logs_before_command("compute_closed_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("compute_closed_volumes", ComputeVolumesResults(model = self._model, json_data = result))
        return ComputeVolumesResults(model = self._model, json_data = result)

    def extract_volumes(self, face_zonelets : Iterable[int], params : ExtractVolumesParams) -> ExtractVolumesResults:
        """ Extracts volumes connected to given face zonelets.


        Parameters
        ----------
        face_zonelets : Iterable[int]
            Ids of face zonelets connected to volumes.
        params : ExtractVolumesParams
            Parameters to compute volumes.

        Returns
        -------
        ExtractVolumesResults
            Returns the results of volume extraction including extracted volume ids.


        Examples
        --------
        >>> results = part.extract_volumes(face_zonelets, params)

        """
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'face_zonelets'. Valid argument type is Iterable[int].")
        if type(params).__name__ != 'ExtractVolumesParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ExtractVolumesParams.")
        args = {"face_zonelets" : face_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/ExtractVolumes"
        self._model._print_logs_before_command("extract_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("extract_volumes", ExtractVolumesResults(model = self._model, json_data = result))
        return ExtractVolumesResults(model = self._model, json_data = result)

    def compute_topo_volumes(self, params : ComputeVolumesParams) -> ComputeTopoVolumesResults:
        """ Computes topovolumes by identifying closed volumes defined by topofaces of the part.


        Parameters
        ----------
        params : ComputeVolumesParams
            Parameters to compute topovolumes.

        Returns
        -------
        ComputeTopoVolumesResults
            Returns the results of topovolume computation including created topovolume ids.


        Examples
        --------
        >>> params = prime.ComputeVolumesParams(model = model, create_zones_type = prime.CreateVolumeZonesType.PERVOLUME)
        >>> results = part.compute_topo_volumes(params)

        """
        if type(params).__name__ != 'ComputeVolumesParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ComputeVolumesParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::Part/ComputeTopoVolumes"
        self._model._print_logs_before_command("compute_topo_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("compute_topo_volumes", ComputeTopoVolumesResults(model = self._model, json_data = result))
        return ComputeTopoVolumesResults(model = self._model, json_data = result)

    def extract_topo_volumes(self, topo_faces : Iterable[int], params : ExtractTopoVolumesParams) -> ExtractTopoVolumesResults:
        """ Extracts topovolumes connected to given cap topofaces.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of topofaces connected to topovolumes.
        params : ExtractTopoVolumesParams
            Parameters to compute topovolumes.

        Returns
        -------
        ExtractTopoVolumesResults
            Returns the results of topovolume extraction including extracted topovolume ids.


        Examples
        --------
        >>> results = part.extract_flow_topo_volumes(topo_faces, params)

        """
        if not isinstance(topo_faces, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_faces'. Valid argument type is Iterable[int].")
        if type(params).__name__ != 'ExtractTopoVolumesParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ExtractTopoVolumesParams.")
        args = {"topo_faces" : topo_faces,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/ExtractTopoVolumes"
        self._model._print_logs_before_command("extract_topo_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("extract_topo_volumes", ExtractTopoVolumesResults(model = self._model, json_data = result))
        return ExtractTopoVolumesResults(model = self._model, json_data = result)

    def extract_external_flow_volume(self, external_flow_part_id : int, params : ExtractExternalFlowVolumeParams) -> ExtractExternalFlowVolumeResults:
        """ Extracts external flow volume by merging, intersecting, and computing volumes.Merges external flow part into the current part (main part), intersects their face zonelets,computes volumes through closed volume identification, and separates volumes intoexternal flow and outer solid volumes. Also, deletes outer solid volumes with proper label or zone transfer.


        Parameters
        ----------
        external_flow_part_id : int
            Id of the external flow part.
        params : ExtractExternalFlowVolumeParams
            Parameters for the extract external flow volume operation.

        Returns
        -------
        ExtractExternalFlowVolumeResults
            Returns the results including external flow volume id and outer solid volume ids.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = main_part.extract_external_flow_volume(external_flow_part_id, params)

        """
        if not isinstance(external_flow_part_id, int):
            raise TypeError("Invalid argument type passed for 'external_flow_part_id'. Valid argument type is int.")
        if type(params).__name__ != 'ExtractExternalFlowVolumeParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ExtractExternalFlowVolumeParams.")
        args = {"external_flow_part_id" : external_flow_part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/ExtractExternalFlowVolume"
        self._model._print_beta_api_warning("extract_external_flow_volume")
        self._model._print_logs_before_command("extract_external_flow_volume", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("extract_external_flow_volume", ExtractExternalFlowVolumeResults(model = self._model, json_data = result))
        return ExtractExternalFlowVolumeResults(model = self._model, json_data = result)

    def extract_mrf_volume(self, mrf_part_id : int, params : ExtractMrfVolumeParams) -> ExtractMrfVolumeResults:
        """ Extracts MRF (Multiple Reference Frame) volume by merging, intersecting, and computing volumes.Merges MRF part into the current part (main part), intersects their face zonelets,computes volumes through closed volume identification, and extracts the MRF volume.Also, deletes the interface zonelets of the MRF part (those shared between two closed boundary regions)after volume extraction.


        Parameters
        ----------
        mrf_part_id : int
            Id of the MRF part.
        params : ExtractMrfVolumeParams
            Parameters for the extract MRF volume operation.

        Returns
        -------
        ExtractMrfVolumeResults
            Returns the results including extracted MRF volume id(s).


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = main_part.extract_mrf_volume(mrf_part_id, params)

        """
        if not isinstance(mrf_part_id, int):
            raise TypeError("Invalid argument type passed for 'mrf_part_id'. Valid argument type is int.")
        if type(params).__name__ != 'ExtractMrfVolumeParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ExtractMrfVolumeParams.")
        args = {"mrf_part_id" : mrf_part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/ExtractMrfVolume"
        self._model._print_beta_api_warning("extract_mrf_volume")
        self._model._print_logs_before_command("extract_mrf_volume", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("extract_mrf_volume", ExtractMrfVolumeResults(model = self._model, json_data = result))
        return ExtractMrfVolumeResults(model = self._model, json_data = result)

    def get_volumes_of_face_zonelet(self, face_zonelet : int) -> Iterable[int]:
        """ Gets volume ids of given face zonelet.


        Parameters
        ----------
        face_zonelet : int
            Id of face zonelet.

        Returns
        -------
        Iterable[int]
            Returns volume ids of given face zonelet.


        Examples
        --------
        >>> volumes = part.get_volumes_of_face_zonelet(face_zonelet)

        """
        if not isinstance(face_zonelet, int):
            raise TypeError("Invalid argument type passed for 'face_zonelet'. Valid argument type is int.")
        args = {"face_zonelet" : face_zonelet}
        command_name = "PrimeMesh::Part/GetVolumesOfFaceZonelet"
        self._model._print_logs_before_command("get_volumes_of_face_zonelet", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volumes_of_face_zonelet")
        return result

    def get_volumes(self) -> Iterable[int]:
        """ Gets all the volumes of the part.


        Returns
        -------
        Iterable[int]
            Returns ids of volumes.


        Examples
        --------
        >>> volumes = part.get_volumes()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetVolumes"
        self._model._print_logs_before_command("get_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volumes")
        return result

    def get_adjacent_volumes_of_volumes(self, volumes : Iterable[int]) -> Iterable[int]:
        """ Gets the adjacent volumes for the provided volume ids.


        Parameters
        ----------
        volumes : Iterable[int]
            Ids of the volume.

        Returns
        -------
        Iterable[int]
            Returns the list of adjacent volume ids.


        Examples
        --------
        >>> adjacent_volumes_of_volumes = part.get_adjacent_volumes_of_volumes(volumes)

        """
        if not isinstance(volumes, Iterable):
            raise TypeError("Invalid argument type passed for 'volumes'. Valid argument type is Iterable[int].")
        args = {"volumes" : volumes}
        command_name = "PrimeMesh::Part/GetAdjacentVolumesOfVolumes"
        self._model._print_logs_before_command("get_adjacent_volumes_of_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_adjacent_volumes_of_volumes")
        return result

    def delete_zonelets(self, zonelets : Iterable[int]) -> DeleteResults:
        """ Deletes given face zonelets.


        Parameters
        ----------
        zonelets : Iterable[int]
            Ids of zonelets to be deleted.

        Returns
        -------
        DeleteResults
            Returns the results of the delete operation.


        Examples
        --------
        >>> results = part.delete_zonelets(zonelets)

        """
        if not isinstance(zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'zonelets'. Valid argument type is Iterable[int].")
        args = {"zonelets" : zonelets}
        command_name = "PrimeMesh::Part/DeleteZonelets"
        self._model._print_logs_before_command("delete_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("delete_zonelets", DeleteResults(model = self._model, json_data = result))
        return DeleteResults(model = self._model, json_data = result)

    def create_face_zonelet_by_facets(self, params : CreateFaceZoneletByFacetsParams) -> CreateFaceZoneletByFacetsResults:
        """ Creates face zonelet by facets with the given node coordinates and face connectivity.


        Parameters
        ----------
        params : CreateFaceZoneletByFacetsParams
            Parameters containing node coordinates and face connectivity list.

        Returns
        -------
        CreateFaceZoneletByFacetsResults
            Returns the CreateFaceZoneletByFacetsResults structure containing created face zonelet id, node ids, and face ids.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = part.create_face_zonelet_by_facets(params)

        """
        if type(params).__name__ != 'CreateFaceZoneletByFacetsParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is CreateFaceZoneletByFacetsParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::Part/CreateFaceZoneletByFacets"
        self._model._print_beta_api_warning("create_face_zonelet_by_facets")
        self._model._print_logs_before_command("create_face_zonelet_by_facets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_face_zonelet_by_facets", CreateFaceZoneletByFacetsResults(model = self._model, json_data = result))
        return CreateFaceZoneletByFacetsResults(model = self._model, json_data = result)

    def get_topo_edges(self) -> Iterable[int]:
        """ Gets the topoedges of a part.


        Returns
        -------
        Iterable[int]
            Returns the ids of topoedges.

        Examples
        --------

        """
        args = {}
        command_name = "PrimeMesh::Part/GetTopoEdges"
        self._model._print_logs_before_command("get_topo_edges", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_edges")
        return result

    def get_topo_faces(self) -> Iterable[int]:
        """ Gets the topofaces of a part.


        Returns
        -------
        Iterable[int]
            Returns the ids of topofaces.


        Examples
        --------
        >>> topo_faces = part.get_topo_faces()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetTopoFaces"
        self._model._print_logs_before_command("get_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_faces")
        return result

    def get_topo_volumes(self) -> Iterable[int]:
        """ Gets topovolumes of the part.


        Returns
        -------
        Iterable[int]
            Returns the list of topovolume ids.


        Examples
        --------
        >>> results = part.get_topo_volumes()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetTopoVolumes"
        self._model._print_logs_before_command("get_topo_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_volumes")
        return result

    def add_topo_entities_to_zone(self, zone_id : int, topo_entities : Iterable[int]) -> AddToZoneResults:
        """ Adds topoentities to zone.


        Parameters
        ----------
        zone_id : int
            Id of a zone.
        topo_entities : Iterable[int]
            Ids of topoentities to be added.

        Returns
        -------
        AddToZoneResults
            Returns the results of the add to zone operation.


        Examples
        --------
        >>> results = part.add_topo_entities_to_zone(zone_id, topo_entities)

        """
        if not isinstance(zone_id, int):
            raise TypeError("Invalid argument type passed for 'zone_id'. Valid argument type is int.")
        if not isinstance(topo_entities, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_entities'. Valid argument type is Iterable[int].")
        args = {"zone_id" : zone_id,
        "topo_entities" : topo_entities}
        command_name = "PrimeMesh::Part/AddTopoEntitiesToZone"
        self._model._print_logs_before_command("add_topo_entities_to_zone", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("add_topo_entities_to_zone", AddToZoneResults(model = self._model, json_data = result))
        return AddToZoneResults(model = self._model, json_data = result)

    def add_zonelets_to_zone(self, zone_id : int, zonelets : Iterable[int]) -> AddToZoneResults:
        """ Adds zonelets to zone.


        Parameters
        ----------
        zone_id : int
            Id of a zone.
        zonelets : Iterable[int]
            Ids of zonelets to be added.

        Returns
        -------
        AddToZoneResults
            Returns the results of the add to zone operation.


        Examples
        --------
        >>> results = part.add_zonelets_to_zone(zone_id, zonelets)

        """
        if not isinstance(zone_id, int):
            raise TypeError("Invalid argument type passed for 'zone_id'. Valid argument type is int.")
        if not isinstance(zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'zonelets'. Valid argument type is Iterable[int].")
        args = {"zone_id" : zone_id,
        "zonelets" : zonelets}
        command_name = "PrimeMesh::Part/AddZoneletsToZone"
        self._model._print_logs_before_command("add_zonelets_to_zone", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("add_zonelets_to_zone", AddToZoneResults(model = self._model, json_data = result))
        return AddToZoneResults(model = self._model, json_data = result)

    def add_volumes_to_zone(self, zone_id : int, volumes : Iterable[int]) -> AddToZoneResults:
        """ Adds volumes to zone.


        Parameters
        ----------
        zone_id : int
            Id of a zone.
        volumes : Iterable[int]
            Ids of volumes to be added.

        Returns
        -------
        AddToZoneResults
            Returns the results of the add to zone operation.


        Examples
        --------
        >>> results = part.add_volumes_to_zone(zone_id, volumes)

        """
        if not isinstance(zone_id, int):
            raise TypeError("Invalid argument type passed for 'zone_id'. Valid argument type is int.")
        if not isinstance(volumes, Iterable):
            raise TypeError("Invalid argument type passed for 'volumes'. Valid argument type is Iterable[int].")
        args = {"zone_id" : zone_id,
        "volumes" : volumes}
        command_name = "PrimeMesh::Part/AddVolumesToZone"
        self._model._print_logs_before_command("add_volumes_to_zone", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("add_volumes_to_zone", AddToZoneResults(model = self._model, json_data = result))
        return AddToZoneResults(model = self._model, json_data = result)

    def get_volume_zone_of_volume(self, volume : int) -> int:
        """ Gets the volume zone of given volume.


        Parameters
        ----------
        volume : int
            Id of the volume.

        Returns
        -------
        int
            Returns the id of volume zone.


        Examples
        --------
        >>> volume_zone = part.get_volume_zone_of_volume(volume)

        """
        if not isinstance(volume, int):
            raise TypeError("Invalid argument type passed for 'volume'. Valid argument type is int.")
        args = {"volume" : volume}
        command_name = "PrimeMesh::Part/GetVolumeZoneOfVolume"
        self._model._print_logs_before_command("get_volume_zone_of_volume", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volume_zone_of_volume")
        return result

    def get_face_zone_of_zonelet(self, zonelet : int) -> int:
        """ Gets the face zone of given zonelet.


        Parameters
        ----------
        zonelet : int
            Id of the zonelet.

        Returns
        -------
        int
            Returns the id of face zone.


        Examples
        --------
        >>> face_zone = part.get_face_zone_of_zonelet(zonelet)

        """
        if not isinstance(zonelet, int):
            raise TypeError("Invalid argument type passed for 'zonelet'. Valid argument type is int.")
        args = {"zonelet" : zonelet}
        command_name = "PrimeMesh::Part/GetFaceZoneOfZonelet"
        self._model._print_logs_before_command("get_face_zone_of_zonelet", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zone_of_zonelet")
        return result

    def get_adjacent_face_zonelets_of_face_zonelets(self, face_zonelets : Iterable[int]) -> Iterable[int]:
        """ Gets the adjacent face zonelets for the provided face zonelets ids.


        Parameters
        ----------
        face_zonelets : Iterable[int]
            Ids of the face zonelets.

        Returns
        -------
        Iterable[int]
            Returns the list of adjacent face zonelet ids.


        Examples
        --------
        >>> face_zonelets_of_face_zonelet = part.get_adjacent_face_zonelets_of_face_zonelets(face_zonelets)

        """
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'face_zonelets'. Valid argument type is Iterable[int].")
        args = {"face_zonelets" : face_zonelets}
        command_name = "PrimeMesh::Part/GetAdjacentFaceZoneletsOfFaceZonelets"
        self._model._print_logs_before_command("get_adjacent_face_zonelets_of_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_adjacent_face_zonelets_of_face_zonelets")
        return result

    def get_edge_zones(self) -> Iterable[int]:
        """ Gets all the edge zones of the part.


        Returns
        -------
        Iterable[int]
            Returns ids of edge zones.


        Examples
        --------
        >>> edge_zones = part.get_edge_zones()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetEdgeZones"
        self._model._print_logs_before_command("get_edge_zones", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_edge_zones")
        return result

    def get_face_zones(self) -> Iterable[int]:
        """ Gets all the face zones of the part.


        Returns
        -------
        Iterable[int]
            Returns ids of face zones.


        Examples
        --------
        >>> face_zones = part.get_face_zones()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetFaceZones"
        self._model._print_logs_before_command("get_face_zones", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zones")
        return result

    def get_volume_zones(self) -> Iterable[int]:
        """ Gets all the volume zones of the part.


        Returns
        -------
        Iterable[int]
            Returns ids of volume zones.


        Examples
        --------
        >>> volume_zones = part.get_volume_zones()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetVolumeZones"
        self._model._print_logs_before_command("get_volume_zones", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volume_zones")
        return result

    def remove_zone_on_volumes(self, volumes : Iterable[int]) -> RemoveZoneResults:
        """ Removes zone on the given volumes.


        Parameters
        ----------
        volumes : Iterable[int]
            Volume ids whose zone is to be removed.

        Returns
        -------
        RemoveZoneResults
            Returns the results of the remove zone operation including error codes if any.


        Examples
        --------
        >>> part.remove_zone_on_volumes(volumes)

        """
        if not isinstance(volumes, Iterable):
            raise TypeError("Invalid argument type passed for 'volumes'. Valid argument type is Iterable[int].")
        args = {"volumes" : volumes}
        command_name = "PrimeMesh::Part/RemoveZoneOnVolumes"
        self._model._print_logs_before_command("remove_zone_on_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("remove_zone_on_volumes", RemoveZoneResults(model = self._model, json_data = result))
        return RemoveZoneResults(model = self._model, json_data = result)

    def remove_zone_on_zonelets(self, zonelets : Iterable[int]) -> RemoveZoneResults:
        """ Removes zone on the given zonelets.


        Parameters
        ----------
        zonelets : Iterable[int]
            Zonelet ids whose zone is to be removed.

        Returns
        -------
        RemoveZoneResults
            Returns the results of the remove zone operation including error codes if any.


        Examples
        --------
        >>> part.remove_zone_on_zonelets(zonelets)

        """
        if not isinstance(zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'zonelets'. Valid argument type is Iterable[int].")
        args = {"zonelets" : zonelets}
        command_name = "PrimeMesh::Part/RemoveZoneOnZonelets"
        self._model._print_logs_before_command("remove_zone_on_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("remove_zone_on_zonelets", RemoveZoneResults(model = self._model, json_data = result))
        return RemoveZoneResults(model = self._model, json_data = result)

    def remove_zone_on_topo_entities(self, topo_entities : Iterable[int]) -> RemoveZoneResults:
        """ Removes zone on the given topoentities.


        Parameters
        ----------
        topo_entities : Iterable[int]
            Topoentity ids whose zone is to be removed.

        Returns
        -------
        RemoveZoneResults
            Returns the results of the remove zone operation including error codes if any.


        Examples
        --------
        >>> part.remove_zone_on_topo_entities(topo_entities)

        """
        if not isinstance(topo_entities, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_entities'. Valid argument type is Iterable[int].")
        args = {"topo_entities" : topo_entities}
        command_name = "PrimeMesh::Part/RemoveZoneOnTopoEntities"
        self._model._print_logs_before_command("remove_zone_on_topo_entities", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("remove_zone_on_topo_entities", RemoveZoneResults(model = self._model, json_data = result))
        return RemoveZoneResults(model = self._model, json_data = result)

    def get_labels(self) -> List[str]:
        """ Gets all labels on entities of part.


        Returns
        -------
        List[str]
            Returns labels on entities of part.


        Examples
        --------
        >>> part.get_labels()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetLabels"
        self._model._print_logs_before_command("get_labels", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_labels")
        return result

    def get_labels_on_zonelet(self, zonelet_id : int) -> List[str]:
        """ Gets labels associated with zonelet.


        Parameters
        ----------
        zonelet_id : int
            Id of zonelet for which label is queried.

        Returns
        -------
        List[str]
            Returns labels associated with zonelet.


        Examples
        --------
        >>> results = part.get_labels_on_zonelet(zonelet_id)

        """
        if not isinstance(zonelet_id, int):
            raise TypeError("Invalid argument type passed for 'zonelet_id'. Valid argument type is int.")
        args = {"zonelet_id" : zonelet_id}
        command_name = "PrimeMesh::Part/GetLabelsOnZonelet"
        self._model._print_logs_before_command("get_labels_on_zonelet", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_labels_on_zonelet")
        return result

    def delete_topo_entities(self, params : DeleteTopoEntitiesParams) -> DeleteTopoEntitiesResults:
        """ Deletes topoentities of part controlled by parameters.


        Parameters
        ----------
        params : DeleteTopoEntitiesParams
            Parameters for control delete topoentities operation.

        Returns
        -------
        DeleteTopoEntitiesResults
            Returns results of delete topoentities.


        Examples
        --------
        >>> results = part.delete_topo_entities(params)

        """
        if type(params).__name__ != 'DeleteTopoEntitiesParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is DeleteTopoEntitiesParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::Part/DeleteTopoEntities"
        self._model._print_logs_before_command("delete_topo_entities", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("delete_topo_entities", DeleteTopoEntitiesResults(model = self._model, json_data = result))
        return DeleteTopoEntitiesResults(model = self._model, json_data = result)

    def get_splines(self) -> Iterable[int]:
        """ Gets the list of spline ids.


        Returns
        -------
        Iterable[int]
            Returns the list of spline ids.


        Examples
        --------
        >>> from ansys.meshing.prime import Part
        >>> results = part.get_splines()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetSplines"
        self._model._print_logs_before_command("get_splines", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_splines")
        return result

    def get_unstructured_spline_surface(self) -> IGAUnstructuredSplineSurf:
        """ Gets the unstructured surface spline for the part.


        Returns
        -------
        IGAUnstructuredSplineSurf
            Returns the surface spline structure.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> from ansys.meshing.prime import Part
        >>> spline = part.GetUnstructuredSplineSurface()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetUnstructuredSplineSurface"
        self._model._print_beta_api_warning("get_unstructured_spline_surface")
        self._model._print_logs_before_command("get_unstructured_spline_surface", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_unstructured_spline_surface", IGAUnstructuredSplineSurf(model = self._model, json_data = result))
        return IGAUnstructuredSplineSurf(model = self._model, json_data = result)

    def get_unstructured_spline_solid(self) -> IGAUnstructuredSplineSolid:
        """ Gets the unstructured solid spline for the part.


        Returns
        -------
        IGAUnstructuredSplineSolid
            Returns the solid spline structure.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> from ansys.meshing.prime import Part
        >>> spline = part.GetUnstructuredSplineSolid()

        """
        args = {}
        command_name = "PrimeMesh::Part/GetUnstructuredSplineSolid"
        self._model._print_beta_api_warning("get_unstructured_spline_solid")
        self._model._print_logs_before_command("get_unstructured_spline_solid", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_unstructured_spline_solid", IGAUnstructuredSplineSolid(model = self._model, json_data = result))
        return IGAUnstructuredSplineSolid(model = self._model, json_data = result)

    def get_summary(self, params : PartSummaryParams) -> PartSummaryResults:
        """ Gets the part summary for the given parameters.


        Parameters
        ----------
        params : PartSummaryParams
            Part summary parameters.

        Returns
        -------
        PartSummaryResults
            Returns the part summary including zonelet counts, entity counts, and volume information.


        Examples
        --------
        >>> results = part.get_summary(PartSummaryParams(model=model))

        """
        if type(params).__name__ != 'PartSummaryParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is PartSummaryParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::Part/GetSummary"
        self._model._print_logs_before_command("get_summary", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_summary", PartSummaryResults(model = self._model, json_data = result))
        return PartSummaryResults(model = self._model, json_data = result)

    def get_component_children_by_path(self, path : str, params : ComponentChildrenParams) -> ComponentChildrenResults:
        """ Gets the child components for a component using the given parameters.


        Parameters
        ----------
        path : str
            Path to component for which child components are queried.
        params : ComponentChildrenParams
            Parameters to get child component.

        Returns
        -------
        ComponentChildrenResults
            Returns the ComponentChildrenResults structure.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = part.get_component_children_by_path(path, params)

        """
        if not isinstance(path, str):
            raise TypeError("Invalid argument type passed for 'path'. Valid argument type is str.")
        if type(params).__name__ != 'ComponentChildrenParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ComponentChildrenParams.")
        args = {"path" : path,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/GetComponentChildrenByPath"
        self._model._print_beta_api_warning("get_component_children_by_path")
        self._model._print_logs_before_command("get_component_children_by_path", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_component_children_by_path", ComponentChildrenResults(model = self._model, json_data = result))
        return ComponentChildrenResults(model = self._model, json_data = result)

    def get_components_by_path_expression(self, path_expression : str) -> List[str]:
        """ Gets component names with the provided path expression.


        Parameters
        ----------
        path_expression : str
            Path expression to determine component names that should be returned.

        Returns
        -------
        List[str]
            Returns a list of component names.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = part.get_components_by_path_expression(path_expression)

        """
        if not isinstance(path_expression, str):
            raise TypeError("Invalid argument type passed for 'path_expression'. Valid argument type is str.")
        args = {"path_expression" : path_expression}
        command_name = "PrimeMesh::Part/GetComponentsByPathExpression"
        self._model._print_beta_api_warning("get_components_by_path_expression")
        self._model._print_logs_before_command("get_components_by_path_expression", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_components_by_path_expression")
        return result

    @property
    def id(self):
        """ Get the id of Part."""
        return self._id

    @property
    def name(self):
        """ Get the name of Part."""
        return self._name
