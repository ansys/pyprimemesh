# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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
from typing import Dict, Any, Union, List, Iterable

class Wrapper(CoreObject):
    """Provide operations to generate surface mesh using wrapper technology.

    Parameters
    ----------
    model : Model
        Server model to create Wrapper object.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize Wrapper """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::Wrapper/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for Wrapper. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for Wrapper. """
        command_name = "PrimeMesh::Wrapper/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def wrap(self, wrapper_control_id : int, params : WrapParams) -> WrapResult:
        """ Performs wrapping with specified controls in wrapper control and with provided parameters.


        Parameters
        ----------
        wrapper_control_id : int
            Id of wrapper control.
        params : WrapParams
            Wrap parameters.

        Returns
        -------
        WrapResult
            Returns the WrapResult.


        Examples
        --------
        >>> results = wrapper.wrap(wrapper_control_id, params)

        """
        if not isinstance(wrapper_control_id, int):
            raise TypeError("Invalid argument type passed for 'wrapper_control_id'. Valid argument type is int.")
        if type(params).__name__ != 'WrapParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is WrapParams.")
        args = {"wrapper_control_id" : wrapper_control_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Wrapper/Wrap"
        self._model._print_logs_before_command("wrap", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("wrap", WrapResult(model = self._model, json_data = result))
        return WrapResult(model = self._model, json_data = result)

    def improve_quality(self, part_id : int, params : WrapperImproveQualityParams) -> WrapperImproveResult:
        """ Improves the surface quality and resolves connectivity issues like intersections, multi, free, spikes, point contacts and so on.


        Parameters
        ----------
        part_id : int
            Id of the part.
        params : WrapperImproveQualityParams
            Wrapper improve quality parameters.

        Returns
        -------
        WrapperImproveResult
            Returns the WrapperImproveResult structure.


        Examples
        --------
        >>> result = wrapper.improve_quality(part_id, params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if type(params).__name__ != 'WrapperImproveQualityParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is WrapperImproveQualityParams.")
        args = {"part_id" : part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Wrapper/ImproveQuality"
        self._model._print_logs_before_command("improve_quality", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("improve_quality", WrapperImproveResult(model = self._model, json_data = result))
        return WrapperImproveResult(model = self._model, json_data = result)

    def close_gaps(self, scope : ScopeDefinition, params : WrapperCloseGapsParams) -> WrapperCloseGapsResult:
        """ Closes gaps and creates patching surfaces within the face zonelets specified by scope using gap size.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition of face zonelets.
        params : WrapperCloseGapsParams
            Wrapper close gaps parameters.

        Returns
        -------
        WrapperCloseGapsResult
            Returns the WrapperCloseGapsResult.


        Examples
        --------
        >>> result = wrapper.close_gaps(scope, params)

        """
        if type(scope).__name__ != 'ScopeDefinition':
            raise TypeError("Invalid argument type passed for 'scope'. Valid argument type is ScopeDefinition.")
        if type(params).__name__ != 'WrapperCloseGapsParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is WrapperCloseGapsParams.")
        args = {"scope" : scope._jsonify(),
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Wrapper/CloseGaps"
        self._model._print_logs_before_command("close_gaps", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("close_gaps", WrapperCloseGapsResult(model = self._model, json_data = result))
        return WrapperCloseGapsResult(model = self._model, json_data = result)

    def patch_flow_regions(self, live_material_point : str, params : WrapperPatchFlowRegionsParams) -> WrapperPatchFlowRegionsResult:
        """ Patches flow regions and creates patching surfaces for regions identified by dead regions from wrapper patch holes parameters.


        Parameters
        ----------
        live_material_point : str
            Name of live material point.
        params : WrapperPatchFlowRegionsParams
            Parameters to define patch flow regions operation.

        Returns
        -------
        WrapperPatchFlowRegionsResult
            Returns the WrapperPatchFlowRegionsResult.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = wrapper.patch_flow_regions(live_material_point, params)

        """
        if not isinstance(live_material_point, str):
            raise TypeError("Invalid argument type passed for 'live_material_point'. Valid argument type is str.")
        if type(params).__name__ != 'WrapperPatchFlowRegionsParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is WrapperPatchFlowRegionsParams.")
        args = {"live_material_point" : live_material_point,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Wrapper/PatchFlowRegions"
        self._model._print_beta_api_warning("patch_flow_regions")
        self._model._print_logs_before_command("patch_flow_regions", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("patch_flow_regions", WrapperPatchFlowRegionsResult(model = self._model, json_data = result))
        return WrapperPatchFlowRegionsResult(model = self._model, json_data = result)

    def replace_surface_with_seeded_surface(self, wrapper_part_id :  int, face_zonelets_to_replace : Iterable[int], seed_face_zonelets : Iterable[int]):
        """ Replaces the specified face zonelets on a wrapper part with the seeded surface.


        Parameters
        ----------
        wrapper_part_id :  int
            Id of the wrapper part.
        face_zonelets_to_replace : Iterable[int]
            Face zonelet ids to replace.
        seed_face_zonelets : Iterable[int]
            Face zonelet ids that define the seeded surface.

        Examples
        --------
        >>> wrapper.replace_surface_with_seeded_surface(wrapper_part_id, face_zonelets_to_replace, seed_face_zonelets)

        """
        if not isinstance(wrapper_part_id,  int):
            raise TypeError("Invalid argument type passed for 'wrapper_part_id'. Valid argument type is  int.")
        if not isinstance(face_zonelets_to_replace, Iterable):
            raise TypeError("Invalid argument type passed for 'face_zonelets_to_replace'. Valid argument type is Iterable[int].")
        if not isinstance(seed_face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'seed_face_zonelets'. Valid argument type is Iterable[int].")
        args = {"wrapper_part_id" : wrapper_part_id,
        "face_zonelets_to_replace" : face_zonelets_to_replace,
        "seed_face_zonelets" : seed_face_zonelets}
        command_name = "PrimeMesh::Wrapper/ReplaceSurfaceWithSeededSurface"
        self._model._print_logs_before_command("replace_surface_with_seeded_surface", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("replace_surface_with_seeded_surface")

    def update_seeded_surface(self, wrapper_control_id : int, params : UpdateSeededSurfaceParams):
        """ Updates the seeded surface on the wrapper part using the seeded scope defined in the wrapper control.


        Parameters
        ----------
        wrapper_control_id : int
            Id of wrapper control.
        params : UpdateSeededSurfaceParams
            Parameters to update seeded surface.

        Examples
        --------
        >>> wrapper.update_seeded_surface(wrapper_control_id, params)

        """
        if not isinstance(wrapper_control_id, int):
            raise TypeError("Invalid argument type passed for 'wrapper_control_id'. Valid argument type is int.")
        if type(params).__name__ != 'UpdateSeededSurfaceParams':
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is UpdateSeededSurfaceParams.")
        args = {"wrapper_control_id" : wrapper_control_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Wrapper/UpdateSeededSurface"
        self._model._print_logs_before_command("update_seeded_surface", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("update_seeded_surface")
