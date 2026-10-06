# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

class FeatureRecoveryControlSummaryResult(CoreObject):
    """Results of Feature Recovery control summary.

    Parameters
    ----------
    model : Model
        Model to create a ``FeatureRecoveryControlSummaryResult`` object with default parameters.
    message : str, optional
        Feature Recovery control summary text.
    json_data : dict, optional
        JSON dictionary to create a ``FeatureRecoveryControlSummaryResult`` object with provided parameters.

    Examples
    --------
    >>> feature_recovery_control_summary_result = prime.FeatureRecoveryControlSummaryResult(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            message : str):
        self._message = message

    def __init__(
            self,
            model: CommunicationManager=None,
            message : str = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``FeatureRecoveryControlSummaryResult`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``FeatureRecoveryControlSummaryResult`` object with default parameters.
        message : str, optional
            Feature Recovery control summary text.
        json_data : dict, optional
            JSON dictionary to create a ``FeatureRecoveryControlSummaryResult`` object with provided parameters.

        Examples
        --------
        >>> feature_recovery_control_summary_result = prime.FeatureRecoveryControlSummaryResult(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["message"] if "message" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [message])
            if all_field_specified:
                self.__initialize(
                    message)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "FeatureRecoveryControlSummaryResult")
                    json_data = param_json["FeatureRecoveryControlSummaryResult"] if "FeatureRecoveryControlSummaryResult" in param_json else {}
                    self.__initialize(
                        message if message is not None else ( FeatureRecoveryControlSummaryResult._default_params["message"] if "message" in FeatureRecoveryControlSummaryResult._default_params else (json_data["message"] if "message" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            message : str = None):
        """Set the default values of the ``FeatureRecoveryControlSummaryResult`` object.

        Parameters
        ----------
        message : str, optional
            Feature Recovery control summary text.
        """
        args = locals()
        [FeatureRecoveryControlSummaryResult._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``FeatureRecoveryControlSummaryResult`` object.

        Examples
        --------
        >>> FeatureRecoveryControlSummaryResult.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FeatureRecoveryControlSummaryResult._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._message is not None:
            json_data["message"] = self._message
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "message :  %s" % (self._message)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def message(self) -> str:
        """Feature Recovery control summary text.
        """
        return self._message

    @message.setter
    def message(self, value: str):
        self._message = value

class FeatureRecoveryControlSummaryParams(CoreObject):
    """Parameters used to get Feature Recovery control summary.

    Parameters
    ----------
    model : Model
        Model to create a ``FeatureRecoveryControlSummaryParams`` object with default parameters.
    json_data : dict, optional
        JSON dictionary to create a ``FeatureRecoveryControlSummaryParams`` object with provided parameters.

    Examples
    --------
    >>> feature_recovery_control_summary_params = prime.FeatureRecoveryControlSummaryParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self):
        pass

    def __init__(
            self,
            model: CommunicationManager=None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``FeatureRecoveryControlSummaryParams`` object.

        Parameters
        ----------
        model : Model
            Model to create a ``FeatureRecoveryControlSummaryParams`` object with default parameters.
        json_data : dict, optional
            JSON dictionary to create a ``FeatureRecoveryControlSummaryParams`` object with provided parameters.

        Examples
        --------
        >>> feature_recovery_control_summary_params = prime.FeatureRecoveryControlSummaryParams(model = model)
        """
        if json_data:
            self.__initialize()
        else:
            all_field_specified = all(arg is not None for arg in [])
            if all_field_specified:
                self.__initialize()
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "FeatureRecoveryControlSummaryParams")
                    json_data = param_json["FeatureRecoveryControlSummaryParams"] if "FeatureRecoveryControlSummaryParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.debug(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of the ``FeatureRecoveryControlSummaryParams`` object.

        """
        args = locals()
        [FeatureRecoveryControlSummaryParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``FeatureRecoveryControlSummaryParams`` object.

        Examples
        --------
        >>> FeatureRecoveryControlSummaryParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FeatureRecoveryControlSummaryParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        if len(message) == 0:
            message = 'The object has no parameters to print.'
        return message
