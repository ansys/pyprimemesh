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

class Transform(CoreObject):
    """Provides functionalities to initialize and manage transformation using transformation matrix.

    Parameters
    ----------
    model : Model
        Server model to create Transform object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize Transform """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::Transform/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for Transform. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for Transform. """
        command_name = "PrimeMesh::Transform/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def transform_zonelets(self, part_id : int, zonelets : Iterable[int], params : TransformParams) -> TransformResults:
        """ Transforms given zonelets using provided transform parameters.


        Parameters
        ----------
        part_id : int
            Part id of zonelets to be transformed.
        zonelets : Iterable[int]
            Ids of zonelets.
        params : TransformParams
            Transform parameters.

        Returns
        -------
        TransformResults
            Returns the transform results.


        Examples
        --------
        >>> params = prime.TransformParams(model=model)
        >>> # scale by a factor of 2 using a 4x4 transformation matrix
        >>> params.transformation_matrix = [
        >>>    2, 0, 0, 0,
        >>>    0, 2, 0, 0,
        >>>    0, 0, 2, 0,
        >>>    0, 0, 0, 1,
        >>> ]
        >>> part = model.get_part_by_name("part_name")
        >>> zonelets = part.get_face_zonelets()
        >>> result = prime.SurfaceUtilities(model).transform_zonelets(part.id, zonelets, params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(params, TransformParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is TransformParams.")
        args = {"part_id" : part_id,
        "zonelets" : zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Transform/TransformZonelets"
        self._model._print_logs_before_command("transform_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("transform_zonelets", TransformResults(model = self._model, json_data = result))
        return TransformResults(model = self._model, json_data = result)
