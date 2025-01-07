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
"""Module for ToggleEdges widget."""
import os
from typing import TYPE_CHECKING

from ansys.tools.visualization_interface.backends.pyvista.widgets import PlotterWidget
from vtk import vtkPNGReader

if TYPE_CHECKING:
    from ansys.meshing.prime.graphics.plotter import PrimePlotter


class ToggleEdges(PlotterWidget):
    """Toggles the edges of the mesh objects.

    Parameters
    ----------
    prime_plotter : PrimePlotter
        Plotter to apply this widget to.
    """

    def __init__(self, prime_plotter: "PrimePlotter") -> None:
        """Initialize the widget."""
        super().__init__(prime_plotter._backend._pl.scene)
        self.prime_plotter = prime_plotter
        self._object_actors_map = self.prime_plotter._backend._object_to_actors_map
        self._button = self.prime_plotter._backend._pl.scene.add_checkbox_button_widget(
            self.callback,
            position=(5, 600),
            size=30,
            border_size=3,
            color_off="white",
            color_on="white",
        )
        self._info_actor_map = self.prime_plotter._info_actor_map

    def callback(self, state: bool) -> None:
        """Toggle the edges of the mesh objects.

        Parameters
        ----------
        state : bool
            Whether the button widget is activated.
        """
        for key, actor in self.prime_plotter._backend._pl.scene.actors.items():
            if actor in self._info_actor_map and self._info_actor_map[actor].has_mesh:
                actor.prop.show_edges = not state

    def update(self) -> None:
        """Define the configuration and representation of the button widget button."""
        show_point_vr = self._button.GetRepresentation()
        show_point_icon_file = os.path.join(os.path.dirname(__file__), "images", "show_edges.png")
        show_point_r = vtkPNGReader()
        show_point_r.SetFileName(show_point_icon_file)
        show_point_r.Update()
        image = show_point_r.GetOutput()
        show_point_vr.SetButtonTexture(0, image)
        show_point_vr.SetButtonTexture(1, image)
