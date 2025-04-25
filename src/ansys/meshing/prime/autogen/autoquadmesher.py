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

class AutoQuadMesher(CoreObject):
    """Generate full quad mesh.

    Parameters
    ----------
    model : Model
        Server model to create AutoQuadMesher object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize AutoQuadMesher """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::AutoQuadMesher/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for AutoQuadMesher. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for AutoQuadMesher. """
        command_name = "PrimeMesh::AutoQuadMesher/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def detect_and_treat_features(self, part_id : int, topo_face_ids : Iterable[int], params : DetectAndTreatFeaturesParams) -> AutoQuadMesherResults:
        """ Detect features in topology and treat them with given parameters.


        Parameters
        ----------
        part_id : int
            Id of the Part.
        topo_face_ids : Iterable[int]
            Ids of topofaces.
        params : DetectAndTreatFeaturesParams
            Parameters of detect and treat features.

        Returns
        -------
        AutoQuadMesherResults
            Returns the AutoQuadMesherResults structure.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> autoQuadMesher = AutoQuadMesher(model=model)
        >>> results = autoQuadMesher.detect_and_treat_features(part_id, topo_face_ids, params);

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(topo_face_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_face_ids'. Valid argument type is Iterable[int].")
        if not isinstance(params, DetectAndTreatFeaturesParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is DetectAndTreatFeaturesParams.")
        args = {"part_id" : part_id,
        "topo_face_ids" : topo_face_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::AutoQuadMesher/DetectAndTreatFeatures"
        self._model._print_beta_api_warning("detect_and_treat_features")
        self._model._print_logs_before_command("detect_and_treat_features", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("detect_and_treat_features", AutoQuadMesherResults(model = self._model, json_data = result))
        return AutoQuadMesherResults(model = self._model, json_data = result)

    def repair_topology(self, part_id : int, topo_face_ids : Iterable[int], params : RepairTopologyParams) -> AutoQuadMesherResults:
        """ Repair topology with given parameters.


        Parameters
        ----------
        part_id : int
            Id of the Part.
        topo_face_ids : Iterable[int]
            Ids of topofaces.
        params : RepairTopologyParams
            Parameters of repair topology.

        Returns
        -------
        AutoQuadMesherResults
            Returns the AutoQuadMesherResults structure.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> autoQuadMesher = AutoQuadMesher(model=model)
        >>> results = autoQuadMesher.repair_topology(part_id, topo_face_ids, params);

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(topo_face_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_face_ids'. Valid argument type is Iterable[int].")
        if not isinstance(params, RepairTopologyParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is RepairTopologyParams.")
        args = {"part_id" : part_id,
        "topo_face_ids" : topo_face_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::AutoQuadMesher/RepairTopology"
        self._model._print_beta_api_warning("repair_topology")
        self._model._print_logs_before_command("repair_topology", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("repair_topology", AutoQuadMesherResults(model = self._model, json_data = result))
        return AutoQuadMesherResults(model = self._model, json_data = result)

    def defeature_topology(self, part_id : int, topo_face_ids : Iterable[int], params : DefeatureTopologyParams) -> AutoQuadMesherResults:
        """ Defeature topology with given parameters.


        Parameters
        ----------
        part_id : int
            Id of the Part.
        topo_face_ids : Iterable[int]
            Ids of topofaces.
        params : DefeatureTopologyParams
            Parameters of defeature topology.

        Returns
        -------
        AutoQuadMesherResults
            Returns the AutoQuadMesherResults structure.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> autoQuadMesher = AutoQuadMesher(model=model)
        >>> results = autoQuadMesher.defeature_topology(part_id, topo_face_ids, params);

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(topo_face_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_face_ids'. Valid argument type is Iterable[int].")
        if not isinstance(params, DefeatureTopologyParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is DefeatureTopologyParams.")
        args = {"part_id" : part_id,
        "topo_face_ids" : topo_face_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::AutoQuadMesher/DefeatureTopology"
        self._model._print_beta_api_warning("defeature_topology")
        self._model._print_logs_before_command("defeature_topology", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("defeature_topology", AutoQuadMesherResults(model = self._model, json_data = result))
        return AutoQuadMesherResults(model = self._model, json_data = result)

    def optimize_quad_mesh(self, part_id : int, topo_face_ids : Iterable[int], params : OptimizeQuadMeshParams) -> AutoQuadMesherResults:
        """ Optimize quad faces with given parameters.


        Parameters
        ----------
        part_id : int
            Id of the Part.
        topo_face_ids : Iterable[int]
            Ids of topofaces.
        params : OptimizeQuadMeshParams
            Parameters of optimize quad mesh.

        Returns
        -------
        AutoQuadMesherResults
            Returns the AutoQuadMesherResults structure.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> autoQuadMesher = AutoQuadMesher(model=model)
        >>> results = autoQuadMesher.optimize_quad_mesh(part_id, topo_face_ids, params);

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(topo_face_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_face_ids'. Valid argument type is Iterable[int].")
        if not isinstance(params, OptimizeQuadMeshParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is OptimizeQuadMeshParams.")
        args = {"part_id" : part_id,
        "topo_face_ids" : topo_face_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::AutoQuadMesher/OptimizeQuadMesh"
        self._model._print_beta_api_warning("optimize_quad_mesh")
        self._model._print_logs_before_command("optimize_quad_mesh", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("optimize_quad_mesh", AutoQuadMesherResults(model = self._model, json_data = result))
        return AutoQuadMesherResults(model = self._model, json_data = result)

    def check_topology(self, part_id : int, topo_face_ids : Iterable[int], params : CheckTopologyParams) -> AutoQuadMesherResults:
        """ Check topology for inconsistencies with the given parameters.


        Parameters
        ----------
        part_id : int
            Id of the Part.
        topo_face_ids : Iterable[int]
            Ids of topofaces.
        params : CheckTopologyParams
            Parameters of check topology.

        Returns
        -------
        AutoQuadMesherResults
            Returns the AutoQuadMesherResults structure.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> autoQuadMesher = AutoQuadMesher(model=model)
        >>> results = autoQuadMesher.check_topology(part_id, topo_face_ids, params);

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(topo_face_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_face_ids'. Valid argument type is Iterable[int].")
        if not isinstance(params, CheckTopologyParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is CheckTopologyParams.")
        args = {"part_id" : part_id,
        "topo_face_ids" : topo_face_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::AutoQuadMesher/CheckTopology"
        self._model._print_beta_api_warning("check_topology")
        self._model._print_logs_before_command("check_topology", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("check_topology", AutoQuadMesherResults(model = self._model, json_data = result))
        return AutoQuadMesherResults(model = self._model, json_data = result)
