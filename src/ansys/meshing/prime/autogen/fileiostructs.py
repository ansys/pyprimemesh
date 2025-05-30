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
    DISCOVERY = 4
    """Denotes Discovery as CAD reader route."""

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

class CdbAnalysisType(enum.IntEnum):
    """Provides the MAPDL CDB analysis type.
    """
    NONE = 0
    """Option to select no analysis type. This is the default option.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    OUTERPANELSTIFFNESS = 1
    """Option to select Outer Panel Stiffness as CDB analysis type.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    BELGIAN = 2
    """Option to select Belgian as CDB analysis type.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SEATRETRACTOR = 3
    """Option to select Seat Retractor as CDB analysis type.

    **This is a beta parameter**. **The behavior and name may change in the future**."""

class CdbSimulationType(enum.IntEnum):
    """Simulation Type for CDB export.
    """
    IMPLICIT = 0
    """Implicit simulation."""
    EXPLICIT = 1
    """Explicit Simulation."""

class SeparateBlocksFormatType(enum.IntEnum):
    """Format type for separate element blocks. Only applicable when write_separate_blocks is true.
    """
    STANDARD = 0
    """Standard format for element blocks.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    COMPACT = 1
    """Compact format for element blocks with reduced columns.

    **This is a beta parameter**. **The behavior and name may change in the future**."""

class LSDynaFileFormatType(enum.IntEnum):
    """Provides the format type to write the LS-DYNA file.
    """
    REGULAR = 0
    """Option to select 8-char width format to write ids for elements and nodes.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    I10 = 1
    """Option to select 10-char width format to write ids for elements and nodes.

    **This is a beta parameter**. **The behavior and name may change in the future**."""

class LSDynaAnalysisType(enum.IntEnum):
    """Provides the LS-DYNA analysis type.
    """
    DOORSLAM = 0
    """Option to select doorslam as LS-DYNA analysis type.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    SEATBELT = 1
    """Option to select Seatbelt as LS-DYNA analysis type.

    **This is a beta parameter**. **The behavior and name may change in the future**."""

class FileReadParams(CoreObject):
    """Parameters to read file.

    Parameters
    ----------
    model: Model
        Model to create a ``FileReadParams`` object with default parameters.
    append: bool, optional
        Option to append imported mesh to existing mesh instead of resetting model to imported mesh.
    json_data: dict, optional
        JSON dictionary to create a ``FileReadParams`` object with provided parameters.

    Examples
    --------
    >>> file_read_params = prime.FileReadParams(model = model)
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
        """Initialize a ``FileReadParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``FileReadParams`` object with default parameters.
        append: bool, optional
            Option to append imported mesh to existing mesh instead of resetting model to imported mesh.
        json_data: dict, optional
            JSON dictionary to create a ``FileReadParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``FileReadParams`` object.

        Parameters
        ----------
        append: bool, optional
            Option to append imported mesh to existing mesh instead of resetting model to imported mesh.
        """
        args = locals()
        [FileReadParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``FileReadParams`` object.

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

    Parameters
    ----------
    model: Model
        Model to create a ``SizeFieldFileReadResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code if size field file read operation was unsuccessful.
    size_field_ids: Iterable[int], optional
        Ids of size fields read by read size field operation.
    json_data: dict, optional
        JSON dictionary to create a ``SizeFieldFileReadResults`` object with provided parameters.

    Examples
    --------
    >>> size_field_file_read_results = prime.SizeFieldFileReadResults(model = model)
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
        """Initialize a ``SizeFieldFileReadResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``SizeFieldFileReadResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code if size field file read operation was unsuccessful.
        size_field_ids: Iterable[int], optional
            Ids of size fields read by read size field operation.
        json_data: dict, optional
            JSON dictionary to create a ``SizeFieldFileReadResults`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``SizeFieldFileReadResults`` object.

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
        """Print the default values of ``SizeFieldFileReadResults`` object.

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

    Parameters
    ----------
    model: Model
        Model to create a ``FileReadResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code if file read operation was unsuccessful.
    json_data: dict, optional
        JSON dictionary to create a ``FileReadResults`` object with provided parameters.

    Examples
    --------
    >>> file_read_results = prime.FileReadResults(model = model)
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
        """Initialize a ``FileReadResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``FileReadResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code if file read operation was unsuccessful.
        json_data: dict, optional
            JSON dictionary to create a ``FileReadResults`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``FileReadResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code if file read operation was unsuccessful.
        """
        args = locals()
        [FileReadResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``FileReadResults`` object.

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

    Parameters
    ----------
    model: Model
        Model to create a ``FileWriteParams`` object with default parameters.
    json_data: dict, optional
        JSON dictionary to create a ``FileWriteParams`` object with provided parameters.

    Examples
    --------
    >>> file_write_params = prime.FileWriteParams(model = model)
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
        """Initialize a ``FileWriteParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``FileWriteParams`` object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a ``FileWriteParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``FileWriteParams`` object.

        """
        args = locals()
        [FileWriteParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``FileWriteParams`` object.

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
        if len(message) == 0:
            message = 'The object has no parameters to print.'
        return message

class FileWriteResults(CoreObject):
    """Results of file write operation.

    Parameters
    ----------
    model: Model
        Model to create a ``FileWriteResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code if file write operation is unsuccessful.
    warning_codes: List[WarningCode], optional
        Warning codes associated with the file write operation.
    json_data: dict, optional
        JSON dictionary to create a ``FileWriteResults`` object with provided parameters.

    Examples
    --------
    >>> file_write_results = prime.FileWriteResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``FileWriteResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``FileWriteResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code if file write operation is unsuccessful.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the file write operation.
        json_data: dict, optional
            JSON dictionary to create a ``FileWriteResults`` object with provided parameters.

        Examples
        --------
        >>> file_write_results = prime.FileWriteResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "FileWriteResults")
                    json_data = param_json["FileWriteResults"] if "FileWriteResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( FileWriteResults._default_params["error_code"] if "error_code" in FileWriteResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( FileWriteResults._default_params["warning_codes"] if "warning_codes" in FileWriteResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of the ``FileWriteResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code if file write operation is unsuccessful.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the file write operation.
        """
        args = locals()
        [FileWriteResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``FileWriteResults`` object.

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
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
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

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the file write operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class ReadSizeFieldParams(CoreObject):
    """Parameters used to read size field file.

    Parameters
    ----------
    model: Model
        Model to create a ``ReadSizeFieldParams`` object with default parameters.
    append: bool, optional
        Option to append the size fields from file.
    json_data: dict, optional
        JSON dictionary to create a ``ReadSizeFieldParams`` object with provided parameters.

    Examples
    --------
    >>> read_size_field_params = prime.ReadSizeFieldParams(model = model)
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
        """Initialize a ``ReadSizeFieldParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ReadSizeFieldParams`` object with default parameters.
        append: bool, optional
            Option to append the size fields from file.
        json_data: dict, optional
            JSON dictionary to create a ``ReadSizeFieldParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``ReadSizeFieldParams`` object.

        Parameters
        ----------
        append: bool, optional
            Option to append the size fields from file.
        """
        args = locals()
        [ReadSizeFieldParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ReadSizeFieldParams`` object.

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

    Parameters
    ----------
    model: Model
        Model to create a ``WriteSizeFieldParams`` object with default parameters.
    write_only_active_size_fields: bool, optional
        Option to write only active size fields into the file.
    json_data: dict, optional
        JSON dictionary to create a ``WriteSizeFieldParams`` object with provided parameters.

    Examples
    --------
    >>> write_size_field_params = prime.WriteSizeFieldParams(model = model)
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
        """Initialize a ``WriteSizeFieldParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``WriteSizeFieldParams`` object with default parameters.
        write_only_active_size_fields: bool, optional
            Option to write only active size fields into the file.
        json_data: dict, optional
            JSON dictionary to create a ``WriteSizeFieldParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``WriteSizeFieldParams`` object.

        Parameters
        ----------
        write_only_active_size_fields: bool, optional
            Option to write only active size fields into the file.
        """
        args = locals()
        [WriteSizeFieldParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``WriteSizeFieldParams`` object.

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

    Parameters
    ----------
    model: Model
        Model to create a ``ExportFluentCaseParams`` object with default parameters.
    cff_format: bool, optional
        Option to specify whether to export Fluent case file in CFF format (.cas.h5) or legacy format (.cas, .cas.gz).
    json_data: dict, optional
        JSON dictionary to create a ``ExportFluentCaseParams`` object with provided parameters.

    Examples
    --------
    >>> export_fluent_case_params = prime.ExportFluentCaseParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            cff_format: bool):
        self._cff_format = cff_format

    def __init__(
            self,
            model: CommunicationManager=None,
            cff_format: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ExportFluentCaseParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ExportFluentCaseParams`` object with default parameters.
        cff_format: bool, optional
            Option to specify whether to export Fluent case file in CFF format (.cas.h5) or legacy format (.cas, .cas.gz).
        json_data: dict, optional
            JSON dictionary to create a ``ExportFluentCaseParams`` object with provided parameters.

        Examples
        --------
        >>> export_fluent_case_params = prime.ExportFluentCaseParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["cffFormat"] if "cffFormat" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [cff_format])
            if all_field_specified:
                self.__initialize(
                    cff_format)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ExportFluentCaseParams")
                    json_data = param_json["ExportFluentCaseParams"] if "ExportFluentCaseParams" in param_json else {}
                    self.__initialize(
                        cff_format if cff_format is not None else ( ExportFluentCaseParams._default_params["cff_format"] if "cff_format" in ExportFluentCaseParams._default_params else (json_data["cffFormat"] if "cffFormat" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            cff_format: bool = None):
        """Set the default values of the ``ExportFluentCaseParams`` object.

        Parameters
        ----------
        cff_format: bool, optional
            Option to specify whether to export Fluent case file in CFF format (.cas.h5) or legacy format (.cas, .cas.gz).
        """
        args = locals()
        [ExportFluentCaseParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ExportFluentCaseParams`` object.

        Examples
        --------
        >>> ExportFluentCaseParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportFluentCaseParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._cff_format is not None:
            json_data["cffFormat"] = self._cff_format
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "cff_format :  %s" % (self._cff_format)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def cff_format(self) -> bool:
        """Option to specify whether to export Fluent case file in CFF format (.cas.h5) or legacy format (.cas, .cas.gz).
        """
        return self._cff_format

    @cff_format.setter
    def cff_format(self, value: bool):
        self._cff_format = value

class ExportFluentMeshingMeshParams(CoreObject):
    """Parameters used to export fluent meshing mesh.

    Parameters
    ----------
    model: Model
        Model to create a ``ExportFluentMeshingMeshParams`` object with default parameters.
    cff_format: bool, optional
        Option to specify whether to export Fluent mesh file in CFF format (.msh.h5) or legacy format (.msh, .msh.gz).

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ExportFluentMeshingMeshParams`` object with provided parameters.

    Examples
    --------
    >>> export_fluent_meshing_mesh_params = prime.ExportFluentMeshingMeshParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            cff_format: bool):
        self._cff_format = cff_format

    def __init__(
            self,
            model: CommunicationManager=None,
            cff_format: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ExportFluentMeshingMeshParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ExportFluentMeshingMeshParams`` object with default parameters.
        cff_format: bool, optional
            Option to specify whether to export Fluent mesh file in CFF format (.msh.h5) or legacy format (.msh, .msh.gz).

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ExportFluentMeshingMeshParams`` object with provided parameters.

        Examples
        --------
        >>> export_fluent_meshing_mesh_params = prime.ExportFluentMeshingMeshParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["cffFormat"] if "cffFormat" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [cff_format])
            if all_field_specified:
                self.__initialize(
                    cff_format)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ExportFluentMeshingMeshParams")
                    json_data = param_json["ExportFluentMeshingMeshParams"] if "ExportFluentMeshingMeshParams" in param_json else {}
                    self.__initialize(
                        cff_format if cff_format is not None else ( ExportFluentMeshingMeshParams._default_params["cff_format"] if "cff_format" in ExportFluentMeshingMeshParams._default_params else (json_data["cffFormat"] if "cffFormat" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            cff_format: bool = None):
        """Set the default values of the ``ExportFluentMeshingMeshParams`` object.

        Parameters
        ----------
        cff_format: bool, optional
            Option to specify whether to export Fluent mesh file in CFF format (.msh.h5) or legacy format (.msh, .msh.gz).
        """
        args = locals()
        [ExportFluentMeshingMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ExportFluentMeshingMeshParams`` object.

        Examples
        --------
        >>> ExportFluentMeshingMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportFluentMeshingMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._cff_format is not None:
            json_data["cffFormat"] = self._cff_format
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "cff_format :  %s" % (self._cff_format)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def cff_format(self) -> bool:
        """Option to specify whether to export Fluent mesh file in CFF format (.msh.h5) or legacy format (.msh, .msh.gz).

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._cff_format

    @cff_format.setter
    def cff_format(self, value: bool):
        self._cff_format = value

class ExportSTLParams(CoreObject):
    """Parameters to export STL file.

    Parameters
    ----------
    model: Model
        Model to create a ``ExportSTLParams`` object with default parameters.
    part_ids: Iterable[int], optional
        Ids of parts to export.
    json_data: dict, optional
        JSON dictionary to create a ``ExportSTLParams`` object with provided parameters.

    Examples
    --------
    >>> export_stlparams = prime.ExportSTLParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            part_ids: Iterable[int]):
        self._part_ids = part_ids if isinstance(part_ids, np.ndarray) else np.array(part_ids, dtype=np.int32) if part_ids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            part_ids: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ExportSTLParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ExportSTLParams`` object with default parameters.
        part_ids: Iterable[int], optional
            Ids of parts to export.
        json_data: dict, optional
            JSON dictionary to create a ``ExportSTLParams`` object with provided parameters.

        Examples
        --------
        >>> export_stlparams = prime.ExportSTLParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["partIds"] if "partIds" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [part_ids])
            if all_field_specified:
                self.__initialize(
                    part_ids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ExportSTLParams")
                    json_data = param_json["ExportSTLParams"] if "ExportSTLParams" in param_json else {}
                    self.__initialize(
                        part_ids if part_ids is not None else ( ExportSTLParams._default_params["part_ids"] if "part_ids" in ExportSTLParams._default_params else (json_data["partIds"] if "partIds" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            part_ids: Iterable[int] = None):
        """Set the default values of the ``ExportSTLParams`` object.

        Parameters
        ----------
        part_ids: Iterable[int], optional
            Ids of parts to export.
        """
        args = locals()
        [ExportSTLParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ExportSTLParams`` object.

        Examples
        --------
        >>> ExportSTLParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportSTLParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._part_ids is not None:
            json_data["partIds"] = self._part_ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "part_ids :  %s" % (self._part_ids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def part_ids(self) -> Iterable[int]:
        """Ids of parts to export.
        """
        return self._part_ids

    @part_ids.setter
    def part_ids(self, value: Iterable[int]):
        self._part_ids = value

class CadRefacetingParams(CoreObject):
    """Parameters to refacet CAD during import.

    Parameters
    ----------
    model: Model
        Model to create a ``CadRefacetingParams`` object with default parameters.
    cad_faceter: CadFaceter, optional
        Specify the available choices for faceter. The available option is Parasolid. (Note: ACIS faceter is being deprecated from 25R1).
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
        JSON dictionary to create a ``CadRefacetingParams`` object with provided parameters.

    Examples
    --------
    >>> cad_refaceting_params = prime.CadRefacetingParams(model = model)
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
        """Initialize a ``CadRefacetingParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``CadRefacetingParams`` object with default parameters.
        cad_faceter: CadFaceter, optional
            Specify the available choices for faceter. The available option is Parasolid. (Note: ACIS faceter is being deprecated from 25R1).
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
            JSON dictionary to create a ``CadRefacetingParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``CadRefacetingParams`` object.

        Parameters
        ----------
        cad_faceter: CadFaceter, optional
            Specify the available choices for faceter. The available option is Parasolid. (Note: ACIS faceter is being deprecated from 25R1).
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
        """Print the default values of ``CadRefacetingParams`` object.

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
        """Specify the available choices for faceter. The available option is Parasolid. (Note: ACIS faceter is being deprecated from 25R1).
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

    Parameters
    ----------
    model: Model
        Model to create a ``ImportCadParams`` object with default parameters.
    append: bool, optional
        Append imported CAD into existing model when true.
    ansys_release: str, optional
        Configures the Ansys release to be used for loading CAD data through non Native route. Supported formats for specifying Ansys release version are '25.2', '252', 'v252', '25R2'.
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
    validate_shared_topology: bool, optional
        Specify whether to validate the shared topology information.
    json_data: dict, optional
        JSON dictionary to create a ``ImportCadParams`` object with provided parameters.

    Examples
    --------
    >>> import_cad_params = prime.ImportCadParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            append: bool,
            ansys_release: str,
            cad_reader_route: CadReaderRoute,
            part_creation_type: PartCreationType,
            geometry_transfer: bool,
            length_unit: LengthUnit,
            refacet: bool,
            cad_refaceting_params: CadRefacetingParams,
            stitch_tolerance: float,
            cad_update_parameters: Dict[str, Union[str, int, float, bool]],
            validate_shared_topology: bool):
        self._append = append
        self._ansys_release = ansys_release
        self._cad_reader_route = CadReaderRoute(cad_reader_route)
        self._part_creation_type = PartCreationType(part_creation_type)
        self._geometry_transfer = geometry_transfer
        self._length_unit = LengthUnit(length_unit)
        self._refacet = refacet
        self._cad_refaceting_params = cad_refaceting_params
        self._stitch_tolerance = stitch_tolerance
        self._cad_update_parameters = cad_update_parameters
        self._validate_shared_topology = validate_shared_topology

    def __init__(
            self,
            model: CommunicationManager=None,
            append: bool = None,
            ansys_release: str = None,
            cad_reader_route: CadReaderRoute = None,
            part_creation_type: PartCreationType = None,
            geometry_transfer: bool = None,
            length_unit: LengthUnit = None,
            refacet: bool = None,
            cad_refaceting_params: CadRefacetingParams = None,
            stitch_tolerance: float = None,
            cad_update_parameters: Dict[str, Union[str, int, float, bool]] = None,
            validate_shared_topology: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ImportCadParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ImportCadParams`` object with default parameters.
        append: bool, optional
            Append imported CAD into existing model when true.
        ansys_release: str, optional
            Configures the Ansys release to be used for loading CAD data through non Native route. Supported formats for specifying Ansys release version are '25.2', '252', 'v252', '25R2'.
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
        validate_shared_topology: bool, optional
            Specify whether to validate the shared topology information.
        json_data: dict, optional
            JSON dictionary to create a ``ImportCadParams`` object with provided parameters.

        Examples
        --------
        >>> import_cad_params = prime.ImportCadParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["append"] if "append" in json_data else None,
                json_data["ansysRelease"] if "ansysRelease" in json_data else None,
                CadReaderRoute(json_data["cadReaderRoute"] if "cadReaderRoute" in json_data else None),
                PartCreationType(json_data["partCreationType"] if "partCreationType" in json_data else None),
                json_data["geometryTransfer"] if "geometryTransfer" in json_data else None,
                LengthUnit(json_data["lengthUnit"] if "lengthUnit" in json_data else None),
                json_data["refacet"] if "refacet" in json_data else None,
                CadRefacetingParams(model = model, json_data = json_data["cadRefacetingParams"] if "cadRefacetingParams" in json_data else None),
                json_data["stitchTolerance"] if "stitchTolerance" in json_data else None,
                json_data["cadUpdateParameters"] if "cadUpdateParameters" in json_data else None,
                json_data["validateSharedTopology"] if "validateSharedTopology" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [append, ansys_release, cad_reader_route, part_creation_type, geometry_transfer, length_unit, refacet, cad_refaceting_params, stitch_tolerance, cad_update_parameters, validate_shared_topology])
            if all_field_specified:
                self.__initialize(
                    append,
                    ansys_release,
                    cad_reader_route,
                    part_creation_type,
                    geometry_transfer,
                    length_unit,
                    refacet,
                    cad_refaceting_params,
                    stitch_tolerance,
                    cad_update_parameters,
                    validate_shared_topology)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ImportCadParams")
                    json_data = param_json["ImportCadParams"] if "ImportCadParams" in param_json else {}
                    self.__initialize(
                        append if append is not None else ( ImportCadParams._default_params["append"] if "append" in ImportCadParams._default_params else (json_data["append"] if "append" in json_data else None)),
                        ansys_release if ansys_release is not None else ( ImportCadParams._default_params["ansys_release"] if "ansys_release" in ImportCadParams._default_params else (json_data["ansysRelease"] if "ansysRelease" in json_data else None)),
                        cad_reader_route if cad_reader_route is not None else ( ImportCadParams._default_params["cad_reader_route"] if "cad_reader_route" in ImportCadParams._default_params else CadReaderRoute(json_data["cadReaderRoute"] if "cadReaderRoute" in json_data else None)),
                        part_creation_type if part_creation_type is not None else ( ImportCadParams._default_params["part_creation_type"] if "part_creation_type" in ImportCadParams._default_params else PartCreationType(json_data["partCreationType"] if "partCreationType" in json_data else None)),
                        geometry_transfer if geometry_transfer is not None else ( ImportCadParams._default_params["geometry_transfer"] if "geometry_transfer" in ImportCadParams._default_params else (json_data["geometryTransfer"] if "geometryTransfer" in json_data else None)),
                        length_unit if length_unit is not None else ( ImportCadParams._default_params["length_unit"] if "length_unit" in ImportCadParams._default_params else LengthUnit(json_data["lengthUnit"] if "lengthUnit" in json_data else None)),
                        refacet if refacet is not None else ( ImportCadParams._default_params["refacet"] if "refacet" in ImportCadParams._default_params else (json_data["refacet"] if "refacet" in json_data else None)),
                        cad_refaceting_params if cad_refaceting_params is not None else ( ImportCadParams._default_params["cad_refaceting_params"] if "cad_refaceting_params" in ImportCadParams._default_params else CadRefacetingParams(model = model, json_data = (json_data["cadRefacetingParams"] if "cadRefacetingParams" in json_data else None))),
                        stitch_tolerance if stitch_tolerance is not None else ( ImportCadParams._default_params["stitch_tolerance"] if "stitch_tolerance" in ImportCadParams._default_params else (json_data["stitchTolerance"] if "stitchTolerance" in json_data else None)),
                        cad_update_parameters if cad_update_parameters is not None else ( ImportCadParams._default_params["cad_update_parameters"] if "cad_update_parameters" in ImportCadParams._default_params else (json_data["cadUpdateParameters"] if "cadUpdateParameters" in json_data else None)),
                        validate_shared_topology if validate_shared_topology is not None else ( ImportCadParams._default_params["validate_shared_topology"] if "validate_shared_topology" in ImportCadParams._default_params else (json_data["validateSharedTopology"] if "validateSharedTopology" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            append: bool = None,
            ansys_release: str = None,
            cad_reader_route: CadReaderRoute = None,
            part_creation_type: PartCreationType = None,
            geometry_transfer: bool = None,
            length_unit: LengthUnit = None,
            refacet: bool = None,
            cad_refaceting_params: CadRefacetingParams = None,
            stitch_tolerance: float = None,
            cad_update_parameters: Dict[str, Union[str, int, float, bool]] = None,
            validate_shared_topology: bool = None):
        """Set the default values of the ``ImportCadParams`` object.

        Parameters
        ----------
        append: bool, optional
            Append imported CAD into existing model when true.
        ansys_release: str, optional
            Configures the Ansys release to be used for loading CAD data through non Native route. Supported formats for specifying Ansys release version are '25.2', '252', 'v252', '25R2'.
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
        validate_shared_topology: bool, optional
            Specify whether to validate the shared topology information.
        """
        args = locals()
        [ImportCadParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ImportCadParams`` object.

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
        if self._ansys_release is not None:
            json_data["ansysRelease"] = self._ansys_release
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
        if self._validate_shared_topology is not None:
            json_data["validateSharedTopology"] = self._validate_shared_topology
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "append :  %s\nansys_release :  %s\ncad_reader_route :  %s\npart_creation_type :  %s\ngeometry_transfer :  %s\nlength_unit :  %s\nrefacet :  %s\ncad_refaceting_params :  %s\nstitch_tolerance :  %s\ncad_update_parameters :  %s\nvalidate_shared_topology :  %s" % (self._append, self._ansys_release, self._cad_reader_route, self._part_creation_type, self._geometry_transfer, self._length_unit, self._refacet, '{ ' + str(self._cad_refaceting_params) + ' }', self._stitch_tolerance, self._cad_update_parameters, self._validate_shared_topology)
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
    def ansys_release(self) -> str:
        """Configures the Ansys release to be used for loading CAD data through non Native route. Supported formats for specifying Ansys release version are '25.2', '252', 'v252', '25R2'.
        """
        return self._ansys_release

    @ansys_release.setter
    def ansys_release(self, value: str):
        self._ansys_release = value

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

    @property
    def validate_shared_topology(self) -> bool:
        """Specify whether to validate the shared topology information.
        """
        return self._validate_shared_topology

    @validate_shared_topology.setter
    def validate_shared_topology(self, value: bool):
        self._validate_shared_topology = value

class ImportCadResults(CoreObject):
    """Results associated with the CAD import.

    Parameters
    ----------
    model: Model
        Model to create a ``ImportCadResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code associated with failure of operation.
    cad_parameters: Dict[str, Union[str, int, float, bool]], optional
        Returns the parameters associated with CAD. Available only with WorkBench CAD Reader route.
    json_data: dict, optional
        JSON dictionary to create a ``ImportCadResults`` object with provided parameters.

    Examples
    --------
    >>> import_cad_results = prime.ImportCadResults(model = model)
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
        """Initialize a ``ImportCadResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ImportCadResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        cad_parameters: Dict[str, Union[str, int, float, bool]], optional
            Returns the parameters associated with CAD. Available only with WorkBench CAD Reader route.
        json_data: dict, optional
            JSON dictionary to create a ``ImportCadResults`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``ImportCadResults`` object.

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
        """Print the default values of ``ImportCadResults`` object.

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

    Parameters
    ----------
    model: Model
        Model to create a ``ImportFluentMeshingMeshParams`` object with default parameters.
    append: bool, optional
        Option to append imported mesh to existing mesh instead of resetting model to imported mesh.
    enable_multi_threading: bool, optional
        Option to import multiple files in parallel using multithreading.
    json_data: dict, optional
        JSON dictionary to create a ``ImportFluentMeshingMeshParams`` object with provided parameters.

    Examples
    --------
    >>> import_fluent_meshing_mesh_params = prime.ImportFluentMeshingMeshParams(model = model)
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
        """Initialize a ``ImportFluentMeshingMeshParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ImportFluentMeshingMeshParams`` object with default parameters.
        append: bool, optional
            Option to append imported mesh to existing mesh instead of resetting model to imported mesh.
        enable_multi_threading: bool, optional
            Option to import multiple files in parallel using multithreading.
        json_data: dict, optional
            JSON dictionary to create a ``ImportFluentMeshingMeshParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``ImportFluentMeshingMeshParams`` object.

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
        """Print the default values of ``ImportFluentMeshingMeshParams`` object.

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

    Parameters
    ----------
    model: Model
        Model to create a ``ImportFluentMeshingMeshResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code associated with the failure of operation.
    new_parts_created: Iterable[int], optional
        Ids of new parts created for each file unreferenced fluent meshing mesh zones.
    json_data: dict, optional
        JSON dictionary to create a ``ImportFluentMeshingMeshResults`` object with provided parameters.

    Examples
    --------
    >>> import_fluent_meshing_mesh_results = prime.ImportFluentMeshingMeshResults(model = model)
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
        """Initialize a ``ImportFluentMeshingMeshResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ImportFluentMeshingMeshResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        new_parts_created: Iterable[int], optional
            Ids of new parts created for each file unreferenced fluent meshing mesh zones.
        json_data: dict, optional
            JSON dictionary to create a ``ImportFluentMeshingMeshResults`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``ImportFluentMeshingMeshResults`` object.

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
        """Print the default values of ``ImportFluentMeshingMeshResults`` object.

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

    Parameters
    ----------
    model: Model
        Model to create a ``ImportFluentCaseParams`` object with default parameters.
    append: bool, optional
        Option to append imported case instead of resetting model to imported case.
    json_data: dict, optional
        JSON dictionary to create a ``ImportFluentCaseParams`` object with provided parameters.

    Examples
    --------
    >>> import_fluent_case_params = prime.ImportFluentCaseParams(model = model)
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
        """Initialize a ``ImportFluentCaseParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ImportFluentCaseParams`` object with default parameters.
        append: bool, optional
            Option to append imported case instead of resetting model to imported case.
        json_data: dict, optional
            JSON dictionary to create a ``ImportFluentCaseParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``ImportFluentCaseParams`` object.

        Parameters
        ----------
        append: bool, optional
            Option to append imported case instead of resetting model to imported case.
        """
        args = locals()
        [ImportFluentCaseParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ImportFluentCaseParams`` object.

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

    Parameters
    ----------
    model: Model
        Model to create a ``ImportFluentCaseResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code associated with failure of operation.
    json_data: dict, optional
        JSON dictionary to create a ``ImportFluentCaseResults`` object with provided parameters.

    Examples
    --------
    >>> import_fluent_case_results = prime.ImportFluentCaseResults(model = model)
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
        """Initialize a ``ImportFluentCaseResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ImportFluentCaseResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        json_data: dict, optional
            JSON dictionary to create a ``ImportFluentCaseResults`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``ImportFluentCaseResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        """
        args = locals()
        [ImportFluentCaseResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ImportFluentCaseResults`` object.

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

class ZoneMeshResult(CoreObject):
    """Results containing zone-wise mesh information.

    Contains zone name, element ids and their corresponding data (such as centroid coordinates)
    for elements within a zone.

    Parameters
    ----------
    model: Model
        Model to create a ``ZoneMeshResult`` object with default parameters.
    zone_name: str, optional
        Name of the zone where the elements belong to.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    element_ids: Iterable[int], optional
        List of element ids in the zone.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    centroids: Iterable[float], optional
        Flattened array of centroid coordinates [x1,y1,z1,x2,y2,z2,...].

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ZoneMeshResult`` object with provided parameters.

    Examples
    --------
    >>> zone_mesh_result = prime.ZoneMeshResult(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            zone_name: str,
            element_ids: Iterable[int],
            centroids: Iterable[float]):
        self._zone_name = zone_name
        self._element_ids = element_ids if isinstance(element_ids, np.ndarray) else np.array(element_ids, dtype=np.int32) if element_ids is not None else None
        self._centroids = centroids if isinstance(centroids, np.ndarray) else np.array(centroids, dtype=np.double) if centroids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            zone_name: str = None,
            element_ids: Iterable[int] = None,
            centroids: Iterable[float] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ZoneMeshResult`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ZoneMeshResult`` object with default parameters.
        zone_name: str, optional
            Name of the zone where the elements belong to.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        element_ids: Iterable[int], optional
            List of element ids in the zone.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        centroids: Iterable[float], optional
            Flattened array of centroid coordinates [x1,y1,z1,x2,y2,z2,...].

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ZoneMeshResult`` object with provided parameters.

        Examples
        --------
        >>> zone_mesh_result = prime.ZoneMeshResult(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["zoneName"] if "zoneName" in json_data else None,
                json_data["elementIds"] if "elementIds" in json_data else None,
                json_data["centroids"] if "centroids" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [zone_name, element_ids, centroids])
            if all_field_specified:
                self.__initialize(
                    zone_name,
                    element_ids,
                    centroids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ZoneMeshResult")
                    json_data = param_json["ZoneMeshResult"] if "ZoneMeshResult" in param_json else {}
                    self.__initialize(
                        zone_name if zone_name is not None else ( ZoneMeshResult._default_params["zone_name"] if "zone_name" in ZoneMeshResult._default_params else (json_data["zoneName"] if "zoneName" in json_data else None)),
                        element_ids if element_ids is not None else ( ZoneMeshResult._default_params["element_ids"] if "element_ids" in ZoneMeshResult._default_params else (json_data["elementIds"] if "elementIds" in json_data else None)),
                        centroids if centroids is not None else ( ZoneMeshResult._default_params["centroids"] if "centroids" in ZoneMeshResult._default_params else (json_data["centroids"] if "centroids" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            zone_name: str = None,
            element_ids: Iterable[int] = None,
            centroids: Iterable[float] = None):
        """Set the default values of the ``ZoneMeshResult`` object.

        Parameters
        ----------
        zone_name: str, optional
            Name of the zone where the elements belong to.
        element_ids: Iterable[int], optional
            List of element ids in the zone.
        centroids: Iterable[float], optional
            Flattened array of centroid coordinates [x1,y1,z1,x2,y2,z2,...].
        """
        args = locals()
        [ZoneMeshResult._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ZoneMeshResult`` object.

        Examples
        --------
        >>> ZoneMeshResult.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ZoneMeshResult._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._zone_name is not None:
            json_data["zoneName"] = self._zone_name
        if self._element_ids is not None:
            json_data["elementIds"] = self._element_ids
        if self._centroids is not None:
            json_data["centroids"] = self._centroids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "zone_name :  %s\nelement_ids :  %s\ncentroids :  %s" % (self._zone_name, self._element_ids, self._centroids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def zone_name(self) -> str:
        """Name of the zone where the elements belong to.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value: str):
        self._zone_name = value

    @property
    def element_ids(self) -> Iterable[int]:
        """List of element ids in the zone.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._element_ids

    @element_ids.setter
    def element_ids(self, value: Iterable[int]):
        self._element_ids = value

    @property
    def centroids(self) -> Iterable[float]:
        """Flattened array of centroid coordinates [x1,y1,z1,x2,y2,z2,...].

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._centroids

    @centroids.setter
    def centroids(self, value: Iterable[float]):
        self._centroids = value

class ImportMapdlCdbParams(CoreObject):
    """Parameters to control MAPDL CDB import settings.

    Parameters
    ----------
    model: Model
        Model to create a ``ImportMapdlCdbParams`` object with default parameters.
    drop_mid_nodes: bool, optional
        Option to import quadratic mesh elements as linear by skipping mid nodes.
    append: bool, optional
        Option to append imported cdb into existing model.
    json_data: dict, optional
        JSON dictionary to create a ``ImportMapdlCdbParams`` object with provided parameters.

    Examples
    --------
    >>> import_mapdl_cdb_params = prime.ImportMapdlCdbParams(model = model)
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
        """Initialize a ``ImportMapdlCdbParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ImportMapdlCdbParams`` object with default parameters.
        drop_mid_nodes: bool, optional
            Option to import quadratic mesh elements as linear by skipping mid nodes.
        append: bool, optional
            Option to append imported cdb into existing model.
        json_data: dict, optional
            JSON dictionary to create a ``ImportMapdlCdbParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``ImportMapdlCdbParams`` object.

        Parameters
        ----------
        drop_mid_nodes: bool, optional
            Option to import quadratic mesh elements as linear by skipping mid nodes.
        append: bool, optional
            Option to append imported cdb into existing model.
        """
        args = locals()
        [ImportMapdlCdbParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ImportMapdlCdbParams`` object.

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
        """Option to import quadratic mesh elements as linear by skipping mid nodes.
        """
        return self._drop_mid_nodes

    @drop_mid_nodes.setter
    def drop_mid_nodes(self, value: bool):
        self._drop_mid_nodes = value

    @property
    def append(self) -> bool:
        """Option to append imported cdb into existing model.
        """
        return self._append

    @append.setter
    def append(self, value: bool):
        self._append = value

class ImportMapdlCdbResults(CoreObject):
    """Results associated with the MAPDL CDB import.

    Parameters
    ----------
    model: Model
        Model to create a ``ImportMapdlCdbResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code associated with failure of operation.
    warning_codes: List[WarningCode], optional
        Warning codes associated with the operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ImportMapdlCdbResults`` object with provided parameters.

    Examples
    --------
    >>> import_mapdl_cdb_results = prime.ImportMapdlCdbResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ImportMapdlCdbResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ImportMapdlCdbResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ImportMapdlCdbResults`` object with provided parameters.

        Examples
        --------
        >>> import_mapdl_cdb_results = prime.ImportMapdlCdbResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ImportMapdlCdbResults")
                    json_data = param_json["ImportMapdlCdbResults"] if "ImportMapdlCdbResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ImportMapdlCdbResults._default_params["error_code"] if "error_code" in ImportMapdlCdbResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( ImportMapdlCdbResults._default_params["warning_codes"] if "warning_codes" in ImportMapdlCdbResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of the ``ImportMapdlCdbResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        """
        args = locals()
        [ImportMapdlCdbResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ImportMapdlCdbResults`` object.

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
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
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
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class ContactElementTypeParams(CoreObject):
    """Parameters to control element type choices for contact surfaces in TIEs and CONTACT PAIRs.

    Parameters
    ----------
    model: Model
        Model to create a ``ContactElementTypeParams`` object with default parameters.
    tie_surf_to_surf: int, optional
        Element type for TIE with Surface-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    tie_node_to_surf: int, optional
        Element type for TIE with Node-to-Surface contact where the contact surface is of type ELEMENT. Default value is 175. The choices are 174 and 175.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    contact_pair_surf_to_surf: int, optional
        Element type for CONTACT PAIR with Surface-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    contact_pair_node_to_surf: int, optional
        Element type for CONTACT PAIR with Node-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ContactElementTypeParams`` object with provided parameters.

    Examples
    --------
    >>> contact_element_type_params = prime.ContactElementTypeParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            tie_surf_to_surf: int,
            tie_node_to_surf: int,
            contact_pair_surf_to_surf: int,
            contact_pair_node_to_surf: int):
        self._tie_surf_to_surf = tie_surf_to_surf
        self._tie_node_to_surf = tie_node_to_surf
        self._contact_pair_surf_to_surf = contact_pair_surf_to_surf
        self._contact_pair_node_to_surf = contact_pair_node_to_surf

    def __init__(
            self,
            model: CommunicationManager=None,
            tie_surf_to_surf: int = None,
            tie_node_to_surf: int = None,
            contact_pair_surf_to_surf: int = None,
            contact_pair_node_to_surf: int = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ContactElementTypeParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ContactElementTypeParams`` object with default parameters.
        tie_surf_to_surf: int, optional
            Element type for TIE with Surface-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        tie_node_to_surf: int, optional
            Element type for TIE with Node-to-Surface contact where the contact surface is of type ELEMENT. Default value is 175. The choices are 174 and 175.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        contact_pair_surf_to_surf: int, optional
            Element type for CONTACT PAIR with Surface-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        contact_pair_node_to_surf: int, optional
            Element type for CONTACT PAIR with Node-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ContactElementTypeParams`` object with provided parameters.

        Examples
        --------
        >>> contact_element_type_params = prime.ContactElementTypeParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["tieSurfToSurf"] if "tieSurfToSurf" in json_data else None,
                json_data["tieNodeToSurf"] if "tieNodeToSurf" in json_data else None,
                json_data["contactPairSurfToSurf"] if "contactPairSurfToSurf" in json_data else None,
                json_data["contactPairNodeToSurf"] if "contactPairNodeToSurf" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [tie_surf_to_surf, tie_node_to_surf, contact_pair_surf_to_surf, contact_pair_node_to_surf])
            if all_field_specified:
                self.__initialize(
                    tie_surf_to_surf,
                    tie_node_to_surf,
                    contact_pair_surf_to_surf,
                    contact_pair_node_to_surf)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ContactElementTypeParams")
                    json_data = param_json["ContactElementTypeParams"] if "ContactElementTypeParams" in param_json else {}
                    self.__initialize(
                        tie_surf_to_surf if tie_surf_to_surf is not None else ( ContactElementTypeParams._default_params["tie_surf_to_surf"] if "tie_surf_to_surf" in ContactElementTypeParams._default_params else (json_data["tieSurfToSurf"] if "tieSurfToSurf" in json_data else None)),
                        tie_node_to_surf if tie_node_to_surf is not None else ( ContactElementTypeParams._default_params["tie_node_to_surf"] if "tie_node_to_surf" in ContactElementTypeParams._default_params else (json_data["tieNodeToSurf"] if "tieNodeToSurf" in json_data else None)),
                        contact_pair_surf_to_surf if contact_pair_surf_to_surf is not None else ( ContactElementTypeParams._default_params["contact_pair_surf_to_surf"] if "contact_pair_surf_to_surf" in ContactElementTypeParams._default_params else (json_data["contactPairSurfToSurf"] if "contactPairSurfToSurf" in json_data else None)),
                        contact_pair_node_to_surf if contact_pair_node_to_surf is not None else ( ContactElementTypeParams._default_params["contact_pair_node_to_surf"] if "contact_pair_node_to_surf" in ContactElementTypeParams._default_params else (json_data["contactPairNodeToSurf"] if "contactPairNodeToSurf" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            tie_surf_to_surf: int = None,
            tie_node_to_surf: int = None,
            contact_pair_surf_to_surf: int = None,
            contact_pair_node_to_surf: int = None):
        """Set the default values of the ``ContactElementTypeParams`` object.

        Parameters
        ----------
        tie_surf_to_surf: int, optional
            Element type for TIE with Surface-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.
        tie_node_to_surf: int, optional
            Element type for TIE with Node-to-Surface contact where the contact surface is of type ELEMENT. Default value is 175. The choices are 174 and 175.
        contact_pair_surf_to_surf: int, optional
            Element type for CONTACT PAIR with Surface-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.
        contact_pair_node_to_surf: int, optional
            Element type for CONTACT PAIR with Node-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.
        """
        args = locals()
        [ContactElementTypeParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ContactElementTypeParams`` object.

        Examples
        --------
        >>> ContactElementTypeParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ContactElementTypeParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._tie_surf_to_surf is not None:
            json_data["tieSurfToSurf"] = self._tie_surf_to_surf
        if self._tie_node_to_surf is not None:
            json_data["tieNodeToSurf"] = self._tie_node_to_surf
        if self._contact_pair_surf_to_surf is not None:
            json_data["contactPairSurfToSurf"] = self._contact_pair_surf_to_surf
        if self._contact_pair_node_to_surf is not None:
            json_data["contactPairNodeToSurf"] = self._contact_pair_node_to_surf
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "tie_surf_to_surf :  %s\ntie_node_to_surf :  %s\ncontact_pair_surf_to_surf :  %s\ncontact_pair_node_to_surf :  %s" % (self._tie_surf_to_surf, self._tie_node_to_surf, self._contact_pair_surf_to_surf, self._contact_pair_node_to_surf)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def tie_surf_to_surf(self) -> int:
        """Element type for TIE with Surface-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._tie_surf_to_surf

    @tie_surf_to_surf.setter
    def tie_surf_to_surf(self, value: int):
        self._tie_surf_to_surf = value

    @property
    def tie_node_to_surf(self) -> int:
        """Element type for TIE with Node-to-Surface contact where the contact surface is of type ELEMENT. Default value is 175. The choices are 174 and 175.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._tie_node_to_surf

    @tie_node_to_surf.setter
    def tie_node_to_surf(self, value: int):
        self._tie_node_to_surf = value

    @property
    def contact_pair_surf_to_surf(self) -> int:
        """Element type for CONTACT PAIR with Surface-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._contact_pair_surf_to_surf

    @contact_pair_surf_to_surf.setter
    def contact_pair_surf_to_surf(self, value: int):
        self._contact_pair_surf_to_surf = value

    @property
    def contact_pair_node_to_surf(self) -> int:
        """Element type for CONTACT PAIR with Node-to-Surface contact where the contact surface is of type ELEMENT. Default value is 174. The choices are 174 and 175.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._contact_pair_node_to_surf

    @contact_pair_node_to_surf.setter
    def contact_pair_node_to_surf(self, value: int):
        self._contact_pair_node_to_surf = value

class LabelExportParams(CoreObject):
    """Parameters to control the export of labels as Nodal or Element Components in CDB. By default, all the labels are exported as Element Components.

    Parameters
    ----------
    model: Model
        Model to create a ``LabelExportParams`` object with default parameters.
    label_expression_for_nodal_components: str, optional
        Label expression to export matching labels as Nodal Components in CDB. Non-matching labels will be exported as Element Components.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``LabelExportParams`` object with provided parameters.

    Examples
    --------
    >>> label_export_params = prime.LabelExportParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            label_expression_for_nodal_components: str):
        self._label_expression_for_nodal_components = label_expression_for_nodal_components

    def __init__(
            self,
            model: CommunicationManager=None,
            label_expression_for_nodal_components: str = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``LabelExportParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``LabelExportParams`` object with default parameters.
        label_expression_for_nodal_components: str, optional
            Label expression to export matching labels as Nodal Components in CDB. Non-matching labels will be exported as Element Components.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``LabelExportParams`` object with provided parameters.

        Examples
        --------
        >>> label_export_params = prime.LabelExportParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["labelExpressionForNodalComponents"] if "labelExpressionForNodalComponents" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [label_expression_for_nodal_components])
            if all_field_specified:
                self.__initialize(
                    label_expression_for_nodal_components)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "LabelExportParams")
                    json_data = param_json["LabelExportParams"] if "LabelExportParams" in param_json else {}
                    self.__initialize(
                        label_expression_for_nodal_components if label_expression_for_nodal_components is not None else ( LabelExportParams._default_params["label_expression_for_nodal_components"] if "label_expression_for_nodal_components" in LabelExportParams._default_params else (json_data["labelExpressionForNodalComponents"] if "labelExpressionForNodalComponents" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            label_expression_for_nodal_components: str = None):
        """Set the default values of the ``LabelExportParams`` object.

        Parameters
        ----------
        label_expression_for_nodal_components: str, optional
            Label expression to export matching labels as Nodal Components in CDB. Non-matching labels will be exported as Element Components.
        """
        args = locals()
        [LabelExportParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``LabelExportParams`` object.

        Examples
        --------
        >>> LabelExportParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in LabelExportParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._label_expression_for_nodal_components is not None:
            json_data["labelExpressionForNodalComponents"] = self._label_expression_for_nodal_components
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "label_expression_for_nodal_components :  %s" % (self._label_expression_for_nodal_components)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def label_expression_for_nodal_components(self) -> str:
        """Label expression to export matching labels as Nodal Components in CDB. Non-matching labels will be exported as Element Components.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._label_expression_for_nodal_components

    @label_expression_for_nodal_components.setter
    def label_expression_for_nodal_components(self, value: str):
        self._label_expression_for_nodal_components = value

class ExportMapdlCdbParams(CoreObject):
    """Parameters to control MAPDL CDB export settings.

    Parameters
    ----------
    model: Model
        Model to create a ``ExportMapdlCdbParams`` object with default parameters.
    config_settings: str, optional
        MAPDL configuration settings in CDB format to be added at the beginning of the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    pre_solution_settings: str, optional
        MAPDL Settings in CDB format to be added before the solution block in the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    material_properties: str, optional
        Materials in CDB format to be added to the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    boundary_conditions: str, optional
        Boundary conditions in CDB format to be added to the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    analysis_settings: str, optional
        MAPDL analysis settings in CDB format to be added after the solution block in the file. Note: Boundary conditions can be included into analysis settings.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    write_cells: bool, optional
        Option to write out cells as part of the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    enable_face_based_labels: bool, optional
        Use LabelExportParams instead. Parameter enableFaceBasedLabels will be removed in 2025R2.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    label_export_params: LabelExportParams, optional
        Parameters to control the export of labels as Nodal or Element Components in CDB.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    write_by_zones: bool, optional
        Option to write zones in the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    consider_general_connectors_as_spot_weld: bool, optional
        Option to translate all general connector joints (other than axial) to spot weld type. This is important when nodes are non coincident.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    analysis_type: CdbAnalysisType, optional
        Option to specify CDB analysis type.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    simulation_type: CdbSimulationType, optional
        Simulation type for the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    analysis_settings_file_name: str, optional
        File path to export mapdl analysis settings.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    write_separate_blocks: bool, optional
        Controls whether element blocks should be written separately. When true, writes elements in separate blocks based on the format specified in separate_blocks_format_type. When false, writes all elements into a single block.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    write_components_with_element_blocks: bool, optional
        Controls whether component definitions should be written within individual element blocks. write_components_with_element_blocks only has effect when write_separate_blocks is true. When write_components_with_element_blocks is true, writes component commands for each element block. When write_components_with_element_blocks is false, writes components separately.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    separate_blocks_format_type: SeparateBlocksFormatType, optional
        Controls the format type when writing separate element blocks. Only used when write_separate_blocks is true.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    export_fasteners_as_swgen: bool, optional
        Option to export fasteners as swgen. When true, translates fasteners into compact swgen blocks in the exported file. The default value is false.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    export_rigid_bodies_as_rbgen: bool, optional
        Option to export rigid bodies as rbgen. When true, translates rigid bodies into compact rbgen blocks in the exported file. The default value is false.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    write_component_based_ties: bool, optional
        Option to write ties using component-based format. When true, writes ties using component selection and surface generation commands instead of explicit element definitions. The default value is false.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    mortar_contact_for_ties: bool, optional
        Option to enable mortar contact for ties. When true, changes the key options for tie surfaces. The default value is false.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    write_thickness_file: bool, optional
        Option to write a thickness file for spotweld fatigue analysis. If true, writes a file named [exportedFilename].cdb.thick.txt containing thickness information.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    contact_element_types: ContactElementTypeParams, optional
        Parameters for choosing element types for contact surfaces in TIEs and CONTACT PAIRs.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ExportMapdlCdbParams`` object with provided parameters.

    Examples
    --------
    >>> export_mapdl_cdb_params = prime.ExportMapdlCdbParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            config_settings: str,
            pre_solution_settings: str,
            material_properties: str,
            boundary_conditions: str,
            analysis_settings: str,
            write_cells: bool,
            enable_face_based_labels: bool,
            label_export_params: LabelExportParams,
            write_by_zones: bool,
            consider_general_connectors_as_spot_weld: bool,
            analysis_type: CdbAnalysisType,
            simulation_type: CdbSimulationType,
            analysis_settings_file_name: str,
            write_separate_blocks: bool,
            write_components_with_element_blocks: bool,
            separate_blocks_format_type: SeparateBlocksFormatType,
            export_fasteners_as_swgen: bool,
            export_rigid_bodies_as_rbgen: bool,
            write_component_based_ties: bool,
            mortar_contact_for_ties: bool,
            write_thickness_file: bool,
            contact_element_types: ContactElementTypeParams):
        self._config_settings = config_settings
        self._pre_solution_settings = pre_solution_settings
        self._material_properties = material_properties
        self._boundary_conditions = boundary_conditions
        self._analysis_settings = analysis_settings
        self._write_cells = write_cells
        self._enable_face_based_labels = enable_face_based_labels
        self._label_export_params = label_export_params
        self._write_by_zones = write_by_zones
        self._consider_general_connectors_as_spot_weld = consider_general_connectors_as_spot_weld
        self._analysis_type = CdbAnalysisType(analysis_type)
        self._simulation_type = CdbSimulationType(simulation_type)
        self._analysis_settings_file_name = analysis_settings_file_name
        self._write_separate_blocks = write_separate_blocks
        self._write_components_with_element_blocks = write_components_with_element_blocks
        self._separate_blocks_format_type = SeparateBlocksFormatType(separate_blocks_format_type)
        self._export_fasteners_as_swgen = export_fasteners_as_swgen
        self._export_rigid_bodies_as_rbgen = export_rigid_bodies_as_rbgen
        self._write_component_based_ties = write_component_based_ties
        self._mortar_contact_for_ties = mortar_contact_for_ties
        self._write_thickness_file = write_thickness_file
        self._contact_element_types = contact_element_types

    def __init__(
            self,
            model: CommunicationManager=None,
            config_settings: str = None,
            pre_solution_settings: str = None,
            material_properties: str = None,
            boundary_conditions: str = None,
            analysis_settings: str = None,
            write_cells: bool = None,
            enable_face_based_labels: bool = None,
            label_export_params: LabelExportParams = None,
            write_by_zones: bool = None,
            consider_general_connectors_as_spot_weld: bool = None,
            analysis_type: CdbAnalysisType = None,
            simulation_type: CdbSimulationType = None,
            analysis_settings_file_name: str = None,
            write_separate_blocks: bool = None,
            write_components_with_element_blocks: bool = None,
            separate_blocks_format_type: SeparateBlocksFormatType = None,
            export_fasteners_as_swgen: bool = None,
            export_rigid_bodies_as_rbgen: bool = None,
            write_component_based_ties: bool = None,
            mortar_contact_for_ties: bool = None,
            write_thickness_file: bool = None,
            contact_element_types: ContactElementTypeParams = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ExportMapdlCdbParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ExportMapdlCdbParams`` object with default parameters.
        config_settings: str, optional
            MAPDL configuration settings in CDB format to be added at the beginning of the file.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        pre_solution_settings: str, optional
            MAPDL Settings in CDB format to be added before the solution block in the file.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        material_properties: str, optional
            Materials in CDB format to be added to the file.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        boundary_conditions: str, optional
            Boundary conditions in CDB format to be added to the file.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        analysis_settings: str, optional
            MAPDL analysis settings in CDB format to be added after the solution block in the file. Note: Boundary conditions can be included into analysis settings.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        write_cells: bool, optional
            Option to write out cells as part of the file.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        enable_face_based_labels: bool, optional
            Use LabelExportParams instead. Parameter enableFaceBasedLabels will be removed in 2025R2.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        label_export_params: LabelExportParams, optional
            Parameters to control the export of labels as Nodal or Element Components in CDB.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        write_by_zones: bool, optional
            Option to write zones in the file.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        consider_general_connectors_as_spot_weld: bool, optional
            Option to translate all general connector joints (other than axial) to spot weld type. This is important when nodes are non coincident.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        analysis_type: CdbAnalysisType, optional
            Option to specify CDB analysis type.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        simulation_type: CdbSimulationType, optional
            Simulation type for the file.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        analysis_settings_file_name: str, optional
            File path to export mapdl analysis settings.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        write_separate_blocks: bool, optional
            Controls whether element blocks should be written separately. When true, writes elements in separate blocks based on the format specified in separate_blocks_format_type. When false, writes all elements into a single block.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        write_components_with_element_blocks: bool, optional
            Controls whether component definitions should be written within individual element blocks. write_components_with_element_blocks only has effect when write_separate_blocks is true. When write_components_with_element_blocks is true, writes component commands for each element block. When write_components_with_element_blocks is false, writes components separately.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        separate_blocks_format_type: SeparateBlocksFormatType, optional
            Controls the format type when writing separate element blocks. Only used when write_separate_blocks is true.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        export_fasteners_as_swgen: bool, optional
            Option to export fasteners as swgen. When true, translates fasteners into compact swgen blocks in the exported file. The default value is false.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        export_rigid_bodies_as_rbgen: bool, optional
            Option to export rigid bodies as rbgen. When true, translates rigid bodies into compact rbgen blocks in the exported file. The default value is false.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        write_component_based_ties: bool, optional
            Option to write ties using component-based format. When true, writes ties using component selection and surface generation commands instead of explicit element definitions. The default value is false.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        mortar_contact_for_ties: bool, optional
            Option to enable mortar contact for ties. When true, changes the key options for tie surfaces. The default value is false.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        write_thickness_file: bool, optional
            Option to write a thickness file for spotweld fatigue analysis. If true, writes a file named [exportedFilename].cdb.thick.txt containing thickness information.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        contact_element_types: ContactElementTypeParams, optional
            Parameters for choosing element types for contact surfaces in TIEs and CONTACT PAIRs.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ExportMapdlCdbParams`` object with provided parameters.

        Examples
        --------
        >>> export_mapdl_cdb_params = prime.ExportMapdlCdbParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["configSettings"] if "configSettings" in json_data else None,
                json_data["preSolutionSettings"] if "preSolutionSettings" in json_data else None,
                json_data["materialProperties"] if "materialProperties" in json_data else None,
                json_data["boundaryConditions"] if "boundaryConditions" in json_data else None,
                json_data["analysisSettings"] if "analysisSettings" in json_data else None,
                json_data["writeCells"] if "writeCells" in json_data else None,
                json_data["enableFaceBasedLabels"] if "enableFaceBasedLabels" in json_data else None,
                LabelExportParams(model = model, json_data = json_data["labelExportParams"] if "labelExportParams" in json_data else None),
                json_data["writeByZones"] if "writeByZones" in json_data else None,
                json_data["considerGeneralConnectorsAsSpotWeld"] if "considerGeneralConnectorsAsSpotWeld" in json_data else None,
                CdbAnalysisType(json_data["analysisType"] if "analysisType" in json_data else None),
                CdbSimulationType(json_data["simulationType"] if "simulationType" in json_data else None),
                json_data["analysisSettingsFileName"] if "analysisSettingsFileName" in json_data else None,
                json_data["writeSeparateBlocks"] if "writeSeparateBlocks" in json_data else None,
                json_data["writeComponentsWithElementBlocks"] if "writeComponentsWithElementBlocks" in json_data else None,
                SeparateBlocksFormatType(json_data["separateBlocksFormatType"] if "separateBlocksFormatType" in json_data else None),
                json_data["exportFastenersAsSwgen"] if "exportFastenersAsSwgen" in json_data else None,
                json_data["exportRigidBodiesAsRbgen"] if "exportRigidBodiesAsRbgen" in json_data else None,
                json_data["writeComponentBasedTies"] if "writeComponentBasedTies" in json_data else None,
                json_data["mortarContactForTies"] if "mortarContactForTies" in json_data else None,
                json_data["writeThicknessFile"] if "writeThicknessFile" in json_data else None,
                ContactElementTypeParams(model = model, json_data = json_data["contactElementTypes"] if "contactElementTypes" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [config_settings, pre_solution_settings, material_properties, boundary_conditions, analysis_settings, write_cells, enable_face_based_labels, label_export_params, write_by_zones, consider_general_connectors_as_spot_weld, analysis_type, simulation_type, analysis_settings_file_name, write_separate_blocks, write_components_with_element_blocks, separate_blocks_format_type, export_fasteners_as_swgen, export_rigid_bodies_as_rbgen, write_component_based_ties, mortar_contact_for_ties, write_thickness_file, contact_element_types])
            if all_field_specified:
                self.__initialize(
                    config_settings,
                    pre_solution_settings,
                    material_properties,
                    boundary_conditions,
                    analysis_settings,
                    write_cells,
                    enable_face_based_labels,
                    label_export_params,
                    write_by_zones,
                    consider_general_connectors_as_spot_weld,
                    analysis_type,
                    simulation_type,
                    analysis_settings_file_name,
                    write_separate_blocks,
                    write_components_with_element_blocks,
                    separate_blocks_format_type,
                    export_fasteners_as_swgen,
                    export_rigid_bodies_as_rbgen,
                    write_component_based_ties,
                    mortar_contact_for_ties,
                    write_thickness_file,
                    contact_element_types)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ExportMapdlCdbParams")
                    json_data = param_json["ExportMapdlCdbParams"] if "ExportMapdlCdbParams" in param_json else {}
                    self.__initialize(
                        config_settings if config_settings is not None else ( ExportMapdlCdbParams._default_params["config_settings"] if "config_settings" in ExportMapdlCdbParams._default_params else (json_data["configSettings"] if "configSettings" in json_data else None)),
                        pre_solution_settings if pre_solution_settings is not None else ( ExportMapdlCdbParams._default_params["pre_solution_settings"] if "pre_solution_settings" in ExportMapdlCdbParams._default_params else (json_data["preSolutionSettings"] if "preSolutionSettings" in json_data else None)),
                        material_properties if material_properties is not None else ( ExportMapdlCdbParams._default_params["material_properties"] if "material_properties" in ExportMapdlCdbParams._default_params else (json_data["materialProperties"] if "materialProperties" in json_data else None)),
                        boundary_conditions if boundary_conditions is not None else ( ExportMapdlCdbParams._default_params["boundary_conditions"] if "boundary_conditions" in ExportMapdlCdbParams._default_params else (json_data["boundaryConditions"] if "boundaryConditions" in json_data else None)),
                        analysis_settings if analysis_settings is not None else ( ExportMapdlCdbParams._default_params["analysis_settings"] if "analysis_settings" in ExportMapdlCdbParams._default_params else (json_data["analysisSettings"] if "analysisSettings" in json_data else None)),
                        write_cells if write_cells is not None else ( ExportMapdlCdbParams._default_params["write_cells"] if "write_cells" in ExportMapdlCdbParams._default_params else (json_data["writeCells"] if "writeCells" in json_data else None)),
                        enable_face_based_labels if enable_face_based_labels is not None else ( ExportMapdlCdbParams._default_params["enable_face_based_labels"] if "enable_face_based_labels" in ExportMapdlCdbParams._default_params else (json_data["enableFaceBasedLabels"] if "enableFaceBasedLabels" in json_data else None)),
                        label_export_params if label_export_params is not None else ( ExportMapdlCdbParams._default_params["label_export_params"] if "label_export_params" in ExportMapdlCdbParams._default_params else LabelExportParams(model = model, json_data = (json_data["labelExportParams"] if "labelExportParams" in json_data else None))),
                        write_by_zones if write_by_zones is not None else ( ExportMapdlCdbParams._default_params["write_by_zones"] if "write_by_zones" in ExportMapdlCdbParams._default_params else (json_data["writeByZones"] if "writeByZones" in json_data else None)),
                        consider_general_connectors_as_spot_weld if consider_general_connectors_as_spot_weld is not None else ( ExportMapdlCdbParams._default_params["consider_general_connectors_as_spot_weld"] if "consider_general_connectors_as_spot_weld" in ExportMapdlCdbParams._default_params else (json_data["considerGeneralConnectorsAsSpotWeld"] if "considerGeneralConnectorsAsSpotWeld" in json_data else None)),
                        analysis_type if analysis_type is not None else ( ExportMapdlCdbParams._default_params["analysis_type"] if "analysis_type" in ExportMapdlCdbParams._default_params else CdbAnalysisType(json_data["analysisType"] if "analysisType" in json_data else None)),
                        simulation_type if simulation_type is not None else ( ExportMapdlCdbParams._default_params["simulation_type"] if "simulation_type" in ExportMapdlCdbParams._default_params else CdbSimulationType(json_data["simulationType"] if "simulationType" in json_data else None)),
                        analysis_settings_file_name if analysis_settings_file_name is not None else ( ExportMapdlCdbParams._default_params["analysis_settings_file_name"] if "analysis_settings_file_name" in ExportMapdlCdbParams._default_params else (json_data["analysisSettingsFileName"] if "analysisSettingsFileName" in json_data else None)),
                        write_separate_blocks if write_separate_blocks is not None else ( ExportMapdlCdbParams._default_params["write_separate_blocks"] if "write_separate_blocks" in ExportMapdlCdbParams._default_params else (json_data["writeSeparateBlocks"] if "writeSeparateBlocks" in json_data else None)),
                        write_components_with_element_blocks if write_components_with_element_blocks is not None else ( ExportMapdlCdbParams._default_params["write_components_with_element_blocks"] if "write_components_with_element_blocks" in ExportMapdlCdbParams._default_params else (json_data["writeComponentsWithElementBlocks"] if "writeComponentsWithElementBlocks" in json_data else None)),
                        separate_blocks_format_type if separate_blocks_format_type is not None else ( ExportMapdlCdbParams._default_params["separate_blocks_format_type"] if "separate_blocks_format_type" in ExportMapdlCdbParams._default_params else SeparateBlocksFormatType(json_data["separateBlocksFormatType"] if "separateBlocksFormatType" in json_data else None)),
                        export_fasteners_as_swgen if export_fasteners_as_swgen is not None else ( ExportMapdlCdbParams._default_params["export_fasteners_as_swgen"] if "export_fasteners_as_swgen" in ExportMapdlCdbParams._default_params else (json_data["exportFastenersAsSwgen"] if "exportFastenersAsSwgen" in json_data else None)),
                        export_rigid_bodies_as_rbgen if export_rigid_bodies_as_rbgen is not None else ( ExportMapdlCdbParams._default_params["export_rigid_bodies_as_rbgen"] if "export_rigid_bodies_as_rbgen" in ExportMapdlCdbParams._default_params else (json_data["exportRigidBodiesAsRbgen"] if "exportRigidBodiesAsRbgen" in json_data else None)),
                        write_component_based_ties if write_component_based_ties is not None else ( ExportMapdlCdbParams._default_params["write_component_based_ties"] if "write_component_based_ties" in ExportMapdlCdbParams._default_params else (json_data["writeComponentBasedTies"] if "writeComponentBasedTies" in json_data else None)),
                        mortar_contact_for_ties if mortar_contact_for_ties is not None else ( ExportMapdlCdbParams._default_params["mortar_contact_for_ties"] if "mortar_contact_for_ties" in ExportMapdlCdbParams._default_params else (json_data["mortarContactForTies"] if "mortarContactForTies" in json_data else None)),
                        write_thickness_file if write_thickness_file is not None else ( ExportMapdlCdbParams._default_params["write_thickness_file"] if "write_thickness_file" in ExportMapdlCdbParams._default_params else (json_data["writeThicknessFile"] if "writeThicknessFile" in json_data else None)),
                        contact_element_types if contact_element_types is not None else ( ExportMapdlCdbParams._default_params["contact_element_types"] if "contact_element_types" in ExportMapdlCdbParams._default_params else ContactElementTypeParams(model = model, json_data = (json_data["contactElementTypes"] if "contactElementTypes" in json_data else None))))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            config_settings: str = None,
            pre_solution_settings: str = None,
            material_properties: str = None,
            boundary_conditions: str = None,
            analysis_settings: str = None,
            write_cells: bool = None,
            enable_face_based_labels: bool = None,
            label_export_params: LabelExportParams = None,
            write_by_zones: bool = None,
            consider_general_connectors_as_spot_weld: bool = None,
            analysis_type: CdbAnalysisType = None,
            simulation_type: CdbSimulationType = None,
            analysis_settings_file_name: str = None,
            write_separate_blocks: bool = None,
            write_components_with_element_blocks: bool = None,
            separate_blocks_format_type: SeparateBlocksFormatType = None,
            export_fasteners_as_swgen: bool = None,
            export_rigid_bodies_as_rbgen: bool = None,
            write_component_based_ties: bool = None,
            mortar_contact_for_ties: bool = None,
            write_thickness_file: bool = None,
            contact_element_types: ContactElementTypeParams = None):
        """Set the default values of the ``ExportMapdlCdbParams`` object.

        Parameters
        ----------
        config_settings: str, optional
            MAPDL configuration settings in CDB format to be added at the beginning of the file.
        pre_solution_settings: str, optional
            MAPDL Settings in CDB format to be added before the solution block in the file.
        material_properties: str, optional
            Materials in CDB format to be added to the file.
        boundary_conditions: str, optional
            Boundary conditions in CDB format to be added to the file.
        analysis_settings: str, optional
            MAPDL analysis settings in CDB format to be added after the solution block in the file. Note: Boundary conditions can be included into analysis settings.
        write_cells: bool, optional
            Option to write out cells as part of the file.
        enable_face_based_labels: bool, optional
            Use LabelExportParams instead. Parameter enableFaceBasedLabels will be removed in 2025R2.
        label_export_params: LabelExportParams, optional
            Parameters to control the export of labels as Nodal or Element Components in CDB.
        write_by_zones: bool, optional
            Option to write zones in the file.
        consider_general_connectors_as_spot_weld: bool, optional
            Option to translate all general connector joints (other than axial) to spot weld type. This is important when nodes are non coincident.
        analysis_type: CdbAnalysisType, optional
            Option to specify CDB analysis type.
        simulation_type: CdbSimulationType, optional
            Simulation type for the file.
        analysis_settings_file_name: str, optional
            File path to export mapdl analysis settings.
        write_separate_blocks: bool, optional
            Controls whether element blocks should be written separately. When true, writes elements in separate blocks based on the format specified in separate_blocks_format_type. When false, writes all elements into a single block.
        write_components_with_element_blocks: bool, optional
            Controls whether component definitions should be written within individual element blocks. write_components_with_element_blocks only has effect when write_separate_blocks is true. When write_components_with_element_blocks is true, writes component commands for each element block. When write_components_with_element_blocks is false, writes components separately.
        separate_blocks_format_type: SeparateBlocksFormatType, optional
            Controls the format type when writing separate element blocks. Only used when write_separate_blocks is true.
        export_fasteners_as_swgen: bool, optional
            Option to export fasteners as swgen. When true, translates fasteners into compact swgen blocks in the exported file. The default value is false.
        export_rigid_bodies_as_rbgen: bool, optional
            Option to export rigid bodies as rbgen. When true, translates rigid bodies into compact rbgen blocks in the exported file. The default value is false.
        write_component_based_ties: bool, optional
            Option to write ties using component-based format. When true, writes ties using component selection and surface generation commands instead of explicit element definitions. The default value is false.
        mortar_contact_for_ties: bool, optional
            Option to enable mortar contact for ties. When true, changes the key options for tie surfaces. The default value is false.
        write_thickness_file: bool, optional
            Option to write a thickness file for spotweld fatigue analysis. If true, writes a file named [exportedFilename].cdb.thick.txt containing thickness information.
        contact_element_types: ContactElementTypeParams, optional
            Parameters for choosing element types for contact surfaces in TIEs and CONTACT PAIRs.
        """
        args = locals()
        [ExportMapdlCdbParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ExportMapdlCdbParams`` object.

        Examples
        --------
        >>> ExportMapdlCdbParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportMapdlCdbParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._config_settings is not None:
            json_data["configSettings"] = self._config_settings
        if self._pre_solution_settings is not None:
            json_data["preSolutionSettings"] = self._pre_solution_settings
        if self._material_properties is not None:
            json_data["materialProperties"] = self._material_properties
        if self._boundary_conditions is not None:
            json_data["boundaryConditions"] = self._boundary_conditions
        if self._analysis_settings is not None:
            json_data["analysisSettings"] = self._analysis_settings
        if self._write_cells is not None:
            json_data["writeCells"] = self._write_cells
        if self._enable_face_based_labels is not None:
            json_data["enableFaceBasedLabels"] = self._enable_face_based_labels
        if self._label_export_params is not None:
            json_data["labelExportParams"] = self._label_export_params._jsonify()
        if self._write_by_zones is not None:
            json_data["writeByZones"] = self._write_by_zones
        if self._consider_general_connectors_as_spot_weld is not None:
            json_data["considerGeneralConnectorsAsSpotWeld"] = self._consider_general_connectors_as_spot_weld
        if self._analysis_type is not None:
            json_data["analysisType"] = self._analysis_type
        if self._simulation_type is not None:
            json_data["simulationType"] = self._simulation_type
        if self._analysis_settings_file_name is not None:
            json_data["analysisSettingsFileName"] = self._analysis_settings_file_name
        if self._write_separate_blocks is not None:
            json_data["writeSeparateBlocks"] = self._write_separate_blocks
        if self._write_components_with_element_blocks is not None:
            json_data["writeComponentsWithElementBlocks"] = self._write_components_with_element_blocks
        if self._separate_blocks_format_type is not None:
            json_data["separateBlocksFormatType"] = self._separate_blocks_format_type
        if self._export_fasteners_as_swgen is not None:
            json_data["exportFastenersAsSwgen"] = self._export_fasteners_as_swgen
        if self._export_rigid_bodies_as_rbgen is not None:
            json_data["exportRigidBodiesAsRbgen"] = self._export_rigid_bodies_as_rbgen
        if self._write_component_based_ties is not None:
            json_data["writeComponentBasedTies"] = self._write_component_based_ties
        if self._mortar_contact_for_ties is not None:
            json_data["mortarContactForTies"] = self._mortar_contact_for_ties
        if self._write_thickness_file is not None:
            json_data["writeThicknessFile"] = self._write_thickness_file
        if self._contact_element_types is not None:
            json_data["contactElementTypes"] = self._contact_element_types._jsonify()
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "config_settings :  %s\npre_solution_settings :  %s\nmaterial_properties :  %s\nboundary_conditions :  %s\nanalysis_settings :  %s\nwrite_cells :  %s\nenable_face_based_labels :  %s\nlabel_export_params :  %s\nwrite_by_zones :  %s\nconsider_general_connectors_as_spot_weld :  %s\nanalysis_type :  %s\nsimulation_type :  %s\nanalysis_settings_file_name :  %s\nwrite_separate_blocks :  %s\nwrite_components_with_element_blocks :  %s\nseparate_blocks_format_type :  %s\nexport_fasteners_as_swgen :  %s\nexport_rigid_bodies_as_rbgen :  %s\nwrite_component_based_ties :  %s\nmortar_contact_for_ties :  %s\nwrite_thickness_file :  %s\ncontact_element_types :  %s" % (self._config_settings, self._pre_solution_settings, self._material_properties, self._boundary_conditions, self._analysis_settings, self._write_cells, self._enable_face_based_labels, '{ ' + str(self._label_export_params) + ' }', self._write_by_zones, self._consider_general_connectors_as_spot_weld, self._analysis_type, self._simulation_type, self._analysis_settings_file_name, self._write_separate_blocks, self._write_components_with_element_blocks, self._separate_blocks_format_type, self._export_fasteners_as_swgen, self._export_rigid_bodies_as_rbgen, self._write_component_based_ties, self._mortar_contact_for_ties, self._write_thickness_file, '{ ' + str(self._contact_element_types) + ' }')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def config_settings(self) -> str:
        """MAPDL configuration settings in CDB format to be added at the beginning of the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._config_settings

    @config_settings.setter
    def config_settings(self, value: str):
        self._config_settings = value

    @property
    def pre_solution_settings(self) -> str:
        """MAPDL Settings in CDB format to be added before the solution block in the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._pre_solution_settings

    @pre_solution_settings.setter
    def pre_solution_settings(self, value: str):
        self._pre_solution_settings = value

    @property
    def material_properties(self) -> str:
        """Materials in CDB format to be added to the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._material_properties

    @material_properties.setter
    def material_properties(self, value: str):
        self._material_properties = value

    @property
    def boundary_conditions(self) -> str:
        """Boundary conditions in CDB format to be added to the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._boundary_conditions

    @boundary_conditions.setter
    def boundary_conditions(self, value: str):
        self._boundary_conditions = value

    @property
    def analysis_settings(self) -> str:
        """MAPDL analysis settings in CDB format to be added after the solution block in the file. Note: Boundary conditions can be included into analysis settings.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._analysis_settings

    @analysis_settings.setter
    def analysis_settings(self, value: str):
        self._analysis_settings = value

    @property
    def write_cells(self) -> bool:
        """Option to write out cells as part of the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._write_cells

    @write_cells.setter
    def write_cells(self, value: bool):
        self._write_cells = value

    @property
    def enable_face_based_labels(self) -> bool:
        """Use LabelExportParams instead. Parameter enableFaceBasedLabels will be removed in 2025R2.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._enable_face_based_labels

    @enable_face_based_labels.setter
    def enable_face_based_labels(self, value: bool):
        self._enable_face_based_labels = value

    @property
    def label_export_params(self) -> LabelExportParams:
        """Parameters to control the export of labels as Nodal or Element Components in CDB.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._label_export_params

    @label_export_params.setter
    def label_export_params(self, value: LabelExportParams):
        self._label_export_params = value

    @property
    def write_by_zones(self) -> bool:
        """Option to write zones in the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._write_by_zones

    @write_by_zones.setter
    def write_by_zones(self, value: bool):
        self._write_by_zones = value

    @property
    def consider_general_connectors_as_spot_weld(self) -> bool:
        """Option to translate all general connector joints (other than axial) to spot weld type. This is important when nodes are non coincident.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._consider_general_connectors_as_spot_weld

    @consider_general_connectors_as_spot_weld.setter
    def consider_general_connectors_as_spot_weld(self, value: bool):
        self._consider_general_connectors_as_spot_weld = value

    @property
    def analysis_type(self) -> CdbAnalysisType:
        """Option to specify CDB analysis type.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._analysis_type

    @analysis_type.setter
    def analysis_type(self, value: CdbAnalysisType):
        self._analysis_type = value

    @property
    def simulation_type(self) -> CdbSimulationType:
        """Simulation type for the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._simulation_type

    @simulation_type.setter
    def simulation_type(self, value: CdbSimulationType):
        self._simulation_type = value

    @property
    def analysis_settings_file_name(self) -> str:
        """File path to export mapdl analysis settings.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._analysis_settings_file_name

    @analysis_settings_file_name.setter
    def analysis_settings_file_name(self, value: str):
        self._analysis_settings_file_name = value

    @property
    def write_separate_blocks(self) -> bool:
        """Controls whether element blocks should be written separately. When true, writes elements in separate blocks based on the format specified in separate_blocks_format_type. When false, writes all elements into a single block.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._write_separate_blocks

    @write_separate_blocks.setter
    def write_separate_blocks(self, value: bool):
        self._write_separate_blocks = value

    @property
    def write_components_with_element_blocks(self) -> bool:
        """Controls whether component definitions should be written within individual element blocks. write_components_with_element_blocks only has effect when write_separate_blocks is true. When write_components_with_element_blocks is true, writes component commands for each element block. When write_components_with_element_blocks is false, writes components separately.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._write_components_with_element_blocks

    @write_components_with_element_blocks.setter
    def write_components_with_element_blocks(self, value: bool):
        self._write_components_with_element_blocks = value

    @property
    def separate_blocks_format_type(self) -> SeparateBlocksFormatType:
        """Controls the format type when writing separate element blocks. Only used when write_separate_blocks is true.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._separate_blocks_format_type

    @separate_blocks_format_type.setter
    def separate_blocks_format_type(self, value: SeparateBlocksFormatType):
        self._separate_blocks_format_type = value

    @property
    def export_fasteners_as_swgen(self) -> bool:
        """Option to export fasteners as swgen. When true, translates fasteners into compact swgen blocks in the exported file. The default value is false.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._export_fasteners_as_swgen

    @export_fasteners_as_swgen.setter
    def export_fasteners_as_swgen(self, value: bool):
        self._export_fasteners_as_swgen = value

    @property
    def export_rigid_bodies_as_rbgen(self) -> bool:
        """Option to export rigid bodies as rbgen. When true, translates rigid bodies into compact rbgen blocks in the exported file. The default value is false.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._export_rigid_bodies_as_rbgen

    @export_rigid_bodies_as_rbgen.setter
    def export_rigid_bodies_as_rbgen(self, value: bool):
        self._export_rigid_bodies_as_rbgen = value

    @property
    def write_component_based_ties(self) -> bool:
        """Option to write ties using component-based format. When true, writes ties using component selection and surface generation commands instead of explicit element definitions. The default value is false.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._write_component_based_ties

    @write_component_based_ties.setter
    def write_component_based_ties(self, value: bool):
        self._write_component_based_ties = value

    @property
    def mortar_contact_for_ties(self) -> bool:
        """Option to enable mortar contact for ties. When true, changes the key options for tie surfaces. The default value is false.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._mortar_contact_for_ties

    @mortar_contact_for_ties.setter
    def mortar_contact_for_ties(self, value: bool):
        self._mortar_contact_for_ties = value

    @property
    def write_thickness_file(self) -> bool:
        """Option to write a thickness file for spotweld fatigue analysis. If true, writes a file named [exportedFilename].cdb.thick.txt containing thickness information.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._write_thickness_file

    @write_thickness_file.setter
    def write_thickness_file(self, value: bool):
        self._write_thickness_file = value

    @property
    def contact_element_types(self) -> ContactElementTypeParams:
        """Parameters for choosing element types for contact surfaces in TIEs and CONTACT PAIRs.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._contact_element_types

    @contact_element_types.setter
    def contact_element_types(self, value: ContactElementTypeParams):
        self._contact_element_types = value

class ExportMapdlCdbResults(CoreObject):
    """Results associated with the MAPDL CDB export.

    Parameters
    ----------
    model: Model
        Model to create a ``ExportMapdlCdbResults`` object with default parameters.
    summary_log: str, optional
        Summary log for the export operation in json format.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    zone_mesh_results: List[ZoneMeshResult], optional
        Zone-wise mesh information for elements in the exported model.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    error_code: ErrorCode, optional
        Error code associated with failure of operation.
    warning_codes: List[WarningCode], optional
        Warning codes associated with the operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ExportMapdlCdbResults`` object with provided parameters.

    Examples
    --------
    >>> export_mapdl_cdb_results = prime.ExportMapdlCdbResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            summary_log: str,
            zone_mesh_results: List[ZoneMeshResult],
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._summary_log = summary_log
        self._zone_mesh_results = zone_mesh_results
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            summary_log: str = None,
            zone_mesh_results: List[ZoneMeshResult] = None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ExportMapdlCdbResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ExportMapdlCdbResults`` object with default parameters.
        summary_log: str, optional
            Summary log for the export operation in json format.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        zone_mesh_results: List[ZoneMeshResult], optional
            Zone-wise mesh information for elements in the exported model.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ExportMapdlCdbResults`` object with provided parameters.

        Examples
        --------
        >>> export_mapdl_cdb_results = prime.ExportMapdlCdbResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["summaryLog"] if "summaryLog" in json_data else None,
                [ZoneMeshResult(model = model, json_data = data) for data in json_data["zoneMeshResults"]] if "zoneMeshResults" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [summary_log, zone_mesh_results, error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    summary_log,
                    zone_mesh_results,
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ExportMapdlCdbResults")
                    json_data = param_json["ExportMapdlCdbResults"] if "ExportMapdlCdbResults" in param_json else {}
                    self.__initialize(
                        summary_log if summary_log is not None else ( ExportMapdlCdbResults._default_params["summary_log"] if "summary_log" in ExportMapdlCdbResults._default_params else (json_data["summaryLog"] if "summaryLog" in json_data else None)),
                        zone_mesh_results if zone_mesh_results is not None else ( ExportMapdlCdbResults._default_params["zone_mesh_results"] if "zone_mesh_results" in ExportMapdlCdbResults._default_params else [ZoneMeshResult(model = model, json_data = data) for data in (json_data["zoneMeshResults"] if "zoneMeshResults" in json_data else None)]),
                        error_code if error_code is not None else ( ExportMapdlCdbResults._default_params["error_code"] if "error_code" in ExportMapdlCdbResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( ExportMapdlCdbResults._default_params["warning_codes"] if "warning_codes" in ExportMapdlCdbResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            summary_log: str = None,
            zone_mesh_results: List[ZoneMeshResult] = None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of the ``ExportMapdlCdbResults`` object.

        Parameters
        ----------
        summary_log: str, optional
            Summary log for the export operation in json format.
        zone_mesh_results: List[ZoneMeshResult], optional
            Zone-wise mesh information for elements in the exported model.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        """
        args = locals()
        [ExportMapdlCdbResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ExportMapdlCdbResults`` object.

        Examples
        --------
        >>> ExportMapdlCdbResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportMapdlCdbResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._summary_log is not None:
            json_data["summaryLog"] = self._summary_log
        if self._zone_mesh_results is not None:
            json_data["zoneMeshResults"] = [data._jsonify() for data in self._zone_mesh_results]
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "summary_log :  %s\nzone_mesh_results :  %s\nerror_code :  %s\nwarning_codes :  %s" % (self._summary_log, '[' + ''.join('\n' + str(data) for data in self._zone_mesh_results) + ']', self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def summary_log(self) -> str:
        """Summary log for the export operation in json format.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._summary_log

    @summary_log.setter
    def summary_log(self, value: str):
        self._summary_log = value

    @property
    def zone_mesh_results(self) -> List[ZoneMeshResult]:
        """Zone-wise mesh information for elements in the exported model.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._zone_mesh_results

    @zone_mesh_results.setter
    def zone_mesh_results(self, value: List[ZoneMeshResult]):
        self._zone_mesh_results = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class ExportLSDynaKeywordFileParams(CoreObject):
    """Parameters to control LS-DYNA keyword file export settings.

    Parameters
    ----------
    model: Model
        Model to create a ``ExportLSDynaKeywordFileParams`` object with default parameters.
    material_properties: str, optional
        Materials in LS-DYNA format to be added to the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    database_keywords: str, optional
        Database keywords in LS-DYNA format to be added to the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    output_format: LSDynaFileFormatType, optional
        Output file format used to write LS-DYNA file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    analysis_type: LSDynaAnalysisType, optional
        Option to specify LS-DYNA analysis type.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    compute_spotweld_thickness: bool, optional
        Option to compute spot weld thickness using shell thickness when set to true. Else, use search radius as thickness.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    write_thickness_file: bool, optional
        Option to write a thickness file for spotweld fatigue analysis. If true, writes a file named [exportedFilename].k.thick.txt containing thickness information.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    output_controls_d3_part: bool, optional
        Option to create D3Part card in output controls.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ExportLSDynaKeywordFileParams`` object with provided parameters.

    Examples
    --------
    >>> export_lsdyna_keyword_file_params = prime.ExportLSDynaKeywordFileParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            material_properties: str,
            database_keywords: str,
            output_format: LSDynaFileFormatType,
            analysis_type: LSDynaAnalysisType,
            compute_spotweld_thickness: bool,
            write_thickness_file: bool,
            output_controls_d3_part: bool):
        self._material_properties = material_properties
        self._database_keywords = database_keywords
        self._output_format = LSDynaFileFormatType(output_format)
        self._analysis_type = LSDynaAnalysisType(analysis_type)
        self._compute_spotweld_thickness = compute_spotweld_thickness
        self._write_thickness_file = write_thickness_file
        self._output_controls_d3_part = output_controls_d3_part

    def __init__(
            self,
            model: CommunicationManager=None,
            material_properties: str = None,
            database_keywords: str = None,
            output_format: LSDynaFileFormatType = None,
            analysis_type: LSDynaAnalysisType = None,
            compute_spotweld_thickness: bool = None,
            write_thickness_file: bool = None,
            output_controls_d3_part: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ExportLSDynaKeywordFileParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ExportLSDynaKeywordFileParams`` object with default parameters.
        material_properties: str, optional
            Materials in LS-DYNA format to be added to the file.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        database_keywords: str, optional
            Database keywords in LS-DYNA format to be added to the file.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        output_format: LSDynaFileFormatType, optional
            Output file format used to write LS-DYNA file.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        analysis_type: LSDynaAnalysisType, optional
            Option to specify LS-DYNA analysis type.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        compute_spotweld_thickness: bool, optional
            Option to compute spot weld thickness using shell thickness when set to true. Else, use search radius as thickness.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        write_thickness_file: bool, optional
            Option to write a thickness file for spotweld fatigue analysis. If true, writes a file named [exportedFilename].k.thick.txt containing thickness information.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        output_controls_d3_part: bool, optional
            Option to create D3Part card in output controls.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ExportLSDynaKeywordFileParams`` object with provided parameters.

        Examples
        --------
        >>> export_lsdyna_keyword_file_params = prime.ExportLSDynaKeywordFileParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["materialProperties"] if "materialProperties" in json_data else None,
                json_data["databaseKeywords"] if "databaseKeywords" in json_data else None,
                LSDynaFileFormatType(json_data["outputFormat"] if "outputFormat" in json_data else None),
                LSDynaAnalysisType(json_data["analysisType"] if "analysisType" in json_data else None),
                json_data["computeSpotweldThickness"] if "computeSpotweldThickness" in json_data else None,
                json_data["writeThicknessFile"] if "writeThicknessFile" in json_data else None,
                json_data["outputControlsD3Part"] if "outputControlsD3Part" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [material_properties, database_keywords, output_format, analysis_type, compute_spotweld_thickness, write_thickness_file, output_controls_d3_part])
            if all_field_specified:
                self.__initialize(
                    material_properties,
                    database_keywords,
                    output_format,
                    analysis_type,
                    compute_spotweld_thickness,
                    write_thickness_file,
                    output_controls_d3_part)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ExportLSDynaKeywordFileParams")
                    json_data = param_json["ExportLSDynaKeywordFileParams"] if "ExportLSDynaKeywordFileParams" in param_json else {}
                    self.__initialize(
                        material_properties if material_properties is not None else ( ExportLSDynaKeywordFileParams._default_params["material_properties"] if "material_properties" in ExportLSDynaKeywordFileParams._default_params else (json_data["materialProperties"] if "materialProperties" in json_data else None)),
                        database_keywords if database_keywords is not None else ( ExportLSDynaKeywordFileParams._default_params["database_keywords"] if "database_keywords" in ExportLSDynaKeywordFileParams._default_params else (json_data["databaseKeywords"] if "databaseKeywords" in json_data else None)),
                        output_format if output_format is not None else ( ExportLSDynaKeywordFileParams._default_params["output_format"] if "output_format" in ExportLSDynaKeywordFileParams._default_params else LSDynaFileFormatType(json_data["outputFormat"] if "outputFormat" in json_data else None)),
                        analysis_type if analysis_type is not None else ( ExportLSDynaKeywordFileParams._default_params["analysis_type"] if "analysis_type" in ExportLSDynaKeywordFileParams._default_params else LSDynaAnalysisType(json_data["analysisType"] if "analysisType" in json_data else None)),
                        compute_spotweld_thickness if compute_spotweld_thickness is not None else ( ExportLSDynaKeywordFileParams._default_params["compute_spotweld_thickness"] if "compute_spotweld_thickness" in ExportLSDynaKeywordFileParams._default_params else (json_data["computeSpotweldThickness"] if "computeSpotweldThickness" in json_data else None)),
                        write_thickness_file if write_thickness_file is not None else ( ExportLSDynaKeywordFileParams._default_params["write_thickness_file"] if "write_thickness_file" in ExportLSDynaKeywordFileParams._default_params else (json_data["writeThicknessFile"] if "writeThicknessFile" in json_data else None)),
                        output_controls_d3_part if output_controls_d3_part is not None else ( ExportLSDynaKeywordFileParams._default_params["output_controls_d3_part"] if "output_controls_d3_part" in ExportLSDynaKeywordFileParams._default_params else (json_data["outputControlsD3Part"] if "outputControlsD3Part" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            material_properties: str = None,
            database_keywords: str = None,
            output_format: LSDynaFileFormatType = None,
            analysis_type: LSDynaAnalysisType = None,
            compute_spotweld_thickness: bool = None,
            write_thickness_file: bool = None,
            output_controls_d3_part: bool = None):
        """Set the default values of the ``ExportLSDynaKeywordFileParams`` object.

        Parameters
        ----------
        material_properties: str, optional
            Materials in LS-DYNA format to be added to the file.
        database_keywords: str, optional
            Database keywords in LS-DYNA format to be added to the file.
        output_format: LSDynaFileFormatType, optional
            Output file format used to write LS-DYNA file.
        analysis_type: LSDynaAnalysisType, optional
            Option to specify LS-DYNA analysis type.
        compute_spotweld_thickness: bool, optional
            Option to compute spot weld thickness using shell thickness when set to true. Else, use search radius as thickness.
        write_thickness_file: bool, optional
            Option to write a thickness file for spotweld fatigue analysis. If true, writes a file named [exportedFilename].k.thick.txt containing thickness information.
        output_controls_d3_part: bool, optional
            Option to create D3Part card in output controls.
        """
        args = locals()
        [ExportLSDynaKeywordFileParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ExportLSDynaKeywordFileParams`` object.

        Examples
        --------
        >>> ExportLSDynaKeywordFileParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportLSDynaKeywordFileParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._material_properties is not None:
            json_data["materialProperties"] = self._material_properties
        if self._database_keywords is not None:
            json_data["databaseKeywords"] = self._database_keywords
        if self._output_format is not None:
            json_data["outputFormat"] = self._output_format
        if self._analysis_type is not None:
            json_data["analysisType"] = self._analysis_type
        if self._compute_spotweld_thickness is not None:
            json_data["computeSpotweldThickness"] = self._compute_spotweld_thickness
        if self._write_thickness_file is not None:
            json_data["writeThicknessFile"] = self._write_thickness_file
        if self._output_controls_d3_part is not None:
            json_data["outputControlsD3Part"] = self._output_controls_d3_part
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "material_properties :  %s\ndatabase_keywords :  %s\noutput_format :  %s\nanalysis_type :  %s\ncompute_spotweld_thickness :  %s\nwrite_thickness_file :  %s\noutput_controls_d3_part :  %s" % (self._material_properties, self._database_keywords, self._output_format, self._analysis_type, self._compute_spotweld_thickness, self._write_thickness_file, self._output_controls_d3_part)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def material_properties(self) -> str:
        """Materials in LS-DYNA format to be added to the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._material_properties

    @material_properties.setter
    def material_properties(self, value: str):
        self._material_properties = value

    @property
    def database_keywords(self) -> str:
        """Database keywords in LS-DYNA format to be added to the file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._database_keywords

    @database_keywords.setter
    def database_keywords(self, value: str):
        self._database_keywords = value

    @property
    def output_format(self) -> LSDynaFileFormatType:
        """Output file format used to write LS-DYNA file.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._output_format

    @output_format.setter
    def output_format(self, value: LSDynaFileFormatType):
        self._output_format = value

    @property
    def analysis_type(self) -> LSDynaAnalysisType:
        """Option to specify LS-DYNA analysis type.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._analysis_type

    @analysis_type.setter
    def analysis_type(self, value: LSDynaAnalysisType):
        self._analysis_type = value

    @property
    def compute_spotweld_thickness(self) -> bool:
        """Option to compute spot weld thickness using shell thickness when set to true. Else, use search radius as thickness.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._compute_spotweld_thickness

    @compute_spotweld_thickness.setter
    def compute_spotweld_thickness(self, value: bool):
        self._compute_spotweld_thickness = value

    @property
    def write_thickness_file(self) -> bool:
        """Option to write a thickness file for spotweld fatigue analysis. If true, writes a file named [exportedFilename].k.thick.txt containing thickness information.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._write_thickness_file

    @write_thickness_file.setter
    def write_thickness_file(self, value: bool):
        self._write_thickness_file = value

    @property
    def output_controls_d3_part(self) -> bool:
        """Option to create D3Part card in output controls.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._output_controls_d3_part

    @output_controls_d3_part.setter
    def output_controls_d3_part(self, value: bool):
        self._output_controls_d3_part = value

class ExportLSDynaResults(CoreObject):
    """Results associated with the LS-DYNA export.

    Parameters
    ----------
    model: Model
        Model to create a ``ExportLSDynaResults`` object with default parameters.
    summary_log: str, optional
        Summary log for the import operation in json format.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    zone_mesh_results: List[ZoneMeshResult], optional
        Zone-wise mesh information for elements in the exported model.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    error_code: ErrorCode, optional
        Error code associated with failure of operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    warning_codes: List[WarningCode], optional
        Warning codes associated with the operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ExportLSDynaResults`` object with provided parameters.

    Examples
    --------
    >>> export_lsdyna_results = prime.ExportLSDynaResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            summary_log: str,
            zone_mesh_results: List[ZoneMeshResult],
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._summary_log = summary_log
        self._zone_mesh_results = zone_mesh_results
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            summary_log: str = None,
            zone_mesh_results: List[ZoneMeshResult] = None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ExportLSDynaResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ExportLSDynaResults`` object with default parameters.
        summary_log: str, optional
            Summary log for the import operation in json format.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        zone_mesh_results: List[ZoneMeshResult], optional
            Zone-wise mesh information for elements in the exported model.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ExportLSDynaResults`` object with provided parameters.

        Examples
        --------
        >>> export_lsdyna_results = prime.ExportLSDynaResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["summaryLog"] if "summaryLog" in json_data else None,
                [ZoneMeshResult(model = model, json_data = data) for data in json_data["zoneMeshResults"]] if "zoneMeshResults" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [summary_log, zone_mesh_results, error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    summary_log,
                    zone_mesh_results,
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ExportLSDynaResults")
                    json_data = param_json["ExportLSDynaResults"] if "ExportLSDynaResults" in param_json else {}
                    self.__initialize(
                        summary_log if summary_log is not None else ( ExportLSDynaResults._default_params["summary_log"] if "summary_log" in ExportLSDynaResults._default_params else (json_data["summaryLog"] if "summaryLog" in json_data else None)),
                        zone_mesh_results if zone_mesh_results is not None else ( ExportLSDynaResults._default_params["zone_mesh_results"] if "zone_mesh_results" in ExportLSDynaResults._default_params else [ZoneMeshResult(model = model, json_data = data) for data in (json_data["zoneMeshResults"] if "zoneMeshResults" in json_data else None)]),
                        error_code if error_code is not None else ( ExportLSDynaResults._default_params["error_code"] if "error_code" in ExportLSDynaResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( ExportLSDynaResults._default_params["warning_codes"] if "warning_codes" in ExportLSDynaResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            summary_log: str = None,
            zone_mesh_results: List[ZoneMeshResult] = None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of the ``ExportLSDynaResults`` object.

        Parameters
        ----------
        summary_log: str, optional
            Summary log for the import operation in json format.
        zone_mesh_results: List[ZoneMeshResult], optional
            Zone-wise mesh information for elements in the exported model.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        """
        args = locals()
        [ExportLSDynaResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ExportLSDynaResults`` object.

        Examples
        --------
        >>> ExportLSDynaResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportLSDynaResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._summary_log is not None:
            json_data["summaryLog"] = self._summary_log
        if self._zone_mesh_results is not None:
            json_data["zoneMeshResults"] = [data._jsonify() for data in self._zone_mesh_results]
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "summary_log :  %s\nzone_mesh_results :  %s\nerror_code :  %s\nwarning_codes :  %s" % (self._summary_log, '[' + ''.join('\n' + str(data) for data in self._zone_mesh_results) + ']', self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def summary_log(self) -> str:
        """Summary log for the import operation in json format.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._summary_log

    @summary_log.setter
    def summary_log(self, value: str):
        self._summary_log = value

    @property
    def zone_mesh_results(self) -> List[ZoneMeshResult]:
        """Zone-wise mesh information for elements in the exported model.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._zone_mesh_results

    @zone_mesh_results.setter
    def zone_mesh_results(self, value: List[ZoneMeshResult]):
        self._zone_mesh_results = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with failure of operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class ExportLSDynaIGAResults(CoreObject):
    """Results associated with the LS-DYNA export.

    Parameters
    ----------
    model: Model
        Model to create a ``ExportLSDynaIGAResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code associated with failure of operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    warning_codes: List[WarningCode], optional
        Warning codes associated with the operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ExportLSDynaIGAResults`` object with provided parameters.

    Examples
    --------
    >>> export_lsdyna_igaesults = prime.ExportLSDynaIGAResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ExportLSDynaIGAResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ExportLSDynaIGAResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ExportLSDynaIGAResults`` object with provided parameters.

        Examples
        --------
        >>> export_lsdyna_igaesults = prime.ExportLSDynaIGAResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ExportLSDynaIGAResults")
                    json_data = param_json["ExportLSDynaIGAResults"] if "ExportLSDynaIGAResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( ExportLSDynaIGAResults._default_params["error_code"] if "error_code" in ExportLSDynaIGAResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( ExportLSDynaIGAResults._default_params["warning_codes"] if "warning_codes" in ExportLSDynaIGAResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of the ``ExportLSDynaIGAResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        """
        args = locals()
        [ExportLSDynaIGAResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ExportLSDynaIGAResults`` object.

        Examples
        --------
        >>> ExportLSDynaIGAResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportLSDynaIGAResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with failure of operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class ExportLSDynaIgaKeywordFileParams(CoreObject):
    """Parameters for exporting LS-DYNA IGA keyword file.

    Parameters
    ----------
    model: Model
        Model to create a ``ExportLSDynaIgaKeywordFileParams`` object with default parameters.
    json_data: dict, optional
        JSON dictionary to create a ``ExportLSDynaIgaKeywordFileParams`` object with provided parameters.

    Examples
    --------
    >>> export_lsdyna_iga_keyword_file_params = prime.ExportLSDynaIgaKeywordFileParams(model = model)
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
        """Initialize a ``ExportLSDynaIgaKeywordFileParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ExportLSDynaIgaKeywordFileParams`` object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a ``ExportLSDynaIgaKeywordFileParams`` object with provided parameters.

        Examples
        --------
        >>> export_lsdyna_iga_keyword_file_params = prime.ExportLSDynaIgaKeywordFileParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "ExportLSDynaIgaKeywordFileParams")
                    json_data = param_json["ExportLSDynaIgaKeywordFileParams"] if "ExportLSDynaIgaKeywordFileParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of the ``ExportLSDynaIgaKeywordFileParams`` object.

        """
        args = locals()
        [ExportLSDynaIgaKeywordFileParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ExportLSDynaIgaKeywordFileParams`` object.

        Examples
        --------
        >>> ExportLSDynaIgaKeywordFileParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ExportLSDynaIgaKeywordFileParams._default_params.items())
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

class ExportBoundaryFittedSplineParams(CoreObject):
    """Parameters for exporting boundary fitted splines.

    Parameters
    ----------
    model: Model
        Model to create a ``ExportBoundaryFittedSplineParams`` object with default parameters.
    id_offset: int, optional
        Offset value for IGA entity ids between parts.
    id_start: int, optional
        Start ids for IGA entities.
    json_data: dict, optional
        JSON dictionary to create a ``ExportBoundaryFittedSplineParams`` object with provided parameters.

    Examples
    --------
    >>> export_boundary_fitted_spline_params = prime.ExportBoundaryFittedSplineParams(model = model)
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
        """Initialize a ``ExportBoundaryFittedSplineParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ExportBoundaryFittedSplineParams`` object with default parameters.
        id_offset: int, optional
            Offset value for IGA entity ids between parts.
        id_start: int, optional
            Start ids for IGA entities.
        json_data: dict, optional
            JSON dictionary to create a ``ExportBoundaryFittedSplineParams`` object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
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
        """Set the default values of the ``ExportBoundaryFittedSplineParams`` object.

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
        """Print the default values of ``ExportBoundaryFittedSplineParams`` object.

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

class ImportAbaqusParams(CoreObject):
    """Parameters for importing Abaqus solver input files.

    Parameters
    ----------
    model: Model
        Model to create a ``ImportAbaqusParams`` object with default parameters.
    json_data: dict, optional
        JSON dictionary to create a ``ImportAbaqusParams`` object with provided parameters.

    Examples
    --------
    >>> import_abaqus_params = prime.ImportAbaqusParams(model = model)
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
        """Initialize a ``ImportAbaqusParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ImportAbaqusParams`` object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a ``ImportAbaqusParams`` object with provided parameters.

        Examples
        --------
        >>> import_abaqus_params = prime.ImportAbaqusParams(model = model)
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
                    param_json = model._communicator.initialize_params(model, "ImportAbaqusParams")
                    json_data = param_json["ImportAbaqusParams"] if "ImportAbaqusParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of the ``ImportAbaqusParams`` object.

        """
        args = locals()
        [ImportAbaqusParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ImportAbaqusParams`` object.

        Examples
        --------
        >>> ImportAbaqusParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ImportAbaqusParams._default_params.items())
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

class ImportAbaqusResults(CoreObject):
    """Results of Abaqus import operation.

    Parameters
    ----------
    model: Model
        Model to create a ``ImportAbaqusResults`` object with default parameters.
    summary_log: str, optional
        Summary log for the import operation in json format.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    error_code: ErrorCode, optional
        Error code associated with failure of operation.
    warning_codes: List[WarningCode], optional
        Warning codes associated with Abaqus import operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ImportAbaqusResults`` object with provided parameters.

    Examples
    --------
    >>> import_abaqus_results = prime.ImportAbaqusResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            summary_log: str,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._summary_log = summary_log
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            summary_log: str = None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ImportAbaqusResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ImportAbaqusResults`` object with default parameters.
        summary_log: str, optional
            Summary log for the import operation in json format.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with Abaqus import operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ImportAbaqusResults`` object with provided parameters.

        Examples
        --------
        >>> import_abaqus_results = prime.ImportAbaqusResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["summaryLog"] if "summaryLog" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [summary_log, error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    summary_log,
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ImportAbaqusResults")
                    json_data = param_json["ImportAbaqusResults"] if "ImportAbaqusResults" in param_json else {}
                    self.__initialize(
                        summary_log if summary_log is not None else ( ImportAbaqusResults._default_params["summary_log"] if "summary_log" in ImportAbaqusResults._default_params else (json_data["summaryLog"] if "summaryLog" in json_data else None)),
                        error_code if error_code is not None else ( ImportAbaqusResults._default_params["error_code"] if "error_code" in ImportAbaqusResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( ImportAbaqusResults._default_params["warning_codes"] if "warning_codes" in ImportAbaqusResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            summary_log: str = None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of the ``ImportAbaqusResults`` object.

        Parameters
        ----------
        summary_log: str, optional
            Summary log for the import operation in json format.
        error_code: ErrorCode, optional
            Error code associated with failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with Abaqus import operation.
        """
        args = locals()
        [ImportAbaqusResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ImportAbaqusResults`` object.

        Examples
        --------
        >>> ImportAbaqusResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ImportAbaqusResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._summary_log is not None:
            json_data["summaryLog"] = self._summary_log
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "summary_log :  %s\nerror_code :  %s\nwarning_codes :  %s" % (self._summary_log, self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def summary_log(self) -> str:
        """Summary log for the import operation in json format.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._summary_log

    @summary_log.setter
    def summary_log(self, value: str):
        self._summary_log = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with Abaqus import operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value
