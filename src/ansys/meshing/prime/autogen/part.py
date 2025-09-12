# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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
from typing import List, Any, Union

class Part(CoreObject):
    """Part contains zonelets and topoentities.

    Topoentities and zonelets are characterized by dimension of entities.
    Zonelets are a group of interconnected elements in a mesh. There are three types of zonelets. They are:

    * FaceZonelet: A group of interconnected face elements.
    * EdgeZonelet: A group of interconnected edge elements.
    * CellZonelet: A group of interconnected cell elements.

    Topoentities represent connectivity information.
    Topoentities can be queried from higher order to lower order topoentities and vice versa.
    Topoentities have geometric representation which may be defined by splines or facets.
    The mesh generated on topoentities will be projected on geometry representation.

    * TopoFace: Topoentity representing surfaces.
    * TopoEdge: Topoentity representing curves.
    * TopoVolume: Topoentity representing volumes.




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
            Returns the SetNameResults.


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
        """ Get the face zonelets of a part.


        Returns
        -------
        Iterable[int]
            Return the ids of face zonelets. Returns an empty list for a topology part.


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
        """ Get the cell zonelet ids in the part.


        Returns
        -------
        Iterable[int]
            Return the ids of cell zonelets. Returns an empty list for a topology part.


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
        """ Get the edge zonelets of a part.


        Returns
        -------
        Iterable[int]
            Return the ids of edge zonelets. Returns an empty list for a topology part.


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
        """ Add the given labels on the provided zonelets.


        Parameters
        ----------
        labels : List[str]
            Labels to be added on zonelets.
        zonelets : Iterable[int]
            Ids of zonelets.

        Returns
        -------
        AddLabelResults
            Returns the AddLabelResults.


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
        """ Remove the given labels from the provided zonelets.


        Parameters
        ----------
        labels : List[str]
            Labels to be removed from zonelets.
        zonelets : Iterable[int]
            Ids of zonelets.

        Returns
        -------
        RemoveLabelResults
            Returns the RemoveLabelResults.


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
        """ Add the given labels on the provided topoentities.


        Parameters
        ----------
        labels : List[str]
            Labels to be added on topoentities.
        topo_entities : Iterable[int]
            Ids of topoentities.

        Returns
        -------
        AddLabelResults
            Returns the AddLabelResults.


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
        """ Remove the given labels from the provided topoentities.


        Parameters
        ----------
        labels : List[str]
            Labels to be removed from topoentities.
        topo_entities : Iterable[int]
            Ids of topoentities.

        Returns
        -------
        RemoveLabelResults
            Returns the RemoveLabelResults.


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
        """ Get ids of face zones with name matching the given name pattern.


        Parameters
        ----------
        zone_name_pattern : str
            Name pattern to be matched with zone name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match zone name pattern.

        Returns
        -------
        Iterable[int]
            Return list of face zone ids matching the zone name pattern.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> zones = part.get_face_zones_of_name_pattern("wall*", name_pattern_params)

        """
        if not isinstance(zone_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'zone_name_pattern'. Valid argument type is str.")
        if not isinstance(name_pattern_params, NamePatternParams):
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"zone_name_pattern" : zone_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetFaceZonesOfNamePattern"
        self._model._print_logs_before_command("get_face_zones_of_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zones_of_name_pattern")
        return result

    def get_volume_zones_of_name_pattern(self, zone_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Get ids of volume zones with name matching the given name pattern.


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
        if not isinstance(name_pattern_params, NamePatternParams):
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"zone_name_pattern" : zone_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetVolumeZonesOfNamePattern"
        self._model._print_logs_before_command("get_volume_zones_of_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volume_zones_of_name_pattern")
        return result

    def get_face_zonelets_of_zone_name_pattern(self, zone_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Get ids of face zonelets of zones with name matching the given name pattern.


        Parameters
        ----------
        zone_name_pattern : str
            Name pattern to be matched with zone name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match zone name pattern.

        Returns
        -------
        Iterable[int]
            Return face zonelet ids of zones with name matching the name pattern. Returns an empty list for a topology part.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> face_zonelets = part.get_face_zonelets_of_zone_name_pattern("wall*", name_pattern_params)

        """
        if not isinstance(zone_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'zone_name_pattern'. Valid argument type is str.")
        if not isinstance(name_pattern_params, NamePatternParams):
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"zone_name_pattern" : zone_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetFaceZoneletsOfZoneNamePattern"
        self._model._print_logs_before_command("get_face_zonelets_of_zone_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zonelets_of_zone_name_pattern")
        return result

    def get_volumes_of_zone_name_pattern(self, zone_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Get volume ids of zones with name matching the given name pattern.


        Parameters
        ----------
        zone_name_pattern : str
            Name pattern to be matched with zone name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match zone name pattern.

        Returns
        -------
        Iterable[int]
            Return volume ids of zones with name matching the name pattern. Returns an empty list for a topology part.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> volumes = part.get_volumes_of_zone_name_pattern("body*", name_pattern_params)

        """
        if not isinstance(zone_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'zone_name_pattern'. Valid argument type is str.")
        if not isinstance(name_pattern_params, NamePatternParams):
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"zone_name_pattern" : zone_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetVolumesOfZoneNamePattern"
        self._model._print_logs_before_command("get_volumes_of_zone_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volumes_of_zone_name_pattern")
        return result

    def get_topo_faces_of_zone_name_pattern(self, zone_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Get topoface ids of zones with name matching the given name pattern.


        Parameters
        ----------
        zone_name_pattern : str
            Name pattern to be matched with zone name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match zone name pattern.

        Returns
        -------
        Iterable[int]
            Return topoface ids of zones with name matching the name pattern.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> topo_faces = part.get_topo_faces_of_zone_name_pattern("wall*", name_pattern_params)

        """
        if not isinstance(zone_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'zone_name_pattern'. Valid argument type is str.")
        if not isinstance(name_pattern_params, NamePatternParams):
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
        if not isinstance(name_pattern_params, NamePatternParams):
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
        """ Get edge zonelet ids of labels with name matching the given name pattern.


        Parameters
        ----------
        label_name_pattern : str
            Name pattern to be matched with label name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match label name pattern.

        Returns
        -------
        Iterable[int]
            Return edge zonelet ids of labels with name matching the name pattern. Returns an empty list for a topology part.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> edge_zonelets = part.get_edge_zonelets_of_label_name_pattern("wall*", name_pattern_params)

        """
        if not isinstance(label_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'label_name_pattern'. Valid argument type is str.")
        if not isinstance(name_pattern_params, NamePatternParams):
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"label_name_pattern" : label_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetEdgeZoneletsOfLabelNamePattern"
        self._model._print_logs_before_command("get_edge_zonelets_of_label_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_edge_zonelets_of_label_name_pattern")
        return result

    def get_face_zonelets_of_label_name_pattern(self, label_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Get face zonelet ids of labels with name matching the given name pattern.


        Parameters
        ----------
        label_name_pattern : str
            Name pattern to be matched with label name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match label name pattern.

        Returns
        -------
        Iterable[int]
            Return face zonelet ids of labels with name matching the name pattern. Returns an empty list for a topology part.


        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> face_zonelets = part.get_face_zonelets_of_label_name_pattern("wall*", name_pattern_params)

        """
        if not isinstance(label_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'label_name_pattern'. Valid argument type is str.")
        if not isinstance(name_pattern_params, NamePatternParams):
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"label_name_pattern" : label_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetFaceZoneletsOfLabelNamePattern"
        self._model._print_logs_before_command("get_face_zonelets_of_label_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zonelets_of_label_name_pattern")
        return result

    def get_face_zonelets_of_component_body_name_pattern(self, component_body_name_pattern : str, type : BodyQueryType, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets face zonelet ids belonging to components or bodies with name matching the given name pattern.


        Parameters
        ----------
        component_body_name_pattern : str
            Name pattern to be matched with component or body names.
        type : BodyQueryType
            Type of query used to match component or body name pattern.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match component or body name pattern.

        Returns
        -------
        Iterable[int]
            Returns face zonelet ids of labels with name matching the name pattern. Returns an empty list for a topology part.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> name_pattern_params = prime.NamePatternParams(model = model)
        >>> face_zonelets = part.get_face_zonelets_of_component_body_pattern("/body*", type, name_pattern_params)

        """
        if not isinstance(component_body_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'component_body_name_pattern'. Valid argument type is str.")
        if not isinstance(type, BodyQueryType):
            raise TypeError("Invalid argument type passed for 'type'. Valid argument type is BodyQueryType.")
        if not isinstance(name_pattern_params, NamePatternParams):
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"component_body_name_pattern" : component_body_name_pattern,
        "type" : type,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetFaceZoneletsOfComponentBodyNamePattern"
        self._model._print_beta_api_warning("get_face_zonelets_of_component_body_name_pattern")
        self._model._print_logs_before_command("get_face_zonelets_of_component_body_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zonelets_of_component_body_name_pattern")
        return result

    def get_topo_edges_of_label_name_pattern(self, label_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Get topoedge ids of labels with name matching the given name pattern.


        Parameters
        ----------
        label_name_pattern : str
            Name pattern to be matched with label name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match label name pattern.

        Returns
        -------
        Iterable[int]
            Return the ids of topoedges.


        Examples
        --------
        >>> topo_edges = part.get_topo_edges_of_label_name_pattern(
        >>>                   label_name_pattern = "edge_label",
        >>>                   params = prime.NamePatternParams(model=model))

        """
        if not isinstance(label_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'label_name_pattern'. Valid argument type is str.")
        if not isinstance(name_pattern_params, NamePatternParams):
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"label_name_pattern" : label_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetTopoEdgesOfLabelNamePattern"
        self._model._print_logs_before_command("get_topo_edges_of_label_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_edges_of_label_name_pattern")
        return result

    def get_topo_faces_of_label_name_pattern(self, label_name_pattern : str, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Get topoface ids of labels with name matching the given name pattern.


        Parameters
        ----------
        label_name_pattern : str
            Name pattern to be matched with label name.
        name_pattern_params : NamePatternParams
            Name pattern parameters used to match label name pattern.

        Returns
        -------
        Iterable[int]
            Return the ids of topofaces.


        Examples
        --------
        >>> topo_faces = part.get_topo_faces_of_label_name_pattern(
        >>>                   label_name_pattern = "face_label",
        >>>                   params = prime.NamePatternParams(model=model))

        """
        if not isinstance(label_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'label_name_pattern'. Valid argument type is str.")
        if not isinstance(name_pattern_params, NamePatternParams):
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"label_name_pattern" : label_name_pattern,
        "name_pattern_params" : name_pattern_params._jsonify()}
        command_name = "PrimeMesh::Part/GetTopoFacesOfLabelNamePattern"
        self._model._print_logs_before_command("get_topo_faces_of_label_name_pattern", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_faces_of_label_name_pattern")
        return result

    def get_topo_faces_of_component_body_name_pattern(self, component_body_name_pattern : str, type : BodyQueryType, name_pattern_params : NamePatternParams) -> Iterable[int]:
        """ Gets topoface ids of component or bodies with name matching the given name pattern.


        Parameters
        ----------
        component_body_name_pattern : str
            Name pattern to be matched with component or body name.
        type : BodyQueryType
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
        >>>                   type = BodyQueryType_All,
        >>>                   params = prime.NamePatternParams(model=model))

        """
        if not isinstance(component_body_name_pattern, str):
            raise TypeError("Invalid argument type passed for 'component_body_name_pattern'. Valid argument type is str.")
        if not isinstance(type, BodyQueryType):
            raise TypeError("Invalid argument type passed for 'type'. Valid argument type is BodyQueryType.")
        if not isinstance(name_pattern_params, NamePatternParams):
            raise TypeError("Invalid argument type passed for 'name_pattern_params'. Valid argument type is NamePatternParams.")
        args = {"component_body_name_pattern" : component_body_name_pattern,
        "type" : type,
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
            Name pattern to be matched with topovolume name
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
        if not isinstance(name_pattern_params, NamePatternParams):
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
        """ Merge zonelets.


        Parameters
        ----------
        zonelets : Iterable[int]
            Ids of zonelets to be merged.
        params : MergeZoneletsParams
            Parameters to merge zonelets.

        Returns
        -------
        MergeZoneletsResults
            Returns the MergeZoneletsResults.


        Examples
        --------
        params = prime.MergeZoneletsParams(model = model)
        results = part.merge_zonelets(zonelets, params)

        """
        if not isinstance(zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(params, MergeZoneletsParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is MergeZoneletsParams.")
        args = {"zonelets" : zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/MergeZonelets"
        self._model._print_logs_before_command("merge_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("merge_zonelets", MergeZoneletsResults(model = self._model, json_data = result))
        return MergeZoneletsResults(model = self._model, json_data = result)

    def merge_volumes(self, volumes : Iterable[int], params : MergeVolumesParams) -> MergeVolumesResults:
        """ Merge volumes by removing shared face zonelets.


        Parameters
        ----------
        volumes : Iterable[int]
            Ids of volumes to be merged.
        params : MergeVolumesParams
            Parameters to merge volumes.

        Returns
        -------
        MergeVolumesResults
            Returns the MergeVolumesResults.


        Examples
        --------
        params = prime.MergeVolumesParams(model = model)
        results = part.merge_volumes(volumes, params)

        """
        if not isinstance(volumes, Iterable):
            raise TypeError("Invalid argument type passed for 'volumes'. Valid argument type is Iterable[int].")
        if not isinstance(params, MergeVolumesParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is MergeVolumesParams.")
        args = {"volumes" : volumes,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/MergeVolumes"
        self._model._print_logs_before_command("merge_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("merge_volumes", MergeVolumesResults(model = self._model, json_data = result))
        return MergeVolumesResults(model = self._model, json_data = result)

    def delete_volumes(self, volumes : Iterable[int], params : DeleteVolumesParams) -> DeleteVolumesResults:
        """ Delete volumes by deleting its face zonelets.


        Parameters
        ----------
        volumes : Iterable[int]
            Ids of volumes to be deleted.
        params : DeleteVolumesParams
            Parameters to delete volumes.

        Returns
        -------
        DeleteVolumesResults
            Returns the DeleteVolumesResults.


        Examples
        --------
        params = prime.DeleteVolumesParams(model = model)
        results = part.delete_volumes(volumes, params)

        """
        if not isinstance(volumes, Iterable):
            raise TypeError("Invalid argument type passed for 'volumes'. Valid argument type is Iterable[int].")
        if not isinstance(params, DeleteVolumesParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is DeleteVolumesParams.")
        args = {"volumes" : volumes,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/DeleteVolumes"
        self._model._print_logs_before_command("delete_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("delete_volumes", DeleteVolumesResults(model = self._model, json_data = result))
        return DeleteVolumesResults(model = self._model, json_data = result)

    def get_face_zonelets_of_volumes(self, volumes : Iterable[int]) -> Iterable[int]:
        """ Get the face zonelets of given volumes.


        Parameters
        ----------
        volumes : Iterable[int]
            Ids of volumes.

        Returns
        -------
        Iterable[int]
            Return the ids of face zonelets.


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
            Returns the ComputeVolumesResults.


        Examples
        --------
        >>> params = prime.ComputeVolumesParams(model = model, create_zones_type = prime.CreateVolumeZonesType.PERVOLUME)
        >>> results = part.compute_closed_volumes(params)

        """
        if not isinstance(params, ComputeVolumesParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ComputeVolumesParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::Part/ComputeClosedVolumes"
        self._model._print_logs_before_command("compute_closed_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("compute_closed_volumes", ComputeVolumesResults(model = self._model, json_data = result))
        return ComputeVolumesResults(model = self._model, json_data = result)

    def extract_volumes(self, face_zonelets : Iterable[int], params : ExtractVolumesParams) -> ExtractVolumesResults:
        """ Extract volumes connected to given face zonelets.


        Parameters
        ----------
        face_zonelets : Iterable[int]
            Ids of face zonelets connected to volumes.
        params : ExtractVolumesParams
            Parameters to compute volumes.

        Returns
        -------
        ExtractVolumesResults
            Return the ExtractVolumesResults.


        Examples
        --------
        >>> results = part.extract_volumes(face_zonelets, params)

        """
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'face_zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(params, ExtractVolumesParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ExtractVolumesParams.")
        args = {"face_zonelets" : face_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/ExtractVolumes"
        self._model._print_logs_before_command("extract_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("extract_volumes", ExtractVolumesResults(model = self._model, json_data = result))
        return ExtractVolumesResults(model = self._model, json_data = result)

    def compute_topo_volumes(self, params : ComputeVolumesParams) -> ComputeTopoVolumesResults:
        """ Compute topovolumes by identifying closed volumes defined by topofaces of the part.


        Parameters
        ----------
        params : ComputeVolumesParams
            Parameters to compute topovolumes.

        Returns
        -------
        ComputeTopoVolumesResults
            Return the ComputeTopoVolumesResults.


        Examples
        --------
        >>> params = prime.ComputeVolumesParams(model = model, create_zones_type = prime.CreateVolumeZonesType.PERVOLUME)
        >>> results = part.compute_topo_volumes(params)

        """
        if not isinstance(params, ComputeVolumesParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ComputeVolumesParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::Part/ComputeTopoVolumes"
        self._model._print_logs_before_command("compute_topo_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("compute_topo_volumes", ComputeTopoVolumesResults(model = self._model, json_data = result))
        return ComputeTopoVolumesResults(model = self._model, json_data = result)

    def extract_topo_volumes(self, topo_faces : Iterable[int], params : ExtractTopoVolumesParams) -> ExtractTopoVolumesResults:
        """ Extract topovolumes connected to given cap topofaces.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of topofaces connected to topovolumes.
        params : ExtractTopoVolumesParams
            Parameters to compute topovolumes.

        Returns
        -------
        ExtractTopoVolumesResults
            Return the ExtractTopoVolumesResults.


        Examples
        --------
        >>> results = part.extract_flow_topo_volumes(topo_faces, params)

        """
        if not isinstance(topo_faces, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_faces'. Valid argument type is Iterable[int].")
        if not isinstance(params, ExtractTopoVolumesParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ExtractTopoVolumesParams.")
        args = {"topo_faces" : topo_faces,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Part/ExtractTopoVolumes"
        self._model._print_logs_before_command("extract_topo_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("extract_topo_volumes", ExtractTopoVolumesResults(model = self._model, json_data = result))
        return ExtractTopoVolumesResults(model = self._model, json_data = result)

    def get_volumes_of_face_zonelet(self, face_zonelet : int) -> Iterable[int]:
        """ Get volume ids of given face zonelet.


        Parameters
        ----------
        face_zonelet : int
            Id of face zonelet.

        Returns
        -------
        Iterable[int]
            Return volume ids of given face zonelet.


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
        """ Get all the volumes of the part.


        Returns
        -------
        Iterable[int]
            Return ids of volumes.


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
        """ Get the adjacent volumes for the provided volume ids.


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
        """ Delete given face zonelets.


        Parameters
        ----------
        zonelets : Iterable[int]
            Ids of zonelets to be deleted.

        Returns
        -------
        DeleteResults
            Return DeleteResults.


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

    def get_topo_edges(self) -> Iterable[int]:
        """ Get the topoedges of a part.


        Returns
        -------
        Iterable[int]
            Return the ids of topoedges.

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
        """ Get the topofaces of a part.


        Returns
        -------
        Iterable[int]
            Return the ids of topofaces.

Return the ids of topofaces.


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
        """ Get topovolumes of part.


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
        """ Add topoentities to zone.


        Parameters
        ----------
        zone_id : int
            Id of a zone .
        topo_entities : Iterable[int]
            Ids of topoentities to be added.

        Returns
        -------
        AddToZoneResults
            Returns the AddToZoneResults.


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
        """ Add zonelets to zone.


        Parameters
        ----------
        zone_id : int
            Id of a zone .
        zonelets : Iterable[int]
            Ids of zonelets to be added.

        Returns
        -------
        AddToZoneResults
            Returns the AddToZoneResults.


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
        """ Add volumes to zone.


        Parameters
        ----------
        zone_id : int
            Id of a zone .
        volumes : Iterable[int]
            Ids of volumes to be added.

        Returns
        -------
        AddToZoneResults
            Returns the AddToZoneResults.


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
            Id of volume.

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
            Id of zonelet.

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
        """ Gets the adjacent facezonelets for the provided facezonelet ids.


        Parameters
        ----------
        face_zonelets : Iterable[int]
            Ids of facezonelets.

        Returns
        -------
        Iterable[int]
            Returns the list of adjacent facezonelet ids.


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
        """ Get all the edge zones of the part.


        Returns
        -------
        Iterable[int]
            Return ids of edge zones.


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
        """ Get all the face zones of the part.


        Returns
        -------
        Iterable[int]
            Return ids of face zones.


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
        """ Get all the volume zones of the part.


        Returns
        -------
        Iterable[int]
            Return ids of volume zones.


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
            Returns the RemoveZoneResults.


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
            Returns the RemoveZoneResults.


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
            Returns the RemoveZoneResults.


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
        """ Get all labels on entities of part.


        Returns
        -------
        List[str]
            Return labels on entities of part.


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
        """ Delete topoentities of part controled by parameters.


        Parameters
        ----------
        params : DeleteTopoEntitiesParams
            Parameters for control delete topoentities operation.

        Returns
        -------
        DeleteTopoEntitiesResults
            Return results of delete topoentities.


        Examples
        --------
        >>> results = part.delete_topo_entities(params)

        """
        if not isinstance(params, DeleteTopoEntitiesParams):
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
        """ Get the part summary.

        Provides the part summary for the given parameters.

        Parameters
        ----------
        params : PartSummaryParams
            Part summary parameters.

        Returns
        -------
        PartSummaryResults
            Return the PartSummaryResults.

        Examples
        --------
        >>> results = part.get_summary(PartSummaryParams(model=model))

        """
        if not isinstance(params, PartSummaryParams):
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
        if not isinstance(params, ComponentChildrenParams):
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
