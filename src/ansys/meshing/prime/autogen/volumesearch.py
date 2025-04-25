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

class VolumeSearch(CoreObject):
    """VolumeSearch allows you to check volume mesh quality.

    VolumeSearch performs volume mesh quality check based on different cell quality measures.


    Parameters
    ----------
    model : Model
        Server model to create VolumeSearch object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize VolumeSearch """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::VolumeSearch/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for VolumeSearch. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for VolumeSearch. """
        command_name = "PrimeMesh::VolumeSearch/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def get_volume_quality_summary(self, params : VolumeQualitySummaryParams) -> VolumeQualitySummaryResults:
        """ Gets the volume quality summary.

        Diagnose volume quality for the given scope and cell quality measures provided in the VolumeQualitySummaryParams structure.
        Use default quality limit if the parameters are not specified.

        Parameters
        ----------
        params : VolumeQualitySummaryParams
            Volume quality summary parameters.

        Returns
        -------
        VolumeQualitySummaryResults
            Returns the VolumeQualitySummaryResults.

        Examples
        --------
        >>> vol_search = VolumeSearch(model=model)
        >>> results = vol_search.get_volume_quality_summary(VolumeQualitySummaryParams(model=model))

        """
        if not isinstance(params, VolumeQualitySummaryParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is VolumeQualitySummaryParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeSearch/GetVolumeQualitySummary"
        self._model._print_logs_before_command("get_volume_quality_summary", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volume_quality_summary", VolumeQualitySummaryResults(model = self._model, json_data = result))
        return VolumeQualitySummaryResults(model = self._model, json_data = result)
