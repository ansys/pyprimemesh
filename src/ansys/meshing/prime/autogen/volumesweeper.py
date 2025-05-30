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

class VolumeSweeper(CoreObject):
    """VolumeSweeper class provide functions to volume mesh a given set of topovolumes by sweeping or stacking a set of face and edge zonelets. Provide operations to generate volume mesh using stacker technology.

    Parameters
    ----------
    model : Model
        Server model to create VolumeSweeper object.
    part_id : int
        Id of the part.
    """

    def __init__(self, model: CommunicationManager, part_id: int):
        """ Initialize VolumeSweeper  """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::VolumeSweeper/Construct"
        args = {"ModelID" : model._object_id , "PartID" : part_id, "MaxID" : -1}
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for VolumeSweeper. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for VolumeSweeper. """
        command_name = "PrimeMesh::VolumeSweeper/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def create_base_face(self, topo_volume_ids : Iterable[int], params : MeshStackerParams) -> MeshStackerResults:
        """ Creates a face at the specified origin perpendicular to the specified direction. Also, imprint model edges on the face, make necessary edge repairs, and duplicate relevant size controls on the base face.


        Parameters
        ----------
        topo_volume_ids : Iterable[int]
            Ids of volumes that need to be meshed.
        params : MeshStackerParams
            Mesh stacker parameters.

        Returns
        -------
        MeshStackerResults
            Returns the MeshStackerResults.


        Examples
        --------
        >>> results = volumesweeper.create_base_face(topo_volume_ids, params)

        """
        if not isinstance(topo_volume_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_volume_ids'. Valid argument type is Iterable[int].")
        if not isinstance(params, MeshStackerParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is MeshStackerParams.")
        args = {"topo_volume_ids" : topo_volume_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeSweeper/CreateBaseFace"
        self._model._print_logs_before_command("create_base_face", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_base_face", MeshStackerResults(model = self._model, json_data = result))
        return MeshStackerResults(model = self._model, json_data = result)

    def stack_base_face(self, base_face_ids : Iterable[int], topo_volume_ids : Iterable[int], params : MeshStackerParams) -> MeshStackerResults:
        """ Generates volume mesh stacking a meshed face layer by layer along the given direction. Calculates the stack layers using size controls and global size parameters.


        Parameters
        ----------
        base_face_ids : Iterable[int]
            Ids of base faces to be stacked
        topo_volume_ids : Iterable[int]
            Ids of volumes that need to be meshed.
        params : MeshStackerParams
            Mesh stacker parameters.

        Returns
        -------
        MeshStackerResults
            Returns the MeshStackerResults.


        Examples
        --------
        >>> results = volumesweeper.stack_base_face(base_face_ids, topo_volume_ids, params)

        """
        if not isinstance(base_face_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'base_face_ids'. Valid argument type is Iterable[int].")
        if not isinstance(topo_volume_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_volume_ids'. Valid argument type is Iterable[int].")
        if not isinstance(params, MeshStackerParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is MeshStackerParams.")
        args = {"base_face_ids" : base_face_ids,
        "topo_volume_ids" : topo_volume_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeSweeper/StackBaseFace"
        self._model._print_logs_before_command("stack_base_face", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("stack_base_face", MeshStackerResults(model = self._model, json_data = result))
        return MeshStackerResults(model = self._model, json_data = result)
