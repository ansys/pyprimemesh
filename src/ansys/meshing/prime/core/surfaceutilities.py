"""Utilities module for surface operations."""
from ansys.meshing.prime.autogen.surfaceutilities import (
    SurfaceUtilities as _SurfaceUtilities,
)

# isort: split
from typing import Iterable

from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    AddThicknessParams as AddThicknessParams,
)
from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    AddThicknessResults as AddThicknessResults,
)
from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    CreateBOIParams as CreateBOIParams,
)
from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    CreateBOIResults as CreateBOIResults,
)
from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    CreateContactPatchParams as CreateContactPatchParams,
)
from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    CreateContactPatchResults as CreateContactPatchResults,
)
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.params.primestructs import ErrorCode as ErrorCode


class SurfaceUtilities(_SurfaceUtilities):
    """Performs various general surface utilities algorithms, such as adding thickness.

    Parameters
    ----------
    model : Model
        Server model in which to perform operations.
    """

    def __init__(self, model: Model):
        """Initialize the superclass and ``model`` variable."""
        _SurfaceUtilities.__init__(self, model)
        self._model = model

    def add_thickness(
        self, zonelets: Iterable[int], params: AddThicknessParams
    ) -> AddThicknessResults:
        """Add thicknesss to input face zonelets.

        Parameters
        ----------
        zonelets : Iterable[int]
            List of input face zonelet IDs.
        params : AddThicknessParams
            Parameters for controlling the addition of thickness.

        Returns
        -------
        AddThicknessResults
            Results for adding thickness.


        Examples
        --------
        >>> result = surf_utils.add_thickness(zonelets, params)

        """
        result = _SurfaceUtilities.add_thickness(self, zonelets, params)
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result

    def create_boi(
        self, face_zonelet_ids: Iterable[int], params: CreateBOIParams
    ) -> CreateBOIResults:
        """Create BOI to input face zonelets.

        Parameters
        ----------
        face_zonelet_ids : Iterable[int]
            List of input face zonelet IDs.
        params : CreateBOIParams
            Parameters for controlling BOI creation.

        Returns
        -------
        CreateBOIResults
            Results from creating BOI.


        Examples
        --------
        >>> result = surf_utils.create_boi(zonelets, params)

        """
        result = _SurfaceUtilities.create_boi(self, face_zonelet_ids, params)
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result

    def create_contact_patch(
        self,
        source_zonelets: Iterable[int],
        target_zonelets: Iterable[int],
        params: CreateContactPatchParams,
    ) -> CreateContactPatchResults:
        """Create a contact patch by offsetting the target zonelets.

        Parameters
        ----------
        source_zonelets : Iterable[int]
            IDS for the source face zonelets.
        target_zonelets : Iterable[int]
            IDs for the target face zonelets.
        params : CreateContactPatchParams
            Parameters for controlling the contact patch creation.

        Returns
        -------
        CreateContactPatchResults
            Results from creating the contact patch.


        Examples
        --------
        >>> result = surf_utils.create_contact_patch(zonelets, params)

        """
        result = _SurfaceUtilities.create_contact_patch(
            self, source_zonelets, target_zonelets, params
        )
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result
