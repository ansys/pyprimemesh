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

class DeleteTool(CoreObject):
    """Performs various delete operation. For example, delete fringes and overlapping faces.

    Parameters
    ----------
    model : Model
        Server model to create DeleteTool object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize DeleteTool """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::DeleteTool/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for DeleteTool. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for DeleteTool. """
        command_name = "PrimeMesh::DeleteTool/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def delete_fringes_and_overlaps_on_zonelets(self, part_id : int, face_zonelets : Iterable[int], params : DeleteFringesAndOverlapsParams) -> DeleteFringesAndOverlapsResults:
        """ Deletes fringes and overlapping faces on the given face zonelets.


        Parameters
        ----------
        part_id : int
            Id of a part.
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        params : DeleteFringesAndOverlapsParams
            Parameters to delete the fringes and overlapping faces.

        Returns
        -------
        DeleteFringesAndOverlapsResults
            Returns the DeleteFringesAndOverlapsResults.

        Examples
        --------
        >>> delete_tool = prime.DeleteTool(model = model)
        >>> results = delete_tool.delete_fringes_and_overlaps_on_zonelets(
        >>>                                    part.id,
        >>>                                    part.get_face_zonelets(),
        >>>                                    prime.DeleteFringesAndOverlapsParams(
        >>>                                       model=model))

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'face_zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(params, DeleteFringesAndOverlapsParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is DeleteFringesAndOverlapsParams.")
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::DeleteTool/DeleteFringesAndOverlapsOnZonelets"
        self._model._print_logs_before_command("delete_fringes_and_overlaps_on_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("delete_fringes_and_overlaps_on_zonelets", DeleteFringesAndOverlapsResults(model = self._model, json_data = result))
        return DeleteFringesAndOverlapsResults(model = self._model, json_data = result)
