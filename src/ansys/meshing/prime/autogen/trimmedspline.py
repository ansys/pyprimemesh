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

class TrimmedSpline(CoreObject):
    """Handles creation and meshing of trimmed spline.

    Parameters
    ----------
    model : Model
        Server model to create TrimmedSpline object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize TrimmedSpline """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::TrimmedSpline/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for TrimmedSpline. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for TrimmedSpline. """
        command_name = "PrimeMesh::TrimmedSpline/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def create_trimmed_uniform_solid_spline_by_brep_mapping(self, part_id : int, spline_params : UniformSolidSplineCreationParams) -> TrimmedSplineResults:
        """ Creates uniform solid spline and maps the CAD geometry in its parametric space.


        Parameters
        ----------
        part_id : int
            Part on which the spline is to be created.
        spline_params : UniformSolidSplineCreationParams
            Parameters used to create the spline.

        Returns
        -------
        TrimmedSplineResults
            Returns the TrimmedSplineResults.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = trimmedSpline.CreateTrimmedUniformSolidSplineByBrepMapping(part_id, spline_params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(spline_params, UniformSolidSplineCreationParams):
            raise TypeError("Invalid argument type passed for 'spline_params'. Valid argument type is UniformSolidSplineCreationParams.")
        args = {"part_id" : part_id,
        "spline_params" : spline_params._jsonify()}
        command_name = "PrimeMesh::TrimmedSpline/CreateTrimmedUniformSolidSplineByBrepMapping"
        self._model._print_beta_api_warning("create_trimmed_uniform_solid_spline_by_brep_mapping")
        self._model._print_logs_before_command("create_trimmed_uniform_solid_spline_by_brep_mapping", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_trimmed_uniform_solid_spline_by_brep_mapping", TrimmedSplineResults(model = self._model, json_data = result))
        return TrimmedSplineResults(model = self._model, json_data = result)

    def create_tet_mesh_on_trimmed_solid_spline(self, part_id : int, mesh_params : TetMeshSplineParams) -> TrimmedSplineResults:
        """ Creates tetrahedral mesh on trimmed solid spline.


        Parameters
        ----------
        part_id : int
            Part on which the tetrahedral meshing is performed.
        mesh_params : TetMeshSplineParams
            Parameters to configure the meshing.

        Returns
        -------
        TrimmedSplineResults
            Returns the TrimmedSplineResults.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = trimmedSpline.CreateTetMeshOnTrimmedSolidSpline(part_id, mesh_params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(mesh_params, TetMeshSplineParams):
            raise TypeError("Invalid argument type passed for 'mesh_params'. Valid argument type is TetMeshSplineParams.")
        args = {"part_id" : part_id,
        "mesh_params" : mesh_params._jsonify()}
        command_name = "PrimeMesh::TrimmedSpline/CreateTetMeshOnTrimmedSolidSpline"
        self._model._print_beta_api_warning("create_tet_mesh_on_trimmed_solid_spline")
        self._model._print_logs_before_command("create_tet_mesh_on_trimmed_solid_spline", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_tet_mesh_on_trimmed_solid_spline", TrimmedSplineResults(model = self._model, json_data = result))
        return TrimmedSplineResults(model = self._model, json_data = result)

    def refine_tet_mesh(self, part_id : int, refine_params : RefineTetMeshParams) -> TrimmedSplineResults:
        """ Refines tetrahedral mesh.


        Parameters
        ----------
        part_id : int
            Part on which mesh refinement is performed.
        refine_params : RefineTetMeshParams
            Parameters to configure mesh refinement.

        Returns
        -------
        TrimmedSplineResults
            Returns the TrimmedSplineResults.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = trimmedSpline.RefineTetMesh(part_id, refine_params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(refine_params, RefineTetMeshParams):
            raise TypeError("Invalid argument type passed for 'refine_params'. Valid argument type is RefineTetMeshParams.")
        args = {"part_id" : part_id,
        "refine_params" : refine_params._jsonify()}
        command_name = "PrimeMesh::TrimmedSpline/RefineTetMesh"
        self._model._print_beta_api_warning("refine_tet_mesh")
        self._model._print_logs_before_command("refine_tet_mesh", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("refine_tet_mesh", TrimmedSplineResults(model = self._model, json_data = result))
        return TrimmedSplineResults(model = self._model, json_data = result)
