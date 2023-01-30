""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class VolumeControlParams(CoreObject):
    """Volume control parameters are used to define the volume type in the volume control.
    """
    _default_params = {}

    def __initialize(
            self,
            cell_zonelet_type: CellZoneletType):
        self._cell_zonelet_type = CellZoneletType(cell_zonelet_type)

    def __init__(
            self,
            model: CommunicationManager=None,
            cell_zonelet_type: CellZoneletType = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the VolumeControlParams.

        Parameters
        ----------
        model: Model
            Model to create a VolumeControlParams object with default parameters.
        cell_zonelet_type: CellZoneletType, optional
            Cell zonelet type is used to define the type of the associated volume.
        json_data: dict, optional
            JSON dictionary to create a VolumeControlParams object with provided parameters.

        Examples
        --------
        >>> volume_control_params = prime.VolumeControlParams(model = model)
        """
        if json_data:
            self.__initialize(
                CellZoneletType(json_data["cellZoneletType"] if "cellZoneletType" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [cell_zonelet_type])
            if all_field_specified:
                self.__initialize(
                    cell_zonelet_type)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "VolumeControlParams")
                    json_data = param_json["VolumeControlParams"] if "VolumeControlParams" in param_json else {}
                    self.__initialize(
                        cell_zonelet_type if cell_zonelet_type is not None else ( VolumeControlParams._default_params["cell_zonelet_type"] if "cell_zonelet_type" in VolumeControlParams._default_params else CellZoneletType(json_data["cellZoneletType"] if "cellZoneletType" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            cell_zonelet_type: CellZoneletType = None):
        """Set the default values of VolumeControlParams.

        Parameters
        ----------
        cell_zonelet_type: CellZoneletType, optional
            Cell zonelet type is used to define the type of the associated volume.
        """
        args = locals()
        [VolumeControlParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of VolumeControlParams.

        Examples
        --------
        >>> VolumeControlParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VolumeControlParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._cell_zonelet_type is not None:
            json_data["cellZoneletType"] = self._cell_zonelet_type
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "cell_zonelet_type :  %s" % (self._cell_zonelet_type)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def cell_zonelet_type(self) -> CellZoneletType:
        """Cell zonelet type is used to define the type of the associated volume.
        """
        return self._cell_zonelet_type

    @cell_zonelet_type.setter
    def cell_zonelet_type(self, value: CellZoneletType):
        self._cell_zonelet_type = value
