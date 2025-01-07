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

"""Module for ColorByTypeWidget."""
import enum
import os
from typing import TYPE_CHECKING

import numpy as np
from ansys.tools.visualization_interface.backends.pyvista.widgets import PlotterWidget
from vtk import vtkPNGReader

if TYPE_CHECKING:
    from ansys.meshing.prime.graphics.plotter import PrimePlotter

from ansys.meshing.prime.core.mesh import DisplayMeshInfo

color_matrix = np.array(
    [
        [155, 186, 126],
        [242, 236, 175],
        [255, 187, 131],
        [194, 187, 97],
        [159, 131, 169],
        [157, 190, 139],
        [233, 218, 158],
        [254, 252, 196],
        [246, 210, 148],
        [215, 208, 198],
        [196, 235, 145],
    ]
)


class ColorByType(enum.IntEnum):
    """Contains the zone types to display."""

    ZONE = 0
    ZONELET = 1
    PART = 2


class ColorByTypeWidget(PlotterWidget):
    """Initializes the color by the type button widget.

    This widget lets you change the color of the mesh
    based on the zone, zonelet, or part.

    Parameters
    ----------
    prime_plotter : Plotter
        Plotter object to use.
    """

    def __init__(self, prime_plotter: "PrimePlotter") -> None:
        """Initialize the widget."""
        super().__init__(prime_plotter._backend._pl.scene)
        self.prime_plotter = prime_plotter
        self._object_actors_map = self.prime_plotter._backend.pv_interface._object_to_actors_map
        self._info_actor_map = self.prime_plotter._info_actor_map
        self._button = self.prime_plotter._backend.pv_interface.scene.add_checkbox_button_widget(
            self.callback, position=(5, 630), size=30, border_size=3
        )
        self._button.GetRepresentation().SetNumberOfStates(3)
        self._color_type = ColorByType.ZONE

    def callback(self, state) -> None:
        """Define the callback function for the button widget."""
        color_type = ColorByType(self._button.GetRepresentation().GetState())
        for actor, object in self._object_actors_map.items():
            if actor in self.prime_plotter._info_actor_map:
                mesh_info = self.prime_plotter._info_actor_map[actor]
                actor.prop.color = self.set_color_by_type(color_type, mesh_info)
                self.update(color_type)

    def update(self, color_type=ColorByType.ZONE) -> None:
        """Define the configuration and representation of the button widget button.

        Parameters
        ----------
        color_type : ColorByType, default: ColorByType.ZONE
            Color type to use.
        """
        vr = self._button.GetRepresentation()
        icon_file = os.path.join(os.path.dirname(__file__), "images", "bin.png")

        if color_type == ColorByType.ZONE:
            icon_file = os.path.join(os.path.dirname(__file__), "images", "bin.png")
        elif color_type == ColorByType.ZONELET:
            icon_file = os.path.join(os.path.dirname(__file__), "images", "surface_body.png")
        elif color_type == ColorByType.PART:
            icon_file = os.path.join(os.path.dirname(__file__), "images", "parts.png")
        reader = vtkPNGReader()
        reader.SetFileName(icon_file)
        reader.Update()
        image = reader.GetOutput()
        vr.SetButtonTexture(0, image)
        vr.SetButtonTexture(1, image)
        vr.SetButtonTexture(2, image)

    def set_color_by_type(self, color_type: ColorByType, mesh_info: DisplayMeshInfo):
        """Get the colors of faces.

        Parameters
        ----------
        color_type : ColorByType
            Color type to use.
        mesh_info : DisplayMeshInfo
            Mesh information that generates an appropriate color.

        Returns
        -------
        List
            List of colors for faces.
        """
        num_colors = int(color_matrix.size / 3)
        if color_type == ColorByType.ZONELET:
            return color_matrix[mesh_info.id % num_colors].tolist()
        elif color_type == ColorByType.PART:
            return color_matrix[mesh_info.part_id % num_colors].tolist()
        else:
            return color_matrix[mesh_info.zone_id % num_colors].tolist()
