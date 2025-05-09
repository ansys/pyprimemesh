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

"""Module containing VolumeControl related classes and methods."""
from ansys.meshing.prime.autogen.volumecontrol import VolumeControl as _VolumeControl

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults
from ansys.meshing.prime.autogen.volumecontrolstructs import VolumeControlParams


class VolumeControl(_VolumeControl):
    """Defines the scope and type of volume mesh to generate.

    Parameters
    ----------
    model : Model
        Server model to create VolumeControl object.
    id : int
        Id of the VolumeControl.
    object_id : int
        Object id of the VolumeControl.
    name : str
        Name of the VolumeControl.
    """

    def __init__(self, model, id, object_id, name, local=False):
        """Initialize the superclass and the ``model`` variable."""
        _VolumeControl.__init__(self, model, id, object_id, name)
        self._model = model
        self._name = name

    def __str__(self) -> str:
        """Get a representation of the class in string format.

        Returns
        -------
        str
            Class data in string format.
        """
        params = VolumeControlParams(model=self._model)
        # TODO: function get_summary() not implemented
        result = _VolumeControl.get_summary(self, params)
        return result.message

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Set the unique name for the volume control based on a suggested name.

        Parameters
        ----------
        name : str
            Suggested name for the volume control.

        Returns
        -------
        SetNameResults
            Newly suggested name of the volume control.


        Examples
        --------
        >>> volume_control.set_suggested_name("control1")

        """
        result = _VolumeControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def name(self):
        """Get the name of the volume control.

        Returns
        -------
        str
            Name of the volume control.

        Examples
        --------
        >>> print(volume_control.name)

        """
        return self._name
