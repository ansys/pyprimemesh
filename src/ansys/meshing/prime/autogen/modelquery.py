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

class ModelQuery(CoreObject):
    """ModelQuery provides functions to query parts, zones, labels, and topology information from a mesh model.

    Use this class to retrieve ids, names, and other properties for parts, zones, and mesh entities.

    Parameters
    ----------
    model : Model
        Server model to create ModelQuery object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize ModelQuery """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::ModelQuery/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for ModelQuery. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for ModelQuery. """
        command_name = "PrimeMesh::ModelQuery/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def get_part_ids(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of all parts matching the scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        Iterable[int]
            Returns part ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_ids = model_query.get_part_ids(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartIDs"
        self._model._print_beta_api_warning("get_part_ids")
        self._model._print_logs_before_command("get_part_ids", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_ids")
        return result

    def get_part_names(self, scope : ScopeDefinition) -> List[str]:
        """ Gets names of all parts matching the scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        List[str]
            Returns part names of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_names = model_query.get_part_names(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartNames"
        self._model._print_beta_api_warning("get_part_names")
        self._model._print_logs_before_command("get_part_names", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_names")
        return result

    def get_parts_with_topology(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of parts with topology.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        Iterable[int]
            Returns part ids with topology of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_ids = model_query.get_parts_with_topology(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartsWithTopology"
        self._model._print_beta_api_warning("get_parts_with_topology")
        self._model._print_logs_before_command("get_parts_with_topology", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_parts_with_topology")
        return result

    def get_parts_without_topology(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of parts without topology.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        Iterable[int]
            Returns part ids without topology of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_ids = model_query.get_parts_without_topology(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartsWithoutTopology"
        self._model._print_beta_api_warning("get_parts_without_topology")
        self._model._print_logs_before_command("get_parts_without_topology", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_parts_without_topology")
        return result

    def get_part_names_with_topology(self, scope : ScopeDefinition) -> List[str]:
        """ Gets names of parts with topology.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        List[str]
            Returns part names with topology of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_names = model_query.get_part_names_with_topology(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartNamesWithTopology"
        self._model._print_beta_api_warning("get_part_names_with_topology")
        self._model._print_logs_before_command("get_part_names_with_topology", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_names_with_topology")
        return result

    def get_part_names_without_topology(self, scope : ScopeDefinition) -> List[str]:
        """ Gets names of parts without topology.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        List[str]
            Returns part names without topology of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_names = model_query.get_part_names_without_topology(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartNamesWithoutTopology"
        self._model._print_beta_api_warning("get_part_names_without_topology")
        self._model._print_logs_before_command("get_part_names_without_topology", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_names_without_topology")
        return result

    def get_parts_with_topo_volumes(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of parts with topovolumes.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        Iterable[int]
            Returns part ids with topovolumes of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_ids = model_query.get_parts_with_topo_volumes(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartsWithTopoVolumes"
        self._model._print_beta_api_warning("get_parts_with_topo_volumes")
        self._model._print_logs_before_command("get_parts_with_topo_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_parts_with_topo_volumes")
        return result

    def get_parts_without_topo_volumes(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of parts without topovolumes.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        Iterable[int]
            Returns part ids without topovolumes of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_ids = model_query.get_parts_without_topo_volumes(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartsWithoutTopoVolumes"
        self._model._print_beta_api_warning("get_parts_without_topo_volumes")
        self._model._print_logs_before_command("get_parts_without_topo_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_parts_without_topo_volumes")
        return result

    def get_meshed_parts(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of meshed parts.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        Iterable[int]
            Returns meshed part ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_ids = model_query.get_meshed_parts(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetMeshedParts"
        self._model._print_beta_api_warning("get_meshed_parts")
        self._model._print_logs_before_command("get_meshed_parts", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_meshed_parts")
        return result

    def get_unmeshed_parts(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of unmeshed parts.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        Iterable[int]
            Returns unmeshed part ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_ids = model_query.get_unmeshed_parts(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetUnmeshedParts"
        self._model._print_beta_api_warning("get_unmeshed_parts")
        self._model._print_logs_before_command("get_unmeshed_parts", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_unmeshed_parts")
        return result

    def get_meshed_part_names(self, scope : ScopeDefinition) -> List[str]:
        """ Gets names of meshed parts.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        List[str]
            Returns meshed part names of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_names = model_query.get_meshed_part_names(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetMeshedPartNames"
        self._model._print_beta_api_warning("get_meshed_part_names")
        self._model._print_logs_before_command("get_meshed_part_names", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_meshed_part_names")
        return result

    def get_unmeshed_part_names(self, scope : ScopeDefinition) -> List[str]:
        """ Gets names of unmeshed parts.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        List[str]
            Returns unmeshed part names of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_names = model_query.get_unmeshed_part_names(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetUnmeshedPartNames"
        self._model._print_beta_api_warning("get_unmeshed_part_names")
        self._model._print_logs_before_command("get_unmeshed_part_names", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_unmeshed_part_names")
        return result

    def get_edge_zones(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of edge zones.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering edge zones.

        Returns
        -------
        Iterable[int]
            Returns edge zone ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> edge_zone_ids = model_query.get_edge_zones(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetEdgeZones"
        self._model._print_beta_api_warning("get_edge_zones")
        self._model._print_logs_before_command("get_edge_zones", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_edge_zones")
        return result

    def get_edge_zone_names(self, scope : ScopeDefinition) -> List[str]:
        """ Gets names of edge zones.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering edge zones.

        Returns
        -------
        List[str]
            Returns edge zone names of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> edge_zone_names = model_query.get_edge_zone_names(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetEdgeZoneNames"
        self._model._print_beta_api_warning("get_edge_zone_names")
        self._model._print_logs_before_command("get_edge_zone_names", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_edge_zone_names")
        return result

    def get_face_zones(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of face zones.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering face zones.

        Returns
        -------
        Iterable[int]
            Returns face zone ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> face_zone_ids = model_query.get_face_zones(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetFaceZones"
        self._model._print_beta_api_warning("get_face_zones")
        self._model._print_logs_before_command("get_face_zones", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zones")
        return result

    def get_face_zone_names(self, scope : ScopeDefinition) -> List[str]:
        """ Gets names of face zones.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering face zones.

        Returns
        -------
        List[str]
            Returns face zone names of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> face_zone_names = model_query.get_face_zone_names(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetFaceZoneNames"
        self._model._print_beta_api_warning("get_face_zone_names")
        self._model._print_logs_before_command("get_face_zone_names", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zone_names")
        return result

    def get_volume_zones(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of volume zones.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering volume zones.

        Returns
        -------
        Iterable[int]
            Returns volume zone ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> volume_zone_ids = model_query.get_volume_zones(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetVolumeZones"
        self._model._print_beta_api_warning("get_volume_zones")
        self._model._print_logs_before_command("get_volume_zones", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volume_zones")
        return result

    def get_volume_zone_names(self, scope : ScopeDefinition) -> List[str]:
        """ Gets names of volume zones.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering volume zones.

        Returns
        -------
        List[str]
            Returns volume zone names of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> volume_zone_names = model_query.get_volume_zone_names(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetVolumeZoneNames"
        self._model._print_beta_api_warning("get_volume_zone_names")
        self._model._print_logs_before_command("get_volume_zone_names", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volume_zone_names")
        return result

    def get_labels(self, scope : ScopeDefinition) -> List[str]:
        """ Gets all labels matching the scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        List[str]
            Returns labels of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> labels = model_query.get_labels(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetLabels"
        self._model._print_beta_api_warning("get_labels")
        self._model._print_logs_before_command("get_labels", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_labels")
        return result

    def get_edge_labels(self, scope : ScopeDefinition) -> List[str]:
        """ Gets edge labels of the given scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        List[str]
            Returns edge labels of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> edge_labels = model_query.get_edge_labels(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetEdgeLabels"
        self._model._print_beta_api_warning("get_edge_labels")
        self._model._print_logs_before_command("get_edge_labels", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_edge_labels")
        return result

    def get_face_labels(self, scope : ScopeDefinition) -> List[str]:
        """ Gets face labels of the given scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        List[str]
            Returns face labels of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> face_labels = model_query.get_face_labels(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetFaceLabels"
        self._model._print_beta_api_warning("get_face_labels")
        self._model._print_logs_before_command("get_face_labels", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_labels")
        return result

    def get_volume_labels(self, scope : ScopeDefinition) -> List[str]:
        """ Gets volume labels of the given scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        List[str]
            Returns volume labels of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> volume_labels = model_query.get_volume_labels(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetVolumeLabels"
        self._model._print_beta_api_warning("get_volume_labels")
        self._model._print_logs_before_command("get_volume_labels", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volume_labels")
        return result

    def get_topo_edges(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of topoedges.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering topoedges.

        Returns
        -------
        Iterable[int]
            Returns topoedge ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> topo_edge_ids = model_query.get_topo_edges(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetTopoEdges"
        self._model._print_beta_api_warning("get_topo_edges")
        self._model._print_logs_before_command("get_topo_edges", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_edges")
        return result

    def get_topo_faces(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of topofaces.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering topofaces.

        Returns
        -------
        Iterable[int]
            Returns topoface ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> topo_face_ids = model_query.get_topo_faces(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetTopoFaces"
        self._model._print_beta_api_warning("get_topo_faces")
        self._model._print_logs_before_command("get_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_faces")
        return result

    def get_meshed_topo_faces(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of meshed topofaces.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering topofaces.

        Returns
        -------
        Iterable[int]
            Returns meshed topoface ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> meshed_topo_face_ids = model_query.get_meshed_topo_faces(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetMeshedTopoFaces"
        self._model._print_beta_api_warning("get_meshed_topo_faces")
        self._model._print_logs_before_command("get_meshed_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_meshed_topo_faces")
        return result

    def get_unmeshed_topo_faces(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of unmeshed topofaces.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering topofaces.

        Returns
        -------
        Iterable[int]
            Returns unmeshed topoface ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> unmeshed_topo_face_ids = model_query.get_unmeshed_topo_faces(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetUnmeshedTopoFaces"
        self._model._print_beta_api_warning("get_unmeshed_topo_faces")
        self._model._print_logs_before_command("get_unmeshed_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_unmeshed_topo_faces")
        return result

    def get_topo_volumes(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of topovolumes.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering topovolumes.

        Returns
        -------
        Iterable[int]
            Returns topovolume ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> topo_volume_ids = model_query.get_topo_volumes(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetTopoVolumes"
        self._model._print_beta_api_warning("get_topo_volumes")
        self._model._print_logs_before_command("get_topo_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_volumes")
        return result

    def get_edge_zonelets(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of edge zonelets.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering edge zonelets.

        Returns
        -------
        Iterable[int]
            Returns edge zonelet ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> edge_zonelet_ids = model_query.get_edge_zonelets(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetEdgeZonelets"
        self._model._print_beta_api_warning("get_edge_zonelets")
        self._model._print_logs_before_command("get_edge_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_edge_zonelets")
        return result

    def get_face_zonelets(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of face zonelets.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering face zonelets.

        Returns
        -------
        Iterable[int]
            Returns face zonelet ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> face_zonelet_ids = model_query.get_face_zonelets(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetFaceZonelets"
        self._model._print_beta_api_warning("get_face_zonelets")
        self._model._print_logs_before_command("get_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zonelets")
        return result

    def get_cell_zonelets(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of cell zonelets.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering cell zonelets.

        Returns
        -------
        Iterable[int]
            Returns cell zonelet ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> cell_zonelet_ids = model_query.get_cell_zonelets(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetCellZonelets"
        self._model._print_beta_api_warning("get_cell_zonelets")
        self._model._print_logs_before_command("get_cell_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_cell_zonelets")
        return result

    def get_volumes(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of volumes.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering volumes.

        Returns
        -------
        Iterable[int]
            Returns volume ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> volume_ids = model_query.get_volumes(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetVolumes"
        self._model._print_beta_api_warning("get_volumes")
        self._model._print_logs_before_command("get_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volumes")
        return result

    def get_topo_edges_without_zone(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of topoedges without zone.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering topoedges.

        Returns
        -------
        Iterable[int]
            Returns topoedge ids without zone of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> topo_edge_ids = model_query.get_topo_edges_without_zone(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetTopoEdgesWithoutZone"
        self._model._print_beta_api_warning("get_topo_edges_without_zone")
        self._model._print_logs_before_command("get_topo_edges_without_zone", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_edges_without_zone")
        return result

    def get_topo_faces_without_zone(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of topofaces without zone.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering topofaces.

        Returns
        -------
        Iterable[int]
            Returns topoface ids without zone of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> topo_face_ids = model_query.get_topo_faces_without_zone(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetTopoFacesWithoutZone"
        self._model._print_beta_api_warning("get_topo_faces_without_zone")
        self._model._print_logs_before_command("get_topo_faces_without_zone", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_faces_without_zone")
        return result

    def get_topo_volumes_without_zone(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of topovolumes without zone.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering topovolumes.

        Returns
        -------
        Iterable[int]
            Returns topovolume ids without zone of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> topo_volume_ids = model_query.get_topo_volumes_without_zone(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetTopoVolumesWithoutZone"
        self._model._print_beta_api_warning("get_topo_volumes_without_zone")
        self._model._print_logs_before_command("get_topo_volumes_without_zone", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_volumes_without_zone")
        return result

    def get_edge_zonelets_without_zone(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of edge zonelets without zone.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering edge zonelets.

        Returns
        -------
        Iterable[int]
            Returns edge zonelet ids without zone of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> edge_zonelet_ids = model_query.get_edge_zonelets_without_zone(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetEdgeZoneletsWithoutZone"
        self._model._print_beta_api_warning("get_edge_zonelets_without_zone")
        self._model._print_logs_before_command("get_edge_zonelets_without_zone", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_edge_zonelets_without_zone")
        return result

    def get_face_zonelets_without_zone(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of face zonelets without zone.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering face zonelets.

        Returns
        -------
        Iterable[int]
            Returns face zonelet ids without zone of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> face_zonelet_ids = model_query.get_face_zonelets_without_zone(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetFaceZoneletsWithoutZone"
        self._model._print_beta_api_warning("get_face_zonelets_without_zone")
        self._model._print_logs_before_command("get_face_zonelets_without_zone", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_zonelets_without_zone")
        return result

    def get_volumes_without_zone(self, scope : ScopeDefinition) -> Iterable[int]:
        """ Gets ids of volumes without zone.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering volumes.

        Returns
        -------
        Iterable[int]
            Returns volume ids without zone of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> volume_ids = model_query.get_volumes_without_zone(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetVolumesWithoutZone"
        self._model._print_beta_api_warning("get_volumes_without_zone")
        self._model._print_logs_before_command("get_volumes_without_zone", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volumes_without_zone")
        return result

    def get_part_topo_edge_map(self, scope : ScopeDefinition) -> JsonObject:
        """ Gets a JSON map of part ids to topoedge ids matching the scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering topoedges.

        Returns
        -------
        JsonObject
            Returns a JSON object mapping part ids to their topoedge ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_topo_edge_map = model_query.get_part_topo_edge_map(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartTopoEdgeMap"
        self._model._print_beta_api_warning("get_part_topo_edge_map")
        self._model._print_logs_before_command("get_part_topo_edge_map", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_topo_edge_map")
        return result

    def get_part_topo_face_map(self, scope : ScopeDefinition) -> JsonObject:
        """ Gets a JSON map of part ids to topoface ids matching the scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering topofaces.

        Returns
        -------
        JsonObject
            Returns a JSON object mapping part ids to their topoface ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_topo_face_map = model_query.get_part_topo_face_map(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartTopoFaceMap"
        self._model._print_beta_api_warning("get_part_topo_face_map")
        self._model._print_logs_before_command("get_part_topo_face_map", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_topo_face_map")
        return result

    def get_part_topo_volume_map(self, scope : ScopeDefinition) -> JsonObject:
        """ Gets a JSON map of part ids to topovolume ids matching the scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering topovolumes.

        Returns
        -------
        JsonObject
            Returns a JSON object mapping part ids to their topovolume ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_topo_volume_map = model_query.get_part_topo_volume_map(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartTopoVolumeMap"
        self._model._print_beta_api_warning("get_part_topo_volume_map")
        self._model._print_logs_before_command("get_part_topo_volume_map", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_topo_volume_map")
        return result

    def get_part_edge_zonelet_map(self, scope : ScopeDefinition) -> JsonObject:
        """ Gets a JSON map of part ids to edge zonelet ids matching the scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering edge zonelets.

        Returns
        -------
        JsonObject
            Returns a JSON object mapping part ids to their edge zonelet ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_edge_zonelet_map = model_query.get_part_edge_zonelet_map(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartEdgeZoneletMap"
        self._model._print_beta_api_warning("get_part_edge_zonelet_map")
        self._model._print_logs_before_command("get_part_edge_zonelet_map", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_edge_zonelet_map")
        return result

    def get_part_face_zonelet_map(self, scope : ScopeDefinition) -> JsonObject:
        """ Gets a JSON map of part ids to face zonelet ids matching the scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering face zonelets.

        Returns
        -------
        JsonObject
            Returns a JSON object mapping part ids to their face zonelet ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_face_zonelet_map = model_query.get_part_face_zonelet_map(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartFaceZoneletMap"
        self._model._print_beta_api_warning("get_part_face_zonelet_map")
        self._model._print_logs_before_command("get_part_face_zonelet_map", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_face_zonelet_map")
        return result

    def get_part_volume_map(self, scope : ScopeDefinition) -> JsonObject:
        """ Gets a JSON map of part ids to volume ids matching the scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering volumes.

        Returns
        -------
        JsonObject
            Returns a JSON object mapping part ids to their volume ids of the given scope.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_volume_map = model_query.get_part_volume_map(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartVolumeMap"
        self._model._print_beta_api_warning("get_part_volume_map")
        self._model._print_logs_before_command("get_part_volume_map", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_volume_map")
        return result

    def get_part_bounding_box_map(self, scope : ScopeDefinition) -> JsonObject:
        """ Gets a JSON map of part ids to bounding boxes matching the scope.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        JsonObject
            Returns a JSON object mapping part ids to their bounding boxes.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> part_bounding_box_map = model_query.get_part_bounding_box_map(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetPartBoundingBoxMap"
        self._model._print_beta_api_warning("get_part_bounding_box_map")
        self._model._print_logs_before_command("get_part_bounding_box_map", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_part_bounding_box_map")
        return result

    def get_topo_faces_with_tag(self, scope : ScopeDefinition, tag : int) -> Iterable[int]:
        """ Gets topofaces tagged with the given tag.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering faces.
        tag : int
            Input tag used to get topofaces.

        Returns
        -------
        Iterable[int]
            Returns the tagged topoface ids.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> suppressed_topo_faces = model_query.get_topo_faces_with_tag(scope,prime.SUPPRESSED)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        if not isinstance(tag, int):
            raise TypeError("Invalid argument type passed for 'tag'. Valid argument type is int.")
        args = {"scope" : scope._jsonify(),
        "tag" : tag}
        command_name = "PrimeMesh::ModelQuery/GetTopoFacesWithTag"
        self._model._print_beta_api_warning("get_topo_faces_with_tag")
        self._model._print_logs_before_command("get_topo_faces_with_tag", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topo_faces_with_tag")
        return result

    def get_topology_summary(self, scope : ScopeDefinition) -> JsonObject:
        """ Gets a JSON of topology summary.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition for filtering parts.

        Returns
        -------
        JsonObject
            Returns a JSON object mapping part ids to their topology summary.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> topology_summary = model_query.get_topology_summary(scope)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::ModelQuery/GetTopologySummary"
        self._model._print_beta_api_warning("get_topology_summary")
        self._model._print_logs_before_command("get_topology_summary", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_topology_summary")
        return result

    def get_assembly_tree(self) -> JsonObject:
        """ Gets a complete topology tree for all parts in the model in a single call.

        Returns a JSON object containing per-part topology data including zone mappings,
        topovolumes, topofaces with their adjacent topovolumes, volumes, face zonelets,
        cell zonelets, topology flag, mesh flag, and label entity mappings.
        The returned JSON has the following structure:

        Returns
        -------
        JsonObject
            Returns a JSON object containing the full topology tree for all parts.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> assembly_tree = model_query.get_assembly_tree()

        """
        args = {}
        command_name = "PrimeMesh::ModelQuery/GetAssemblyTree"
        self._model._print_beta_api_warning("get_assembly_tree")
        self._model._print_logs_before_command("get_assembly_tree", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_assembly_tree")
        return result
