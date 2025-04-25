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

class BoundaryFittedSpline(CoreObject):
    """BoundaryFittedSpline helps you to create splines for structured hex-mesh model.

    BoundaryFittedSpline allows you to perform H and P refinement.

    Parameters
    ----------
    model : Model
        Server model to create BoundaryFittedSpline object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize BoundaryFittedSpline """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::BoundaryFittedSpline/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for BoundaryFittedSpline. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for BoundaryFittedSpline. """
        command_name = "PrimeMesh::BoundaryFittedSpline/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def create_boundary_fitted_spline(self, part_id : int, cell_zonelet_ids : Iterable[int], boundary_fitted_spline_params : BoundaryFittedSplineParams) -> IGAResults:
        """ Create boundary fitted spline for structured hex-mesh.

        The hex-mesh can be structured in blocks but must be conformally connected.
        That is, each block must have six sided volume and must be connected to other blocks through unique face.
        The degree and number of control points of the spline can be set in the fitting parameter structure.

        Parameters
        ----------
        part_id : int
            Id of the part.
        cell_zonelet_ids : Iterable[int]
            Ids of the cell zonelets on which spline will be fit.
        boundary_fitted_spline_params : BoundaryFittedSplineParams
            Structure containing spline fitting parameters.

        Returns
        -------
        IGAResults
            Returns the IGAResults.


        Examples
        --------
        >>> from ansys.meshing.prime import BoundaryFittedSpline
        >>> #connect client to server and get model from it
        >>> client = Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> boundary_fitted_spline = BoundaryFittedSpline(model = model)
        >>> results = boundary_fitted_spline.create_boundary_fitted_spline(part_id, cell_zonelet_ids, boundary_fitted_spline_params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(cell_zonelet_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'cell_zonelet_ids'. Valid argument type is Iterable[int].")
        if not isinstance(boundary_fitted_spline_params, BoundaryFittedSplineParams):
            raise TypeError("Invalid argument type passed for 'boundary_fitted_spline_params'. Valid argument type is BoundaryFittedSplineParams.")
        args = {"part_id" : part_id,
        "cell_zonelet_ids" : cell_zonelet_ids,
        "boundary_fitted_spline_params" : boundary_fitted_spline_params._jsonify()}
        command_name = "PrimeMesh::BoundaryFittedSpline/CreateBoundaryFittedSpline"
        self._model._print_logs_before_command("create_boundary_fitted_spline", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_boundary_fitted_spline", IGAResults(model = self._model, json_data = result))
        return IGAResults(model = self._model, json_data = result)

    def refine_spline(self, part_id : int, spline_ids : Iterable[int], refine_spline_params : RefineSplineParams) -> IGAResults:
        """ Refine boundary fitted splines.

        Now H and P refinement are supported.
        Refinement along one or more dimension can be suppressed using refinement parameters in the input.

        Parameters
        ----------
        part_id : int
            Id of the part.
        spline_ids : Iterable[int]
            Ids of the splines on which refinement is performed.
        refine_spline_params : RefineSplineParams
            Structure containing parameters for spline refinement.

        Returns
        -------
        IGAResults
            Returns the IGAResults Structure.


        Examples
        --------
        >>> from ansys.meshing.prime import BoundaryFittedSpline
        >>> #connect client to server and get model from it
        >>> client = Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> boundary_fitted_spline = BoundaryFittedSpline(model = model)
        >>> results = boundary_fitted_spline.refine_spline(part_id, spline_ids, refine_spline_params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(spline_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'spline_ids'. Valid argument type is Iterable[int].")
        if not isinstance(refine_spline_params, RefineSplineParams):
            raise TypeError("Invalid argument type passed for 'refine_spline_params'. Valid argument type is RefineSplineParams.")
        args = {"part_id" : part_id,
        "spline_ids" : spline_ids,
        "refine_spline_params" : refine_spline_params._jsonify()}
        command_name = "PrimeMesh::BoundaryFittedSpline/RefineSpline"
        self._model._print_logs_before_command("refine_spline", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("refine_spline", IGAResults(model = self._model, json_data = result))
        return IGAResults(model = self._model, json_data = result)
