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
"""Module for PickedInfo widget."""
import os
from typing import TYPE_CHECKING

from ansys.tools.visualization_interface.backends.pyvista.widgets import PlotterWidget
from vtk import vtkPNGReader

from ansys.meshing.prime.core.mesh import DisplayMeshInfo, DisplayMeshType

if TYPE_CHECKING:
    from ansys.meshing.prime.graphics.plotter import PrimePlotter


class PickedInfo(PlotterWidget):
    """Initializes the picked information button widget.

    This widget lets you get information about the picked mesh objects.

    Parameters
    ----------
    prime_plotter : PrimePlotter
        Plotter to apply this widget to.
    """

    def __init__(self, prime_plotter: "PrimePlotter") -> None:
        """Initialize widget."""
        super().__init__(prime_plotter._backend._pl.scene)
        self.prime_plotter = prime_plotter
        self._picked_dict = self.prime_plotter._backend._picked_dict
        self._object_actors_map = self.prime_plotter._backend._object_to_actors_map
        self._button = self.prime_plotter._backend._pl.scene.add_checkbox_button_widget(
            self.callback,
            position=(5, 570),
            size=30,
            border_size=3,
            color_off="white",
            color_on="white",
        )
        self._info_actor_map = self.prime_plotter._info_actor_map

    def info_message(self, mesh_info: DisplayMeshInfo) -> str:
        """Get the information message for the selected mesh object.

        Parameters
        ----------
        mesh_info : DisplayMeshInfo
            Mesh information object to print.

        Returns
        -------
        str
            Message with the information of the selected mesh object.
        """
        mesh_type = mesh_info.display_mesh_type
        id = mesh_info.id
        part_id = mesh_info.part_id
        part_name = mesh_info.part_name
        zone_id = mesh_info.zone_id
        zone_name = mesh_info.zone_name

        if mesh_type == DisplayMeshType.TOPOFACE or mesh_type == DisplayMeshType.FACEZONELET:
            msg = "Selected FaceZonelet "
            if mesh_type is DisplayMeshType.TOPOFACE:
                msg = "Selected TopoFace "
            msg += str(id)
        elif mesh_type == DisplayMeshType.TOPOEDGE or mesh_type == DisplayMeshType.EDGEZONELET:
            msg = "Selected EdgeZonelet "
            if mesh_type is DisplayMeshType.TOPOEDGE:
                msg = "Selected TopoEdge "
            msg += str(id)
        msg += ", in Part Id : " + str(part_id) + ", Part Name : " + part_name + "\n"
        if zone_id > 0:
            msg += "Zone Id : " + str(zone_id) + ", Zone Name : " + zone_name
        return msg

    def callback(self, state: bool) -> None:
        """Define the callback function for the button widget.

        Parameters
        ----------
        state : bool
            State of the button widget.
        """
        for meshobject in list(self._picked_dict.values()):
            mesh_info = self._info_actor_map[meshobject.actor]
            print(self.info_message(mesh_info))

    def update(self) -> None:
        """Define the configuration and representation of the button widget button."""
        show_point_vr = self._button.GetRepresentation()
        show_point_icon_file = os.path.join(
            os.path.dirname(__file__), "images", "selectioninfo.png"
        )
        show_point_r = vtkPNGReader()
        show_point_r.SetFileName(show_point_icon_file)
        show_point_r.Update()
        image = show_point_r.GetOutput()
        show_point_vr.SetButtonTexture(0, image)
        show_point_vr.SetButtonTexture(1, image)
