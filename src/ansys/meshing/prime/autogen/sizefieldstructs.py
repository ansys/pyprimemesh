""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class SFPeriodicParams(CoreObject):
    """Parameters for setting periodic size fields.
    """
    _default_params = {}

    def __initialize(
            self,
            axis: Iterable[float],
            angle: float,
            center: Iterable[float]):
        self._axis = axis if isinstance(axis, np.ndarray) else np.array(axis, dtype=np.double) if axis is not None else None
        self._angle = angle
        self._center = center if isinstance(center, np.ndarray) else np.array(center, dtype=np.double) if center is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            axis: Iterable[float] = None,
            angle: float = None,
            center: Iterable[float] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SFPeriodicParams.

        Parameters
        ----------
        model: Model
            Model to create a SFPeriodicParams object with default parameters.
        axis: Iterable[float], optional
            Axis vector coordinates.
        angle: float, optional
            Angle in degrees.
        center: Iterable[float], optional
            Center coordinates.
        json_data: dict, optional
            JSON dictionary to create a SFPeriodicParams object with provided parameters.

        Examples
        --------
        >>> s_fperiodic_params = prime.SFPeriodicParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["axis"] if "axis" in json_data else None,
                json_data["angle"] if "angle" in json_data else None,
                json_data["center"] if "center" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [axis, angle, center])
            if all_field_specified:
                self.__initialize(
                    axis,
                    angle,
                    center)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SFPeriodicParams")
                    json_data = param_json["SFPeriodicParams"] if "SFPeriodicParams" in param_json else {}
                    self.__initialize(
                        axis if axis is not None else ( SFPeriodicParams._default_params["axis"] if "axis" in SFPeriodicParams._default_params else (json_data["axis"] if "axis" in json_data else None)),
                        angle if angle is not None else ( SFPeriodicParams._default_params["angle"] if "angle" in SFPeriodicParams._default_params else (json_data["angle"] if "angle" in json_data else None)),
                        center if center is not None else ( SFPeriodicParams._default_params["center"] if "center" in SFPeriodicParams._default_params else (json_data["center"] if "center" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            axis: Iterable[float] = None,
            angle: float = None,
            center: Iterable[float] = None):
        """Set the default values of SFPeriodicParams.

        Parameters
        ----------
        axis: Iterable[float], optional
            Axis vector coordinates.
        angle: float, optional
            Angle in degrees.
        center: Iterable[float], optional
            Center coordinates.
        """
        args = locals()
        [SFPeriodicParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SFPeriodicParams.

        Examples
        --------
        >>> SFPeriodicParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SFPeriodicParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._axis is not None:
            json_data["axis"] = self._axis
        if self._angle is not None:
            json_data["angle"] = self._angle
        if self._center is not None:
            json_data["center"] = self._center
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "axis :  %s\nangle :  %s\ncenter :  %s" % (self._axis, self._angle, self._center)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

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

    @property
    def center(self) -> Iterable[float]:
        """Center coordinates.
        """
        return self._center

    @center.setter
    def center(self, value: Iterable[float]):
        self._center = value

class VolumetricSizeFieldComputeResults(CoreObject):
    """Results associated with the compute volumetric size field operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            size_field_id: int):
        self._error_code = ErrorCode(error_code)
        self._size_field_id = size_field_id

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            size_field_id: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the VolumetricSizeFieldComputeResults.

        Parameters
        ----------
        model: Model
            Model to create a VolumetricSizeFieldComputeResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the compute volumetric size field operation.
        size_field_id: int, optional
            Id of the computed size field.
        json_data: dict, optional
            JSON dictionary to create a VolumetricSizeFieldComputeResults object with provided parameters.

        Examples
        --------
        >>> volumetric_size_field_compute_results = prime.VolumetricSizeFieldComputeResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["sizeFieldId"] if "sizeFieldId" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, size_field_id])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    size_field_id)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "VolumetricSizeFieldComputeResults")
                    json_data = param_json["VolumetricSizeFieldComputeResults"] if "VolumetricSizeFieldComputeResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( VolumetricSizeFieldComputeResults._default_params["error_code"] if "error_code" in VolumetricSizeFieldComputeResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        size_field_id if size_field_id is not None else ( VolumetricSizeFieldComputeResults._default_params["size_field_id"] if "size_field_id" in VolumetricSizeFieldComputeResults._default_params else (json_data["sizeFieldId"] if "sizeFieldId" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            size_field_id: int = None):
        """Set the default values of VolumetricSizeFieldComputeResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the compute volumetric size field operation.
        size_field_id: int, optional
            Id of the computed size field.
        """
        args = locals()
        [VolumetricSizeFieldComputeResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of VolumetricSizeFieldComputeResults.

        Examples
        --------
        >>> VolumetricSizeFieldComputeResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VolumetricSizeFieldComputeResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._size_field_id is not None:
            json_data["sizeFieldId"] = self._size_field_id
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nsize_field_id :  %s" % (self._error_code, self._size_field_id)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the compute volumetric size field operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def size_field_id(self) -> int:
        """Id of the computed size field.
        """
        return self._size_field_id

    @size_field_id.setter
    def size_field_id(self, value: int):
        self._size_field_id = value

class VolumetricSizeFieldComputeParams(CoreObject):
    """Parameters associated with the compute volumetric size field operation.
    """
    _default_params = {}

    def __initialize(
            self,
            enable_multi_threading: bool,
            enable_periodicity: bool,
            periodic_params: SFPeriodicParams):
        self._enable_multi_threading = enable_multi_threading
        self._enable_periodicity = enable_periodicity
        self._periodic_params = periodic_params

    def __init__(
            self,
            model: CommunicationManager=None,
            enable_multi_threading: bool = None,
            enable_periodicity: bool = None,
            periodic_params: SFPeriodicParams = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the VolumetricSizeFieldComputeParams.

        Parameters
        ----------
        model: Model
            Model to create a VolumetricSizeFieldComputeParams object with default parameters.
        enable_multi_threading: bool, optional
            Option to compute volumetric size field in parallel using multithreads.
        enable_periodicity: bool, optional
            Option to enable periodic size field computations.
        periodic_params: SFPeriodicParams, optional
            Periodic parameters to compute the size field.
        json_data: dict, optional
            JSON dictionary to create a VolumetricSizeFieldComputeParams object with provided parameters.

        Examples
        --------
        >>> volumetric_size_field_compute_params = prime.VolumetricSizeFieldComputeParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["enableMultiThreading"] if "enableMultiThreading" in json_data else None,
                json_data["enablePeriodicity"] if "enablePeriodicity" in json_data else None,
                SFPeriodicParams(model = model, json_data = json_data["periodicParams"] if "periodicParams" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [enable_multi_threading, enable_periodicity, periodic_params])
            if all_field_specified:
                self.__initialize(
                    enable_multi_threading,
                    enable_periodicity,
                    periodic_params)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "VolumetricSizeFieldComputeParams")
                    json_data = param_json["VolumetricSizeFieldComputeParams"] if "VolumetricSizeFieldComputeParams" in param_json else {}
                    self.__initialize(
                        enable_multi_threading if enable_multi_threading is not None else ( VolumetricSizeFieldComputeParams._default_params["enable_multi_threading"] if "enable_multi_threading" in VolumetricSizeFieldComputeParams._default_params else (json_data["enableMultiThreading"] if "enableMultiThreading" in json_data else None)),
                        enable_periodicity if enable_periodicity is not None else ( VolumetricSizeFieldComputeParams._default_params["enable_periodicity"] if "enable_periodicity" in VolumetricSizeFieldComputeParams._default_params else (json_data["enablePeriodicity"] if "enablePeriodicity" in json_data else None)),
                        periodic_params if periodic_params is not None else ( VolumetricSizeFieldComputeParams._default_params["periodic_params"] if "periodic_params" in VolumetricSizeFieldComputeParams._default_params else SFPeriodicParams(model = model, json_data = (json_data["periodicParams"] if "periodicParams" in json_data else None))))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            enable_multi_threading: bool = None,
            enable_periodicity: bool = None,
            periodic_params: SFPeriodicParams = None):
        """Set the default values of VolumetricSizeFieldComputeParams.

        Parameters
        ----------
        enable_multi_threading: bool, optional
            Option to compute volumetric size field in parallel using multithreads.
        enable_periodicity: bool, optional
            Option to enable periodic size field computations.
        periodic_params: SFPeriodicParams, optional
            Periodic parameters to compute the size field.
        """
        args = locals()
        [VolumetricSizeFieldComputeParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of VolumetricSizeFieldComputeParams.

        Examples
        --------
        >>> VolumetricSizeFieldComputeParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VolumetricSizeFieldComputeParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._enable_multi_threading is not None:
            json_data["enableMultiThreading"] = self._enable_multi_threading
        if self._enable_periodicity is not None:
            json_data["enablePeriodicity"] = self._enable_periodicity
        if self._periodic_params is not None:
            json_data["periodicParams"] = self._periodic_params._jsonify()
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "enable_multi_threading :  %s\nenable_periodicity :  %s\nperiodic_params :  %s" % (self._enable_multi_threading, self._enable_periodicity, '{ ' + str(self._periodic_params) + ' }')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def enable_multi_threading(self) -> bool:
        """Option to compute volumetric size field in parallel using multithreads.
        """
        return self._enable_multi_threading

    @enable_multi_threading.setter
    def enable_multi_threading(self, value: bool):
        self._enable_multi_threading = value

    @property
    def enable_periodicity(self) -> bool:
        """Option to enable periodic size field computations.
        """
        return self._enable_periodicity

    @enable_periodicity.setter
    def enable_periodicity(self, value: bool):
        self._enable_periodicity = value

    @property
    def periodic_params(self) -> SFPeriodicParams:
        """Periodic parameters to compute the size field.
        """
        return self._periodic_params

    @periodic_params.setter
    def periodic_params(self, value: SFPeriodicParams):
        self._periodic_params = value
