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

"""This module contains the HidePicked class."""

import os
from typing import TYPE_CHECKING, List

from ansys.tools.visualization_interface.backends.pyvista.widgets import PlotterWidget
from vtk import vtkPNGReader

from ansys.meshing.prime.core.mesh import DisplayEntityKey

if TYPE_CHECKING:
    from ansys.meshing.prime.graphics.plotter import PrimePlotter


class HidePicked(PlotterWidget):
    """Hide or restore currently selected Prime display entities.

    Selection is tracked using DisplayEntityKey so identical entity IDs in
    different parts remain independent.
    """

    def __init__(self, prime_plotter: "PrimePlotter") -> None:
        """Initialize the widget."""
        super().__init__(prime_plotter._backend._pl.scene)

        self.prime_plotter = prime_plotter

        self._button = (
            self.prime_plotter._backend._pl.scene.add_checkbox_button_widget(
                self.callback,
                position=(5, 660),
                size=30,
                border_size=3,
                color_off="white",
                color_on="white",
            )
        )

        self._hidden_entities: List[DisplayEntityKey] = []

    def callback(self, state: bool) -> None:
        """Hide or restore the currently selected entities.

        Parameters
        ----------
        state : bool
            State of the checkbox widget.
        """
        if state:
            hidden_entities = []
            seen = set()

            for info in self.prime_plotter.selected_entity_infos:
                key = info.key

                if key in seen:
                    continue

                seen.add(key)
                hidden_entities.append(key)

            self._hidden_entities = hidden_entities

            if self._hidden_entities:
                self.prime_plotter.set_entities_visible(
                    self._hidden_entities,
                    False,
                )

        else:
            if self._hidden_entities:
                self.prime_plotter.set_entities_visible(
                    self._hidden_entities,
                    True,
                )

            self._hidden_entities = []

    def update(self) -> None:
        """Configure the button appearance."""
        representation = self._button.GetRepresentation()

        icon_file = os.path.join(
            os.path.dirname(__file__),
            "images",
            "invert_visibility.png",
        )

        reader = vtkPNGReader()
        reader.SetFileName(icon_file)
        reader.Update()

        image = reader.GetOutput()

        representation.SetButtonTexture(0, image)
        representation.SetButtonTexture(1, image)
