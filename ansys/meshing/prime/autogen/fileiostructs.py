""" Auto-generated file. DO NOT MODIFY """
import enum
import logging
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *

from ansys.meshing.prime.params.primestructs import *



class FileReadResults(CoreObject):
    """ 
      Results of file read.

    """ 
    default_params = {}
    def __initialize(
        self,
        error_code : ErrorCode):
        self._error_code = error_code
    
    def __init__(
        self,
        model: CommunicationManager=None,
        error_code : ErrorCode = None,
        json_data : dict = None,
         **kwargs):
        """ 
        Initializes FileReadResults

        Parameters 
        ---------- 
        model : CommunicationManager 
            CommunicationManager to create a FileReadResults object with default parameters.
        error_code : ErrorCode, optional
             Appropriate error code is set if the read was unsuccessful. 
        json_data : dict, optional 
            JSON dictionary to create a FileReadResults object with provided parameters.

        Examples 
        ------- 
        >>> file_read_results = FileReadResults(model = model)
        """ 
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"]))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model.communicator.initialize_params("FileReadResults")["FileReadResults"]
                    self.__initialize(
                        error_code if error_code is not None else ( FileReadResults.default_params["error_code"] if "error_code" in FileReadResults.default_params else ErrorCode(json_data["errorCode"])))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()
    
    @staticmethod
    def set_default(
        error_code : ErrorCode = None):
        args = locals()
        [FileReadResults.default_params.update({ key: value }) for key, value in args.items() if value is not None]
    
    @staticmethod
    def print_default():
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in FileReadResults.default_params.items())
        print(message)
    
    def jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data
    
    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key,value in self._custom_params.items())
        return message
    
    @property
    def error_code(self) -> ErrorCode:
        """ 
         Appropriate error code is set if the read was unsuccessful. 

        """ 
        return self._error_code
    
    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
    
    

