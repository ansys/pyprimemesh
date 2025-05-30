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

class Surfer(CoreObject):
    """Generates surface mesh.

    Performs surface meshing using various surface meshing algorithms on topofaces or face zonelets.
    For example, constant size or volumetric size surface meshing.

    Parameters
    ----------
    model : Model
        Server model to create Surfer object.
    part_id : int
        Id of the part.
    """

    def __init__(self, model: CommunicationManager, part_id: int):
        """ Initialize Surfer  """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::Surfer/Construct"
        args = {"ModelID" : model._object_id , "PartID" : part_id, "MaxID" : -1}
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for Surfer. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for Surfer. """
        command_name = "PrimeMesh::Surfer/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def remesh_face_zonelets(self, face_zonelets : Iterable[int], edge_zonelets : Iterable[int], params : SurferParams) -> SurferResults:
        """ Performs meshing on the given face zonelets with provided parameters.


        Parameters
        ----------
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        edge_zonelets : Iterable[int]
            Ids of edge zonelets.
        params : SurferParams
            Surfer parameters.

        Returns
        -------
        SurferResults
            Returns the SurferResults.


        Examples
        --------
        >>> results = surfer.remesh_face_zonelets(face_zonelets, edge_zonelets, params)

        """
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'face_zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(edge_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'edge_zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(params, SurferParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is SurferParams.")
        args = {"face_zonelets" : face_zonelets,
        "edge_zonelets" : edge_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Surfer/RemeshFaceZonelets"
        self._model._print_logs_before_command("remesh_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("remesh_face_zonelets", SurferResults(model = self._model, json_data = result))
        return SurferResults(model = self._model, json_data = result)

    def refacet_topo_faces(self, topo_faces : Iterable[int], params : SurferParams) -> SurferResults:
        """ Performs refaceting on the given topofaces with provided parameters.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of topofaces.
        params : SurferParams
            Surfer Parameters.

        Returns
        -------
        SurferResults
            Returns the SurferResults.


        Examples
        --------
        >>> results = surfer.RefacetTopoFaces(topo_faces, params)

        """
        if not isinstance(topo_faces, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_faces'. Valid argument type is Iterable[int].")
        if not isinstance(params, SurferParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is SurferParams.")
        args = {"topo_faces" : topo_faces,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Surfer/RefacetTopoFaces"
        self._model._print_logs_before_command("refacet_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("refacet_topo_faces", SurferResults(model = self._model, json_data = result))
        return SurferResults(model = self._model, json_data = result)

    def mesh_topo_faces(self, topo_faces : Iterable[int], params : SurferParams) -> SurferResults:
        """ Performs meshing on the given topofaces with provided parameters.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of topofaces.
        params : SurferParams
            Surfer Parameters.

        Returns
        -------
        SurferResults
            Returns the SurferResults.


        Examples
        --------
        >>> results = surfer.mesh_topo_faces(topo_faces, params)

        """
        if not isinstance(topo_faces, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_faces'. Valid argument type is Iterable[int].")
        if not isinstance(params, SurferParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is SurferParams.")
        args = {"topo_faces" : topo_faces,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Surfer/MeshTopoFaces"
        self._model._print_logs_before_command("mesh_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("mesh_topo_faces", SurferResults(model = self._model, json_data = result))
        return SurferResults(model = self._model, json_data = result)

    def initialize_surfer_params_for_wrapper(self) -> SurferParams:
        """ Initializes surfer parameters to mesh surfaces generated by wrapper.


        Returns
        -------
        SurferParams
            Returns the SurferParams initialized for wrapper inputs.


        Examples
        --------
        >>> surfer_params = surfer.initialize_surfer_params_for_wrapper()

        """
        args = {}
        command_name = "PrimeMesh::Surfer/InitializeSurferParamsForWrapper"
        self._model._print_logs_before_command("initialize_surfer_params_for_wrapper", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("initialize_surfer_params_for_wrapper", SurferParams(model = self._model, json_data = result))
        return SurferParams(model = self._model, json_data = result)

    def remesh_face_zonelets_locally(self, face_zonelets : Iterable[int], register_id : int, local_surfer_params : LocalSurferParams) -> LocalSurferResults:
        """ Remesh the given face zonelets locally at the registered faces with provided parameters.


        Parameters
        ----------
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        register_id : int
            Register id of the target faces.
        local_surfer_params : LocalSurferParams
            Local surfer Parameters.

        Returns
        -------
        LocalSurferResults
            Returns the LocalSurferResults.


        Examples
        --------
        >>> results = surfer.remesh_face_zonelets_locally(face_zonelets, register_id, local_surfer_params)

        """
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'face_zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(register_id, int):
            raise TypeError("Invalid argument type passed for 'register_id'. Valid argument type is int.")
        if not isinstance(local_surfer_params, LocalSurferParams):
            raise TypeError("Invalid argument type passed for 'local_surfer_params'. Valid argument type is LocalSurferParams.")
        args = {"face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "local_surfer_params" : local_surfer_params._jsonify()}
        command_name = "PrimeMesh::Surfer/RemeshFaceZoneletsLocally"
        self._model._print_logs_before_command("remesh_face_zonelets_locally", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("remesh_face_zonelets_locally", LocalSurferResults(model = self._model, json_data = result))
        return LocalSurferResults(model = self._model, json_data = result)

    def create_shell_bl_using_controls(self, part_id : int, shell_bl_control_ids : Iterable[int], shell_bl_params : ShellBLParams) -> CreateShellBLResults:
        """ Creates ShellBL using data stored in controls.


        Parameters
        ----------
        part_id : int
            Id of the part.
        shell_bl_control_ids : Iterable[int]
            Ids of ShellBL control.
        shell_bl_params : ShellBLParams
            Parameters related to ShellBL.

        Returns
        -------
        CreateShellBLResults
            Returns the CreateShellBLResults.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = surfer.create_shell_bl_using_controls(part_id,shell_bl_control_ids,shell_bl_params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(shell_bl_control_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'shell_bl_control_ids'. Valid argument type is Iterable[int].")
        if not isinstance(shell_bl_params, ShellBLParams):
            raise TypeError("Invalid argument type passed for 'shell_bl_params'. Valid argument type is ShellBLParams.")
        args = {"part_id" : part_id,
        "shell_bl_control_ids" : shell_bl_control_ids,
        "shell_bl_params" : shell_bl_params._jsonify()}
        command_name = "PrimeMesh::Surfer/CreateShellBLUsingControls"
        self._model._print_beta_api_warning("create_shell_bl_using_controls")
        self._model._print_logs_before_command("create_shell_bl_using_controls", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_shell_bl_using_controls", CreateShellBLResults(model = self._model, json_data = result))
        return CreateShellBLResults(model = self._model, json_data = result)
