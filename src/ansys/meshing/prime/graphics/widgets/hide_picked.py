# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
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

"""This module contains the HidePicked class."""
import os
from typing import TYPE_CHECKING

from ansys.tools.visualization_interface.backends.pyvista.widgets import PlotterWidget
from vtk import vtkPNGReader

if TYPE_CHECKING:
    from ansys.meshing.prime.graphics.plotter import PrimePlotter


class HidePicked(PlotterWidget):
    """Initializes the hide picked button widget.

    This widget lets you hide the picked mesh objects.

    Parameters
    ----------
    prime_plotter : Plotter
        Plotter to apply this widget to.
    """

    def __init__(self, prime_plotter: "PrimePlotter") -> None:
        """Initialize the widget."""
        super().__init__(prime_plotter._backend._pl.scene)
        self.prime_plotter = prime_plotter
        self._picked_dict = self.prime_plotter._backend._picked_dict
        self._object_actors_map = self.prime_plotter._backend._object_to_actors_map
        self._button = self.prime_plotter._backend._pl.scene.add_checkbox_button_widget(
            self.callback,
            position=(5, 660),
            size=30,
            border_size=3,
            color_off="white",
            color_on="white",
        )
        self._removed_actors = []

    def callback(self, state: bool) -> None:
        """Define callback function for the button widget."""
        if state:
            for meshobject in list(self._picked_dict.values()):
                self.prime_plotter._backend.pv_interface.scene.remove_actor(meshobject.actor)
                self._removed_actors.append(meshobject.actor)
        else:
            for actor in self._removed_actors:
                self.prime_plotter._backend._pl.scene.add_actor(actor)

    def update(self) -> None:
        """Define the configuration and representation of the button widget button."""
        vr = self._button.GetRepresentation()
        icon_file = os.path.join(os.path.dirname(__file__), "images", "invert_visibility.png")
        r = vtkPNGReader()
        r.SetFileName(icon_file)
        r.Update()
        image = r.GetOutput()
        vr.SetButtonTexture(0, image)
        vr.SetButtonTexture(1, image)
