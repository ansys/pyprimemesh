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

"""Module containing PrismControl related classes and methods."""
from ansys.meshing.prime.autogen.prismcontrol import PrismControl as _PrismControl

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults


class PrismControl(_PrismControl):
    """PrismControl allows you to generate prisms.

    PrismControl allows you to control generation of prisms.
    Controls include setting the face scope, volume scope and growth parameters.

    Parameters
    ----------
    model : Model
        Server model to create PrismControl object.
    id : int
        Id of the PrismControl.
    object_id : int
        Object id of the PrismControl.
    name : str
        Name of the PrismControl.
    """

    def __init__(self, model, id, object_id, name, local=False):
        """Initialize class variables and the superclass."""
        _PrismControl.__init__(self, model, id, object_id, name)
        self._model = model
        self._name = name

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Set the unique name for the prism control based on the suggested name.

        Parameters
        ----------
        name : str
            Suggested name for the prism control.

        Returns
        -------
        SetNameResults
            Returns the SetNameResults.


        Examples
        --------
        >>> prism_control.set_suggested_name("control1")

        """
        result = _PrismControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result
