""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

class FileIO(CoreObject):
    """ 
     Handles reading/writing files

    Description 
    ----------- 
    Contains methods to read/write files from disk
    """ 

    def __init__(self, model: CommunicationManager):
        """ Initialize FileIO """
        self._model = model
        self._comm = model.communicator
        command_name = "PrimeMesh::FileIO/Construct"
        args = {"ModelID" : model.object_id , "MaxID" : -1 }
        result = self._comm.serve(command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()
    
    def __enter__(self):
        """ Enter context for FileIO """
        return self
    
    def __exit__(self, type, value, traceback) :
        """ Exit context for FileIO """
        command_name = "PrimeMesh::FileIO/Destruct"
        self._comm.serve(command_name, self.object_id, args={})
    
    def read_pmdat(self, file_name : str) -> FileReadResults:
        """  Function that reads PRIME's database file.

        Description 
        ----------- 
        Read PRIME's database file from disk.
        PRIME's database files have pmdat extension.
        Unicode paths are not currently supported by this API

        Parameters 
        ---------- 
        file_name : str
             Path to file on disk

        Return 
        ------ 
        FileReadResults
             Returns FileReadResults

        Example 
        ------- 
        
        >>> from ansys.meshing.prime import FileIO
        >>> #connect client to server and get model from it
        >>> client = Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = FileIO(model = model)
        >>> results = file_io.read_pmdat("/tmp/my_prime_database.pmdat")

        """
        args = {"file_name" : file_name}
        command_name = "PrimeMesh::FileIO/ReadPMDAT"
        self._model._print_logs_before_command("read_pmdat", args)
        result = self._comm.serve(command_name, self.object_id, args=args)
        self._model._print_logs_after_command("read_pmdat", FileReadResults(model = self._model, json_data = result))
        return FileReadResults(model = self._model, json_data = result)
    
    @property
    def object_id(self):
        """ Object id of FileIO """
        return self._object_id
    
