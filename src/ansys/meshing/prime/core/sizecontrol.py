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

"""Module containing SizeControl related classes and methods."""
from ansys.meshing.prime.autogen.sizecontrol import SizeControl as _SizeControl

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults
from ansys.meshing.prime.autogen.sizecontrolstructs import SizeControlSummaryParams


class SizeControl(_SizeControl):
    """Size control is used to compute the size field.

    The size field is computed based on the size control defined.
    Different type of size controls provide control over how the mesh size is distributed on a
    surface or within the volume.

    Parameters
    ----------
    model : Model
        Server model to create SizeControl object.
    id : int
        Id of the SizeControl.
    object_id : int
        Object id of the SizeControl.
    name : str
        Name of the SizeControl..
    local : bool, optional
        Unused. The default is ``False``.
    """

    def __init__(self, model, id, object_id, name, local=False):
        """Initialize class variables and the superclass."""
        _SizeControl.__init__(self, model, id, object_id, name)
        self._model = model
        self._name = name

    def __str__(self) -> str:
        """Get a representation of the class in string format.

        Returns
        -------
        str
            Class data in string format.
        """
        params = SizeControlSummaryParams(model=self._model)
        result = _SizeControl.get_summary(self, params)
        return result.message

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Set the unique name for the size control to a suggested name.

        Parameters
        ----------
        name : str
            Suggested name for the size control.

        Returns
        -------
        SetNameResults
            Newly suggested name for the size control.


        Examples
        --------
        >>> size_control.set_suggested_name("control1")

        """
        result = _SizeControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def name(self):
        """Get the name of size control.

        Returns
        -------
        str
            Name of the size control.

        Examples
        --------
        >>> print(size_control.name)

        """
        return self._name
