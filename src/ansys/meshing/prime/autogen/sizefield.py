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

class SizeField(CoreObject):
    """The size field is computed based on the size control defined.

    You can remesh surfaces and edges based on the size field.


    Parameters
    ----------
    model : Model
        Server model to create SizeField object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize SizeField """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::SizeField/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for SizeField. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for SizeField. """
        command_name = "PrimeMesh::SizeField/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def compute_volumetric(self, size_control_ids : Iterable[int], volumetric_sizefield_params : VolumetricSizeFieldComputeParams) -> VolumetricSizeFieldComputeResults:
        """ Computes the volumetric size field using given size control ids.


        Parameters
        ----------
        size_control_ids : Iterable[int]
            Ids of size controls.

        Examples
        --------
        >>> size_field.compute_volumetric(
        >>>           [size_control.id for size_control in model.control_data.size_controls], volumetric_sizefield_params))

        """
        if not isinstance(size_control_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'size_control_ids'. Valid argument type is Iterable[int].")
        if not isinstance(volumetric_sizefield_params, VolumetricSizeFieldComputeParams):
            raise TypeError("Invalid argument type passed for 'volumetric_sizefield_params'. Valid argument type is VolumetricSizeFieldComputeParams.")
        args = {"size_control_ids" : size_control_ids,
        "volumetric_sizefield_params" : volumetric_sizefield_params._jsonify()}
        command_name = "PrimeMesh::SizeField/ComputeVolumetric"
        self._model._print_logs_before_command("compute_volumetric", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("compute_volumetric", VolumetricSizeFieldComputeResults(model = self._model, json_data = result))
        return VolumetricSizeFieldComputeResults(model = self._model, json_data = result)
