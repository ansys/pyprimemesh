# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
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

"""Module for surfer data."""
from typing import Iterable

# isort: split
from ansys.meshing.prime.autogen.surfer import Surfer as _Surfer

# isort: split
from ansys.meshing.prime.autogen.coreobject import CoreObject
from ansys.meshing.prime.autogen.surferstructs import (
    CreateShellBLResults,
    LocalSurferParams,
    LocalSurferResults,
    ShellBLParams,
    SurferParams,
    SurferResults,
)
from ansys.meshing.prime.core.model import Model


class Surfer(CoreObject):
    """Generates surface mesh.

    Performs surface meshing using various surface meshing algorithms on topofaces or face zonelets.
    For example, constant size or volumetric size surface meshing.

    Parameters
    ----------
    model : Model
        Server model to create Surfer object.
    """

    __doc__ = _Surfer.__doc__

    def __init__(self, model: Model):
        """Initialize a surfer instance."""
        self._model = model

    def mesh_topo_faces(
        self, part_id: int, topo_faces: Iterable[int], params: SurferParams
    ) -> SurferResults:
        """Perform meshing on TopoFaces with given parameters.

        Parameters
        ----------
        part_id : int
            ID of part.
        topo_faces : Iterable[int]
            IDs of the TopoFaces.
        params : SurferParams
            Surfer parameters.

        Returns
        -------
        SurferResults
            Results from performing meshing on the TopoFaces.

        Examples
        --------
        >>> surfer = prime.Surfer(model)
        >>> surfer_params = prime.SurferParams(model)
        >>> results = surfer.mesh_topo_faces(part_id, topo_faces, surfer_params)

        """
        with _Surfer(model=self._model, part_id=part_id) as surfer:
            return surfer.mesh_topo_faces(topo_faces, params)

    def create_shell_bl_using_controls(
        self, part_id: int, shell_bl_control_ids: Iterable[int], shell_bl_params: ShellBLParams
    ) -> CreateShellBLResults:
        """Create ShellBL using data stored in controls.

        Parameters
        ----------
        part_id : int
            Id of the part.
        shell_bl_control_ids : Iterable[int]
            Ids of ShellBL control.
        shell_bl_params : ShellBLParams
            Parameters related to ShellBL.

        Returns
        -------
        CreateShellBLResults
            Returns the CreateShellBLResults.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = surfer.create_shell_bl_using_controls(part_id,
                                                            shell_bl_control_ids,
                                                            shell_bl_params)

        """
        with _Surfer(model=self._model, part_id=part_id) as surfer:
            return surfer.create_shell_bl_using_controls(
                part_id, shell_bl_control_ids, shell_bl_params
            )

    def remesh_face_zonelets_locally(
        self,
        part_id: int,
        face_zonelets: Iterable[int],
        register_id: int,
        local_surfer_params: LocalSurferParams,
    ) -> LocalSurferResults:
        """Remesh face zonelets locally at the registered faces with given parameters.

        Parameters
        ----------
        part_id : int
            ID of part.
        face_zonelets : Iterable[int]
            IDs of the face zonelets.
        register_id : int
            Register ID of the target faces.
        local_surfer_params : LocalSurferParams
            Local surfer parameters.

        Returns
        -------
        LocalSurferResults
            Results from remeshing the face zonelets.

        Examples
        --------
        >>> surfer = prime.Surfer(model)
        >>> local_surfer_params = prime.LocalSurferParams(model)
        >>> results = surfer.remesh_face_zonelets_locally(part_id,
                        face_zonelets, register_id, local_surfer_params)

        """
        with _Surfer(model=self._model, part_id=part_id) as surfer:
            return surfer.remesh_face_zonelets_locally(
                face_zonelets, register_id, local_surfer_params
            )

    def remesh_face_zonelets(
        self,
        part_id: int,
        face_zonelets: Iterable[int],
        edge_zonelets: Iterable[int],
        params: SurferParams,
    ) -> SurferResults:
        """Perform meshing on face zonelets with given parameters.

        Parameters
        ----------
        part_id : int
            ID of part.
        face_zonelets : Iterable[int]
            IDs of the face zonelets.
        edge_zonelets : Iterable[int]
            IDs of the edge zonelets.
        params : SurferParams
            Surfer parameters.

        Returns
        -------
        SurferResults
            Results from meshing the face zonelets.

        Examples
        --------
        >>> surfer = prime.Surfer(model)
        >>> surfer_params = prime.SurferParams(model)
        >>> results = surfer.remesh_face_zonelets(part_id,
                        face_zonelets, edge_zonelets, surfer_params)

        """
        with _Surfer(model=self._model, part_id=part_id) as surfer:
            return surfer.remesh_face_zonelets(face_zonelets, edge_zonelets, params)

    def initialize_surfer_params_for_wrapper(self) -> SurferParams:
        """Initialize surfer parameters to mesh surfaces generated by the wrapper.

        Returns
        -------
        SurferParams
            Surfer parameters initialized for wrapper inputs.

        Examples
        --------
        >>> surfer = prime.Surfer(model)
        >>> surfer_params = surfer.initialize_surfer_params_for_wrapper()

        """
        with _Surfer(model=self._model, part_id=-1) as surfer:
            return surfer.initialize_surfer_params_for_wrapper()

    def __enter__(self):
        """Run initializing context manager."""
        return self

    def __exit__(self, type, value, traceback):
        """Run when closing the context manager."""
        pass
