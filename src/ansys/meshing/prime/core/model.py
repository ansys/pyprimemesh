# Copyright (C) 2026 ANSYS, Inc. and/or its affiliates.
# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

"""Module containing the managing logic of the Prime model."""
from typing import Iterable, List, Union

# isort: split
from ansys.meshing.prime.autogen.model import Model as _Model
from ansys.meshing.prime.autogen.topodata import TopoData

# isort: split
import os

import ansys.meshing.prime.internals.json_utils as json
from ansys.meshing.prime.autogen.commonstructs import DeleteResults
from ansys.meshing.prime.autogen.materialpointmanager import MaterialPointManager
from ansys.meshing.prime.autogen.modelstructs import (
    GlobalSizingParams,
    MergePartsParams,
    MergePartsResults,
)
from ansys.meshing.prime.autogen.primeconfig import ErrorCode
from ansys.meshing.prime.autogen.topodata import TopoData
from ansys.meshing.prime.core.controldata import ControlData
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.internals.communicator import Communicator
from ansys.meshing.prime.internals.error_handling import PrimeRuntimeError
from ansys.meshing.prime.internals.logger import PrimeLogger


class Model(_Model):
    """Contains all information about Ansys Prime Server.

    This class provides the nucleus of Ansys meshing technology. You can access
    any information in Ansys Prime Server only through the ``Model`` class.
    Using this class, you can query topo data, control data, parts, size fields,
    and more.

    Parameters
    ----------
    comm : Communicator
        Communicator to connect with the Ansys Prime server.
    id : int
        ID of the model.
    object_id : int
        Object ID of the model.
    name : str
        Name of the model.
    """

    __doc__ = _Model.__doc__

    def __init__(self, comm: Communicator, id: int, object_id: int, name: str):
        """Initialize the model and the parameters."""
        _Model.__init__(self, comm, id, object_id, name)
        self._parts = []
        self._global_sf_params = GlobalSizingParams(model=self)
        self._default_part = None
        self._topo_data = None
        self._control_data = None
        self._material_point_data = None
        self._model_pv_mesh = None
        self._use_standby_apis = False
        self._freeze()

    @property
    def progress_callback(self):
        """Get the current progress callback function.

        Returns
        -------
        function or None
            The current progress callback function, or None if no callback is set.
        """
        return self._comm._progress_callback

    @progress_callback.setter
    def progress_callback(self, callback):
        """Set a callback function to receive progress updates from the server.

        Parameters
        ----------
        callback : function
            A function that takes a single argument, which will be the progress update data
            from the server.

        Examples
        --------
            >>> def my_progress_callback(progress_data):
            ...     print("Progress update:", progress_data)
            ...
            >>> model.progress_callback = my_progress_callback

        """
        self._comm._progress_callback = callback

    def _sync_up_model(self):
        """Synchronize the client model with the server model.

        This method Updates proxy child objects of the client model with the
        child objects of the server model.

        Examples
        --------
        >>> from ansys.meshing.prime import Model
        >>> model = client.model
        >>> model._sync_up_model()
        """
        res = json.loads(
            self._comm.serve(self, "PrimeMesh::Model/GetChildObjectsJson", self._object_id, args={})
        )
        part_data = res["Parts"]
        sc_data = res["SizeControl"]
        pc_data = res["PrismControl"]
        shc_data = res["ShellBLControl"]
        wc_data = res["WrapperControl"]
        mc_data = res["MultiZoneControl"]
        vc_data = res["VolumeControl"]

        if "ThinVolumeControl" in res:
            tvc_data = res["ThinVolumeControl"]

        if "PeriodicControl" in res:
            percon_data = res["PeriodicControl"]

        sf_params = res["GlobalSizingParams"]

        self._global_sf_params = GlobalSizingParams(
            model=self, min=sf_params[0], max=sf_params[1], growth_rate=sf_params[2]
        )
        from ansys.meshing.prime import Part as PPart

        self._parts = [PPart(self, part[0], part[1], part[2]) for part in part_data]
        from ansys.meshing.prime import ControlData as CData

        self._control_data = CData(self, -1, res["ControlData"], "")
        self._control_data._update_size_controls(sc_data)
        self._control_data._update_prism_controls(pc_data)
        self._control_data._update_shell_bl_controls(shc_data)
        self._control_data._update_wrapper_controls(wc_data)
        self._control_data._update_multi_zone_controls(mc_data)
        self._control_data._update_volume_controls(vc_data)
        self._control_data._update_thin_volume_controls(tvc_data)
        from ansys.meshing.prime import TopoData as TData

        self._topo_data = TData(self, -1, res["TopoData"], "")
        if "PeriodicControl" in res:
            self._control_data._update_periodic_controls(percon_data)
        self._material_point_data = MaterialPointManager(self, -1, res["MaterialPointData"], "")

    def _update_size_controls(self):
        """Update size control proxy objects from the server model."""
        res = json.loads(
            self._comm.serve(self, "PrimeMesh::Model/GetChildObjectsJson", self._object_id, args={})
        )
        from ansys.meshing.prime import ControlData as CData

        if self._control_data is None:
            self._control_data = CData(self, -1, res["ControlData"], "")
        self._control_data._update_size_controls(res["SizeControl"])

    def _update_prism_controls(self):
        """Update prism control proxy objects from the server model."""
        res = json.loads(
            self._comm.serve(self, "PrimeMesh::Model/GetChildObjectsJson", self._object_id, args={})
        )
        from ansys.meshing.prime import ControlData as CData

        if self._control_data is None:
            self._control_data = CData(self, -1, res["ControlData"], "")
        self._control_data._update_prism_controls(res["PrismControl"])

    def _update_wrapper_controls(self):
        """Update wrapper control proxy objects from the server model."""
        res = json.loads(
            self._comm.serve(self, "PrimeMesh::Model/GetChildObjectsJson", self._object_id, args={})
        )
        from ansys.meshing.prime import ControlData as CData

        if self._control_data is None:
            self._control_data = CData(self, -1, res["ControlData"], "")
        self._control_data._update_wrapper_controls(res["WrapperControl"])

    def _add_part(self, id: int):
        """Add a part that is present on the server.

        Parameters
        ----------
        id : int
            ID of the part.

        Raises
        ------
        PrimeRuntimeError
            Raise if unable to create the part.
        """
        res = json.loads(
            self._comm.serve(self, "PrimeMesh::Model/GetChildObjectsJson", self._object_id, args={})
        )
        part_data = res["Parts"]
        new_part = None
        for part in part_data:
            if part[0] == id:
                new_part = Part(self, part[0], part[1], part[2])
                self._parts.append(new_part)
                break
        if new_part == None:
            raise PrimeRuntimeError("Unable to create part", ErrorCode.PARTNOTFOUND)

    def _add_parts(self, ids: Iterable[int]):
        """Add parts that are present on the server.

        Parameters
        ----------
        ids : Iterable[int]
            Ids of the parts.

        Raises
        ------
        PrimeRuntimeError
            Raise if unable to create any of the parts.
        """
        res = json.loads(
            self._comm.serve(self, "PrimeMesh::Model/GetChildObjectsJson", self._object_id, args={})
        )
        part_data = res["Parts"]
        added_parts = []
        for part in part_data:
            if part[0] in ids:
                new_part = Part(self, part[0], part[1], part[2])
                self._parts.append(new_part)
                added_parts.append(part[0])

        missing_parts = set(ids) - set(added_parts)
        if missing_parts:
            raise PrimeRuntimeError(
                f"Unable to create parts with IDs: {missing_parts}", ErrorCode.PARTNOTFOUND
            )

    def _remove_parts(self, part_ids: Iterable[int]):
        """Remove already deleted parts from the client model.

        Parameters
        ----------
        part_ids : Iterable[int]
            Ids of parts to remove.

        Returns
        -------
        None
            This method does not return any value.


        Examples
        --------
            >>> results = model.remove_parts(part_ids)

        """
        for id in part_ids:
            for part in list(self._parts):
                if part.id == id:
                    self._parts.remove(part)

    def get_part_by_name(self, name: str) -> Part:
        """Get the part by name.

        Parameters
        ----------
        name : str
            Name of the part.

        Returns
        -------
        Part
            Part or ``None`` if the given part name doesn't exist.

        Examples
        --------
            >>> from ansys.meshing.prime import Model
            >>> model = client.model
            >>> part = model.get_part_by_name("part.1")
        """
        for part in self._parts:
            if part.name == name:
                return part
        return None

    def get_part(self, id: int) -> Part:
        """Get the part by ID.

        Parameters
        ----------
        id : int
            ID of the part.

        Returns
        -------
        Part
            Part or ``None`` if the given part ID doesn't exist.

        Examples
        --------
            >>> from ansys.meshing.prime import Model
            >>> model = client.model
            >>> part = model.get_part(2)
        """
        for part in self._parts:
            if part.id == id:
                return part
        return None

    def merge_parts(self, part_ids: Iterable[int], params: MergePartsParams) -> MergePartsResults:
        """Merge multiple parts into a single part.

        Parameters
        ----------
        part_ids : Iterable[int]
            IDs of the parts to merge.
        params : MergePartsParams
            Parameters for merging parts.

        Returns
        -------
        MergePartsResults
            Results for merging the parts into a single part.


        Examples
        --------
        >>> params = prime.MergePartsParams(model = model)
        >>> results = model.merge_parts(part_ids, params)

        """
        res = _Model.merge_parts(self, part_ids, params)
        merged_part = self.get_part_by_name(res.merged_part_assigned_name)
        if merged_part is None:
            self._sync_up_model()
        else:
            for id in part_ids:
                part = self.get_part(id)
                if part.id != merged_part.id:
                    self._parts.remove(part)
        return res

    def delete_parts(self, part_ids: Iterable[int]) -> DeleteResults:
        """Delete parts and their contents.

        Parameters
        ----------
        part_ids : Iterable[int]
            IDs of parts to delete.

        Returns
        -------
        DeleteResults
            Results from deleting parts and their contents.


        Examples
        --------
        >>> results = model.delete_parts(part_ids)

        """
        res = _Model.delete_parts(self, part_ids)
        if res.error_code == ErrorCode.NOERROR:
            self._remove_parts(part_ids)
        return res

    def get_global_sizing_params(self) -> GlobalSizingParams:
        """Get global sizing parameters.

        Returns
        -------
        GlobalSizingParams
            Global sizing parameters.

        Examples
        --------
            >>> model = client.model
            >>> sf_params = model.get_global_sizing_params()
        """
        return self._global_sf_params

    def set_global_sizing_params(self, params: GlobalSizingParams):
        """Set global sizing parameters.

        Parameters
        ----------
        params : GlobalSizingParams
            Global sizing parameters for initializing surfer parameters and
            various size control parameters.

        Examples
        --------
        >>> model = client.model
        >>> model.set_global_sizing_params(GlobalSizingParams(model=model,
        ...                                          min=0.1,
        ...                                          max=1.0,
        ...                                          growth_rate=1.2))
        """
        _Model.set_global_sizing_params(self, params)
        self._global_sf_params = params

    def set_working_directory(self, path: Union[str, os.PathLike]):
        """Set working directory.

        Set the working directory to be considered for file i/o when the file paths are relative.

        Parameters
        ----------
        path : str, os.PathLike
            Path to the directory.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> client = prime.launch_prime()
        >>> model = client.model
        >>> zones = model.set_working_directory("C:/input_files")

        """
        path = os.fspath(path)
        _Model.set_working_directory(self, path)
        os.chdir(path)

    def __str__(self):
        """Print the summary of the model.

        Returns
        -------
        str
            Summary of the model.

        Examples
        --------
        >>> from ansys.meshing.prime import Model
        >>> model = client.model
        >>> print(model)
        """
        result = ""
        result += "Part Summary:\n"
        for part in self._parts:
            result += part.__str__() + "\n"
        return result

    @property
    def parts(self) -> List[Part]:
        """Get the list of parts for the model.

        Returns
        -------
        List[Part]
            List of parts for the model.

        Examples
        --------
            >>> from ansys.meshing.prime import Model
            >>> model = client.model
            >>> parts = model.parts
        """
        return self._parts

    @property
    def topo_data(self) -> TopoData:
        """Get the TopoData for the model.

        Returns
        -------
        TopoData
            TopoData for the model.

        Examples
        --------
            >>> topo_data=model.topo_data
        """
        return self._topo_data

    @property
    def control_data(self) -> ControlData:
        """Get the control data for the model.

        Returns
        -------
        ControlData
            Control data for the model.

        Examples
        --------
            >>> control_data = model.control_data
        """
        if self._control_data is None:
            self._sync_up_model()
        return self._control_data

    @property
    def material_point_data(self) -> MaterialPointManager:
        """Get material point data for the model.

        The Material Point Manager is used to create, delete, and manage material points.

        Returns
        -------
        MaterialPointManager
            Material Point Manager.

        Examples
        --------
            >>> mpt_data = model.material_point_data
        """
        if self._material_point_data is None:
            self._sync_up_model()
        return self._material_point_data

    @property
    def python_logger(self):
        """Get python standard logger from PyPrimeMesh's logger instance.

        PyPrimeMesh's python standard logger instance can be used to control
        the verbosity of messages printed by PyPrimeMesh and more.

        Returns
        -------
        logging.Logger
            PyPrimeMesh's python standard logger instance.

        Examples
        --------
        Set log level to debug.

        >>> model.python_logger.setLevel(logging.DEBUG)

        """
        return PrimeLogger().python_logger

    @property
    def logger(self) -> PrimeLogger:
        """Get PyPrimeMesh's logger instance.

        PyPrimeMesh's logger instance can be used to save the logs to a file,
        redirect the logs to the given stream, control the verbosity
        of messages printed by PyPrimeMesh and more.

        Returns
        -------
        PrimeLogger
            PyPrimeMesh's logger instance.

        Examples
        --------
        Save logs to a file.

        >>> model.logger.add_file_handler(logs_dir=r"./tmp")

        """
        return PrimeLogger()

    @property
    def use_standby_apis(self) -> bool:
        """Get the status of using standby APIs.

        Returns
        -------
        bool
            True if standby APIs are being used, False otherwise.

        Examples
        --------
            >>> model.use_standby_apis
        """
        return self._use_standby_apis

    @use_standby_apis.setter
    def use_standby_apis(self, value: bool):
        """Set the status of using standby APIs.

        Parameters
        ----------
        value : bool
            True to use standby APIs, False otherwise.

        Examples
        --------
            >>> model.use_standby_apis = True
        """
        self._use_standby_apis = value

    def as_polydata(self, update: bool = False):
        """Get the model as a polydata.

        Parameters
        ----------
        update : bool, optional
            Update the polydata if it is already present, by default False.

        Returns
        -------
        vtk.vtkPolyData
            Polydata of the model.

        Examples
        --------
            >>> polydata = model.as_polydata()
        """
        try:
            from ansys.meshing.prime.core.mesh import Mesh
        except ImportError:
            raise ImportError(
                "Please install optional dependencies to use visualization features:"
                + "pip install ansys-meshing-prime[all]"
            )
        if self._model_pv_mesh is None or update:
            self._model_pv_mesh = Mesh(self)
        return self._model_pv_mesh.as_polydata(update=update)

    def build_render_data(self, update: bool = False):
        """Build merged render geometry for :class:`PrimePlotter`.

        Parameters
        ----------
        update : bool, optional
            Rebuild even when cached data is present, by default False.

        Returns
        -------
        ModelRenderData
            Model-wide render geometry grouped by entity type.
        """
        try:
            from ansys.meshing.prime.core.mesh import Mesh
        except ImportError:
            raise ImportError(
                "Please install optional dependencies to use visualization features:"
                + "pip install ansys-meshing-prime[all]"
            )
        if self._model_pv_mesh is None or update:
            self._model_pv_mesh = Mesh(self)
        return self._model_pv_mesh.build_render_data(update=update)

    def get_scoped_render_data(self, scope, update: bool = False):
        """Build merged render geometry for a scope.

        Parameters
        ----------
        scope : Scope
            Scope of the model.
        update : bool, optional
            Rebuild even when cached data is present, by default False.

        Returns
        -------
        ModelRenderData
            Scoped model-wide render geometry.
        """
        try:
            from ansys.meshing.prime.core.mesh import Mesh
        except ImportError:
            raise ImportError(
                "Please install optional dependencies to use visualization features:"
                + "pip install ansys-meshing-prime[all]"
            )
        if self._model_pv_mesh is None or update:
            self._model_pv_mesh = Mesh(self)
        return self._model_pv_mesh.get_scoped_render_data(scope, update=update)

    def get_scoped_polydata(self, scope, update: bool = False):
        """Get the scoped polydata of the model.

        Parameters
        ----------
        scope : Scope
            Scope of the model.
        update : bool, default: False
            Whether to rebuild the geometry rather than reuse what is cached.

        Returns
        -------
        vtk.vtkPolyData
            Scoped polydata of the model.

        Examples
        --------
            >>> scoped_polydata = model.get_scoped_polydata(scope)
        """
        try:
            from ansys.meshing.prime.core.mesh import Mesh
        except ImportError:
            raise ImportError(
                "Please install optional dependencies to use visualization features:"
                + "pip install ansys-meshing-prime[all]"
            )

        if self._model_pv_mesh is None or update:
            self._model_pv_mesh = Mesh(self)
        return self._model_pv_mesh.get_scoped_polydata(scope, update=update)

    def create_part(self, suggested_name: str) -> Part:
        """Create a part with the given name.

        Parameters
        ----------
        suggested_name : str
            Name of the part.

        Returns
        -------
        Part
            Returns a part with the given name.


        Examples
        --------
        >>> new_part = model.create_part('part_name')

        """
        res = super().create_part(suggested_name)
        self._add_part(res[0])
        return self.get_part(res[0])

    def as_usd(self, update: bool = False):
        """Get the model as USD geometry DTOs.

        Parameters
        ----------
        update : bool, optional
            Update the USD geometry if it is already present, by default False.

        Returns
        -------
        dict
            Dictionary mapping part_id -> {"faces": [...], "edges": [...],
            "ctrlpts": [...], "splinesurf": [...]} where each list contains
            FaceGeometry, EdgeGeometry, or SplineGeometry DTOs.

        Examples
        --------
        >>> usd_geom = model.as_usd()
        >>> for part_id, geoms in usd_geom.items():
        ...     for face_geom in geoms.get("faces", []):
        ...         print(face_geom.mesh_id, face_geom.color)
        """
        try:
            from ansys.meshing.prime.core.mesh import MeshUSD
        except ImportError:
            raise ImportError(
                "Please install optional dependencies to use visualization features:"
                + "pip install ansys-meshing-prime[all]"
            )
        if self._model_usd_mesh is None or update:
            self._model_usd_mesh = MeshUSD(self)
        return self._model_usd_mesh.as_usd(update=update)

    def get_scoped_usd(self, scope, update: bool = False):
        """Get the scoped USD geometry of the model.

        Parameters
        ----------
        scope : Scope
            Scope of the model.
        update : bool, optional
            Update the USD geometry if it is already present, by default False.

        Returns
        -------
        dict
            Dictionary mapping part_id -> {"faces": [...], "edges": [...], ...}
            containing only geometry within the specified scope.

        Examples
        --------
        >>> scoped_usd = model.get_scoped_usd(scope)
        """
        try:
            from ansys.meshing.prime.core.mesh import MeshUSD
        except ImportError:
            raise ImportError(
                "Please install optional dependencies to use visualization features:"
                + "pip install ansys-meshing-prime[all]"
            )

        if self._model_usd_mesh is None or update:
            self._model_usd_mesh = MeshUSD(self)
        return self._model_usd_mesh.get_scoped_usd(scope, update=update)
