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

"""Module for the SelectionTargetWidget widget."""

import os
from typing import TYPE_CHECKING

from ansys.tools.visualization_interface.backends.pyvista.widgets import PlotterWidget
from vtk import vtkPNGReader

from ansys.meshing.prime.core.mesh import SelectionTarget
from ansys.meshing.prime.graphics.widgets.toolbar import ToolbarButton

if TYPE_CHECKING:
    from ansys.meshing.prime.graphics.plotter import PrimePlotter

#: How each selection target reads in the button hover text.
SELECTION_TARGET_LABELS = {
    SelectionTarget.BOTH: "faces and edges",
    SelectionTarget.FACES: "faces only",
    SelectionTarget.EDGES: "edges only",
}


class SelectionTargetWidget(ToolbarButton, PlotterWidget):
    """Choose whether picking selects faces, edges, or both.

    Narrowing the target only changes what the next click can hit. Entities that
    are already selected stay selected, so faces and edges can be collected
    together by switching the target between picks.

    Parameters
    ----------
    prime_plotter : PrimePlotter
        Plotter whose selection target the widget controls.
    """

    def __init__(self, prime_plotter: "PrimePlotter") -> None:
        """Initialize the widget."""
        super().__init__(prime_plotter._backend._pl.scene)

        self.prime_plotter = prime_plotter

        self._button = self._add_button((5, 540), color_off="white", color_on="white")

        self._button.GetRepresentation().SetNumberOfStates(len(SelectionTarget))

        self._target = SelectionTarget.BOTH

    def callback(self, state) -> None:
        """Apply the selected target.

        Parameters
        ----------
        state : bool
            Checkbox widget state. Unused, because the target is read from the
            button, which cycles through more than two states.
        """
        del state

        target = SelectionTarget(self._button.GetRepresentation().GetState())

        self._target = target

        self.prime_plotter.set_selection_target(target)

        self.update(target)

        self.prime_plotter.refresh_tooltips()

    def tooltip(self) -> str:
        """Return hover text naming the target and what the next click selects.

        Returns
        -------
        str
            Description of the current and next selection target.
        """
        current = SelectionTarget(self._button.GetRepresentation().GetState())
        following = SelectionTarget((int(current) + 1) % len(SelectionTarget))
        return (
            f"Selecting {SELECTION_TARGET_LABELS[current]}.\n"
            f"Click to select {SELECTION_TARGET_LABELS[following]}."
        )

    def update(self, target: SelectionTarget = SelectionTarget.BOTH) -> None:
        """Configure the widget icon.

        Parameters
        ----------
        target : SelectionTarget, default: SelectionTarget.BOTH
            Active selection target.
        """
        representation = self._button.GetRepresentation()

        image_dir = os.path.join(
            os.path.dirname(__file__),
            "images",
        )

        image_map = {
            SelectionTarget.BOTH: "select_both.png",
            SelectionTarget.FACES: "select_faces.png",
            SelectionTarget.EDGES: "select_edges.png",
        }

        icon_file = os.path.join(
            image_dir,
            image_map[target],
        )

        reader = vtkPNGReader()
        reader.SetFileName(icon_file)
        reader.Update()

        image = reader.GetOutput()

        for state in range(len(SelectionTarget)):
            representation.SetButtonTexture(state, image)

    def reset(self) -> None:
        """Return the widget to its unpressed state without calling back."""
        self._button.GetRepresentation().SetState(0)
        self._target = SelectionTarget.BOTH
        self.update(SelectionTarget.BOTH)
        self.prime_plotter.refresh_tooltips()
