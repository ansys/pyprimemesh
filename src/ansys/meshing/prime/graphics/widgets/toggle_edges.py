# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Module for ToggleEdges widget."""

import os
from typing import TYPE_CHECKING

from ansys.tools.visualization_interface.backends.pyvista.widgets import PlotterWidget
from vtk import vtkPNGReader

from ansys.meshing.prime.graphics.widgets.toolbar import ToolbarButton

if TYPE_CHECKING:
    from ansys.meshing.prime.graphics.plotter import PrimePlotter


class ToggleEdges(ToolbarButton, PlotterWidget):
    """Toggle display of model element edges.

    In actor-per-entity-type rendering, element outlines are drawn as
    dedicated outline actors and this widget controls their visibility.

    Parameters
    ----------
    prime_plotter : PrimePlotter
        Plotter whose outline actors the widget shows and hides.
    """

    def __init__(self, prime_plotter: "PrimePlotter") -> None:
        """Initialize the widget."""
        super().__init__(prime_plotter._backend._pl.scene)

        self.prime_plotter = prime_plotter

        self._button = self._add_button((5, 600), color_off="white", color_on="white")

    def callback(self, state: bool) -> None:
        """Toggle edge visibility.

        Parameters
        ----------
        state : bool
            Checkbox widget state.
        """
        self.prime_plotter.set_show_edges(not state)
        self.prime_plotter.refresh_tooltips()

    def tooltip(self) -> str:
        """Return hover text naming what interior edges are drawn.

        Returns
        -------
        str
            Description of the current and next interior edge display.
        """
        showing_mesh = self.prime_plotter._show_element_edges
        if not self.prime_plotter.has_faceting:
            # Everything shown is meshed, so there is no faceting to switch to and
            # the button simply shows or hides the mesh.
            if showing_mesh:
                return "Showing mesh edges.\nClick to hide mesh edges."
            return "Mesh edges hidden.\nClick to show mesh edges."
        if not self.prime_plotter.has_mesh_edges:
            # Nothing is meshed, so the alternative to the faceting is the bare
            # topology rather than a mesh that is not there.
            if showing_mesh:
                return "Showing topology.\nClick to show the CAD faceting."
            return "Showing the CAD faceting.\nClick to show topology."
        if showing_mesh:
            return "Showing mesh edges.\nClick to show the CAD faceting of unmeshed faces."
        return "Showing the CAD faceting of unmeshed faces.\nClick to show mesh edges."

    def update(self) -> None:
        """Configure the widget icon."""
        representation = self._button.GetRepresentation()

        icon_file = os.path.join(
            os.path.dirname(__file__),
            "images",
            "show_edges.png",
        )

        reader = vtkPNGReader()
        reader.SetFileName(icon_file)
        reader.Update()

        image = reader.GetOutput()

        representation.SetButtonTexture(0, image)
        representation.SetButtonTexture(1, image)

    def reset(self) -> None:
        """Return the widget to its unpressed state without calling back."""
        self._button.GetRepresentation().SetState(0)
        self.update()
        self.prime_plotter.refresh_tooltips()
