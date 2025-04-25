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

class TopoUtilities(CoreObject):
    """Performs various general topology utility algorithms. For example, fill hole.

    Parameters
    ----------
    model : Model
        Server model to create TopoUtilities object.
    part_id : int
        Id of the part.
    """

    def __init__(self, model: CommunicationManager, part_id: int):
        """ Initialize TopoUtilities  """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::TopoUtilities/Construct"
        args = {"ModelID" : model._object_id , "PartID" : part_id, "MaxID" : -1}
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for TopoUtilities. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for TopoUtilities. """
        command_name = "PrimeMesh::TopoUtilities/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def fill_hole(self, topo_edges : Iterable[int], params : TopoFillHoleParams) -> TopoFillHoleResult:
        """ Fill holes bounded by given topoedges.


        Parameters
        ----------
        topo_edges : Iterable[int]
            Ids of topoedges to be used to find holes.
        params : TopoFillHoleParams
            Parameters to fill holes.

        Returns
        -------
        TopoFillHoleResult
            Return the TopoFillHoleResult.


        Examples
        --------
        >>> results = topo_utils.fill_hole(topo_edges, params)

        """
        if not isinstance(topo_edges, Iterable):
            raise TypeError("Invalid argument type passed for 'topo_edges'. Valid argument type is Iterable[int].")
        if not isinstance(params, TopoFillHoleParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is TopoFillHoleParams.")
        args = {"topo_edges" : topo_edges,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::TopoUtilities/FillHole"
        self._model._print_logs_before_command("fill_hole", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("fill_hole", TopoFillHoleResult(model = self._model, json_data = result))
        return TopoFillHoleResult(model = self._model, json_data = result)
