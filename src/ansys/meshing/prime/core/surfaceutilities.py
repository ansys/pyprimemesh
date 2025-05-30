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
    """Performs various general surface utilities algorithms.

    For example, copy zonelets, resolve surface intersections.

    Parameters
    ----------
    model : Model
        Server model to create SurfaceUtilities object.
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
