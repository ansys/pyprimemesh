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

class AutoMesh(CoreObject):
    """Generates volume mesh.

    Performs volume meshing using various volume meshing algorithms.
    For example, with prisms.

    Parameters
    ----------
    model : Model
        Server model to create AutoMesh object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize AutoMesh """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::AutoMesh/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for AutoMesh. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for AutoMesh. """
        command_name = "PrimeMesh::AutoMesh/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def mesh(self, part_id : int, automesh_params : AutoMeshParams) -> AutoMeshResults:
        """ Performs volume meshing on the part with the given meshing parameters.


        Parameters
        ----------
        part_id : int
            Id of the part.
        automesh_params : AutoMeshParams
            Parameters for auto mesh.

        Returns
        -------
        AutoMeshResults
            Returns the AutomeshResults.


        Examples
        --------
        >>> auto_mesh = AutoMesh(model = model)
        >>> automesh_params = AutoMeshParams(model = model)
        >>> results = auto_mesh.mesh(part_id, automesh_params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(automesh_params, AutoMeshParams):
            raise TypeError("Invalid argument type passed for 'automesh_params'. Valid argument type is AutoMeshParams.")
        args = {"part_id" : part_id,
        "automesh_params" : automesh_params._jsonify()}
        command_name = "PrimeMesh::AutoMesh/Mesh"
        self._model._print_logs_before_command("mesh", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("mesh", AutoMeshResults(model = self._model, json_data = result))
        return AutoMeshResults(model = self._model, json_data = result)
