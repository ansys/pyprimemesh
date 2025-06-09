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

"""Module for volume sweeper operations."""
from ansys.meshing.prime.autogen.volumesweeper import VolumeSweeper as _Sweeper

# isort: split
from typing import Iterable

from ansys.meshing.prime.autogen.volumesweeperstructs import (
    MeshStackerParams,
    MeshStackerResults,
)
from ansys.meshing.prime.core.model import Model


class VolumeSweeper(_Sweeper):
    """Provides operations to generate volume meshes using stacker technology.

    TopoVolumes are volume meshed by sweeping or stacking a set of face
    and edge zonelets.

    Parameters
    ----------
    model : Model
        Server model to create VolumeSweeper object.
    """

    __doc__ = _Sweeper.__doc__

    def __init__(self, model: Model):
        """Initialize the model in the volume sweeper."""
        self._model = model

    def create_base_face(
        self, part_id: int, topo_volume_ids: Iterable[int], params: MeshStackerParams
    ) -> MeshStackerResults:
        """Create a face at the specified origin.

        This method creates a face at the specified origin and perpendicular to the
        specified direction. Also, it imprints model edges on the face, makes necessary
        edge repairs, and duplicates relevant size controls on the base face.


        Parameters
        ----------
        part_id : int
            ID of part.
        topo_volume_ids : Iterable[int]
            IDs of the volumes to mesh.
        params : MeshStackerParams
            Mesh stacker parameters.

        Returns
        -------
        MeshStackerResults
            Results from creating the face.


        Examples
        --------
        >>> results = volumesweeper.create_base_face(part_id, topo_volume_ids, params)

        """
        with _Sweeper(model=self._model, part_id=part_id) as sweeper:
            return sweeper.create_base_face(topo_volume_ids, params)

    def stack_base_face(
        self,
        part_id: int,
        base_face_ids: Iterable[int],
        topo_volume_ids: Iterable[int],
        params: MeshStackerParams,
    ) -> MeshStackerResults:
        """Generate volume mesh by stacking a meshed face.

        This method generates volume mesh by stacking a meshed face, layer by layer, along
        the given direction. It calculates the stack layers using size controls and global
        size parameters.


        Parameters
        ----------
        part_id : int
            ID of the part.
        base_face_ids: Iterable[int]
            IDs of the base faces to stack.
        topo_volume_ids : Iterable[int]
            IDs of the volumes to mesh.
        params : MeshStackerParams
            Mesh stacker parameters.

        Returns
        -------
        MeshStackerResults
            Results from generating the volume mesh.


        Examples
        --------
        >>> results = volumesweeper.stack_base_face(part_id, base_face_ids, topo_volume_ids, params)

        """
        with _Sweeper(model=self._model, part_id=part_id) as sweeper:
            return sweeper.stack_base_face(base_face_ids, topo_volume_ids, params)
