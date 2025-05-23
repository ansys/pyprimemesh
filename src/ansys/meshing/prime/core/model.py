# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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
from typing import Iterable, List

# isort: split
from ansys.meshing.prime.autogen.model import Model as _Model

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
        self._freeze()

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
        self._parts = [Part(self, part[0], part[1], part[2]) for part in part_data]
        self._control_data = ControlData(self, -1, res["ControlData"], "")
        self._control_data._update_size_controls(sc_data)
        self._control_data._update_prism_controls(pc_data)
        self._control_data._update_shell_bl_controls(shc_data)
        self._control_data._update_wrapper_controls(wc_data)
        self._control_data._update_multi_zone_controls(mc_data)
        self._control_data._update_volume_controls(vc_data)
        self._control_data._update_thin_volume_controls(tvc_data)
        self._topo_data = TopoData(self, -1, res["TopoData"], "")
        if "PeriodicControl" in res:
            self._control_data._update_periodic_controls(percon_data)
        self._material_point_data = MaterialPointManager(self, -1, res["MaterialPointData"], "")

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
            for id in part_ids:
                for part in list(self._parts):
                    if part.id == id:
                        self._parts.remove(part)
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

    def set_working_directory(self, path: str):
        """Set working directory.

        Set the working directory to be considered for file i/o when the file paths are relative.

        Parameters
        ----------
        path : str
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

    def get_scoped_polydata(self, scope, update: bool = False):
        """Get the scoped polydata of the model.

        Parameters
        ----------
        scope : Scope
            Scope of the model.

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
