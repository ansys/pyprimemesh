""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class SizingType(enum.IntEnum):
    """Sizing type decides the type of size control.
    """
    CURVATURE = 0
    """Denotes the size control type is curvature."""
    PROXIMITY = 1
    """Denotes the size control type is proximity."""
    HARD = 2
    """Denotes the size control type is hard."""
    SOFT = 3
    """Denotes the size control type is soft."""
    MESHED = 4
    """Denotes the size control type is meshed."""
    BOI = 5
    """Denotes the size control type is body of influence."""

class CurvatureSizingParams(CoreObject):
    """Size field using curvature size control computes edge and face sizes using their size and normal angle parameters.

    The curvature size control uses the normal angle parameter as the maximum allowable angle that one element edge may span.
    For example, a value of 5 implies that a division will be made when the angle change along the curve is 5 degrees.
    Hence, a 90 degree arc will be divided into approximately 18 segments.
    """
    _default_params = {}

    def __initialize(
            self,
            min: float,
            max: float,
            growth_rate: float,
            normal_angle: float,
            use_cad_curvature: bool):
        self._min = min
        self._max = max
        self._growth_rate = growth_rate
        self._normal_angle = normal_angle
        self._use_cad_curvature = use_cad_curvature

    def __init__(
            self,
            model: CommunicationManager=None,
            min: float = None,
            max: float = None,
            growth_rate: float = None,
            normal_angle: float = None,
            use_cad_curvature: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CurvatureSizingParams.

        Parameters
        ----------
        model: Model
            Model to create a CurvatureSizingParams object with default parameters.
        min: float, optional
            Minimum size used for computing edge and face size using curavture size control.
        max: float, optional
            Maximum size used for computing edge and face size using curavture size control.
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        normal_angle: float, optional
            Maximum allowable angle at which one element edge may span.
        use_cad_curvature: bool, optional
            Option to enable use of CAD curvature for computing edge and face size.
        json_data: dict, optional
            JSON dictionary to create a CurvatureSizingParams object with provided parameters.

        Examples
        --------
        >>> curvature_sizing_params = prime.CurvatureSizingParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["min"] if "min" in json_data else None,
                json_data["max"] if "max" in json_data else None,
                json_data["growthRate"] if "growthRate" in json_data else None,
                json_data["normalAngle"] if "normalAngle" in json_data else None,
                json_data["useCadCurvature"] if "useCadCurvature" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [min, max, growth_rate, normal_angle, use_cad_curvature])
            if all_field_specified:
                self.__initialize(
                    min,
                    max,
                    growth_rate,
                    normal_angle,
                    use_cad_curvature)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "CurvatureSizingParams")
                    json_data = param_json["CurvatureSizingParams"] if "CurvatureSizingParams" in param_json else {}
                    self.__initialize(
                        min if min is not None else ( CurvatureSizingParams._default_params["min"] if "min" in CurvatureSizingParams._default_params else (json_data["min"] if "min" in json_data else None)),
                        max if max is not None else ( CurvatureSizingParams._default_params["max"] if "max" in CurvatureSizingParams._default_params else (json_data["max"] if "max" in json_data else None)),
                        growth_rate if growth_rate is not None else ( CurvatureSizingParams._default_params["growth_rate"] if "growth_rate" in CurvatureSizingParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)),
                        normal_angle if normal_angle is not None else ( CurvatureSizingParams._default_params["normal_angle"] if "normal_angle" in CurvatureSizingParams._default_params else (json_data["normalAngle"] if "normalAngle" in json_data else None)),
                        use_cad_curvature if use_cad_curvature is not None else ( CurvatureSizingParams._default_params["use_cad_curvature"] if "use_cad_curvature" in CurvatureSizingParams._default_params else (json_data["useCadCurvature"] if "useCadCurvature" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            min: float = None,
            max: float = None,
            growth_rate: float = None,
            normal_angle: float = None,
            use_cad_curvature: bool = None):
        """Set the default values of CurvatureSizingParams.

        Parameters
        ----------
        min: float, optional
            Minimum size used for computing edge and face size using curavture size control.
        max: float, optional
            Maximum size used for computing edge and face size using curavture size control.
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        normal_angle: float, optional
            Maximum allowable angle at which one element edge may span.
        use_cad_curvature: bool, optional
            Option to enable use of CAD curvature for computing edge and face size.
        """
        args = locals()
        [CurvatureSizingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CurvatureSizingParams.

        Examples
        --------
        >>> CurvatureSizingParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CurvatureSizingParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._min is not None:
            json_data["min"] = self._min
        if self._max is not None:
            json_data["max"] = self._max
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        if self._normal_angle is not None:
            json_data["normalAngle"] = self._normal_angle
        if self._use_cad_curvature is not None:
            json_data["useCadCurvature"] = self._use_cad_curvature
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "min :  %s\nmax :  %s\ngrowth_rate :  %s\nnormal_angle :  %s\nuse_cad_curvature :  %s" % (self._min, self._max, self._growth_rate, self._normal_angle, self._use_cad_curvature)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def min(self) -> float:
        """Minimum size used for computing edge and face size using curavture size control.
        """
        return self._min

    @min.setter
    def min(self, value: float):
        self._min = value

    @property
    def max(self) -> float:
        """Maximum size used for computing edge and face size using curavture size control.
        """
        return self._max

    @max.setter
    def max(self, value: float):
        self._max = value

    @property
    def growth_rate(self) -> float:
        """Growth rate used for transitioning from one element size to neighbor element size.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

    @property
    def normal_angle(self) -> float:
        """Maximum allowable angle at which one element edge may span.
        """
        return self._normal_angle

    @normal_angle.setter
    def normal_angle(self, value: float):
        self._normal_angle = value

    @property
    def use_cad_curvature(self) -> bool:
        """Option to enable use of CAD curvature for computing edge and face size.
        """
        return self._use_cad_curvature

    @use_cad_curvature.setter
    def use_cad_curvature(self, value: bool):
        self._use_cad_curvature = value

class ProximitySizingParams(CoreObject):
    """Size field using proximity size control computes edge and face sizes in `gaps` using the specified minimum number of element layers.
    """
    _default_params = {}

    def __initialize(
            self,
            min: float,
            max: float,
            growth_rate: float,
            elements_per_gap: float,
            ignore_self_proximity: bool,
            ignore_orientation: bool):
        self._min = min
        self._max = max
        self._growth_rate = growth_rate
        self._elements_per_gap = elements_per_gap
        self._ignore_self_proximity = ignore_self_proximity
        self._ignore_orientation = ignore_orientation

    def __init__(
            self,
            model: CommunicationManager=None,
            min: float = None,
            max: float = None,
            growth_rate: float = None,
            elements_per_gap: float = None,
            ignore_self_proximity: bool = None,
            ignore_orientation: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ProximitySizingParams.

        Parameters
        ----------
        model: Model
            Model to create a ProximitySizingParams object with default parameters.
        min: float, optional
            Minimum size used for computing edge and face size using proximity size control.
        max: float, optional
            Maximum size used for computing edge and face size using proximity size control.
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        elements_per_gap: float, optional
            The number of elements per gap can be a real value.  This has the effect of stretching face elements with larger sizes along side faces,  or gaps, thereby reducing the overall face count, and ultimately the cell count.
        ignore_self_proximity: bool, optional
            Ignore proximity within zonelets.
        ignore_orientation: bool, optional
            The ignore orientation option can be used to ignore the face normal orientation during the proximity calculation. The default is false.
        json_data: dict, optional
            JSON dictionary to create a ProximitySizingParams object with provided parameters.

        Examples
        --------
        >>> proximity_sizing_params = prime.ProximitySizingParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["min"] if "min" in json_data else None,
                json_data["max"] if "max" in json_data else None,
                json_data["growthRate"] if "growthRate" in json_data else None,
                json_data["elementsPerGap"] if "elementsPerGap" in json_data else None,
                json_data["ignoreSelfProximity"] if "ignoreSelfProximity" in json_data else None,
                json_data["ignoreOrientation"] if "ignoreOrientation" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [min, max, growth_rate, elements_per_gap, ignore_self_proximity, ignore_orientation])
            if all_field_specified:
                self.__initialize(
                    min,
                    max,
                    growth_rate,
                    elements_per_gap,
                    ignore_self_proximity,
                    ignore_orientation)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ProximitySizingParams")
                    json_data = param_json["ProximitySizingParams"] if "ProximitySizingParams" in param_json else {}
                    self.__initialize(
                        min if min is not None else ( ProximitySizingParams._default_params["min"] if "min" in ProximitySizingParams._default_params else (json_data["min"] if "min" in json_data else None)),
                        max if max is not None else ( ProximitySizingParams._default_params["max"] if "max" in ProximitySizingParams._default_params else (json_data["max"] if "max" in json_data else None)),
                        growth_rate if growth_rate is not None else ( ProximitySizingParams._default_params["growth_rate"] if "growth_rate" in ProximitySizingParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)),
                        elements_per_gap if elements_per_gap is not None else ( ProximitySizingParams._default_params["elements_per_gap"] if "elements_per_gap" in ProximitySizingParams._default_params else (json_data["elementsPerGap"] if "elementsPerGap" in json_data else None)),
                        ignore_self_proximity if ignore_self_proximity is not None else ( ProximitySizingParams._default_params["ignore_self_proximity"] if "ignore_self_proximity" in ProximitySizingParams._default_params else (json_data["ignoreSelfProximity"] if "ignoreSelfProximity" in json_data else None)),
                        ignore_orientation if ignore_orientation is not None else ( ProximitySizingParams._default_params["ignore_orientation"] if "ignore_orientation" in ProximitySizingParams._default_params else (json_data["ignoreOrientation"] if "ignoreOrientation" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            min: float = None,
            max: float = None,
            growth_rate: float = None,
            elements_per_gap: float = None,
            ignore_self_proximity: bool = None,
            ignore_orientation: bool = None):
        """Set the default values of ProximitySizingParams.

        Parameters
        ----------
        min: float, optional
            Minimum size used for computing edge and face size using proximity size control.
        max: float, optional
            Maximum size used for computing edge and face size using proximity size control.
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        elements_per_gap: float, optional
            The number of elements per gap can be a real value.  This has the effect of stretching face elements with larger sizes along side faces,  or gaps, thereby reducing the overall face count, and ultimately the cell count.
        ignore_self_proximity: bool, optional
            Ignore proximity within zonelets.
        ignore_orientation: bool, optional
            The ignore orientation option can be used to ignore the face normal orientation during the proximity calculation. The default is false.
        """
        args = locals()
        [ProximitySizingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ProximitySizingParams.

        Examples
        --------
        >>> ProximitySizingParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ProximitySizingParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._min is not None:
            json_data["min"] = self._min
        if self._max is not None:
            json_data["max"] = self._max
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        if self._elements_per_gap is not None:
            json_data["elementsPerGap"] = self._elements_per_gap
        if self._ignore_self_proximity is not None:
            json_data["ignoreSelfProximity"] = self._ignore_self_proximity
        if self._ignore_orientation is not None:
            json_data["ignoreOrientation"] = self._ignore_orientation
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "min :  %s\nmax :  %s\ngrowth_rate :  %s\nelements_per_gap :  %s\nignore_self_proximity :  %s\nignore_orientation :  %s" % (self._min, self._max, self._growth_rate, self._elements_per_gap, self._ignore_self_proximity, self._ignore_orientation)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def min(self) -> float:
        """Minimum size used for computing edge and face size using proximity size control.
        """
        return self._min

    @min.setter
    def min(self, value: float):
        self._min = value

    @property
    def max(self) -> float:
        """Maximum size used for computing edge and face size using proximity size control.
        """
        return self._max

    @max.setter
    def max(self, value: float):
        self._max = value

    @property
    def growth_rate(self) -> float:
        """Growth rate used for transitioning from one element size to neighbor element size.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

    @property
    def elements_per_gap(self) -> float:
        """The number of elements per gap can be a real value.  This has the effect of stretching face elements with larger sizes along side faces,  or gaps, thereby reducing the overall face count, and ultimately the cell count.
        """
        return self._elements_per_gap

    @elements_per_gap.setter
    def elements_per_gap(self, value: float):
        self._elements_per_gap = value

    @property
    def ignore_self_proximity(self) -> bool:
        """Ignore proximity within zonelets.
        """
        return self._ignore_self_proximity

    @ignore_self_proximity.setter
    def ignore_self_proximity(self, value: bool):
        self._ignore_self_proximity = value

    @property
    def ignore_orientation(self) -> bool:
        """The ignore orientation option can be used to ignore the face normal orientation during the proximity calculation. The default is false.
        """
        return self._ignore_orientation

    @ignore_orientation.setter
    def ignore_orientation(self, value: bool):
        self._ignore_orientation = value

class SoftSizingParams(CoreObject):
    """Size field computed using soft size control enables you to set the maximum size on the scoped zonelets .

    When the soft sizing is computed for edges or faces, the size will be affected by size computed using other controls.
    The minimum size on the zonelet will be determined based on the influence of other size controls,
    else a uniform size will be maintained.
    """
    _default_params = {}

    def __initialize(
            self,
            max: float,
            growth_rate: float):
        self._max = max
        self._growth_rate = growth_rate

    def __init__(
            self,
            model: CommunicationManager=None,
            max: float = None,
            growth_rate: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SoftSizingParams.

        Parameters
        ----------
        model: Model
            Model to create a SoftSizingParams object with default parameters.
        max: float, optional
            Maximum size used for computing edge and face size using soft size control.
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        json_data: dict, optional
            JSON dictionary to create a SoftSizingParams object with provided parameters.

        Examples
        --------
        >>> soft_sizing_params = prime.SoftSizingParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["max"] if "max" in json_data else None,
                json_data["growthRate"] if "growthRate" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [max, growth_rate])
            if all_field_specified:
                self.__initialize(
                    max,
                    growth_rate)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SoftSizingParams")
                    json_data = param_json["SoftSizingParams"] if "SoftSizingParams" in param_json else {}
                    self.__initialize(
                        max if max is not None else ( SoftSizingParams._default_params["max"] if "max" in SoftSizingParams._default_params else (json_data["max"] if "max" in json_data else None)),
                        growth_rate if growth_rate is not None else ( SoftSizingParams._default_params["growth_rate"] if "growth_rate" in SoftSizingParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            max: float = None,
            growth_rate: float = None):
        """Set the default values of SoftSizingParams.

        Parameters
        ----------
        max: float, optional
            Maximum size used for computing edge and face size using soft size control.
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        """
        args = locals()
        [SoftSizingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SoftSizingParams.

        Examples
        --------
        >>> SoftSizingParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SoftSizingParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._max is not None:
            json_data["max"] = self._max
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "max :  %s\ngrowth_rate :  %s" % (self._max, self._growth_rate)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def max(self) -> float:
        """Maximum size used for computing edge and face size using soft size control.
        """
        return self._max

    @max.setter
    def max(self, value: float):
        self._max = value

    @property
    def growth_rate(self) -> float:
        """Growth rate used for transitioning from one element size to neighbor element size.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

class HardSizingParams(CoreObject):
    """Size field computed using hard size control enables you to maintain a uniform size based on the size specified.

    The hard sizing will override any other specified size.
    """
    _default_params = {}

    def __initialize(
            self,
            min: float,
            growth_rate: float):
        self._min = min
        self._growth_rate = growth_rate

    def __init__(
            self,
            model: CommunicationManager=None,
            min: float = None,
            growth_rate: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the HardSizingParams.

        Parameters
        ----------
        model: Model
            Model to create a HardSizingParams object with default parameters.
        min: float, optional
            Minimum size used for computing edge and face size using hard size control.
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        json_data: dict, optional
            JSON dictionary to create a HardSizingParams object with provided parameters.

        Examples
        --------
        >>> hard_sizing_params = prime.HardSizingParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["min"] if "min" in json_data else None,
                json_data["growthRate"] if "growthRate" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [min, growth_rate])
            if all_field_specified:
                self.__initialize(
                    min,
                    growth_rate)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "HardSizingParams")
                    json_data = param_json["HardSizingParams"] if "HardSizingParams" in param_json else {}
                    self.__initialize(
                        min if min is not None else ( HardSizingParams._default_params["min"] if "min" in HardSizingParams._default_params else (json_data["min"] if "min" in json_data else None)),
                        growth_rate if growth_rate is not None else ( HardSizingParams._default_params["growth_rate"] if "growth_rate" in HardSizingParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            min: float = None,
            growth_rate: float = None):
        """Set the default values of HardSizingParams.

        Parameters
        ----------
        min: float, optional
            Minimum size used for computing edge and face size using hard size control.
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        """
        args = locals()
        [HardSizingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of HardSizingParams.

        Examples
        --------
        >>> HardSizingParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in HardSizingParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._min is not None:
            json_data["min"] = self._min
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "min :  %s\ngrowth_rate :  %s" % (self._min, self._growth_rate)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def min(self) -> float:
        """Minimum size used for computing edge and face size using hard size control.
        """
        return self._min

    @min.setter
    def min(self, value: float):
        self._min = value

    @property
    def growth_rate(self) -> float:
        """Growth rate used for transitioning from one element size to neighbor element size.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

class MeshedSizingParams(CoreObject):
    """Size field computed using meshed size control enables you to set the size based on existing sizes.
    """
    _default_params = {}

    def __initialize(
            self,
            growth_rate: float):
        self._growth_rate = growth_rate

    def __init__(
            self,
            model: CommunicationManager=None,
            growth_rate: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the MeshedSizingParams.

        Parameters
        ----------
        model: Model
            Model to create a MeshedSizingParams object with default parameters.
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        json_data: dict, optional
            JSON dictionary to create a MeshedSizingParams object with provided parameters.

        Examples
        --------
        >>> meshed_sizing_params = prime.MeshedSizingParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["growthRate"] if "growthRate" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [growth_rate])
            if all_field_specified:
                self.__initialize(
                    growth_rate)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "MeshedSizingParams")
                    json_data = param_json["MeshedSizingParams"] if "MeshedSizingParams" in param_json else {}
                    self.__initialize(
                        growth_rate if growth_rate is not None else ( MeshedSizingParams._default_params["growth_rate"] if "growth_rate" in MeshedSizingParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            growth_rate: float = None):
        """Set the default values of MeshedSizingParams.

        Parameters
        ----------
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        """
        args = locals()
        [MeshedSizingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MeshedSizingParams.

        Examples
        --------
        >>> MeshedSizingParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MeshedSizingParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "growth_rate :  %s" % (self._growth_rate)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def growth_rate(self) -> float:
        """Growth rate used for transitioning from one element size to neighbor element size.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

class BoiSizingParams(CoreObject):
    """Size field computed using body of influence size control enables you to specify a body of influence(that is, a region for sizing control).

    The maximum mesh size will be equal to the specified size within the body of influence.
    The minimum size will be determined based on the influence of other size controls.
    """
    _default_params = {}

    def __initialize(
            self,
            max: float,
            growth_rate: float):
        self._max = max
        self._growth_rate = growth_rate

    def __init__(
            self,
            model: CommunicationManager=None,
            max: float = None,
            growth_rate: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the BoiSizingParams.

        Parameters
        ----------
        model: Model
            Model to create a BoiSizingParams object with default parameters.
        max: float, optional
            Maximum size used for computing edge and face size using boi size control.
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        json_data: dict, optional
            JSON dictionary to create a BoiSizingParams object with provided parameters.

        Examples
        --------
        >>> boi_sizing_params = prime.BoiSizingParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["max"] if "max" in json_data else None,
                json_data["growthRate"] if "growthRate" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [max, growth_rate])
            if all_field_specified:
                self.__initialize(
                    max,
                    growth_rate)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "BoiSizingParams")
                    json_data = param_json["BoiSizingParams"] if "BoiSizingParams" in param_json else {}
                    self.__initialize(
                        max if max is not None else ( BoiSizingParams._default_params["max"] if "max" in BoiSizingParams._default_params else (json_data["max"] if "max" in json_data else None)),
                        growth_rate if growth_rate is not None else ( BoiSizingParams._default_params["growth_rate"] if "growth_rate" in BoiSizingParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            max: float = None,
            growth_rate: float = None):
        """Set the default values of BoiSizingParams.

        Parameters
        ----------
        max: float, optional
            Maximum size used for computing edge and face size using boi size control.
        growth_rate: float, optional
            Growth rate used for transitioning from one element size to neighbor element size.
        """
        args = locals()
        [BoiSizingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of BoiSizingParams.

        Examples
        --------
        >>> BoiSizingParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in BoiSizingParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._max is not None:
            json_data["max"] = self._max
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "max :  %s\ngrowth_rate :  %s" % (self._max, self._growth_rate)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def max(self) -> float:
        """Maximum size used for computing edge and face size using boi size control.
        """
        return self._max

    @max.setter
    def max(self, value: float):
        self._max = value

    @property
    def growth_rate(self) -> float:
        """Growth rate used for transitioning from one element size to neighbor element size.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

class SizeControlSummaryResult(CoreObject):
    """Results of size control summary.
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
        """Initializes the SizeControlSummaryResult.

        Parameters
        ----------
        model: Model
            Model to create a SizeControlSummaryResult object with default parameters.
        message: str, optional
            Size control summary text.
        json_data: dict, optional
            JSON dictionary to create a SizeControlSummaryResult object with provided parameters.

        Examples
        --------
        >>> size_control_summary_result = prime.SizeControlSummaryResult(model = model)
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
                    param_json = model._communicator.initialize_params(model, "SizeControlSummaryResult")
                    json_data = param_json["SizeControlSummaryResult"] if "SizeControlSummaryResult" in param_json else {}
                    self.__initialize(
                        message if message is not None else ( SizeControlSummaryResult._default_params["message"] if "message" in SizeControlSummaryResult._default_params else (json_data["message"] if "message" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            message: str = None):
        """Set the default values of SizeControlSummaryResult.

        Parameters
        ----------
        message: str, optional
            Size control summary text.
        """
        args = locals()
        [SizeControlSummaryResult._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SizeControlSummaryResult.

        Examples
        --------
        >>> SizeControlSummaryResult.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SizeControlSummaryResult._default_params.items())
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
        """Size control summary text.
        """
        return self._message

    @message.setter
    def message(self, value: str):
        self._message = value

class SizeControlSummaryParams(CoreObject):
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
        """Initializes the SizeControlSummaryParams.

        Parameters
        ----------
        model: Model
            Model to create a SizeControlSummaryParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a SizeControlSummaryParams object with provided parameters.

        Examples
        --------
        >>> size_control_summary_params = prime.SizeControlSummaryParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "SizeControlSummaryParams")
                    json_data = param_json["SizeControlSummaryParams"] if "SizeControlSummaryParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of SizeControlSummaryParams.

        """
        args = locals()
        [SizeControlSummaryParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SizeControlSummaryParams.

        Examples
        --------
        >>> SizeControlSummaryParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SizeControlSummaryParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class SetSizingResults(CoreObject):
    """Result associated with the different set sizing parameters.
    """
    _default_params = {}

    def __initialize(
            self,
            warning_codes: List[WarningCode],
            error_code: ErrorCode):
        self._warning_codes = warning_codes
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            warning_codes: List[WarningCode] = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SetSizingResults.

        Parameters
        ----------
        model: Model
            Model to create a SetSizingResults object with default parameters.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the set sizing parameters.
        error_code: ErrorCode, optional
            Error code associated with the set sizing parameters.
        json_data: dict, optional
            JSON dictionary to create a SetSizingResults object with provided parameters.

        Examples
        --------
        >>> set_sizing_results = prime.SetSizingResults(model = model)
        """
        if json_data:
            self.__initialize(
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [warning_codes, error_code])
            if all_field_specified:
                self.__initialize(
                    warning_codes,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SetSizingResults")
                    json_data = param_json["SetSizingResults"] if "SetSizingResults" in param_json else {}
                    self.__initialize(
                        warning_codes if warning_codes is not None else ( SetSizingResults._default_params["warning_codes"] if "warning_codes" in SetSizingResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]),
                        error_code if error_code is not None else ( SetSizingResults._default_params["error_code"] if "error_code" in SetSizingResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            warning_codes: List[WarningCode] = None,
            error_code: ErrorCode = None):
        """Set the default values of SetSizingResults.

        Parameters
        ----------
        warning_codes: List[WarningCode], optional
            Warning codes associated with the set sizing parameters.
        error_code: ErrorCode, optional
            Error code associated with the set sizing parameters.
        """
        args = locals()
        [SetSizingResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SetSizingResults.

        Examples
        --------
        >>> SetSizingResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SetSizingResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "warning_codes :  %s\nerror_code :  %s" % ('[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']', self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the set sizing parameters.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the set sizing parameters.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
