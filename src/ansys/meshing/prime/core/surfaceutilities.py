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
    """Performs various general surface utilities algorithms. For example, add thickness.

    Parameters
    ----------
    model : Model
        Server model in which to perform the operations.
    """

    def __init__(self, model: Model):
        """Initialize the superclass and Model variable."""
        _SurfaceUtilities.__init__(self, model)
        self._model = model

    def add_thickness(
        self, zonelets: Iterable[int], params: AddThicknessParams
    ) -> AddThicknessResults:
        """Thickens the selected list of face zonelet ids.

        Parameters
        ----------
        zonelets : Iterable[int]
            List of input face zonelet ids.
        params : AddThicknessParams
            Parameters to control the add thickness operation.

        Returns
        -------
        AddThicknessResults
            Returns the AddThicknessResults.


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
        """Creates BOI to the selected list of face zonelet ids.


        Parameters
        ----------
        face_zonelet_ids : Iterable[int]
            List of input face zonelet ids.
        params : CreateBOIParams
            Parameters to control the BOI creation operation.

        Returns
        -------
        CreateBOIResults
            Returns the BOIResults.


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
        """Creates contact patch by offsetting the target zonelets.


        Parameters
        ----------
        source_zonelets : Iterable[int]
            Source face zonelet ids.
        target_zonelets : Iterable[int]
            Target face zonelet ids.
        params : CreateContactPatchParams
            Parameters to control the contact patch creation operation.

        Returns
        -------
        CreateContactPatchResults
            Returns the CreateContactPatchResults.


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
