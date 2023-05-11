""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class BCsVolumetricModality(enum.IntEnum):
    """Indicate options to identify morphable region in input volumetric mesh.
    """
    BOX = 1
    """Option to identify nodes enclosed by bounding box as morphable nodes from the input volumetric mesh."""
    ALL = 2
    """Option to identify all nodes expect fixed nodes as morphable nodes from the input volumetric mesh."""

class MorphBCParams(CoreObject):
    """MorphBCParams contains the input parameters for calculating the boundary conditions for a morphing problem.
    """
    _default_params = {}

    def __initialize(
            self,
            morph_region_method: BCsVolumetricModality,
            morphable_layers: int,
            morph_region_box_extension: float):
        self._morph_region_method = BCsVolumetricModality(morph_region_method)
        self._morphable_layers = morphable_layers
        self._morph_region_box_extension = morph_region_box_extension

    def __init__(
            self,
            model: CommunicationManager=None,
            morph_region_method: BCsVolumetricModality = None,
            morphable_layers: int = None,
            morph_region_box_extension: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the MorphBCParams.

        Parameters
        ----------
        model: Model
            Model to create a MorphBCParams object with default parameters.
        morph_region_method: BCsVolumetricModality, optional
            Indicate options to identify morphable regions in the input volumetric mesh.
        morphable_layers: int, optional
            Number of layers around defined boundary.
        morph_region_box_extension: float, optional
            Percentage extension for the volumetric box.
        json_data: dict, optional
            JSON dictionary to create a MorphBCParams object with provided parameters.

        Examples
        --------
        >>> morph_bcparams = prime.MorphBCParams(model = model)
        """
        if json_data:
            self.__initialize(
                BCsVolumetricModality(json_data["morphRegionMethod"] if "morphRegionMethod" in json_data else None),
                json_data["morphableLayers"] if "morphableLayers" in json_data else None,
                json_data["morphRegionBoxExtension"] if "morphRegionBoxExtension" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [morph_region_method, morphable_layers, morph_region_box_extension])
            if all_field_specified:
                self.__initialize(
                    morph_region_method,
                    morphable_layers,
                    morph_region_box_extension)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "MorphBCParams")
                    json_data = param_json["MorphBCParams"] if "MorphBCParams" in param_json else {}
                    self.__initialize(
                        morph_region_method if morph_region_method is not None else ( MorphBCParams._default_params["morph_region_method"] if "morph_region_method" in MorphBCParams._default_params else BCsVolumetricModality(json_data["morphRegionMethod"] if "morphRegionMethod" in json_data else None)),
                        morphable_layers if morphable_layers is not None else ( MorphBCParams._default_params["morphable_layers"] if "morphable_layers" in MorphBCParams._default_params else (json_data["morphableLayers"] if "morphableLayers" in json_data else None)),
                        morph_region_box_extension if morph_region_box_extension is not None else ( MorphBCParams._default_params["morph_region_box_extension"] if "morph_region_box_extension" in MorphBCParams._default_params else (json_data["morphRegionBoxExtension"] if "morphRegionBoxExtension" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            morph_region_method: BCsVolumetricModality = None,
            morphable_layers: int = None,
            morph_region_box_extension: float = None):
        """Set the default values of MorphBCParams.

        Parameters
        ----------
        morph_region_method: BCsVolumetricModality, optional
            Indicate options to identify morphable regions in the input volumetric mesh.
        morphable_layers: int, optional
            Number of layers around defined boundary.
        morph_region_box_extension: float, optional
            Percentage extension for the volumetric box.
        """
        args = locals()
        [MorphBCParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MorphBCParams.

        Examples
        --------
        >>> MorphBCParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MorphBCParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._morph_region_method is not None:
            json_data["morphRegionMethod"] = self._morph_region_method
        if self._morphable_layers is not None:
            json_data["morphableLayers"] = self._morphable_layers
        if self._morph_region_box_extension is not None:
            json_data["morphRegionBoxExtension"] = self._morph_region_box_extension
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "morph_region_method :  %s\nmorphable_layers :  %s\nmorph_region_box_extension :  %s" % (self._morph_region_method, self._morphable_layers, self._morph_region_box_extension)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def morph_region_method(self) -> BCsVolumetricModality:
        """Indicate options to identify morphable regions in the input volumetric mesh.
        """
        return self._morph_region_method

    @morph_region_method.setter
    def morph_region_method(self, value: BCsVolumetricModality):
        self._morph_region_method = value

    @property
    def morphable_layers(self) -> int:
        """Number of layers around defined boundary.
        """
        return self._morphable_layers

    @morphable_layers.setter
    def morphable_layers(self, value: int):
        self._morphable_layers = value

    @property
    def morph_region_box_extension(self) -> float:
        """Percentage extension for the volumetric box.
        """
        return self._morph_region_box_extension

    @morph_region_box_extension.setter
    def morph_region_box_extension(self, value: float):
        self._morph_region_box_extension = value
