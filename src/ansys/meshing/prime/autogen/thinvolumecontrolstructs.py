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

    Parameters
    ----------
    model: Model
        Model to create a ``ThinVolumeMeshParams`` object with default parameters.
    n_layers: int, optional
        Number of thin volume layers to be generated.
    imprint_sides: bool, optional
        Checks whether to imprint quad faces on side zonelets.
    n_ignore_rings: int, optional
        Number of rings of cells at the sides to ignore when no imprint on sides. Volume fill type will be used in this buffer region at the thin volume sides to transition to thin volume mesh internally.
    json_data: dict, optional
        JSON dictionary to create a ``ThinVolumeMeshParams`` object with provided parameters.

    Examples
    --------
    >>> thin_volume_mesh_params = prime.ThinVolumeMeshParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            n_layers: int,
            imprint_sides: bool,
            n_ignore_rings: int):
        self._n_layers = n_layers
        self._imprint_sides = imprint_sides
        self._n_ignore_rings = n_ignore_rings

    def __init__(
            self,
            model: CommunicationManager=None,
            n_layers: int = None,
            imprint_sides: bool = None,
            n_ignore_rings: int = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ThinVolumeMeshParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ThinVolumeMeshParams`` object with default parameters.
        n_layers: int, optional
            Number of thin volume layers to be generated.
        imprint_sides: bool, optional
            Checks whether to imprint quad faces on side zonelets.
        n_ignore_rings: int, optional
            Number of rings of cells at the sides to ignore when no imprint on sides. Volume fill type will be used in this buffer region at the thin volume sides to transition to thin volume mesh internally.
        json_data: dict, optional
            JSON dictionary to create a ``ThinVolumeMeshParams`` object with provided parameters.

        Examples
        --------
        >>> thin_volume_mesh_params = prime.ThinVolumeMeshParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nLayers"] if "nLayers" in json_data else None,
                json_data["imprintSides"] if "imprintSides" in json_data else None,
                json_data["nIgnoreRings"] if "nIgnoreRings" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [n_layers, imprint_sides, n_ignore_rings])
            if all_field_specified:
                self.__initialize(
                    n_layers,
                    imprint_sides,
                    n_ignore_rings)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ThinVolumeMeshParams")
                    json_data = param_json["ThinVolumeMeshParams"] if "ThinVolumeMeshParams" in param_json else {}
                    self.__initialize(
                        n_layers if n_layers is not None else ( ThinVolumeMeshParams._default_params["n_layers"] if "n_layers" in ThinVolumeMeshParams._default_params else (json_data["nLayers"] if "nLayers" in json_data else None)),
                        imprint_sides if imprint_sides is not None else ( ThinVolumeMeshParams._default_params["imprint_sides"] if "imprint_sides" in ThinVolumeMeshParams._default_params else (json_data["imprintSides"] if "imprintSides" in json_data else None)),
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
            imprint_sides: bool = None,
            n_ignore_rings: int = None):
        """Set the default values of the ``ThinVolumeMeshParams`` object.

        Parameters
        ----------
        n_layers: int, optional
            Number of thin volume layers to be generated.
        imprint_sides: bool, optional
            Checks whether to imprint quad faces on side zonelets.
        n_ignore_rings: int, optional
            Number of rings of cells at the sides to ignore when no imprint on sides. Volume fill type will be used in this buffer region at the thin volume sides to transition to thin volume mesh internally.
        """
        args = locals()
        [ThinVolumeMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ThinVolumeMeshParams`` object.

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
        if self._imprint_sides is not None:
            json_data["imprintSides"] = self._imprint_sides
        if self._n_ignore_rings is not None:
            json_data["nIgnoreRings"] = self._n_ignore_rings
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_layers :  %s\nimprint_sides :  %s\nn_ignore_rings :  %s" % (self._n_layers, self._imprint_sides, self._n_ignore_rings)
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
    def imprint_sides(self) -> bool:
        """Checks whether to imprint quad faces on side zonelets.
        """
        return self._imprint_sides

    @imprint_sides.setter
    def imprint_sides(self, value: bool):
        self._imprint_sides = value

    @property
    def n_ignore_rings(self) -> int:
        """Number of rings of cells at the sides to ignore when no imprint on sides. Volume fill type will be used in this buffer region at the thin volume sides to transition to thin volume mesh internally.
        """
        return self._n_ignore_rings

    @n_ignore_rings.setter
    def n_ignore_rings(self, value: int):
        self._n_ignore_rings = value
