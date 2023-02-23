from ansys.meshing.prime.autogen.surfaceutilities import (
    SurfaceUtilities as _SurfaceUtilities,
)

# isort: split
from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    AddThicknessParams as AddParams,
)
from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    AddThicknessResults as AddResults,
)
from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    CreateBOIParams as CreateBOIParams,
)
from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    CreateBOIResults as CreateBOIResults,
)
from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    CreateContactPatchParams as CPP,
)
from ansys.meshing.prime.autogen.surfaceutilitystructs import (
    CreateContactPatchResults as CPR,
)
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.params.primestructs import ErrorCode as ErrorCode
from ansys.meshing.prime.params.primestructs import Iterable as Iterable
from ansys.meshing.prime.params.primestructs import ScopeDefinition as SD


class SurfaceUtilities(_SurfaceUtilities):
    """Performs various general surface utilities algorithms. For example, add thickness."""

    def __init__(self, model: Model):
        """__init__(Model self, int id, int object_id, char* name)"""
        _SurfaceUtilities.__init__(self, model)
        self._model = model

    def add_thickness(self, zonelets: Iterable[int], params: AddParams) -> AddResults:
        """Adds thickness to the selected list of face zonelet ids.


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

    def create_boi(self, scope: SD, params: CreateBOIParams) -> CreateBOIResults:
        """Creates BOI to the selected list of face zonelet ids.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope of zonelets.
        params : CreateBOIParams
            Parameters to control the BOI creation operation.

        Returns
        -------
        CreateBOIResults
            Returns the BOIResults.


        Examples
        --------
        >>> result = surf_utils.create_surface_boi(zonelets, params)

        """
        result = _SurfaceUtilities.create_boi(self, scope, params)
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result

    def create_contact_patch(self, source_scope: SD, target_scope: SD, params: CPP) -> CPR:
        """Creates contact patches.


        Parameters
        ----------
        source_scope : ScopeDefinition
            Scope of source zonelets.
        target_scope : ScopeDefinition
            Scope of target zonelets which is to be offsetted for contact patch creation.
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
        result = _SurfaceUtilities.create_contact_patch(self, source_scope, target_scope, params)
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result
