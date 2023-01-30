""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class CadReaderRoute(enum.IntEnum):
    """CAD Reader routes.
    """
    PROGRAMCONTROLLED = 0
    """Denotes program controlled CAD reader route."""
    NATIVE = 1
    """Denotes native CAD reader route."""
    WORKBENCH = 2
    """Denotes WorkBench as CAD reader route."""
    SPACECLAIM = 3
    """Denotes SpaceClaim as CAD reader route."""

class PartCreationType(enum.IntEnum):
    """Part Creation Type decides whether to create a part per CAD Model, Assembly, Part, Body.
    """
    MODEL = 0
    """Denotes a part per CAD Model."""
    ASSEMBLY = 1
    """Denotes a part per CAD Assembly."""
    PART = 2
    """Denotes a part per CAD Part."""
    BODY = 3
    """Denotes a part per CAD Body."""

class LengthUnit(enum.IntEnum):
    """Length units
    """
    M = 0
    """Denotes length unit is meters."""
    CM = 1
    """Denotes length unit is centimeters."""
    MM = 2
    """Denotes length unit is milimeters."""
    UM = 3
    """Denotes length unit is micrometers."""
    NM = 4
    """Denotes length unit is nanometers."""
    IN = 5
    """Denotes length unit is inches."""
    FT = 6
    """Denotes length unit is feet."""

class CadFaceter(enum.IntEnum):
    """Types of CAD faceter.
    """
    ACIS = 0
    """Denotes CAD faceter is Acis."""
    PARASOLID = 1
    """Denotes CAD faceter is Parasolid."""

class CadRefacetingResolution(enum.IntEnum):
    """Levels of CAD faceting refinement.
    """
    COARSE = 0
    """Denotes coarse resolution of CAD faceting."""
    MEDIUM = 1
    """Denotes medium resolution of CAD faceting."""
    FINE = 2
    """Denotes fine resolution of CAD faceting."""
    CUSTOM = 3
    """Denotes custom resolution of CAD faceting."""

class CadRefacetingMaxEdgeSizeLimit(enum.IntEnum):
    """Types of maximum edge size limit for CAD faceting.
    """
    NONE = 0
    """Denotes no maximum edge size limit for CAD faceting."""
    ABSOLUTE = 1
    """Denotes absolute maximum edge size limit for CAD faceting."""
    RELATIVE = 2
    """Denotes relative maximum edge size limit for CAD faceting."""

class FileReadParams(CoreObject):
    """Parameters to read file.
    """
    _default_params = {}

    def __initialize(
            self,
            append: bool):
        self._append = append

    def __init__(
            self,
            model: CommunicationManager=None,
            append: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the FileReadParams.

        Parameters
        ----------
        model: Model
            Model to create a FileReadParams object with default parameters.
        append: bool, optional
            Option to append imported mesh to existing mesh instead of resetting model to imported mesh.
        json_data: dict, optional
            JSON dictionary to create a FileReadParams object with provided parameters.

        Examples
        --------
        >>> file_read_params = prime.FileReadParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["append"] if "append" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [append])
            if all_field_specified:
                self.__initialize(
                    append)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "FileReadParams")
                    json_data = param_json["FileReadParams"] if "FileReadParams" in param_json else {}
                    self.__initialize(
                        append if append is not None else ( FileReadParams._default_params["append"] if "append" in FileReadParams._default_params else (json_data["append"] if "append" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            append: bool = None):
        """Set the default values of FileReadParams.

        Parameters
        ----------
        append: bool, optional
            Option to append imported mesh to existing mesh instead of resetting model to imported mesh.
        """
        args = locals()
        [FileReadParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FileReadParams.

        Examples
        --------
        >>> FileReadParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FileReadParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._append is not None:
            json_data["append"] = self._append
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "append :  %s" % (self._append)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def append(self) -> bool:
        """Option to append imported mesh to existing mesh instead of resetting model to imported mesh.
        """
        return self._append

    @append.setter
    def append(self, value: bool):
        self._append = value

class SizeFieldFileReadResults(CoreObject):
    """Results of size field file read operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            size_field_ids: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._size_field_ids = size_field_ids if isinstance(size_field_ids, np.ndarray) else np.array(size_field_ids, dtype=np.int32) if size_field_ids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            size_field_ids: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SizeFieldFileReadResults.

        Parameters
        ----------
        model: Model
            Model to create a SizeFieldFileReadResults object with default parameters.
        error_code: ErrorCode, optional
            Error code if size field file read operation was unsuccessful.
        size_field_ids: Iterable[int], optional
            Ids of size fields read by read size field operation.
        json_data: dict, optional
            JSON dictionary to create a SizeFieldFileReadResults object with provided parameters.

        Examples
        --------
        >>> size_field_file_read_results = prime.SizeFieldFileReadResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["sizeFieldIds"] if "sizeFieldIds" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, size_field_ids])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    size_field_ids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SizeFieldFileReadResults")
                    json_data = param_json["SizeFieldFileReadResults"] if "SizeFieldFileReadResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( SizeFieldFileReadResults._default_params["error_code"] if "error_code" in SizeFieldFileReadResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        size_field_ids if size_field_ids is not None else ( SizeFieldFileReadResults._default_params["size_field_ids"] if "size_field_ids" in SizeFieldFileReadResults._default_params else (json_data["sizeFieldIds"] if "sizeFieldIds" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            size_field_ids: Iterable[int] = None):
        """Set the default values of SizeFieldFileReadResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code if size field file read operation was unsuccessful.
        size_field_ids: Iterable[int], optional
            Ids of size fields read by read size field operation.
        """
        args = locals()
        [SizeFieldFileReadResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SizeFieldFileReadResults.

        Examples
        --------
        >>> SizeFieldFileReadResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SizeFieldFileReadResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._size_field_ids is not None:
            json_data["sizeFieldIds"] = self._size_field_ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nsize_field_ids :  %s" % (self._error_code, self._size_field_ids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code if size field file read operation was unsuccessful.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def size_field_ids(self) -> Iterable[int]:
        """Ids of size fields read by read size field operation.
        """
        return self._size_field_ids

    @size_field_ids.setter
    def size_field_ids(self, value: Iterable[int]):
        self._size_field_ids = value

class FileReadResults(CoreObject):
    """Results of file read operation.
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
        """Initializes the FileReadResults.

        Parameters
        ----------
        model: Model
            Model to create a FileReadResults object with default parameters.
        error_code: ErrorCode, optional
            Error code if file read operation was unsuccessful.
        json_data: dict, optional
            JSON dictionary to create a FileReadResults object with provided parameters.

        Examples
        --------
        >>> file_read_results = prime.FileReadResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "FileReadResults")
                    json_data = param_json["FileReadResults"] if "FileReadResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( FileReadResults._default_params["error_code"] if "error_code" in FileReadResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of FileReadResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code if file read operation was unsuccessful.
        """
        args = locals()
        [FileReadResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FileReadResults.

        Examples
        --------
        >>> FileReadResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FileReadResults._default_params.items())
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
        """Error code if file read operation was unsuccessful.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class FileWriteParams(CoreObject):
    """Parameters to write a file.
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
        """Initializes the FileWriteParams.

        Parameters
        ----------
        model: Model
            Model to create a FileWriteParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a FileWriteParams object with provided parameters.

        Examples
        --------
        >>> file_write_params = prime.FileWriteParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "FileWriteParams")
                    json_data = param_json["FileWriteParams"] if "FileWriteParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of FileWriteParams.

        """
        args = locals()
        [FileWriteParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FileWriteParams.

        Examples
        --------
        >>> FileWriteParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FileWriteParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class FileWriteResults(CoreObject):
    """Results of file write operation.
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
        """Initializes the FileWriteResults.

        Parameters
        ----------
        model: Model
            Model to create a FileWriteResults object with default parameters.
        error_code: ErrorCode, optional
            Error code if file write operation is unsuccessful.
        json_data: dict, optional
            JSON dictionary to create a FileWriteResults object with provided parameters.

        Examples
        --------
        >>> file_write_results = prime.FileWriteResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "FileWriteResults")
                    json_data = param_json["FileWriteResults"] if "FileWriteResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( FileWriteResults._default_params["error_code"] if "error_code" in FileWriteResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of FileWriteResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code if file write operation is unsuccessful.
        """
        args = locals()
        [FileWriteResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of FileWriteResults.

        Examples
        --------
        >>> FileWriteResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FileWriteResults._default_params.items())
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
        """Error code if file write operation is unsuccessful.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class ReadSizeFieldParams(CoreObject):
    """Parameters used to read size field file.
    """
    _default_params = {}

    def __initialize(
            self,
            append: bool):
        self._append = append

    def __init__(
            self,
            model: CommunicationManager=None,
            append: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ReadSizeFieldParams.

        Parameters
        ----------
        model: Model
            Model to create a ReadSizeFieldParams object with default parameters.
        append: bool, optional
            Option to append the size fields from file.
        json_data: dict, optional
            JSON dictionary to create a ReadSizeFieldParams object with provided parameters.

        Examples
        --------
        >>> read_size_field_params = prime.ReadSizeFieldParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["append"] if "append" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [append])
            if all_field_specified:
                self.__initialize(
                    append)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ReadSizeFieldParams")
                    json_data = param_json["ReadSizeFieldParams"] if "ReadSizeFieldParams" in param_json else {}
                    self.__initialize(
                        append if append is not None else ( ReadSizeFieldParams._default_params["append"] if "append" in ReadSizeFieldParams._default_params else (json_data["append"] if "append" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            append: bool = None):
        """Set the default values of ReadSizeFieldParams.

        Parameters
        ----------
        append: bool, optional
            Option to append the size fields from file.
        """
        args = locals()
        [ReadSizeFieldParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ReadSizeFieldParams.

        Examples
        --------
        >>> ReadSizeFieldParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ReadSizeFieldParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._append is not None:
            json_data["append"] = self._append
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "append :  %s" % (self._append)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def append(self) -> bool:
        """Option to append the size fields from file.
        """
        return self._append

    @append.setter
    def append(self, value: bool):
        self._append = value

class WriteSizeFieldParams(CoreObject):
    """Parameters used to write size field file.
    """
    _default_params = {}

    def __initialize(
            self,
            write_only_active_size_fields: bool):
        self._write_only_active_size_fields = write_only_active_size_fields

    def __init__(
            self,
            model: CommunicationManager=None,
            write_only_active_size_fields: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the WriteSizeFieldParams.

        Parameters
        ----------
        model: Model
            Model to create a WriteSizeFieldParams object with default parameters.
        write_only_active_size_fields: bool, optional
            Option to write only active size fields into the file.
        json_data: dict, optional
            JSON dictionary to create a WriteSizeFieldParams object with provided parameters.

        Examples
        --------
        >>> write_size_field_params = prime.WriteSizeFieldParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["writeOnlyActiveSizeFields"] if "writeOnlyActiveSizeFields" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [write_only_active_size_fields])
            if all_field_specified:
                self.__initialize(
                    write_only_active_size_fields)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "WriteSizeFieldParams")
                    json_data = param_json["WriteSizeFieldParams"] if "WriteSizeFieldParams" in param_json else {}
                    self.__initialize(
                        write_only_active_size_fields if write_only_active_size_fields is not None else ( WriteSizeFieldParams._default_params["write_only_active_size_fields"] if "write_only_active_size_fields" in WriteSizeFieldParams._default_params else (json_data["writeOnlyActiveSizeFields"] if "writeOnlyActiveSizeFields" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            write_only_active_size_fields: bool = None):
        """Set the default values of WriteSizeFieldParams.

        Parameters
        ----------
        write_only_active_size_fields: bool, optional
            Option to write only active size fields into the file.
        """
        args = locals()
        [WriteSizeFieldParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of WriteSizeFieldParams.

        Examples
        --------
        >>> WriteSizeFieldParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in WriteSizeFieldParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._write_only_active_size_fields is not None:
            json_data["writeOnlyActiveSizeFields"] = self._write_only_active_size_fields
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "write_only_active_size_fields :  %s" % (self._write_only_active_size_fields)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def write_only_active_size_fields(self) -> bool:
        """Option to write only active size fields into the file.
        """
        return self._write_only_active_size_fields

    @write_only_active_size_fields.setter
    def write_only_active_size_fields(self, value: bool):
        self._write_only_active_size_fields = value

class ExportFluentCaseParams(CoreObject):
    """Parameters to export fluent case file.
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
        """Initializes the ExportFluentCaseParams.

        Parameters
        ----------
        model: Model
            Model to create a ExportFluentCaseParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a ExportFluentCaseParams object with provided parameters.

        Examples
        --------
        >>> export_fluent_case_params = prime.ExportFluentCaseParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "ExportFluentCaseParams")
                    json_data = param_json["ExportFluentCaseParams"] if "ExportFluentCaseParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of ExportFluentCaseParams.

        """
        args = locals()
        [ExportFluentCaseParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExportFluentCaseParams.

        Examples
        --------
        >>> ExportFluentCaseParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportFluentCaseParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class ExportFluentMeshingMeshParams(CoreObject):
    """Parameters used to export fluent meshing mesh.
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
        """Initializes the ExportFluentMeshingMeshParams.

        Parameters
        ----------
        model: Model
            Model to create a ExportFluentMeshingMeshParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a ExportFluentMeshingMeshParams object with provided parameters.

        Examples
        --------
        >>> export_fluent_meshing_mesh_params = prime.ExportFluentMeshingMeshParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "ExportFluentMeshingMeshParams")
                    json_data = param_json["ExportFluentMeshingMeshParams"] if "ExportFluentMeshingMeshParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of ExportFluentMeshingMeshParams.

        """
        args = locals()
        [ExportFluentMeshingMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExportFluentMeshingMeshParams.

        Examples
        --------
        >>> ExportFluentMeshingMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportFluentMeshingMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class CadRefacetingParams(CoreObject):
    """Parameters to refacet CAD during import.
    """
    _default_params = {}

    def __initialize(
            self,
            cad_faceter: CadFaceter,
            faceting_resolution: CadRefacetingResolution,
            custom_surface_deviation_tolerance: float,
            custom_normal_angle_tolerance: float,
            max_edge_size_limit: CadRefacetingMaxEdgeSizeLimit,
            max_edge_size: float):
        self._cad_faceter = CadFaceter(cad_faceter)
        self._faceting_resolution = CadRefacetingResolution(faceting_resolution)
        self._custom_surface_deviation_tolerance = custom_surface_deviation_tolerance
        self._custom_normal_angle_tolerance = custom_normal_angle_tolerance
        self._max_edge_size_limit = CadRefacetingMaxEdgeSizeLimit(max_edge_size_limit)
        self._max_edge_size = max_edge_size

    def __init__(
            self,
            model: CommunicationManager=None,
            cad_faceter: CadFaceter = None,
            faceting_resolution: CadRefacetingResolution = None,
            custom_surface_deviation_tolerance: float = None,
            custom_normal_angle_tolerance: float = None,
            max_edge_size_limit: CadRefacetingMaxEdgeSizeLimit = None,
            max_edge_size: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the CadRefacetingParams.

        Parameters
        ----------
        model: Model
            Model to create a CadRefacetingParams object with default parameters.
        cad_faceter: CadFaceter, optional
            Specify the available choices for faceter. The available options are Acis, Parasolid.
        faceting_resolution: CadRefacetingResolution, optional
            Set the faceting resolution.
        custom_surface_deviation_tolerance: float, optional
            Set custom tolerance for surface deviation in specified length unit.
        custom_normal_angle_tolerance: float, optional
            Set custom tolerance for normal angle in degree.
        max_edge_size_limit: CadRefacetingMaxEdgeSizeLimit, optional
            Specify maximum edge size limit for faceting.
        max_edge_size: float, optional
            Set maximum edge size of the facets.
        json_data: dict, optional
            JSON dictionary to create a CadRefacetingParams object with provided parameters.

        Examples
        --------
        >>> cad_refaceting_params = prime.CadRefacetingParams(model = model)
        """
        if json_data:
            self.__initialize(
                CadFaceter(json_data["cadFaceter"] if "cadFaceter" in json_data else None),
                CadRefacetingResolution(json_data["facetingResolution"] if "facetingResolution" in json_data else None),
                json_data["customSurfaceDeviationTolerance"] if "customSurfaceDeviationTolerance" in json_data else None,
                json_data["customNormalAngleTolerance"] if "customNormalAngleTolerance" in json_data else None,
                CadRefacetingMaxEdgeSizeLimit(json_data["maxEdgeSizeLimit"] if "maxEdgeSizeLimit" in json_data else None),
                json_data["maxEdgeSize"] if "maxEdgeSize" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [cad_faceter, faceting_resolution, custom_surface_deviation_tolerance, custom_normal_angle_tolerance, max_edge_size_limit, max_edge_size])
            if all_field_specified:
                self.__initialize(
                    cad_faceter,
                    faceting_resolution,
                    custom_surface_deviation_tolerance,
                    custom_normal_angle_tolerance,
                    max_edge_size_limit,
                    max_edge_size)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "CadRefacetingParams")
                    json_data = param_json["CadRefacetingParams"] if "CadRefacetingParams" in param_json else {}
                    self.__initialize(
                        cad_faceter if cad_faceter is not None else ( CadRefacetingParams._default_params["cad_faceter"] if "cad_faceter" in CadRefacetingParams._default_params else CadFaceter(json_data["cadFaceter"] if "cadFaceter" in json_data else None)),
                        faceting_resolution if faceting_resolution is not None else ( CadRefacetingParams._default_params["faceting_resolution"] if "faceting_resolution" in CadRefacetingParams._default_params else CadRefacetingResolution(json_data["facetingResolution"] if "facetingResolution" in json_data else None)),
                        custom_surface_deviation_tolerance if custom_surface_deviation_tolerance is not None else ( CadRefacetingParams._default_params["custom_surface_deviation_tolerance"] if "custom_surface_deviation_tolerance" in CadRefacetingParams._default_params else (json_data["customSurfaceDeviationTolerance"] if "customSurfaceDeviationTolerance" in json_data else None)),
                        custom_normal_angle_tolerance if custom_normal_angle_tolerance is not None else ( CadRefacetingParams._default_params["custom_normal_angle_tolerance"] if "custom_normal_angle_tolerance" in CadRefacetingParams._default_params else (json_data["customNormalAngleTolerance"] if "customNormalAngleTolerance" in json_data else None)),
                        max_edge_size_limit if max_edge_size_limit is not None else ( CadRefacetingParams._default_params["max_edge_size_limit"] if "max_edge_size_limit" in CadRefacetingParams._default_params else CadRefacetingMaxEdgeSizeLimit(json_data["maxEdgeSizeLimit"] if "maxEdgeSizeLimit" in json_data else None)),
                        max_edge_size if max_edge_size is not None else ( CadRefacetingParams._default_params["max_edge_size"] if "max_edge_size" in CadRefacetingParams._default_params else (json_data["maxEdgeSize"] if "maxEdgeSize" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            cad_faceter: CadFaceter = None,
            faceting_resolution: CadRefacetingResolution = None,
            custom_surface_deviation_tolerance: float = None,
            custom_normal_angle_tolerance: float = None,
            max_edge_size_limit: CadRefacetingMaxEdgeSizeLimit = None,
            max_edge_size: float = None):
        """Set the default values of CadRefacetingParams.

        Parameters
        ----------
        cad_faceter: CadFaceter, optional
            Specify the available choices for faceter. The available options are Acis, Parasolid.
        faceting_resolution: CadRefacetingResolution, optional
            Set the faceting resolution.
        custom_surface_deviation_tolerance: float, optional
            Set custom tolerance for surface deviation in specified length unit.
        custom_normal_angle_tolerance: float, optional
            Set custom tolerance for normal angle in degree.
        max_edge_size_limit: CadRefacetingMaxEdgeSizeLimit, optional
            Specify maximum edge size limit for faceting.
        max_edge_size: float, optional
            Set maximum edge size of the facets.
        """
        args = locals()
        [CadRefacetingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of CadRefacetingParams.

        Examples
        --------
        >>> CadRefacetingParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CadRefacetingParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._cad_faceter is not None:
            json_data["cadFaceter"] = self._cad_faceter
        if self._faceting_resolution is not None:
            json_data["facetingResolution"] = self._faceting_resolution
        if self._custom_surface_deviation_tolerance is not None:
            json_data["customSurfaceDeviationTolerance"] = self._custom_surface_deviation_tolerance
        if self._custom_normal_angle_tolerance is not None:
            json_data["customNormalAngleTolerance"] = self._custom_normal_angle_tolerance
        if self._max_edge_size_limit is not None:
            json_data["maxEdgeSizeLimit"] = self._max_edge_size_limit
        if self._max_edge_size is not None:
            json_data["maxEdgeSize"] = self._max_edge_size
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "cad_faceter :  %s\nfaceting_resolution :  %s\ncustom_surface_deviation_tolerance :  %s\ncustom_normal_angle_tolerance :  %s\nmax_edge_size_limit :  %s\nmax_edge_size :  %s" % (self._cad_faceter, self._faceting_resolution, self._custom_surface_deviation_tolerance, self._custom_normal_angle_tolerance, self._max_edge_size_limit, self._max_edge_size)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def cad_faceter(self) -> CadFaceter:
        """Specify the available choices for faceter. The available options are Acis, Parasolid.
        """
        return self._cad_faceter

    @cad_faceter.setter
    def cad_faceter(self, value: CadFaceter):
        self._cad_faceter = value

    @property
    def faceting_resolution(self) -> CadRefacetingResolution:
        """Set the faceting resolution.
        """
        return self._faceting_resolution

    @faceting_resolution.setter
    def faceting_resolution(self, value: CadRefacetingResolution):
        self._faceting_resolution = value

    @property
    def custom_surface_deviation_tolerance(self) -> float:
        """Set custom tolerance for surface deviation in specified length unit.
        """
        return self._custom_surface_deviation_tolerance

    @custom_surface_deviation_tolerance.setter
    def custom_surface_deviation_tolerance(self, value: float):
        self._custom_surface_deviation_tolerance = value

    @property
    def custom_normal_angle_tolerance(self) -> float:
        """Set custom tolerance for normal angle in degree.
        """
        return self._custom_normal_angle_tolerance

    @custom_normal_angle_tolerance.setter
    def custom_normal_angle_tolerance(self, value: float):
        self._custom_normal_angle_tolerance = value

    @property
    def max_edge_size_limit(self) -> CadRefacetingMaxEdgeSizeLimit:
        """Specify maximum edge size limit for faceting.
        """
        return self._max_edge_size_limit

    @max_edge_size_limit.setter
    def max_edge_size_limit(self, value: CadRefacetingMaxEdgeSizeLimit):
        self._max_edge_size_limit = value

    @property
    def max_edge_size(self) -> float:
        """Set maximum edge size of the facets.
        """
        return self._max_edge_size

    @max_edge_size.setter
    def max_edge_size(self, value: float):
        self._max_edge_size = value

class ImportCadParams(CoreObject):
    """Parameters to control CAD import settings.
    """
    _default_params = {}

    def __initialize(
            self,
            append: bool,
            cad_reader_route: CadReaderRoute,
            part_creation_type: PartCreationType,
            geometry_transfer: bool,
            length_unit: LengthUnit,
            refacet: bool,
            cad_refaceting_params: CadRefacetingParams,
            stitch_tolerance: float,
            cad_update_parameters: Dict[str, Union[str, int, float, bool]]):
        self._append = append
        self._cad_reader_route = CadReaderRoute(cad_reader_route)
        self._part_creation_type = PartCreationType(part_creation_type)
        self._geometry_transfer = geometry_transfer
        self._length_unit = LengthUnit(length_unit)
        self._refacet = refacet
        self._cad_refaceting_params = cad_refaceting_params
        self._stitch_tolerance = stitch_tolerance
        self._cad_update_parameters = cad_update_parameters

    def __init__(
            self,
            model: CommunicationManager=None,
            append: bool = None,
            cad_reader_route: CadReaderRoute = None,
            part_creation_type: PartCreationType = None,
            geometry_transfer: bool = None,
            length_unit: LengthUnit = None,
            refacet: bool = None,
            cad_refaceting_params: CadRefacetingParams = None,
            stitch_tolerance: float = None,
            cad_update_parameters: Dict[str, Union[str, int, float, bool]] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ImportCadParams.

        Parameters
        ----------
        model: Model
            Model to create a ImportCadParams object with default parameters.
        append: bool, optional
            Append imported CAD into existing model when true.
        cad_reader_route: CadReaderRoute, optional
            Specify the available CAD reader routes. The available CAD reader routes are ProgramControlled, Native, WorkBench, SpaceClaim.
        part_creation_type: PartCreationType, optional
            Create a part per CAD Model, Assembly, Part, Body.
        geometry_transfer: bool, optional
            Option to enable transfer of geometry data (NURBS).
        length_unit: LengthUnit, optional
            Specify length unit for import.
        refacet: bool, optional
            Refine or coarsen the CAD faceting based on refaceting parameters when true.
        cad_refaceting_params: CadRefacetingParams, optional
            Specify refaceting parameters.
        stitch_tolerance: float, optional
            Stitch facets based on tolerance. Available only with WorkBench CAD Reader route.
        cad_update_parameters: Dict[str, Union[str, int, float, bool]], optional
            Specify the CAD parameters for parametric CAD update. Available only with WorkBench CAD Reader route.
        json_data: dict, optional
            JSON dictionary to create a ImportCadParams object with provided parameters.

        Examples
        --------
        >>> import_cad_params = prime.ImportCadParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["append"] if "append" in json_data else None,
                CadReaderRoute(json_data["cadReaderRoute"] if "cadReaderRoute" in json_data else None),
                PartCreationType(json_data["partCreationType"] if "partCreationType" in json_data else None),
                json_data["geometryTransfer"] if "geometryTransfer" in json_data else None,
                LengthUnit(json_data["lengthUnit"] if "lengthUnit" in json_data else None),
                json_data["refacet"] if "refacet" in json_data else None,
                CadRefacetingParams(model = model, json_data = json_data["cadRefacetingParams"] if "cadRefacetingParams" in json_data else None),
                json_data["stitchTolerance"] if "stitchTolerance" in json_data else None,
                json_data["cadUpdateParameters"] if "cadUpdateParameters" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [append, cad_reader_route, part_creation_type, geometry_transfer, length_unit, refacet, cad_refaceting_params, stitch_tolerance, cad_update_parameters])
            if all_field_specified:
                self.__initialize(
                    append,
                    cad_reader_route,
                    part_creation_type,
                    geometry_transfer,
                    length_unit,
                    refacet,
                    cad_refaceting_params,
                    stitch_tolerance,
                    cad_update_parameters)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ImportCadParams")
                    json_data = param_json["ImportCadParams"] if "ImportCadParams" in param_json else {}
                    self.__initialize(
                        append if append is not None else ( ImportCadParams._default_params["append"] if "append" in ImportCadParams._default_params else (json_data["append"] if "append" in json_data else None)),
                        cad_reader_route if cad_reader_route is not None else ( ImportCadParams._default_params["cad_reader_route"] if "cad_reader_route" in ImportCadParams._default_params else CadReaderRoute(json_data["cadReaderRoute"] if "cadReaderRoute" in json_data else None)),
                        part_creation_type if part_creation_type is not None else ( ImportCadParams._default_params["part_creation_type"] if "part_creation_type" in ImportCadParams._default_params else PartCreationType(json_data["partCreationType"] if "partCreationType" in json_data else None)),
                        geometry_transfer if geometry_transfer is not None else ( ImportCadParams._default_params["geometry_transfer"] if "geometry_transfer" in ImportCadParams._default_params else (json_data["geometryTransfer"] if "geometryTransfer" in json_data else None)),
                        length_unit if length_unit is not None else ( ImportCadParams._default_params["length_unit"] if "length_unit" in ImportCadParams._default_params else LengthUnit(json_data["lengthUnit"] if "lengthUnit" in json_data else None)),
                        refacet if refacet is not None else ( ImportCadParams._default_params["refacet"] if "refacet" in ImportCadParams._default_params else (json_data["refacet"] if "refacet" in json_data else None)),
                        cad_refaceting_params if cad_refaceting_params is not None else ( ImportCadParams._default_params["cad_refaceting_params"] if "cad_refaceting_params" in ImportCadParams._default_params else CadRefacetingParams(model = model, json_data = (json_data["cadRefacetingParams"] if "cadRefacetingParams" in json_data else None))),
                        stitch_tolerance if stitch_tolerance is not None else ( ImportCadParams._default_params["stitch_tolerance"] if "stitch_tolerance" in ImportCadParams._default_params else (json_data["stitchTolerance"] if "stitchTolerance" in json_data else None)),
                        cad_update_parameters if cad_update_parameters is not None else ( ImportCadParams._default_params["cad_update_parameters"] if "cad_update_parameters" in ImportCadParams._default_params else (json_data["cadUpdateParameters"] if "cadUpdateParameters" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            append: bool = None,
            cad_reader_route: CadReaderRoute = None,
            part_creation_type: PartCreationType = None,
            geometry_transfer: bool = None,
            length_unit: LengthUnit = None,
            refacet: bool = None,
            cad_refaceting_params: CadRefacetingParams = None,
            stitch_tolerance: float = None,
            cad_update_parameters: Dict[str, Union[str, int, float, bool]] = None):
        """Set the default values of ImportCadParams.

        Parameters
        ----------
        append: bool, optional
            Append imported CAD into existing model when true.
        cad_reader_route: CadReaderRoute, optional
            Specify the available CAD reader routes. The available CAD reader routes are ProgramControlled, Native, WorkBench, SpaceClaim.
        part_creation_type: PartCreationType, optional
            Create a part per CAD Model, Assembly, Part, Body.
        geometry_transfer: bool, optional
            Option to enable transfer of geometry data (NURBS).
        length_unit: LengthUnit, optional
            Specify length unit for import.
        refacet: bool, optional
            Refine or coarsen the CAD faceting based on refaceting parameters when true.
        cad_refaceting_params: CadRefacetingParams, optional
            Specify refaceting parameters.
        stitch_tolerance: float, optional
            Stitch facets based on tolerance. Available only with WorkBench CAD Reader route.
        cad_update_parameters: Dict[str, Union[str, int, float, bool]], optional
            Specify the CAD parameters for parametric CAD update. Available only with WorkBench CAD Reader route.
        """
        args = locals()
        [ImportCadParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ImportCadParams.

        Examples
        --------
        >>> ImportCadParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ImportCadParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._append is not None:
            json_data["append"] = self._append
        if self._cad_reader_route is not None:
            json_data["cadReaderRoute"] = self._cad_reader_route
        if self._part_creation_type is not None:
            json_data["partCreationType"] = self._part_creation_type
        if self._geometry_transfer is not None:
            json_data["geometryTransfer"] = self._geometry_transfer
        if self._length_unit is not None:
            json_data["lengthUnit"] = self._length_unit
        if self._refacet is not None:
            json_data["refacet"] = self._refacet
        if self._cad_refaceting_params is not None:
            json_data["cadRefacetingParams"] = self._cad_refaceting_params._jsonify()
        if self._stitch_tolerance is not None:
            json_data["stitchTolerance"] = self._stitch_tolerance
        if self._cad_update_parameters is not None:
            json_data["cadUpdateParameters"] = self._cad_update_parameters
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "append :  %s\ncad_reader_route :  %s\npart_creation_type :  %s\ngeometry_transfer :  %s\nlength_unit :  %s\nrefacet :  %s\ncad_refaceting_params :  %s\nstitch_tolerance :  %s\ncad_update_parameters :  %s" % (self._append, self._cad_reader_route, self._part_creation_type, self._geometry_transfer, self._length_unit, self._refacet, '{ ' + str(self._cad_refaceting_params) + ' }', self._stitch_tolerance, self._cad_update_parameters)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def append(self) -> bool:
        """Append imported CAD into existing model when true.
        """
        return self._append

    @append.setter
    def append(self, value: bool):
        self._append = value

    @property
    def cad_reader_route(self) -> CadReaderRoute:
        """Specify the available CAD reader routes. The available CAD reader routes are ProgramControlled, Native, WorkBench, SpaceClaim.
        """
        return self._cad_reader_route

    @cad_reader_route.setter
    def cad_reader_route(self, value: CadReaderRoute):
        self._cad_reader_route = value

    @property
    def part_creation_type(self) -> PartCreationType:
        """Create a part per CAD Model, Assembly, Part, Body.
        """
        return self._part_creation_type

    @part_creation_type.setter
    def part_creation_type(self, value: PartCreationType):
        self._part_creation_type = value

    @property
    def geometry_transfer(self) -> bool:
        """Option to enable transfer of geometry data (NURBS).
        """
        return self._geometry_transfer

    @geometry_transfer.setter
    def geometry_transfer(self, value: bool):
        self._geometry_transfer = value

    @property
    def length_unit(self) -> LengthUnit:
        """Specify length unit for import.
        """
        return self._length_unit

    @length_unit.setter
    def length_unit(self, value: LengthUnit):
        self._length_unit = value

    @property
    def refacet(self) -> bool:
        """Refine or coarsen the CAD faceting based on refaceting parameters when true.
        """
        return self._refacet

    @refacet.setter
    def refacet(self, value: bool):
        self._refacet = value

    @property
    def cad_refaceting_params(self) -> CadRefacetingParams:
        """Specify refaceting parameters.
        """
        return self._cad_refaceting_params

    @cad_refaceting_params.setter
    def cad_refaceting_params(self, value: CadRefacetingParams):
        self._cad_refaceting_params = value

    @property
    def stitch_tolerance(self) -> float:
        """Stitch facets based on tolerance. Available only with WorkBench CAD Reader route.
        """
        return self._stitch_tolerance

    @stitch_tolerance.setter
    def stitch_tolerance(self, value: float):
        self._stitch_tolerance = value

    @property
    def cad_update_parameters(self) -> Dict[str, Union[str, int, float, bool]]:
        """Specify the CAD parameters for parametric CAD update. Available only with WorkBench CAD Reader route.
        """
        return self._cad_update_parameters

    @cad_update_parameters.setter
    def cad_update_parameters(self, value: Dict[str, Union[str, int, float, bool]]):
        self._cad_update_parameters = value

class ImportCadResults(CoreObject):
    """Results associated with the CAD import.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            cad_parameters: Dict[str, Union[str, int, float, bool]]):
        self._error_code = ErrorCode(error_code)
        self._cad_parameters = cad_parameters

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            cad_parameters: Dict[str, Union[str, int, float, bool]] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ImportCadResults.

        Parameters
        ----------
        model: Model
            Model to create a ImportCadResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        cad_parameters: Dict[str, Union[str, int, float, bool]], optional
            Returns the parameters associated with CAD. Available only with WorkBench CAD Reader route.
        json_data: dict, optional
            JSON dictionary to create a ImportCadResults object with provided parameters.

        Examples
        --------
        >>> import_cad_results = prime.ImportCadResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["cadParameters"] if "cadParameters" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, cad_parameters])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    cad_parameters)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ImportCadResults")
                    json_data = param_json["ImportCadResults"] if "ImportCadResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ImportCadResults._default_params["error_code"] if "error_code" in ImportCadResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        cad_parameters if cad_parameters is not None else ( ImportCadResults._default_params["cad_parameters"] if "cad_parameters" in ImportCadResults._default_params else (json_data["cadParameters"] if "cadParameters" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            cad_parameters: Dict[str, Union[str, int, float, bool]] = None):
        """Set the default values of ImportCadResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        cad_parameters: Dict[str, Union[str, int, float, bool]], optional
            Returns the parameters associated with CAD. Available only with WorkBench CAD Reader route.
        """
        args = locals()
        [ImportCadResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ImportCadResults.

        Examples
        --------
        >>> ImportCadResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ImportCadResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._cad_parameters is not None:
            json_data["cadParameters"] = self._cad_parameters
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\ncad_parameters :  %s" % (self._error_code, self._cad_parameters)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def cad_parameters(self) -> Dict[str, Union[str, int, float, bool]]:
        """Returns the parameters associated with CAD. Available only with WorkBench CAD Reader route.
        """
        return self._cad_parameters

    @cad_parameters.setter
    def cad_parameters(self, value: Dict[str, Union[str, int, float, bool]]):
        self._cad_parameters = value

class ImportFluentMeshingMeshParams(CoreObject):
    """Parameters used to import fluent meshing mesh.
    """
    _default_params = {}

    def __initialize(
            self,
            append: bool,
            enable_multi_threading: bool):
        self._append = append
        self._enable_multi_threading = enable_multi_threading

    def __init__(
            self,
            model: CommunicationManager=None,
            append: bool = None,
            enable_multi_threading: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ImportFluentMeshingMeshParams.

        Parameters
        ----------
        model: Model
            Model to create a ImportFluentMeshingMeshParams object with default parameters.
        append: bool, optional
            Option to append imported mesh to existing mesh instead of resetting model to imported mesh.
        enable_multi_threading: bool, optional
            Option to import multiple files in parallel using multithreading.
        json_data: dict, optional
            JSON dictionary to create a ImportFluentMeshingMeshParams object with provided parameters.

        Examples
        --------
        >>> import_fluent_meshing_mesh_params = prime.ImportFluentMeshingMeshParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["append"] if "append" in json_data else None,
                json_data["enableMultiThreading"] if "enableMultiThreading" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [append, enable_multi_threading])
            if all_field_specified:
                self.__initialize(
                    append,
                    enable_multi_threading)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ImportFluentMeshingMeshParams")
                    json_data = param_json["ImportFluentMeshingMeshParams"] if "ImportFluentMeshingMeshParams" in param_json else {}
                    self.__initialize(
                        append if append is not None else ( ImportFluentMeshingMeshParams._default_params["append"] if "append" in ImportFluentMeshingMeshParams._default_params else (json_data["append"] if "append" in json_data else None)),
                        enable_multi_threading if enable_multi_threading is not None else ( ImportFluentMeshingMeshParams._default_params["enable_multi_threading"] if "enable_multi_threading" in ImportFluentMeshingMeshParams._default_params else (json_data["enableMultiThreading"] if "enableMultiThreading" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            append: bool = None,
            enable_multi_threading: bool = None):
        """Set the default values of ImportFluentMeshingMeshParams.

        Parameters
        ----------
        append: bool, optional
            Option to append imported mesh to existing mesh instead of resetting model to imported mesh.
        enable_multi_threading: bool, optional
            Option to import multiple files in parallel using multithreading.
        """
        args = locals()
        [ImportFluentMeshingMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ImportFluentMeshingMeshParams.

        Examples
        --------
        >>> ImportFluentMeshingMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ImportFluentMeshingMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._append is not None:
            json_data["append"] = self._append
        if self._enable_multi_threading is not None:
            json_data["enableMultiThreading"] = self._enable_multi_threading
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "append :  %s\nenable_multi_threading :  %s" % (self._append, self._enable_multi_threading)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def append(self) -> bool:
        """Option to append imported mesh to existing mesh instead of resetting model to imported mesh.
        """
        return self._append

    @append.setter
    def append(self, value: bool):
        self._append = value

    @property
    def enable_multi_threading(self) -> bool:
        """Option to import multiple files in parallel using multithreading.
        """
        return self._enable_multi_threading

    @enable_multi_threading.setter
    def enable_multi_threading(self, value: bool):
        self._enable_multi_threading = value

class ImportFluentMeshingMeshResults(CoreObject):
    """Results associated with fluent meshing mesh import.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            new_parts_created: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._new_parts_created = new_parts_created if isinstance(new_parts_created, np.ndarray) else np.array(new_parts_created, dtype=np.int32) if new_parts_created is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            new_parts_created: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ImportFluentMeshingMeshResults.

        Parameters
        ----------
        model: Model
            Model to create a ImportFluentMeshingMeshResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        new_parts_created: Iterable[int], optional
            Ids of new parts created for each file unreferenced fluent meshing mesh zones.
        json_data: dict, optional
            JSON dictionary to create a ImportFluentMeshingMeshResults object with provided parameters.

        Examples
        --------
        >>> import_fluent_meshing_mesh_results = prime.ImportFluentMeshingMeshResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["newPartsCreated"] if "newPartsCreated" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, new_parts_created])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    new_parts_created)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ImportFluentMeshingMeshResults")
                    json_data = param_json["ImportFluentMeshingMeshResults"] if "ImportFluentMeshingMeshResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ImportFluentMeshingMeshResults._default_params["error_code"] if "error_code" in ImportFluentMeshingMeshResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        new_parts_created if new_parts_created is not None else ( ImportFluentMeshingMeshResults._default_params["new_parts_created"] if "new_parts_created" in ImportFluentMeshingMeshResults._default_params else (json_data["newPartsCreated"] if "newPartsCreated" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            new_parts_created: Iterable[int] = None):
        """Set the default values of ImportFluentMeshingMeshResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        new_parts_created: Iterable[int], optional
            Ids of new parts created for each file unreferenced fluent meshing mesh zones.
        """
        args = locals()
        [ImportFluentMeshingMeshResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ImportFluentMeshingMeshResults.

        Examples
        --------
        >>> ImportFluentMeshingMeshResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ImportFluentMeshingMeshResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._new_parts_created is not None:
            json_data["newPartsCreated"] = self._new_parts_created
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nnew_parts_created :  %s" % (self._error_code, self._new_parts_created)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def new_parts_created(self) -> Iterable[int]:
        """Ids of new parts created for each file unreferenced fluent meshing mesh zones.
        """
        return self._new_parts_created

    @new_parts_created.setter
    def new_parts_created(self, value: Iterable[int]):
        self._new_parts_created = value

class ImportFluentCaseParams(CoreObject):
    """Parameters to import fluent case file.
    """
    _default_params = {}

    def __initialize(
            self,
            append: bool):
        self._append = append

    def __init__(
            self,
            model: CommunicationManager=None,
            append: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ImportFluentCaseParams.

        Parameters
        ----------
        model: Model
            Model to create a ImportFluentCaseParams object with default parameters.
        append: bool, optional
            Option to append imported case instead of resetting model to imported case.
        json_data: dict, optional
            JSON dictionary to create a ImportFluentCaseParams object with provided parameters.

        Examples
        --------
        >>> import_fluent_case_params = prime.ImportFluentCaseParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["append"] if "append" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [append])
            if all_field_specified:
                self.__initialize(
                    append)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ImportFluentCaseParams")
                    json_data = param_json["ImportFluentCaseParams"] if "ImportFluentCaseParams" in param_json else {}
                    self.__initialize(
                        append if append is not None else ( ImportFluentCaseParams._default_params["append"] if "append" in ImportFluentCaseParams._default_params else (json_data["append"] if "append" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            append: bool = None):
        """Set the default values of ImportFluentCaseParams.

        Parameters
        ----------
        append: bool, optional
            Option to append imported case instead of resetting model to imported case.
        """
        args = locals()
        [ImportFluentCaseParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ImportFluentCaseParams.

        Examples
        --------
        >>> ImportFluentCaseParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ImportFluentCaseParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._append is not None:
            json_data["append"] = self._append
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "append :  %s" % (self._append)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def append(self) -> bool:
        """Option to append imported case instead of resetting model to imported case.
        """
        return self._append

    @append.setter
    def append(self, value: bool):
        self._append = value

class ImportFluentCaseResults(CoreObject):
    """Results associated with fluent case import.
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
        """Initializes the ImportFluentCaseResults.

        Parameters
        ----------
        model: Model
            Model to create a ImportFluentCaseResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        json_data: dict, optional
            JSON dictionary to create a ImportFluentCaseResults object with provided parameters.

        Examples
        --------
        >>> import_fluent_case_results = prime.ImportFluentCaseResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "ImportFluentCaseResults")
                    json_data = param_json["ImportFluentCaseResults"] if "ImportFluentCaseResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ImportFluentCaseResults._default_params["error_code"] if "error_code" in ImportFluentCaseResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of ImportFluentCaseResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        """
        args = locals()
        [ImportFluentCaseResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ImportFluentCaseResults.

        Examples
        --------
        >>> ImportFluentCaseResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ImportFluentCaseResults._default_params.items())
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
        """Error code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class ImportMapdlCdbParams(CoreObject):
    """Parameters to control MAPDL CDB import settings.
    """
    _default_params = {}

    def __initialize(
            self,
            drop_mid_nodes: bool,
            append: bool):
        self._drop_mid_nodes = drop_mid_nodes
        self._append = append

    def __init__(
            self,
            model: CommunicationManager=None,
            drop_mid_nodes: bool = None,
            append: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ImportMapdlCdbParams.

        Parameters
        ----------
        model: Model
            Model to create a ImportMapdlCdbParams object with default parameters.
        drop_mid_nodes: bool, optional
        append: bool, optional
        json_data: dict, optional
            JSON dictionary to create a ImportMapdlCdbParams object with provided parameters.

        Examples
        --------
        >>> import_mapdl_cdb_params = prime.ImportMapdlCdbParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["dropMidNodes"] if "dropMidNodes" in json_data else None,
                json_data["append"] if "append" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [drop_mid_nodes, append])
            if all_field_specified:
                self.__initialize(
                    drop_mid_nodes,
                    append)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ImportMapdlCdbParams")
                    json_data = param_json["ImportMapdlCdbParams"] if "ImportMapdlCdbParams" in param_json else {}
                    self.__initialize(
                        drop_mid_nodes if drop_mid_nodes is not None else ( ImportMapdlCdbParams._default_params["drop_mid_nodes"] if "drop_mid_nodes" in ImportMapdlCdbParams._default_params else (json_data["dropMidNodes"] if "dropMidNodes" in json_data else None)),
                        append if append is not None else ( ImportMapdlCdbParams._default_params["append"] if "append" in ImportMapdlCdbParams._default_params else (json_data["append"] if "append" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            drop_mid_nodes: bool = None,
            append: bool = None):
        """Set the default values of ImportMapdlCdbParams.

        Parameters
        ----------
        drop_mid_nodes: bool, optional
        append: bool, optional
        """
        args = locals()
        [ImportMapdlCdbParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ImportMapdlCdbParams.

        Examples
        --------
        >>> ImportMapdlCdbParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ImportMapdlCdbParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._drop_mid_nodes is not None:
            json_data["dropMidNodes"] = self._drop_mid_nodes
        if self._append is not None:
            json_data["append"] = self._append
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "drop_mid_nodes :  %s\nappend :  %s" % (self._drop_mid_nodes, self._append)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def drop_mid_nodes(self) -> bool:
        """
        Option to import quadratic mesh elements as linear by skipping mid nodes.
        """
        return self._drop_mid_nodes

    @drop_mid_nodes.setter
    def drop_mid_nodes(self, value: bool):
        self._drop_mid_nodes = value

    @property
    def append(self) -> bool:
        """
        Option to append imported cdb into existing model.
        """
        return self._append

    @append.setter
    def append(self, value: bool):
        self._append = value

class ImportMapdlCdbResults(CoreObject):
    """Results associated with the MAPDL CDB import.
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
        """Initializes the ImportMapdlCdbResults.

        Parameters
        ----------
        model: Model
            Model to create a ImportMapdlCdbResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        json_data: dict, optional
            JSON dictionary to create a ImportMapdlCdbResults object with provided parameters.

        Examples
        --------
        >>> import_mapdl_cdb_results = prime.ImportMapdlCdbResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "ImportMapdlCdbResults")
                    json_data = param_json["ImportMapdlCdbResults"] if "ImportMapdlCdbResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ImportMapdlCdbResults._default_params["error_code"] if "error_code" in ImportMapdlCdbResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of ImportMapdlCdbResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        """
        args = locals()
        [ImportMapdlCdbResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ImportMapdlCdbResults.

        Examples
        --------
        >>> ImportMapdlCdbResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ImportMapdlCdbResults._default_params.items())
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
        """Error code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class ExportMapdlCdbParams(CoreObject):
    """Parameters to control MAPDL CDB export settings.
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
        """Initializes the ExportMapdlCdbParams.

        Parameters
        ----------
        model: Model
            Model to create a ExportMapdlCdbParams object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a ExportMapdlCdbParams object with provided parameters.

        Examples
        --------
        >>> export_mapdl_cdb_params = prime.ExportMapdlCdbParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "ExportMapdlCdbParams")
                    json_data = param_json["ExportMapdlCdbParams"] if "ExportMapdlCdbParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of ExportMapdlCdbParams.

        """
        args = locals()
        [ExportMapdlCdbParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExportMapdlCdbParams.

        Examples
        --------
        >>> ExportMapdlCdbParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportMapdlCdbParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

class ExportMapdlCdbResults(CoreObject):
    """Results associated with the MAPDL CDB export.
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
        """Initializes the ExportMapdlCdbResults.

        Parameters
        ----------
        model: Model
            Model to create a ExportMapdlCdbResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        json_data: dict, optional
            JSON dictionary to create a ExportMapdlCdbResults object with provided parameters.

        Examples
        --------
        >>> export_mapdl_cdb_results = prime.ExportMapdlCdbResults(model = model)
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
                    param_json = model._communicator.initialize_params(model, "ExportMapdlCdbResults")
                    json_data = param_json["ExportMapdlCdbResults"] if "ExportMapdlCdbResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ExportMapdlCdbResults._default_params["error_code"] if "error_code" in ExportMapdlCdbResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of ExportMapdlCdbResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        """
        args = locals()
        [ExportMapdlCdbResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExportMapdlCdbResults.

        Examples
        --------
        >>> ExportMapdlCdbResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportMapdlCdbResults._default_params.items())
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
        """Error code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class ExportBoundaryFittedSplineParams(CoreObject):
    """Parameters for exporting boundary fitted splines.
    """
    _default_params = {}

    def __initialize(
            self,
            id_offset: int,
            id_start: int):
        self._id_offset = id_offset
        self._id_start = id_start

    def __init__(
            self,
            model: CommunicationManager=None,
            id_offset: int = None,
            id_start: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ExportBoundaryFittedSplineParams.

        Parameters
        ----------
        model: Model
            Model to create a ExportBoundaryFittedSplineParams object with default parameters.
        id_offset: int, optional
            Offset value for IGA entity ids between parts.
        id_start: int, optional
            Start ids for IGA entities.
        json_data: dict, optional
            JSON dictionary to create a ExportBoundaryFittedSplineParams object with provided parameters.

        Examples
        --------
        >>> export_boundary_fitted_spline_params = prime.ExportBoundaryFittedSplineParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["idOffset"] if "idOffset" in json_data else None,
                json_data["idStart"] if "idStart" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [id_offset, id_start])
            if all_field_specified:
                self.__initialize(
                    id_offset,
                    id_start)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ExportBoundaryFittedSplineParams")
                    json_data = param_json["ExportBoundaryFittedSplineParams"] if "ExportBoundaryFittedSplineParams" in param_json else {}
                    self.__initialize(
                        id_offset if id_offset is not None else ( ExportBoundaryFittedSplineParams._default_params["id_offset"] if "id_offset" in ExportBoundaryFittedSplineParams._default_params else (json_data["idOffset"] if "idOffset" in json_data else None)),
                        id_start if id_start is not None else ( ExportBoundaryFittedSplineParams._default_params["id_start"] if "id_start" in ExportBoundaryFittedSplineParams._default_params else (json_data["idStart"] if "idStart" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            id_offset: int = None,
            id_start: int = None):
        """Set the default values of ExportBoundaryFittedSplineParams.

        Parameters
        ----------
        id_offset: int, optional
            Offset value for IGA entity ids between parts.
        id_start: int, optional
            Start ids for IGA entities.
        """
        args = locals()
        [ExportBoundaryFittedSplineParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ExportBoundaryFittedSplineParams.

        Examples
        --------
        >>> ExportBoundaryFittedSplineParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportBoundaryFittedSplineParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._id_offset is not None:
            json_data["idOffset"] = self._id_offset
        if self._id_start is not None:
            json_data["idStart"] = self._id_start
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "id_offset :  %s\nid_start :  %s" % (self._id_offset, self._id_start)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def id_offset(self) -> int:
        """Offset value for IGA entity ids between parts.
        """
        return self._id_offset

    @id_offset.setter
    def id_offset(self, value: int):
        self._id_offset = value

    @property
    def id_start(self) -> int:
        """Start ids for IGA entities.
        """
        return self._id_start

    @id_start.setter
    def id_start(self, value: int):
        self._id_start = value
