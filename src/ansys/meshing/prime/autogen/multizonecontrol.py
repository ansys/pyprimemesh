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

class MultiZoneControl(CoreObject):
    """MultiZoneControl provides a way to gather all the information required for MultiZone meshing.

    The MultiZone meshing provides hex meshing capabilities.
    Different type of mesh can be generated using MultiZoneControl. For example, sweep mesh, map mesh and edge biased mesh.

    Parameters
    ----------
    model : Model
        Server model to create MultiZoneControl object.
    id : int
        Id of the MultiZoneControl.
    object_id : int
        Object id of the MultiZoneControl.
    name : str
        Name of the MultiZoneControl.
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize MultiZoneControl """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def set_volume_scope(self, scope_info : ScopeDefinition):
        """ Sets the scope for volume in terms of topovolumes.The topovolumes given by the scope are imported by MultiZone to generate MultiZone mesh on it.


        Parameters
        ----------
        scope_info : ScopeDefinition
            Scoped topovolumes.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> multizone_control.set_volume_scope(scope_info)

        """
        if not isinstance(scope_info, ScopeDefinition):
            raise TypeError("Invalid argument type passed for 'scope_info'. Valid argument type is ScopeDefinition.")
        args = {"scope_info" : scope_info._jsonify()}
        command_name = "PrimeMesh::MultiZoneControl/SetVolumeScope"
        self._model._print_beta_api_warning("set_volume_scope")
        self._model._print_logs_before_command("set_volume_scope", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_volume_scope")

    def set_surface_scope(self, scope_info : ScopeDefinition):
        """ Sets the scope for surface in terms of topofaces.


        Parameters
        ----------
        scope_info : ScopeDefinition
            Scoped topofaces.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> multizone_control.set_surface_scope(scope_info)

        """
        if not isinstance(scope_info, ScopeDefinition):
            raise TypeError("Invalid argument type passed for 'scope_info'. Valid argument type is ScopeDefinition.")
        args = {"scope_info" : scope_info._jsonify()}
        command_name = "PrimeMesh::MultiZoneControl/SetSurfaceScope"
        self._model._print_beta_api_warning("set_surface_scope")
        self._model._print_logs_before_command("set_surface_scope", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_surface_scope")

    def set_map_mesh_params(self, scope_info : MultiZoneMapMeshParams):
        """ Set the parameters for map meshing in terms of topofaces during MultiZone mesh.


        Parameters
        ----------
        scope_info : MultiZoneMapMeshParams
            Scoped topofaces to be map meshed.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> multizone_control.set_map_mesh_params(scope_info)

        """
        if not isinstance(scope_info, MultiZoneMapMeshParams):
            raise TypeError("Invalid argument type passed for 'scope_info'. Valid argument type is MultiZoneMapMeshParams.")
        args = {"scope_info" : scope_info._jsonify()}
        command_name = "PrimeMesh::MultiZoneControl/SetMapMeshParams"
        self._model._print_beta_api_warning("set_map_mesh_params")
        self._model._print_logs_before_command("set_map_mesh_params", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_map_mesh_params")

    def set_sweep_mesh_params(self, scope_info : MultiZoneSweepMeshParams):
        """ Set the parameters for sweep meshing in terms of topofaces during MultiZone mesh.


        Parameters
        ----------
        scope_info : MultiZoneSweepMeshParams
            Information required for sweep meshing.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> multizone_control.set_sweep_mesh_params(scope_info)

        """
        if not isinstance(scope_info, MultiZoneSweepMeshParams):
            raise TypeError("Invalid argument type passed for 'scope_info'. Valid argument type is MultiZoneSweepMeshParams.")
        args = {"scope_info" : scope_info._jsonify()}
        command_name = "PrimeMesh::MultiZoneControl/SetSweepMeshParams"
        self._model._print_beta_api_warning("set_sweep_mesh_params")
        self._model._print_logs_before_command("set_sweep_mesh_params", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_sweep_mesh_params")

    def set_edge_biasing_params(self, scope_info : MultiZoneEdgeBiasingParams):
        """ Sets the parameters for edge biasing in terms of topoedges and topofaces during MultiZone mesh.


        Parameters
        ----------
        scope_info : MultiZoneEdgeBiasingParams
            Information for edge biasing in MultiZone meshing.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> multizone_control.set_edge_biasing_params(scope_info)

        """
        if not isinstance(scope_info, MultiZoneEdgeBiasingParams):
            raise TypeError("Invalid argument type passed for 'scope_info'. Valid argument type is MultiZoneEdgeBiasingParams.")
        args = {"scope_info" : scope_info._jsonify()}
        command_name = "PrimeMesh::MultiZoneControl/SetEdgeBiasingParams"
        self._model._print_beta_api_warning("set_edge_biasing_params")
        self._model._print_logs_before_command("set_edge_biasing_params", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_edge_biasing_params")

    def set_multi_zone_sizing_params(self, params : MultiZoneSizingParams):
        """ Sets the MultiZone parameters.


        Parameters
        ----------
        params : MultiZoneSizingParams
            Parameters required for MultiZone mesh.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> multizone_control.set_multi_zone_params(params)

        """
        if not isinstance(params, MultiZoneSizingParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is MultiZoneSizingParams.")
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::MultiZoneControl/SetMultiZoneSizingParams"
        self._model._print_beta_api_warning("set_multi_zone_sizing_params")
        self._model._print_logs_before_command("set_multi_zone_sizing_params", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_multi_zone_sizing_params")

    @property
    def id(self):
        """ Get the id of MultiZoneControl."""
        return self._id

    @property
    def name(self):
        """ Get the name of MultiZoneControl."""
        return self._name
