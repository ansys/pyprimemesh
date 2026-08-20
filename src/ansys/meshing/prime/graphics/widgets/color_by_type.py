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

"""Module for ColorByTypeWidget."""

import os
from typing import TYPE_CHECKING

from ansys.tools.visualization_interface.backends.pyvista.widgets import PlotterWidget
from vtk import vtkPNGReader

from ansys.meshing.prime.core.mesh import (
    ColorByType,
    DisplayMeshInfo,
    entity_color,
)

if TYPE_CHECKING:
    from ansys.meshing.prime.graphics.plotter import PrimePlotter


class ColorByTypeWidget(PlotterWidget):
    """Widget controlling entity coloring mode.

    The plotter maintains actor-per-entity-type rendering and recolors
    entities using per-cell metadata. This widget only changes the active
    coloring mode.
    """

    def __init__(self, prime_plotter: "PrimePlotter") -> None:
        """Initialize the widget."""
        super().__init__(prime_plotter._backend._pl.scene)

        self.prime_plotter = prime_plotter

        self._button = (
            self.prime_plotter._backend.pv_interface.scene.add_checkbox_button_widget(
                self.callback,
                position=(5, 630),
                size=30,
                border_size=3,
            )
        )

        self._button.GetRepresentation().SetNumberOfStates(3)

        self._color_type = ColorByType.ZONE

    def callback(self, state) -> None:
        """Apply the selected coloring mode."""
        del state

        color_type = ColorByType(
            self._button.GetRepresentation().GetState()
        )

        self._color_type = color_type

        self.prime_plotter.set_color_by_type(color_type)

        self.update(color_type)

    def update(
        self,
        color_type: ColorByType = ColorByType.ZONE,
    ) -> None:
        """Update the widget icon.

        Parameters
        ----------
        color_type : ColorByType, default: ColorByType.ZONE
            Active coloring mode.
        """
        representation = self._button.GetRepresentation()

        image_dir = os.path.join(
            os.path.dirname(__file__),
            "images",
        )

        image_map = {
            ColorByType.ZONE: "bin.png",
            ColorByType.ZONELET: "surface_body.png",
            ColorByType.PART: "parts.png",
        }

        icon_file = os.path.join(
            image_dir,
            image_map[color_type],
        )

        reader = vtkPNGReader()
        reader.SetFileName(icon_file)
        reader.Update()

        image = reader.GetOutput()

        representation.SetButtonTexture(0, image)
        representation.SetButtonTexture(1, image)
        representation.SetButtonTexture(2, image)

    @staticmethod
    def set_color_by_type(
        color_type: ColorByType,
        mesh_info: DisplayMeshInfo,
    ):
        """Return the RGB color for a display entity.

        Parameters
        ----------
        color_type : ColorByType
            Active coloring mode.
        mesh_info : DisplayMeshInfo
            Entity metadata.

        Returns
        -------
        List[int]
            RGB color.
        """
        return entity_color(
            mesh_info,
            color_type,
        ).tolist()
