""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class ThinVolumeMeshParams(CoreObject):
    """Parameters to generate thin volume mesh. This is for internal use only.
    """
    _default_params = {}

    def __initialize(
            self,
            n_layers: int,
            no_side_imprint: bool,
            n_ignore_rings: int):
        self._n_layers = n_layers
        self._no_side_imprint = no_side_imprint
        self._n_ignore_rings = n_ignore_rings

    def __init__(
            self,
            model: CommunicationManager=None,
            n_layers: int = None,
            no_side_imprint: bool = None,
            n_ignore_rings: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ThinVolumeMeshParams.

        Parameters
        ----------
        model: Model
            Model to create a ThinVolumeMeshParams object with default parameters.
        n_layers: int, optional
            Number of thin volume layers to be generated.
        no_side_imprint: bool, optional
            Checks whether to imprint quad faces on side zonelets.
        n_ignore_rings: int, optional
            Number of layers to ignore when no imprint on sides.
        json_data: dict, optional
            JSON dictionary to create a ThinVolumeMeshParams object with provided parameters.

        Examples
        --------
        >>> thin_volume_mesh_params = prime.ThinVolumeMeshParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nLayers"] if "nLayers" in json_data else None,
                json_data["noSideImprint"] if "noSideImprint" in json_data else None,
                json_data["nIgnoreRings"] if "nIgnoreRings" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [n_layers, no_side_imprint, n_ignore_rings])
            if all_field_specified:
                self.__initialize(
                    n_layers,
                    no_side_imprint,
                    n_ignore_rings)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ThinVolumeMeshParams")
                    json_data = param_json["ThinVolumeMeshParams"] if "ThinVolumeMeshParams" in param_json else {}
                    self.__initialize(
                        n_layers if n_layers is not None else ( ThinVolumeMeshParams._default_params["n_layers"] if "n_layers" in ThinVolumeMeshParams._default_params else (json_data["nLayers"] if "nLayers" in json_data else None)),
                        no_side_imprint if no_side_imprint is not None else ( ThinVolumeMeshParams._default_params["no_side_imprint"] if "no_side_imprint" in ThinVolumeMeshParams._default_params else (json_data["noSideImprint"] if "noSideImprint" in json_data else None)),
                        n_ignore_rings if n_ignore_rings is not None else ( ThinVolumeMeshParams._default_params["n_ignore_rings"] if "n_ignore_rings" in ThinVolumeMeshParams._default_params else (json_data["nIgnoreRings"] if "nIgnoreRings" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            n_layers: int = None,
            no_side_imprint: bool = None,
            n_ignore_rings: int = None):
        """Set the default values of ThinVolumeMeshParams.

        Parameters
        ----------
        n_layers: int, optional
            Number of thin volume layers to be generated.
        no_side_imprint: bool, optional
            Checks whether to imprint quad faces on side zonelets.
        n_ignore_rings: int, optional
            Number of layers to ignore when no imprint on sides.
        """
        args = locals()
        [ThinVolumeMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ThinVolumeMeshParams.

        Examples
        --------
        >>> ThinVolumeMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ThinVolumeMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._n_layers is not None:
            json_data["nLayers"] = self._n_layers
        if self._no_side_imprint is not None:
            json_data["noSideImprint"] = self._no_side_imprint
        if self._n_ignore_rings is not None:
            json_data["nIgnoreRings"] = self._n_ignore_rings
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_layers :  %s\nno_side_imprint :  %s\nn_ignore_rings :  %s" % (self._n_layers, self._no_side_imprint, self._n_ignore_rings)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def n_layers(self) -> int:
        """Number of thin volume layers to be generated.
        """
        return self._n_layers

    @n_layers.setter
    def n_layers(self, value: int):
        self._n_layers = value

    @property
    def no_side_imprint(self) -> bool:
        """Checks whether to imprint quad faces on side zonelets.
        """
        return self._no_side_imprint

    @no_side_imprint.setter
    def no_side_imprint(self, value: bool):
        self._no_side_imprint = value

    @property
    def n_ignore_rings(self) -> int:
        """Number of layers to ignore when no imprint on sides.
        """
        return self._n_ignore_rings

    @n_ignore_rings.setter
    def n_ignore_rings(self, value: int):
        self._n_ignore_rings = value
