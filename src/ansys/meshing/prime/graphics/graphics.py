import enum
import os

import numpy as np
import pyvista as pv
from pyvista import _vtk
from pyvista.plotting.plotting import Plotter

import ansys.meshing.prime as prime
from ansys.meshing.prime.internals import defaults


def compute_face_list_from_structured_nodes(nodes, dim):
    flist = []
    for w in range(dim[2]):
        for u in range(dim[0] - 1):
            for v in range(dim[1] - 1):
                flist.append(4)
                flist.append(u + v * dim[0] + w * dim[0] * dim[1])
                flist.append(u + 1 + v * dim[0] + w * dim[0] * dim[1])
                flist.append(u + 1 + (v + 1) * dim[0] + w * dim[0] * dim[1])
                flist.append(u + (v + 1) * dim[0] + w * dim[0] * dim[1])

    for v in range(dim[1]):
        for u in range(dim[0] - 1):
            for w in range(dim[2] - 1):
                flist.append(4)
                flist.append(u + v * dim[0] + w * dim[0] * dim[1])
                flist.append(u + 1 + v * dim[0] + w * dim[0] * dim[1])
                flist.append(u + 1 + v * dim[0] + (w + 1) * dim[0] * dim[1])
                flist.append(u + v * dim[0] + (w + 1) * dim[0] * dim[1])

    for u in range(dim[0]):
        for v in range(dim[1] - 1):
            for w in range(dim[2] - 1):
                flist.append(4)
                flist.append(u + v * dim[0] + w * dim[0] * dim[1])
                flist.append(u + (v + 1) * dim[0] + w * dim[0] * dim[1])
                flist.append(u + (v + 1) * dim[0] + (w + 1) * dim[0] * dim[1])
                flist.append(u + v * dim[0] + (w + 1) * dim[0] * dim[1])
    return flist


class DisplayMeshType(enum.IntEnum):
    TOPOFACE = 0
    TOPOEDGE = 1
    FACEZONELET = 2
    EDGEZONELET = 3
    SPLINECONTROLPOINTS = 4
    SPLINESURFACE = 5


class ColorByType(enum.IntEnum):
    ZONE = 0
    ZONELET = 1
    PART = 2


''' bright color palette '''
'''color_matrix = np.array([
[0.99609375, 0.76171875, 0.0703125],
[0.96484375, 0.62109375, 0.12109375],
[0.9296875, 0.3515625, 0.140625],
[0.9140625, 0.125, 0.15234375],
[0.765625, 0.89453125, 0.21875],
[0.63671875, 0.79296875, 0.21875],
[0, 0.578125, 0.1953125],
[0, 0.3828125, 0.3984375],
[0.0703125, 0.79296875, 0.765625],
[0.0703125, 0.53515625, 0.65234375],
[0.0234375, 0.3203125, 0.86328125],
[0.10546875, 0.078125, 0.390625],
[0.98828125, 0.65234375, 0.87109375],
[0.84765625, 0.5, 0.9765625],
[0.59765625, 0.5, 0.9765625] ]) * 255 '''


''' winter color palette '''
'''color_matrix = np.array([
[0.2734375, 0.71875, 0.8671875],
[0.2734375, 0.90234375, 0.86328125],
[0.2734375, 0.87109375, 0.62109375],
[0.2734375, 0.80078125, 0.84765625],
[0.2734375, 0.70703125, 0.66796875],
[0.2734375, 0.84375, 0.90234375],
[0.2734375, 0.64453125, 0.71875],
[0.2734375, 0.921875, 0.703125],
[0.2734375, 0.765625, 0.66015625],
[0.2734375, 0.9140625, 0.87890625],
[0.2734375, 0.70703125, 0.5],
[0.2734375, 0.8828125, 0.70703125],
[0.2734375, 0.99609375, 0.8515625],
[0.2734375, 0.91015625, 0.9765625],
[0.2734375, 0.99609375, 0.6171875] ]) * 255'''

''' light fall color palette '''
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


def compute_distance(point1, point2):
    dist = np.linalg.norm(np.array(point2) - np.array(point1))
    return dist


class Picker:
    def __init__(self, plotter, graphics):
        self.plotter = plotter
        self._graphics = graphics
        self._selected_disp_mesh: list[_DisplayMesh] = []
        self._points = []
        self._ignore = False

    @property
    def selections(self):
        """To access all the selected disp mesh when done."""
        return self._selected_disp_mesh

    def clear_selection(self):
        """ """
        [disp_mesh.deselect() for disp_mesh in self._selected_disp_mesh]
        self._selected_disp_mesh.clear()

    def ignore(self, ignore_pick):
        self._ignore = ignore_pick

    def __call__(self, *args, **kwargs):
        if self._ignore:
            return
        picked_pt = np.array(self.plotter.pick_mouse_position())
        direction = picked_pt - self.plotter.camera_position[0]
        direction = direction / np.linalg.norm(direction)
        start = picked_pt - 1000 * direction
        end = picked_pt + 10000 * direction
        disp_mesh_list = self._graphics.get_face_mesh_data()
        closest_disp_mesh = None
        closest_dist = np.finfo(0.0).max
        for disp_mesh in disp_mesh_list:
            if disp_mesh.poly_data is None:
                continue
            point, ix = disp_mesh.poly_data.ray_trace(start, end, first_point=True)
            if ix.size != 0:
                dist = compute_distance(start, point)
                if dist < closest_dist and disp_mesh not in self._selected_disp_mesh:
                    closest_dist = dist
                    closest_disp_mesh = disp_mesh
                elif disp_mesh in self._selected_disp_mesh:
                    disp_mesh.deselect()
                    self._selected_disp_mesh.remove(disp_mesh)
        if closest_disp_mesh is not None:
            self._selected_disp_mesh.append(closest_disp_mesh)
        [disp_mesh.select() for disp_mesh in self._selected_disp_mesh]
        return


class Graphics(object):
    """ """

    def __init__(self, model: prime.Model):
        """ """
        self._model = model
        self._display_data = {}
        self._display_spline_data = {}
        self._plotter = None
        self._picker = None
        self._color_by_type = ColorByType.ZONE
        self._parts = None
        self._facet_result = prime.FaceAndEdgeConnectivityResults(model=model)
        self._app = None
        self._ruler_visible = False
        self._ruler_actor = None
        self._colorByTypeBt: _vtk.vtkButtonWidget = None
        self._hideBt: _vtk.vtkButtonWidget = None
        self._showEdgeBt: _vtk.vtkButtonWidget = None
        self._printInfoBt: _vtk.vtkButtonWidget = None
        self._showRulerBt: _vtk.vtkButtonWidget = None
        self._sphinx_build = defaults.get_sphinx_build()
        if os.getenv('PRIME_APP_RUN'):
            self._app = __import__('PrimeApp')
        else:
            self.__update_display_data()

    def __update_display_data(self):
        """ """
        part_ids = [part.id for part in self._model.parts]
        mesh_info = prime.MeshInfo(self._model)
        self._display_data.clear()
        with prime.numpy_array_optimization_enabled():
            self._facet_result = mesh_info.get_face_and_edge_connectivity(
                part_ids, prime.FaceAndEdgeConnectivityParams(model=self._model)
            )
        for i, part_id in enumerate(self._facet_result.part_ids):
            data = {}
            part = self._model.get_part(part_id)
            splines = part.get_splines()
            disp_mesh_data: list[_DisplayMesh] = [
                self.__get_face_display_mesh_object(part_id, face_facet_res, j)
                for face_facet_res in self._facet_result.face_connectivity_result_per_part
                for j in range(0, len(face_facet_res.face_zonelet_ids))
            ]
            disp_e_mesh_data: list[_DisplayMesh] = [
                self.__get_edge_display_mesh_object(part_id, edge_facet_res, j)
                for edge_facet_res in self._facet_result.edge_connectivity_result_per_part
                for j in range(0, len(edge_facet_res.edge_zonelet_ids))
            ]
            disp_ctrl_point_data: list[_DisplayMesh] = [
                self.__get_ctrl_point_display_mesh_object(part_ids[i], j) for j in splines
            ]
            disp_spline_surf_data: list[_DisplayMesh] = [
                self.__get_spline_surf_display_mesh_object(part_ids[i], j) for j in splines
            ]
            if len(disp_mesh_data) > 0:
                data["faces"] = disp_mesh_data
            if len(disp_e_mesh_data) > 0:
                data["edges"] = disp_e_mesh_data
            if len(disp_ctrl_point_data) > 0:
                data["ctrlpts"] = disp_ctrl_point_data
            if len(disp_spline_surf_data) > 0:
                data["splinesurf"] = disp_spline_surf_data
            self._display_data[part_id] = data

    def __get_ctrl_point_display_mesh_object(self, part_id, spline_id):
        part = self._model.get_part(part_id)
        spline = part.get_spline(spline_id)
        dim = spline.control_points_count
        nodes = spline.control_points
        face_list = compute_face_list_from_structured_nodes(nodes, dim)
        display_mesh_type = DisplayMeshType.SPLINECONTROLPOINTS
        id = spline.id
        disp_mesh = _DisplayMesh(
            display_mesh_type,
            id,
            part_id,
            self,
            self._model,
            nodes,
            face_list,
            False,
            zone_id=-1,
            zone_name="",
            part_name=part.name,
        )
        return disp_mesh

    def __get_spline_surf_display_mesh_object(self, part_id, spline_id):
        part = self._model.get_part(part_id)
        spline = part.get_spline(spline_id)
        dim = spline.spline_points_count
        nodes = spline.spline_points
        face_list = compute_face_list_from_structured_nodes(nodes, dim)
        display_mesh_type = DisplayMeshType.SPLINESURFACE
        id = spline.id
        disp_mesh = _DisplayMesh(
            display_mesh_type,
            id,
            part_id,
            self,
            self._model,
            nodes,
            face_list,
            False,
            zone_id=-1,
            zone_name="",
            part_name=part.name,
        )
        return disp_mesh

    def __get_face_display_mesh_object(
        self, part_id: int, face_facet_res: prime.FaceConnectivityResults, index: int
    ):
        """ """
        part = self._model.get_part(part_id)
        node_start = 3 * np.sum(face_facet_res.num_nodes_per_face_zonelet[0:index])
        num_node_coords = 3 * face_facet_res.num_nodes_per_face_zonelet[index]
        face_list_start = np.sum(face_facet_res.num_face_list_per_face_zonelet[0:index])
        num_face_list = face_facet_res.num_face_list_per_face_zonelet[index]
        has_mesh = True
        if face_facet_res.topo_face_ids[index] > 0:
            display_mesh_type = DisplayMeshType.TOPOFACE
            id = face_facet_res.topo_face_ids[index]
            has_mesh = face_facet_res.mesh_face_ids[index] > 0
        else:
            display_mesh_type = DisplayMeshType.FACEZONELET
            id = face_facet_res.face_zonelet_ids[index]
        disp_mesh = _DisplayMesh(
            display_mesh_type,
            id,
            part_id,
            self,
            self._model,
            face_facet_res.node_coords[node_start : node_start + num_node_coords].reshape((-1, 3)),
            face_facet_res.face_list[face_list_start : face_list_start + num_face_list],
            has_mesh,
            zone_id=face_facet_res.face_zone_ids[index],
            zone_name=face_facet_res.face_zone_names[index],
            part_name=part.name,
        )
        return disp_mesh

    def __get_edge_display_mesh_object(
        self, part_id: int, edge_facet_res: prime.EdgeConnectivityResults, index: int
    ):
        """ """
        part = self._model.get_part(part_id)
        node_start = 3 * np.sum(edge_facet_res.num_nodes_per_edge_zonelet[0:index])
        num_node_coords = 3 * edge_facet_res.num_nodes_per_edge_zonelet[index]
        edge_list_start = np.sum(edge_facet_res.num_edge_list_per_edge_zonelet[0:index])
        num_edge_list = edge_facet_res.num_edge_list_per_edge_zonelet[index]
        has_mesh = True
        if edge_facet_res.topo_edge_ids[index] > 0:
            display_mesh_type = DisplayMeshType.TOPOEDGE
            id = edge_facet_res.topo_edge_ids[index]
            has_mesh = edge_facet_res.mesh_edge_ids[index] > 0
        else:
            display_mesh_type = DisplayMeshType.EDGEZONELET
            id = edge_facet_res.edge_zonelet_ids[index]
        disp_mesh = _DisplayMesh(
            display_mesh_type,
            id,
            part_id,
            self,
            self._model,
            edge_facet_res.node_coords[node_start : node_start + num_node_coords].reshape((-1, 3)),
            edge_facet_res.edge_list[edge_list_start : edge_list_start + num_edge_list],
            has_mesh,
            part_name=part.name,
            topo_edge_type=edge_facet_res.topo_edge_types[index],
            number_of_edges=edge_facet_res.num_edges_per_edge_zonelet[index],
        )
        return disp_mesh

    def __call__(self, parts=None, update=True, spline=False, scope: prime.ScopeDefinition = None):
        """ """
        self._parts = parts
        # if(spline):
        #     self.__draw_spline(update)
        # el
        if scope != None:
            self.__draw_scope_parts(update, scope)
        elif parts != None:
            self.__draw_parts(parts, update, spline)
        else:
            self.show(update)

    def __color_by_type_callback(self, flag):
        """ """
        vr = self._colorByTypeBt.GetRepresentation()
        state = vr.GetState()
        self._color_by_type = ColorByType(state)
        r = _vtk.vtkPNGReader()
        color_by_type_icon_file = ""
        if self._color_by_type == ColorByType.ZONELET:
            color_by_type_icon_file = os.path.join(
                os.path.dirname(__file__), 'images', 'surface_body.png'
            )
        elif self._color_by_type == ColorByType.ZONE:
            color_by_type_icon_file = os.path.join(os.path.dirname(__file__), 'images', 'bin.png')
        else:
            color_by_type_icon_file = os.path.join(os.path.dirname(__file__), 'images', 'parts.png')
        r.SetFileName(color_by_type_icon_file)
        r.Update()
        image = r.GetOutput()
        vr.SetButtonTexture(state, image)
        [
            disp_mesh.set_color_by_type(self._color_by_type)
            for part_id, data in self._display_data.items()
            if data.get("faces") != None
            for disp_mesh in data["faces"]
        ]

    def __hide_unhide_selection(self, flag):
        """ """
        sel_disp_mesh = self._picker.selections
        if len(sel_disp_mesh) > 0:
            [disp_mesh.hide(self._plotter) for disp_mesh in sel_disp_mesh]
            self._picker.clear_selection()
        else:
            [
                disp_mesh.unhide(self._plotter)
                for part_id, data in self._display_data.items()
                if data.get("faces") != None
                for disp_mesh in data["faces"]
            ]

    def __show_edges_callback(self, flag):
        [
            disp_mesh.show_edges(flag)
            for part_id, data in self._display_data.items()
            if data.get("faces") != None
            for disp_mesh in data["faces"]
        ]

    def __print_callback(self, flag):
        sel_disp_mesh = self._picker.selections
        [print(disp_mesh) for disp_mesh in sel_disp_mesh]

    def __show_ruler_callback(self, flag):
        """This function shows ruler on UI when clicked on ruler button"""
        if self._plotter is not None:
            if self._ruler_visible and self._ruler_actor is not None:
                self._plotter.remove_actor(self._ruler_actor)
                self._ruler_visible = False
            else:
                self._ruler_actor = self._plotter.show_bounds(
                    grid='front',
                    location='outer',
                    all_edges=False,
                    show_xaxis=True,
                    show_yaxis=True,
                    show_zaxis=True,
                )
                self._ruler_visible = True

    def get_face_mesh_data(self):
        """ """
        face_mesh_data = [
            disp_mesh
            for part_id, data in self._display_data.items()
            if data.get("faces") != None
            for disp_mesh in data["faces"]
        ]
        return face_mesh_data

    def show(self, update=False):
        """ """
        if os.getenv('PRIME_APP_RUN') and self._app is not None:
            app_g = self._app.Graphics().Get()
            app_g.DisplayModel()
            app_g.FitToScreen()
            return
        if update == True:
            self.__update_display_data()
        self._plotter = pv.Plotter()
        self._plotter.show_axes()
        [
            disp_mesh.add_to_plotter(self._plotter)
            for part_id, data in self._display_data.items()
            for key, disp_mesh_data in data.items()
            for disp_mesh in disp_mesh_data
        ]
        if self._sphinx_build == False:
            self._colorByTypeBt = self._plotter.add_checkbox_button_widget(
                self.__color_by_type_callback,
                value=int(self._color_by_type) is ColorByType.ZONELET,
                position=(10, 700),
                size=30,
                border_size=3,
            )
            self._hideBt = self._plotter.add_checkbox_button_widget(
                self.__hide_unhide_selection, position=(10, 650), size=30, border_size=3
            )
            self._showEdgeBt = self._plotter.add_checkbox_button_widget(
                self.__show_edges_callback, value=False, position=(10, 600), size=30, border_size=3
            )
            # self._plotter.add_checkbox_button_widget(
            #                  self.__surface_mesh_callback, position=(1870, 700),
            #                  color_on='yellow', color_off='yellow', size = 30, border_size=3)
            self._printInfoBt = self._plotter.add_checkbox_button_widget(
                self.__print_callback, position=(10, 550), size=30, border_size=3
            )
            self._showRulerBt = self._plotter.add_checkbox_button_widget(
                self.__show_ruler_callback, position=(10, 500), size=30, border_size=3
            )
        self._picker = Picker(self._plotter, self)
        self._plotter.track_click_position(self._picker, side='left')
        # self._plotter.window_size = [1920, 1017]
        if self._sphinx_build == False:
            self.__update_bt_icons()
        self._plotter.show()

    def __draw_parts(self, parts=[], update=False, spline=False):
        """ """
        if os.getenv('PRIME_APP_RUN') and self._app is not None:
            app_g = self._app.Graphics().Get()
            app_g.Clear()
            [app_g.DrawPart(part) for part in parts]
            app_g.FitToScreen()
            return
        if update == True:
            self.__update_display_data()
        self._plotter = pv.Plotter()
        self._plotter.show_axes()
        if spline:
            [
                disp_mesh.add_to_plotter(self._plotter)
                for part_id, data in self._display_data.items()
                if (part_id in parts)
                for key, disp_mesh_data in data.items()
                for disp_mesh in disp_mesh_data
            ]
        else:
            [
                disp_mesh.add_to_plotter(self._plotter)
                for part_id, data in self._display_data.items()
                if (part_id in parts)
                for key, disp_mesh_data in data.items()
                for disp_mesh in disp_mesh_data
                if (
                    disp_mesh.type != DisplayMeshType.SPLINECONTROLPOINTS
                    or disp_mesh.type != DisplayMeshType.SPLINESURFACE
                )
            ]
        if self._sphinx_build == False:
            self._colorByTypeBt = self._plotter.add_checkbox_button_widget(
                self.__color_by_type_callback,
                value=self._color_by_type is ColorByType.ZONELET,
                position=(10, 700),
                size=30,
                border_size=3,
            )
            self._hideBt = self._plotter.add_checkbox_button_widget(
                self.__hide_unhide_selection, position=(10, 650), size=30, border_size=3
            )
            self._showEdgeBt = self._plotter.add_checkbox_button_widget(
                self.__show_edges_callback, value=False, position=(10, 600), size=30, border_size=3
            )
            # self._plotter.add_checkbox_button_widget(self.__surface_mesh_callback,
            #                  position=(1870, 700), color_on='yellow',
            #                  color_off='yellow', size = 30, border_size=3)
            self._printInfoBt = self._plotter.add_checkbox_button_widget(
                self.__print_callback, position=(10, 550), size=30, border_size=3
            )
            self._showRulerBt = self._plotter.add_checkbox_button_widget(
                self.__show_ruler_callback, position=(10, 500), size=30, border_size=3
            )
        self._picker = Picker(self._plotter, self)
        self._plotter.track_click_position(self._picker, side='left')
        # self._plotter.window_size = [1920, 1017]
        if self._sphinx_build == False:
            self.__update_bt_icons()
        self._plotter.show()

    def __draw_scope_parts(self, update=False, scope: prime.ScopeDefinition = None):
        """ """
        self._plotter = pv.Plotter()
        self._plotter.show_axes()
        if os.getenv('PRIME_APP_RUN') and self._app is not None:
            app_g = self._app.Graphics().Get()
            app_g.Clear()
        elif update == True:
            self.__update_display_data()

        parts = self._model.control_data.get_scope_parts(scope)
        scope_def = scope
        for part_id in parts:
            part = self._model.get_part(part_id)
            scope_def.part_expression = part.name
            disp_data = None
            disp_ids = []
            if scope.entity_type == prime.ScopeEntity.FACEZONELETS:
                disp_ids = self._model.control_data.get_scope_face_zonelets(
                    scope=scope_def, params=prime.ScopeZoneletParams(model=self._model)
                )
                disp_data = self._display_data[part_id]["faces"]

            if disp_data is not None:
                [
                    disp_mesh.add_to_plotter(self._plotter)
                    for disp_mesh in disp_data
                    if (disp_mesh._id in disp_ids)
                ]

        if self._sphinx_build == False:
            self._colorByTypeBt = self._plotter.add_checkbox_button_widget(
                self.__color_by_type_callback,
                value=self._color_by_type is ColorByType.ZONELET,
                position=(10, 700),
                size=30,
                border_size=3,
            )
            self._hideBt = self._plotter.add_checkbox_button_widget(
                self.__hide_unhide_selection, position=(10, 650), size=30, border_size=3
            )
            self._showEdgeBt = self._plotter.add_checkbox_button_widget(
                self.__show_edges_callback, value=False, position=(10, 600), size=30, border_size=3
            )
            # self._plotter.add_checkbox_button_widget(self.__surface_mesh_callback,
            #                  position=(1870, 700), color_on='yellow',
            #                  color_off='yellow', size = 30, border_size=3)
            self._printInfoBt = self._plotter.add_checkbox_button_widget(
                self.__print_callback, position=(10, 550), size=30, border_size=3
            )
            self._showRulerBt = self._plotter.add_checkbox_button_widget(
                self.__show_ruler_callback, position=(10, 500), size=30, border_size=3
            )
        self._picker = Picker(self._plotter, self)
        self._plotter.track_click_position(self._picker, side='left')
        # self._plotter.window_size = [1920, 1017]
        if self._sphinx_build == False:
            self.__update_bt_icons()
        self._plotter.show()

    def __update_bt_icons(self):
        vr = self._colorByTypeBt.GetRepresentation()
        vr.SetNumberOfStates(3)
        r = _vtk.vtkPNGReader()
        color_by_zone_icon_file = os.path.join(os.path.dirname(__file__), 'images', 'bin.png')
        r.SetFileName(color_by_zone_icon_file)
        r.Update()
        image_1 = r.GetOutput()
        vr.SetButtonTexture(0, image_1)
        hide_vr = self._hideBt.GetRepresentation()
        hide_unhide_icon_file = os.path.join(
            os.path.dirname(__file__), 'images', 'invert_visibility.png'
        )
        hide_r = _vtk.vtkPNGReader()
        hide_r.SetFileName(hide_unhide_icon_file)
        hide_r.Update()
        image_2 = hide_r.GetOutput()
        hide_vr.SetButtonTexture(0, image_2)
        hide_vr.SetButtonTexture(1, image_2)
        show_edge_vr = self._showEdgeBt.GetRepresentation()
        show_edges_icon_file = os.path.join(os.path.dirname(__file__), 'images', 'show_edges.png')
        show_edge_r = _vtk.vtkPNGReader()
        show_edge_r.SetFileName(show_edges_icon_file)
        show_edge_r.Update()
        image_3 = show_edge_r.GetOutput()
        show_edge_vr.SetButtonTexture(0, image_3)
        show_edge_vr.SetButtonTexture(1, image_3)
        print_info_vr = self._printInfoBt.GetRepresentation()
        print_info_icon_file = os.path.join(
            os.path.dirname(__file__), 'images', 'selectioninfo.png'
        )
        print_info_r = _vtk.vtkPNGReader()
        print_info_r.SetFileName(print_info_icon_file)
        print_info_r.Update()
        image_4 = print_info_r.GetOutput()
        print_info_vr.SetButtonTexture(0, image_4)
        print_info_vr.SetButtonTexture(1, image_4)
        show_ruler_vr = self._showRulerBt.GetRepresentation()
        show_ruler_icon_file = os.path.join(os.path.dirname(__file__), 'images', 'show_ruler.png')
        show_ruler_r = _vtk.vtkPNGReader()
        show_ruler_r.SetFileName(show_ruler_icon_file)
        show_ruler_r.Update()
        image_5 = show_ruler_r.GetOutput()
        show_ruler_vr.SetButtonTexture(0, image_5)
        show_ruler_vr.SetButtonTexture(1, image_5)

    def get_color_by_type(self) -> ColorByType:
        """ """
        return self._color_by_type


class _DisplayMesh(object):
    """ """

    def __init__(
        self,
        type: DisplayMeshType,
        id: int,
        part_id: int,
        graphics: Graphics,
        model: prime.Model,
        vertices: np.array,
        facet_list: np.array,
        has_mesh: bool,
        zone_id: int = 0,
        zone_name: str = "",
        part_name: str = "",
        topo_edge_type: int = 0,
        number_of_edges: int = 0,
    ):
        """ """
        self._type = type
        self._id = id
        self._part_id = part_id
        self._geom_id = None
        self._mesh_id = None
        self._graphics = graphics
        self._model = model
        self._vertices = vertices
        self._facet_list = facet_list
        self._n_edges = number_of_edges
        self._topo_edge_type = topo_edge_type
        self._has_mesh = has_mesh
        self._poly_data = None
        self._actor = None
        self._show_edges = self._has_mesh if self._type is DisplayMeshType.TOPOFACE else True
        self._zone_id = zone_id
        self._zone_name = zone_name
        self._part_name = part_name
        # self.__update()

    @property
    def poly_data(self):
        return self._poly_data

    def __str__(self):
        if self._type == DisplayMeshType.TOPOFACE or self._type == DisplayMeshType.FACEZONELET:
            msg = "Selected FaceZonelet "
            if self._type is DisplayMeshType.TOPOFACE:
                msg = "Selected TopoFace "
            msg += str(self._id)
        elif self._type == DisplayMeshType.TOPOEDGE or self._type == DisplayMeshType.EDGEZONELET:
            msg = "Selected EdgeZonelet "
            if self._type is DisplayMeshType.TOPOEDGE:
                msg = "Selected TopoEdge "
            msg += str(self._id)
        msg += ", in Part Id : " + str(self._part_id) + ", Part Name : " + self._part_name + "\n"
        if self._zone_id > 0:
            msg += "Zone Id : " + str(self._zone_id) + ", Zone Name : " + self._zone_name
        return msg

    def add_to_plotter(self, plotter: Plotter):
        """ """
        if self._type == DisplayMeshType.TOPOFACE or self._type == DisplayMeshType.FACEZONELET:
            if self._poly_data == None:
                surf = pv.PolyData(self._vertices, self._facet_list)
                fcolor = np.array(self.get_face_color())
                colors = np.tile(fcolor, (surf.n_faces, 1))
                surf["colors"] = colors
                surf.disp_mesh = self
                self._poly_data = surf
            sh_edge = self._has_mesh if self._type is DisplayMeshType.TOPOFACE else True
            if self._poly_data.n_points > 0:
                self._actor = plotter.add_mesh(
                    self._poly_data, show_edges=sh_edge, scalars="colors", rgb=True, pickable=True
                )
        elif self._type == DisplayMeshType.TOPOEDGE or self._type == DisplayMeshType.EDGEZONELET:
            if self._poly_data == None:
                edge = pv.PolyData()
                edge.points = self._vertices
                cells = np.full((self._n_edges, 3), 2, dtype=np.int_)
                i = 0
                j = 0
                while j < len(self._facet_list):
                    nnodes = self._facet_list[j]
                    j += 1
                    cells[i, 1] = self._facet_list[j]
                    if nnodes == 2:
                        cells[i, 2] = self._facet_list[j + 1]
                    elif nnodes == 3:
                        cells[i, 2] = self._facet_list[j + 2]
                    j += nnodes
                    i += 1
                edge.lines = cells
                ecolor = np.array(self.get_edge_color())
                colors = np.tile(ecolor, (self._n_edges, 1))
                edge["colors"] = colors
                edge.disp_mesh = self
                self._poly_data = edge
            if self._poly_data.n_points > 0:
                self._actor = plotter.add_mesh(
                    self._poly_data, scalars="colors", rgb=True, line_width=4
                )
        elif self._type == DisplayMeshType.SPLINECONTROLPOINTS:
            if self._poly_data == None:
                surf = pv.PolyData(self._vertices, self._facet_list)
                fcolor = np.array([0, 0, 255])
                colors = np.tile(fcolor, (surf.n_faces, 1))
                surf["colors"] = colors
                surf.disp_mesh = self
                self._poly_data = surf
            if self._poly_data.n_points > 0:
                self._actor = plotter.add_mesh(
                    self._poly_data,
                    show_edges=True,
                    scalars="colors",
                    rgb=True,
                    pickable=False,
                    style='wireframe',
                    edge_color=[0, 0, 255],
                )
        elif self._type == DisplayMeshType.SPLINESURFACE:
            if self._poly_data == None:
                surf = pv.PolyData(self._vertices, self._facet_list)
                fcolor = np.array(color_matrix[1])
                colors = np.tile(fcolor, (surf.n_faces, 1))
                surf["colors"] = colors
                surf.disp_mesh = self
                self._poly_data = surf
            if self._poly_data.n_points > 0:
                self._actor = plotter.add_mesh(
                    self._poly_data, show_edges=False, scalars="colors", rgb=True, pickable=False
                )

    def get_face_color(self):
        """ """
        type = self._graphics.get_color_by_type()
        num_colors = int(color_matrix.size / 3)
        if type == ColorByType.ZONELET:
            return color_matrix[self._id % num_colors].tolist()
        elif type == ColorByType.PART:
            return color_matrix[self._part_id % num_colors].tolist()
        else:
            return color_matrix[self._zone_id % num_colors].tolist()

    def get_edge_color(self):
        """ """
        num_colors = int(color_matrix.size / 3)
        if self._type == DisplayMeshType.EDGEZONELET:
            return color_matrix[self._id % num_colors].tolist()
        elif self._type == DisplayMeshType.TOPOEDGE:
            if self._topo_edge_type == 1:
                return [255, 0, 0]
            elif self._topo_edge_type == 2:
                return [0, 0, 0]
            elif self._topo_edge_type == 3:
                return [0, 255, 255]
            elif self._topo_edge_type == 4:
                return [255, 0, 255]
            elif self._topo_edge_type == 5:
                return [255, 255, 0]
            elif self._topo_edge_type == 6:
                return [128, 0, 128]
            else:
                return color_matrix[self._id % num_colors].tolist()

    def deselect(self):
        if self._type == DisplayMeshType.TOPOFACE or self._type == DisplayMeshType.FACEZONELET:
            if self._poly_data != None:
                fcolor = np.array(self.get_face_color())
                colors = np.tile(fcolor, (self._poly_data.n_faces, 1))
                self._poly_data["colors"] = colors

    def select(self):
        if self._type == DisplayMeshType.TOPOFACE or self._type == DisplayMeshType.FACEZONELET:
            if self._poly_data != None:
                # fcolor = np.array([255, 255, 0])
                fcolor = np.array([233, 99, 28])
                colors = np.tile(fcolor, (self._poly_data.n_faces, 1))
                self._poly_data["colors"] = colors

    def hide(self, plotter: Plotter):
        plotter.remove_actor(self._actor)
        self._actor = None

    def clear(self, plotter: Plotter):
        plotter.remove_actor(self._actor)
        del self._actor
        self._actor = None

    def unhide(self, plotter: Plotter):
        if self._actor is None and self._poly_data.n_points > 0:
            self._actor = plotter.add_mesh(
                self._poly_data,
                show_edges=self._show_edges,
                scalars="colors",
                rgb=True,
                pickable=True,
            )

    def show_edges(self, show: bool):
        if self._actor is not None and self._has_mesh:
            prop = self._actor.GetProperty()
            self._show_edges = not prop.GetEdgeVisibility()
            prop.SetEdgeVisibility(not prop.GetEdgeVisibility())

    def set_color_by_type(self, type: ColorByType):
        """ """
        if self._type == DisplayMeshType.TOPOFACE or self._type == DisplayMeshType.FACEZONELET:
            if self._poly_data != None:
                fcolor = np.array(self.get_face_color())
                colors = np.tile(fcolor, (self._poly_data.n_faces, 1))
                self._poly_data["colors"] = colors

    @property
    def type(self):
        return self._type
