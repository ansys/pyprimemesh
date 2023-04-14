from ansys.meshing.prime.autogen.volumesweeper import VolumeSweeper as _Sweeper

# isort: split
from typing import Iterable

from ansys.meshing.prime.autogen.volumesweeperstructs import (
    MeshStackerParams,
    MeshStackerResults,
)
from ansys.meshing.prime.core.model import Model


class VolumeSweeper(_Sweeper):

    """VolumeSweeper class provide functions to volume mesh a given set of topovolumes by sweeping
    or stacking a set of face and edge zonelets.
    Provide operations to generate volume mesh using stacker technology."""

    __doc__ = _Sweeper.__doc__

    def __init__(self, model: Model):
        """__init__(Sweeper self, Model model)"""
        self._model = model

    def create_base_face(
        self, part_id: int, topo_volume_ids: Iterable[int], params: MeshStackerParams
    ) -> MeshStackerResults:
        """Creates a face at the specified origin and perpendicular to the specified direction.
        Also, imprint model edges on the face, make necessary edge repairs, and duplicate relevant
        size controls on the base face.


        Parameters
        ----------
        part_id : int
            Id of part.
        topo_volume_ids : Iterable[int]
            Ids of volumes that need to be meshed.
        params : MeshStackerParams
            Mesh stacker parameters.

        Returns
        -------
        MeshStackerResults
            Returns the MeshStackerResults.


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
        """Generate volume mesh stacking a meshed face, layer by layer, along the given
        direction. Calculates the stack layers using size controls and global size parameters.


        Parameters
        ----------
        part_id : int
            Id of part.
        base_face_ids: Iterable[int]
            Ids of base faces to be stacked.
        topo_volume_ids : Iterable[int]
            Ids of volumes that need to be meshed.
        params : MeshStackerParams
            Mesh stacker parameters.

        Returns
        -------
        MeshStackerResults
            Returns the MeshStackerResults.


        Examples
        --------
        >>> results = volumesweeper.stack_base_face(part_id, base_face_ids, topo_volume_ids, params)

        """
        with _Sweeper(model=self._model, part_id=part_id) as sweeper:
            return sweeper.stack_base_face(base_face_ids, topo_volume_ids, params)
