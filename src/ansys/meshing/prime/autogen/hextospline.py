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

class HexToSpline(CoreObject):
    """Converts all-hex mesh to spline.

    Parameters
    ----------
    model : Model
        Server model to create HexToSpline object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize HexToSpline """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::HexToSpline/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for HexToSpline. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for HexToSpline. """
        command_name = "PrimeMesh::HexToSpline/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def convert_hex_to_spline(self, input_scope : ScopeDefinition, hex_to_spline_params : HexToSplineParams) -> IGAResults:
        """ Converts fully hex mesh with topology to spline.


        Parameters
        ----------
        input_scope : ScopeDefinition
            Scope definition for input hex mesh.
        hex_to_spline_params : HexToSplineParams
            Parameters to convert hex to spline.

        Returns
        -------
        IGAResults
            Returns the IGAResults structure.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = hexToSpline.ConvertHexToSpline(input_scope, hex_to_spline_params)

        """
        if not isinstance(input_scope, ScopeDefinition):
            raise TypeError("Invalid argument type passed for 'input_scope'. Valid argument type is ScopeDefinition.")
        if not isinstance(hex_to_spline_params, HexToSplineParams):
            raise TypeError("Invalid argument type passed for 'hex_to_spline_params'. Valid argument type is HexToSplineParams.")
        args = {"input_scope" : input_scope._jsonify(),
        "hex_to_spline_params" : hex_to_spline_params._jsonify()}
        command_name = "PrimeMesh::HexToSpline/ConvertHexToSpline"
        self._model._print_beta_api_warning("convert_hex_to_spline")
        self._model._print_logs_before_command("convert_hex_to_spline", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("convert_hex_to_spline", IGAResults(model = self._model, json_data = result))
        return IGAResults(model = self._model, json_data = result)
