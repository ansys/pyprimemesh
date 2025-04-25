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

class CollapseTool(CoreObject):
    """Performs various collapse operations. For example, split and collapse on face zonelets.

    Parameters
    ----------
    model : Model
        Server model to create CollapseTool object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize CollapseTool """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::CollapseTool/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for CollapseTool. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for CollapseTool. """
        command_name = "PrimeMesh::CollapseTool/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def split_and_collapse_on_zonelets(self, part_id : int, face_zonelets : Iterable[int], register_id : int, split_params : SplitParams, collapse_params : CollapseParams) -> CollapseResults:
        """ Split and collapse elements on face zonelets with the specified register id.


        Parameters
        ----------
        part_id : int
            Id of a part.
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        register_id : int
            Id used to identify face elements to split and collapse.
        split_params : SplitParams
            Parameters to split longest edge of face elements before collapse.
        collapse_params : CollapseParams
            Parameters to collapse shortest edge of face elements.

        Returns
        -------
        CollapseResults
            Returns the CollapseResults.

        Examples
        --------
        >>> collapse_tool = prime.CollapseTool(model = model)
        >>> results = collapse_tool.split_and_collapse_on_zonelets(
        >>>     part_id=part.id,
        >>>     face_zonelets=part.get_face_zonelets(),
        >>>     register_id=register_id,
        >>>     split_params=prime.SplitParams(model=model),
        >>>     collapse_params=prime.CollapseParams(model=model))

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'face_zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(register_id, int):
            raise TypeError("Invalid argument type passed for 'register_id'. Valid argument type is int.")
        if not isinstance(split_params, SplitParams):
            raise TypeError("Invalid argument type passed for 'split_params'. Valid argument type is SplitParams.")
        if not isinstance(collapse_params, CollapseParams):
            raise TypeError("Invalid argument type passed for 'collapse_params'. Valid argument type is CollapseParams.")
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "split_params" : split_params._jsonify(),
        "collapse_params" : collapse_params._jsonify()}
        command_name = "PrimeMesh::CollapseTool/SplitAndCollapseOnZonelets"
        self._model._print_logs_before_command("split_and_collapse_on_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("split_and_collapse_on_zonelets", CollapseResults(model = self._model, json_data = result))
        return CollapseResults(model = self._model, json_data = result)
