from typing import Iterable, List

# isort: split
from ansys.meshing.prime.autogen.model import Model as _Model

# isort: split
import ansys.meshing.prime.internals.json_utils as json
from ansys.meshing.prime.autogen.commonstructs import DeleteResults
from ansys.meshing.prime.autogen.materialpointmanager import MaterialPointManager
from ansys.meshing.prime.autogen.modelstructs import (
    GlobalSizingParams,
    MergePartsParams,
    MergePartsResults,
)
from ansys.meshing.prime.autogen.primeconfig import ErrorCode
from ansys.meshing.prime.core.controldata import ControlData
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.internals.communicator import Communicator
from ansys.meshing.prime.internals.error_handling import PrimeRuntimeError


class Model(_Model):
    __doc__ = _Model.__doc__

    def __init__(self, comm: Communicator, id: int, object_id: int, name: str):
        """Initialize Model"""
        _Model.__init__(self, comm, id, object_id, name)
        self._parts = []
        self._global_sf_params = GlobalSizingParams(model=self)
        self._default_part = None
        self._topo_data = None
        self._control_data = None
        self._material_point_data = None
        self._freeze()

    def _sync_up_model(self):
        """Synchronizes client model with the server model.

        Updates proxy child objects of the client model with the child objects of the server model.

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
        wc_data = res["WrapperControl"]
        vc_data = res["VolumeControl"]
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
        self._control_data._update_wrapper_controls(wc_data)
        self._control_data._update_volume_controls(vc_data)
        if "PeriodicControl" in res:
            self._control_data._update_periodic_controls(percon_data)
        self._material_point_data = MaterialPointManager(self, -1, res["MaterialPointData"], "")

    def _add_part(self, id: int):
        """Add a part that is present on server."""
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
        """Gets the part by name. Returns None if part doesn't exist for the given name.

        Parameters
        ----------
        name : str
            Name of the part.

        Returns
        -------
        Part
            Returns the part.

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
        """Gets the part by id. Returns None if part doesn't exist for the given id.

        Parameters
        ----------
        id : int
            Id of the part.

        Returns
        -------
        Part
            Returns the part.

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
        """Merges given parts into one.


        Parameters
        ----------
        part_ids : Iterable[int]
            Ids of parts to be merged.
        params : MergePartsParams
            Parameters to merge parts.

        Returns
        -------
        MergePartsResults
            Returns the MergePartsResults.


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
        """Deletes the parts and its contents.


        Parameters
        ----------
        part_ids : Iterable[int]
            Ids of parts to be deleted.

        Returns
        -------
        DeleteResults
            Returns DeleteResults.


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
        """Gets the GlobalSizingParams.

        Returns
        -------
        GlobalSizingParams
            Returns the GlobalSizingParams.

        Examples
        --------
            >>> model = client.model
            >>> sf_params = model.get_global_sizing_params()
        """
        return self._global_sf_params

    def set_global_sizing_params(self, params: GlobalSizingParams):
        """Sets the global sizing parameters.

        Sets the global sizing params to initialize surfer parameters and various size control
        parameters.

        Parameters
        ----------
        params : GlobalSizingParams
             Global sizing parameters.

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

    def __str__(self):
        """Prints the summary of the model.

        Returns
        -------
        str
            Returns the summary of the model.

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
        """Gets the list of parts of a model.

        Returns
        -------
        List[Part]
            Returns the list of parts.

        Examples
        --------
            >>> from ansys.meshing.prime import Model
            >>> model = client.model
            >>> parts = model.parts
        """
        return self._parts

    @property
    def control_data(self) -> ControlData:
        """Gets the control data of a model.

        Returns
        -------
        ControlData
            Returns the control data.

        Examples
        --------
            >>> control_data = model.control_data
        """
        return self._control_data

    @property
    def material_point_data(self) -> MaterialPointManager:
        """Get Material Point Data.

        MaterialPointManager is used to create, delete and manage material points.

        Returns
        -------
        MaterialPointManager
            Returns the material point manager.

        Examples
        --------
            >>> mpt_data = model.material_point_data
        """
        return self._material_point_data

    @property
    def python_logger(self):
        """Get PyPrimeMesh's Logger instance.

        PyPrimeMesh's Logger instance can be used to control the verbosity
        of messages printed by PyPrimeMesh.

        Returns
        -------
        Logger
             Returns logging.Logger instance.

        Examples
        --------
        Set log level to debug.

        >>> model.python_logger.setLevel(logging.DEBUG)

        """
        return self._logger
