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

"""Module containing WrapperControl related classes and methods."""
from ansys.meshing.prime.autogen.wrappercontrol import WrapperControl as _WrapperControl

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults as SetNameResults
from ansys.meshing.prime.internals.comm_manager import CommunicationManager


class WrapperControl(_WrapperControl):
    """Wrapper Control to describe all parameters and controls used for wrapping..

    Parameters
    ----------
    model : Model
        Server model to create WrapperControl object.
    id : int
        Id of the WrapperControl.
    object_id : int
        Object id of the WrapperControl.
    name : str
        Name of the WrapperControl.
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """Initialize the superclass and the ''Model'' variable."""
        self._model = model
        _WrapperControl.__init__(self, model, id, object_id, name)

    def __str__(self) -> str:
        """Get a representation of the class in string format.

        Returns
        -------
        str
            Class data in string format.
        """
        return "Not implemented yet"

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Set the unique name for the wrapper control based on a suggested name.

        Parameters
        ----------
        name : str
            Suggested name for the wrapper control.

        Returns
        -------
        SetNameResults
            Newly assigned name of the wrapper control.


        Examples
        --------
        >>> wrapper_control.set_suggested_name("wrapper_control1")

        """
        result = _WrapperControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def name(self):
        """Get the name of the wrapper control.

        Returns
        -------
        str
            Name of the wrapper control.

        Examples
        --------
        >>> print(wrapper_control.name)

        """
        return self._name
