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
        Model to apply the operations to.
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
