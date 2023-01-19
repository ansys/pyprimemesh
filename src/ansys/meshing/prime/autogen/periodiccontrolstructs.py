""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class PeriodicControlParams(CoreObject):
    """PeriodicControlParams contains the parameters for periodic surface recovery.  Parameters like center, axis and angle determine the transformation from  one surface to its matching periodic surface.
    """
    _default_params = {}

    def __initialize(
            self,
            center: Iterable[float],
            axis: Iterable[float],
            angle: float):
        self._center = center if isinstance(center, np.ndarray) else np.array(center, dtype=np.double) if center is not None else None
        self._axis = axis if isinstance(axis, np.ndarray) else np.array(axis, dtype=np.double) if axis is not None else None
        self._angle = angle

    def __init__(
            self,
            model: CommunicationManager=None,
            center: Iterable[float] = None,
            axis: Iterable[float] = None,
            angle: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the PeriodicControlParams.

        Parameters
        ----------
        model: Model
            Model to create a PeriodicControlParams object with default parameters.
        center: Iterable[float], optional
            Center coordinates.
        axis: Iterable[float], optional
            Axis vector coordinates.
        angle: float, optional
            Angle in degrees.
        json_data: dict, optional
            JSON dictionary to create a PeriodicControlParams object with provided parameters.

        Examples
        --------
        >>> periodic_control_params = prime.PeriodicControlParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["center"] if "center" in json_data else None,
                json_data["axis"] if "axis" in json_data else None,
                json_data["angle"] if "angle" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [center, axis, angle])
            if all_field_specified:
                self.__initialize(
                    center,
                    axis,
                    angle)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "PeriodicControlParams")
                    json_data = param_json["PeriodicControlParams"] if "PeriodicControlParams" in param_json else {}
                    self.__initialize(
                        center if center is not None else ( PeriodicControlParams._default_params["center"] if "center" in PeriodicControlParams._default_params else (json_data["center"] if "center" in json_data else None)),
                        axis if axis is not None else ( PeriodicControlParams._default_params["axis"] if "axis" in PeriodicControlParams._default_params else (json_data["axis"] if "axis" in json_data else None)),
                        angle if angle is not None else ( PeriodicControlParams._default_params["angle"] if "angle" in PeriodicControlParams._default_params else (json_data["angle"] if "angle" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            center: Iterable[float] = None,
            axis: Iterable[float] = None,
            angle: float = None):
        """Set the default values of PeriodicControlParams.

        Parameters
        ----------
        center: Iterable[float], optional
            Center coordinates.
        axis: Iterable[float], optional
            Axis vector coordinates.
        angle: float, optional
            Angle in degrees.
        """
        args = locals()
        [PeriodicControlParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of PeriodicControlParams.

        Examples
        --------
        >>> PeriodicControlParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PeriodicControlParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._center is not None:
            json_data["center"] = self._center
        if self._axis is not None:
            json_data["axis"] = self._axis
        if self._angle is not None:
            json_data["angle"] = self._angle
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "center :  %s\naxis :  %s\nangle :  %s" % (self._center, self._axis, self._angle)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def center(self) -> Iterable[float]:
        """Center coordinates.
        """
        return self._center

    @center.setter
    def center(self, value: Iterable[float]):
        self._center = value

    @property
    def axis(self) -> Iterable[float]:
        """Axis vector coordinates.
        """
        return self._axis

    @axis.setter
    def axis(self, value: Iterable[float]):
        self._axis = value

    @property
    def angle(self) -> float:
        """Angle in degrees.
        """
        return self._angle

    @angle.setter
    def angle(self, value: float):
        self._angle = value

class PeriodicControlSummaryResult(CoreObject):
    """Results of Periodic control summary.
    """
    _default_params = {}

    def __initialize(
            self,
            message: str):
        self._message = message

    def __init__(
            self,
            model: CommunicationManager=None,
            message: str = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the PeriodicControlSummaryResult.

        Parameters
        ----------
        model: Model
            Model to create a PeriodicControlSummaryResult object with default parameters.
        message: str, optional
            String with the periodic control summary.
        json_data: dict, optional
            JSON dictionary to create a PeriodicControlSummaryResult object with provided parameters.

        Examples
        --------
        >>> periodic_control_summary_result = prime.PeriodicControlSummaryResult(model = model)
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
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "PeriodicControlSummaryResult")
                    json_data = param_json["PeriodicControlSummaryResult"] if "PeriodicControlSummaryResult" in param_json else {}
                    self.__initialize(
                        message if message is not None else ( PeriodicControlSummaryResult._default_params["message"] if "message" in PeriodicControlSummaryResult._default_params else (json_data["message"] if "message" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            message: str = None):
        """Set the default values of PeriodicControlSummaryResult.

        Parameters
        ----------
        message: str, optional
            String with the periodic control summary.
        """
        args = locals()
        [PeriodicControlSummaryResult._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of PeriodicControlSummaryResult.

        Examples
        --------
        >>> PeriodicControlSummaryResult.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PeriodicControlSummaryResult._default_params.items())
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
        """String with the periodic control summary.
        """
        return self._message

    @message.setter
    def message(self, value: str):
        self._message = value

class PeriodicControlSummaryParams(CoreObject):
    """Parameters used to get size control summary.
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
        """Initializes the PeriodicControlSummaryParams.

        Parameters
        ----------
        model: Model
            Model to create a PeriodicControlSummaryParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a PeriodicControlSummaryParams object with provided parameters.

        Examples
        --------
        >>> periodic_control_summary_params = prime.PeriodicControlSummaryParams(model = model)
        """
        if json_data:
            self.__initialize()
        else:
            all_field_specified = all(arg is not None for arg in [])
            if all_field_specified:
                self.__initialize()
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "PeriodicControlSummaryParams")
                    json_data = param_json["PeriodicControlSummaryParams"] if "PeriodicControlSummaryParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of PeriodicControlSummaryParams.

        """
        args = locals()
        [PeriodicControlSummaryParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of PeriodicControlSummaryParams.

        Examples
        --------
        >>> PeriodicControlSummaryParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PeriodicControlSummaryParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message
