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

"""Module containing classes and methods related to periodic control."""

from ansys.meshing.prime.autogen.periodiccontrol import (
    PeriodicControl as _PeriodicControl,
)

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults
from ansys.meshing.prime.autogen.periodiccontrolstructs import PeriodicControlParams


class PeriodicControl(_PeriodicControl):
    """Periodic controls provide settings for the recovery of periodic surfaces.

    A periodic control is specified by the scope (source surfaces) and
    the transformation parameters: the center, axis and angle.

    Parameters
    ----------
    model : Model
        Server model to create PeriodicControl object.
    id : int
        Id of the PeriodicControl.
    object_id : int
        Object id of the PeriodicControl.
    name : str
        Name of the PeriodicControl.
    local : bool, optional
        Unused. The default is ``False``.
    """

    def __init__(self, model, id, object_id, name, local=False):
        """Initialize class variables and the superclass."""
        _PeriodicControl.__init__(self, model, id, object_id, name)
        self._model = model
        self._name = name

    def __str__(self) -> str:
        """Get a representation of the class in string format.

        Returns
        -------
        str
            Class data in string format.
        """
        params = PeriodicControlParams(model=self._model)
        result = _PeriodicControl.get_summary(self, params)
        return result.message

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Set the unique name for the periodic control to a suggested name.

        Parameters
        ----------
        name : str
            Suggested name for the periodic control.

        Returns
        -------
        SetNameResults
            Newly suggested name of the periodic control.

        Examples
        --------
        >>> periodic_control.set_suggested_name("control1")

        """
        result = _PeriodicControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def name(self):
        """Get the name of the periodic control.

        Returns
        -------
        str
            Name of the periodic control.

        Examples
        --------
        >>> print(periodic_control.name)

        """
        return self._name
