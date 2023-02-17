"""Utilities module for surface operations."""
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
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.params.primestructs import ErrorCode as ErrorCode
from ansys.meshing.prime.params.primestructs import Iterable as Iterable


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

    def add_thickness(self, zonelets: Iterable[int], params: AddParams) -> AddResults:
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
