""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class BCPairType(enum.IntEnum):
    """Option to specify boundary condition pair type.
    """
    FACE = 1
    """Option to specify face zonelet as boundary condition pair."""
    EDGE = 2
    """Option to specify edge zonelet as boundary condition pair."""

class MatchPairTargetType(enum.IntEnum):
    """Match morph target type.
    """
    FACEZONELET = 1
    """Option to specify face zonelet as target."""
    TOPOFACE = 2
    """Option to specify topoface as target."""

class MorphSolveParams(CoreObject):
    """Morpher solve parameters.
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
        """Initializes the MorphSolveParams.

        Parameters
        ----------
        model: Model
            Model to create a MorphSolveParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a MorphSolveParams object with provided parameters.

        Examples
        --------
        >>> morph_solve_params = prime.MorphSolveParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "MorphSolveParams")
                    json_data = param_json["MorphSolveParams"] if "MorphSolveParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of MorphSolveParams.

        """
        args = locals()
        [MorphSolveParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MorphSolveParams.

        Examples
        --------
        >>> MorphSolveParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MorphSolveParams._default_params.items())
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

class MatchMorphParams(CoreObject):
    """MatchMorphParams describes the parameters required for match morphing.
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
        """Initializes the MatchMorphParams.

        Parameters
        ----------
        model: Model
            Model to create a MatchMorphParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a MatchMorphParams object with provided parameters.

        Examples
        --------
        >>> match_morph_params = prime.MatchMorphParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "MatchMorphParams")
                    json_data = param_json["MatchMorphParams"] if "MatchMorphParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of MatchMorphParams.

        """
        args = locals()
        [MatchMorphParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MatchMorphParams.

        Examples
        --------
        >>> MatchMorphParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MatchMorphParams._default_params.items())
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

class MatchMorphResults(CoreObject):
    """Results associated with match morph operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the MatchMorphResults.

        Parameters
        ----------
        model: Model
            Model to create a MatchMorphResults object with default parameters.
        error_code: ErrorCode, optional
            Errorcode associated with match morph operation.
        json_data: dict, optional
            JSON dictionary to create a MatchMorphResults object with provided parameters.

        Examples
        --------
        >>> match_morph_results = prime.MatchMorphResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "MatchMorphResults")
                    json_data = param_json["MatchMorphResults"] if "MatchMorphResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( MatchMorphResults._default_params["error_code"] if "error_code" in MatchMorphResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of MatchMorphResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Errorcode associated with match morph operation.
        """
        args = locals()
        [MatchMorphResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MatchMorphResults.

        Examples
        --------
        >>> MatchMorphResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MatchMorphResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Errorcode associated with match morph operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class BCPair(CoreObject):
    """Used to define boundary conditions for match morphing.
    """
    _default_params = {}

    def __initialize(
            self,
            source_zonelet: int,
            target_zonelet: int,
            type: BCPairType):
        self._source_zonelet = source_zonelet
        self._target_zonelet = target_zonelet
        self._type = BCPairType(type)

    def __init__(
            self,
            model: CommunicationManager=None,
            source_zonelet: int = None,
            target_zonelet: int = None,
            type: BCPairType = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the BCPair.

        Parameters
        ----------
        model: Model
            Model to create a BCPair object with default parameters.
        source_zonelet: int, optional
            Id of source zonelet.
        target_zonelet: int, optional
            Id of target zonelet.
        type: BCPairType, optional
            Option to specify boundary condition pair type.
        json_data: dict, optional
            JSON dictionary to create a BCPair object with provided parameters.

        Examples
        --------
        >>> b_cpair = prime.BCPair(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["sourceZonelet"] if "sourceZonelet" in json_data else None,
                json_data["targetZonelet"] if "targetZonelet" in json_data else None,
                BCPairType(json_data["type"] if "type" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [source_zonelet, target_zonelet, type])
            if all_field_specified:
                self.__initialize(
                    source_zonelet,
                    target_zonelet,
                    type)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "BCPair")
                    json_data = param_json["BCPair"] if "BCPair" in param_json else {}
                    self.__initialize(
                        source_zonelet if source_zonelet is not None else ( BCPair._default_params["source_zonelet"] if "source_zonelet" in BCPair._default_params else (json_data["sourceZonelet"] if "sourceZonelet" in json_data else None)),
                        target_zonelet if target_zonelet is not None else ( BCPair._default_params["target_zonelet"] if "target_zonelet" in BCPair._default_params else (json_data["targetZonelet"] if "targetZonelet" in json_data else None)),
                        type if type is not None else ( BCPair._default_params["type"] if "type" in BCPair._default_params else BCPairType(json_data["type"] if "type" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            source_zonelet: int = None,
            target_zonelet: int = None,
            type: BCPairType = None):
        """Set the default values of BCPair.

        Parameters
        ----------
        source_zonelet: int, optional
            Id of source zonelet.
        target_zonelet: int, optional
            Id of target zonelet.
        type: BCPairType, optional
            Option to specify boundary condition pair type.
        """
        args = locals()
        [BCPair._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of BCPair.

        Examples
        --------
        >>> BCPair.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in BCPair._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._source_zonelet is not None:
            json_data["sourceZonelet"] = self._source_zonelet
        if self._target_zonelet is not None:
            json_data["targetZonelet"] = self._target_zonelet
        if self._type is not None:
            json_data["type"] = self._type
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "source_zonelet :  %s\ntarget_zonelet :  %s\ntype :  %s" % (self._source_zonelet, self._target_zonelet, self._type)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def source_zonelet(self) -> int:
        """Id of source zonelet.
        """
        return self._source_zonelet

    @source_zonelet.setter
    def source_zonelet(self, value: int):
        self._source_zonelet = value

    @property
    def target_zonelet(self) -> int:
        """Id of target zonelet.
        """
        return self._target_zonelet

    @target_zonelet.setter
    def target_zonelet(self, value: int):
        self._target_zonelet = value

    @property
    def type(self) -> BCPairType:
        """Option to specify boundary condition pair type.
        """
        return self._type

    @type.setter
    def type(self, value: BCPairType):
        self._type = value

class MatchPair(CoreObject):
    """Match pair to specify sources, targets for match morphing. Included boundary conditions specification.
    """
    _default_params = {}

    def __initialize(
            self,
            source_surfaces: Iterable[int],
            target_surfaces: Iterable[int],
            target_type: MatchPairTargetType,
            bc_pairs: List[BCPair]):
        self._source_surfaces = source_surfaces if isinstance(source_surfaces, np.ndarray) else np.array(source_surfaces, dtype=np.int32) if source_surfaces is not None else None
        self._target_surfaces = target_surfaces if isinstance(target_surfaces, np.ndarray) else np.array(target_surfaces, dtype=np.int32) if target_surfaces is not None else None
        self._target_type = MatchPairTargetType(target_type)
        self._bc_pairs = bc_pairs

    def __init__(
            self,
            model: CommunicationManager=None,
            source_surfaces: Iterable[int] = None,
            target_surfaces: Iterable[int] = None,
            target_type: MatchPairTargetType = None,
            bc_pairs: List[BCPair] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the MatchPair.

        Parameters
        ----------
        model: Model
            Model to create a MatchPair object with default parameters.
        source_surfaces: Iterable[int], optional
            Ids of source surfaces.
        target_surfaces: Iterable[int], optional
            Ids of target surfaces.
        target_type: MatchPairTargetType, optional
            Option to specify target surface type.
        bc_pairs: List[BCPair], optional
            Array of boundary condition pairs.
        json_data: dict, optional
            JSON dictionary to create a MatchPair object with provided parameters.

        Examples
        --------
        >>> match_pair = prime.MatchPair(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["sourceSurfaces"] if "sourceSurfaces" in json_data else None,
                json_data["targetSurfaces"] if "targetSurfaces" in json_data else None,
                MatchPairTargetType(json_data["targetType"] if "targetType" in json_data else None),
                [BCPair(model = model, json_data = data) for data in json_data["bcPairs"]] if "bcPairs" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [source_surfaces, target_surfaces, target_type, bc_pairs])
            if all_field_specified:
                self.__initialize(
                    source_surfaces,
                    target_surfaces,
                    target_type,
                    bc_pairs)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "MatchPair")
                    json_data = param_json["MatchPair"] if "MatchPair" in param_json else {}
                    self.__initialize(
                        source_surfaces if source_surfaces is not None else ( MatchPair._default_params["source_surfaces"] if "source_surfaces" in MatchPair._default_params else (json_data["sourceSurfaces"] if "sourceSurfaces" in json_data else None)),
                        target_surfaces if target_surfaces is not None else ( MatchPair._default_params["target_surfaces"] if "target_surfaces" in MatchPair._default_params else (json_data["targetSurfaces"] if "targetSurfaces" in json_data else None)),
                        target_type if target_type is not None else ( MatchPair._default_params["target_type"] if "target_type" in MatchPair._default_params else MatchPairTargetType(json_data["targetType"] if "targetType" in json_data else None)),
                        bc_pairs if bc_pairs is not None else ( MatchPair._default_params["bc_pairs"] if "bc_pairs" in MatchPair._default_params else [BCPair(model = model, json_data = data) for data in (json_data["bcPairs"] if "bcPairs" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            source_surfaces: Iterable[int] = None,
            target_surfaces: Iterable[int] = None,
            target_type: MatchPairTargetType = None,
            bc_pairs: List[BCPair] = None):
        """Set the default values of MatchPair.

        Parameters
        ----------
        source_surfaces: Iterable[int], optional
            Ids of source surfaces.
        target_surfaces: Iterable[int], optional
            Ids of target surfaces.
        target_type: MatchPairTargetType, optional
            Option to specify target surface type.
        bc_pairs: List[BCPair], optional
            Array of boundary condition pairs.
        """
        args = locals()
        [MatchPair._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of MatchPair.

        Examples
        --------
        >>> MatchPair.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MatchPair._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._source_surfaces is not None:
            json_data["sourceSurfaces"] = self._source_surfaces
        if self._target_surfaces is not None:
            json_data["targetSurfaces"] = self._target_surfaces
        if self._target_type is not None:
            json_data["targetType"] = self._target_type
        if self._bc_pairs is not None:
            json_data["bcPairs"] = [data._jsonify() for data in self._bc_pairs]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "source_surfaces :  %s\ntarget_surfaces :  %s\ntarget_type :  %s\nbc_pairs :  %s" % (self._source_surfaces, self._target_surfaces, self._target_type, '[' + ''.join('\n' + str(data) for data in self._bc_pairs) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def source_surfaces(self) -> Iterable[int]:
        """Ids of source surfaces.
        """
        return self._source_surfaces

    @source_surfaces.setter
    def source_surfaces(self, value: Iterable[int]):
        self._source_surfaces = value

    @property
    def target_surfaces(self) -> Iterable[int]:
        """Ids of target surfaces.
        """
        return self._target_surfaces

    @target_surfaces.setter
    def target_surfaces(self, value: Iterable[int]):
        self._target_surfaces = value

    @property
    def target_type(self) -> MatchPairTargetType:
        """Option to specify target surface type.
        """
        return self._target_type

    @target_type.setter
    def target_type(self, value: MatchPairTargetType):
        self._target_type = value

    @property
    def bc_pairs(self) -> List[BCPair]:
        """Array of boundary condition pairs.
        """
        return self._bc_pairs

    @bc_pairs.setter
    def bc_pairs(self, value: List[BCPair]):
        self._bc_pairs = value
