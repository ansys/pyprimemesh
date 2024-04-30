import os

from ansys.visualizer import Plotter, PlotterWidget
from vtk import vtkButtonWidget, vtkPNGReader

from ansys.meshing.prime.core.mesh import DisplayMeshInfo, DisplayMeshType


class PickedInfo(PlotterWidget):
    def __init__(self, plotter_helper: "Plotter") -> None:
        super().__init__(plotter_helper._pl.scene)
        self.plotter_helper = plotter_helper
        self._picked_list = self.plotter_helper._picked_list
        self._object_actors_map = self.plotter_helper._object_to_actors_map
        self._button = self.plotter_helper._pl.scene.add_checkbox_button_widget(
            self.callback,
            position=(5, 570),
            size=30,
            border_size=3,
            color_off="white",
            color_on="white",
        )
        self._info_actor_map = self.plotter_helper._info_actor_map

    def info_message(self, mesh_info: DisplayMeshInfo) -> str:
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
        for meshobject in self._picked_list:
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
