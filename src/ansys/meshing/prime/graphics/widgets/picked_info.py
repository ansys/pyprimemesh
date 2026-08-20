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
"""Module for the picked-information widget."""

import os
from typing import TYPE_CHECKING

from ansys.tools.visualization_interface.backends.pyvista.widgets import PlotterWidget
from vtk import vtkPNGReader

from ansys.meshing.prime.core.mesh import DisplayMeshInfo, DisplayMeshType

if TYPE_CHECKING:
    from ansys.meshing.prime.graphics.plotter import PrimePlotter


class PickedInfo(PlotterWidget):
    """Initialize the picked-information button widget.

    This widget prints information about each uniquely selected Prime display
    entity. Entity uniqueness includes the owning part and display entity type,
    so equal entity IDs in different parts remain distinct.

    Parameters
    ----------
    prime_plotter : PrimePlotter
        Plotter to which this widget is attached.
    """

    def __init__(self, prime_plotter: "PrimePlotter") -> None:
        """Initialize the widget."""
        super().__init__(prime_plotter._backend._pl.scene)
        self.prime_plotter = prime_plotter
        self._button = self.prime_plotter._backend._pl.scene.add_checkbox_button_widget(
            self.callback,
            position=(5, 570),
            size=30,
            border_size=3,
            color_off="white",
            color_on="white",
        )

    @staticmethod
    def _entity_description(mesh_info: DisplayMeshInfo) -> str:
        """Return a readable description of a selected display entity.

        Parameters
        ----------
        mesh_info : DisplayMeshInfo
            Information about the selected display entity.

        Returns
        -------
        str
            Entity type and original Prime entity ID.
        """
        descriptions = {
            DisplayMeshType.TOPOFACE: "Selected TopoFace",
            DisplayMeshType.FACEZONELET: "Selected FaceZonelet",
            DisplayMeshType.TOPOEDGE: "Selected TopoEdge",
            DisplayMeshType.EDGEZONELET: "Selected EdgeZonelet",
            DisplayMeshType.SPLINECONTROLPOINTS: "Selected Spline Control Points",
            DisplayMeshType.SPLINESURFACE: "Selected Spline Surface",
        }
        description = descriptions.get(
            mesh_info.display_mesh_type,
            "Selected Entity",
        )
        return f"{description} {mesh_info.id}"

    def info_message(self, mesh_info: DisplayMeshInfo) -> str:
        """Return the information message for a selected display entity.

        Parameters
        ----------
        mesh_info : DisplayMeshInfo
            Information about the selected display entity.

        Returns
        -------
        str
            Human-readable selection information.
        """
        part_name = mesh_info.part_name or "<unknown>"
        entity_type_name = mesh_info.display_mesh_type.name

        message = (
            f"{self._entity_description(mesh_info)}, "
            f"Part Id : {mesh_info.part_id}, "
            f"Part Name : {part_name}, "
            f"Entity Type : {entity_type_name}"
        )

        if mesh_info.zone_id > 0:
            zone_name = mesh_info.zone_name or "<unknown>"
            message += f"\nZone Id : {mesh_info.zone_id}, " f"Zone Name : {zone_name}"

        return message

    def callback(self, state: bool) -> None:
        """Print information for each uniquely selected entity.

        Parameters
        ----------
        state : bool
            State of the checkbox button. Selection information is printed for
            either state to preserve the widget's existing callback behavior.
        """
        del state

        seen = set()
        for mesh_info in self.prime_plotter.selected_entity_infos:
            key = mesh_info.key
            if key in seen:
                continue
            seen.add(key)
            print(self.info_message(mesh_info))

    def update(self) -> None:
        """Configure the button texture."""
        representation = self._button.GetRepresentation()
        icon_file = os.path.join(
            os.path.dirname(__file__),
            "images",
            "selectioninfo.png",
        )
        reader = vtkPNGReader()
        reader.SetFileName(icon_file)
        reader.Update()
        image = reader.GetOutput()
        representation.SetButtonTexture(0, image)
        representation.SetButtonTexture(1, image)
