from ansys.meshing.prime.autogen.model import Model as _Model
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.internals.communicator import Communicator

from typing import List
import json

import logging

class Model( _Model ):

    """Proxy of C++ PrimeMesh::Model class."""
    def __init__(self, comm : Communicator , id : int, object_id : int, name : str):
        """ Initialize Model """
        _Model.__init__(self, comm, id, object_id, name)
        self._parts = []
        self._size_controls = []
        self._prism_controls = []
        self._default_part = None
        self._topo_data = None
        self._control_data = None
        self._material_point_data = None
        self._freeze()
    
    def _sync_up_model(self):
        """  Synchronizes client model with the server model. 

        Description 
        ----------- 
            Updates proxy child objects of the client model with the child objects of the server model.

        Parameters 
        ----------  

        Return 
        ------ 
        
        Example 
        ------- 
        >>> from ansys.meshing.prime import local_model
        >>> model = local_model()
        >>> model.sync_up_model()
        """
        res = json.loads(_Model.get_child_objects_json(self))
        part_data = res["Parts"]
        self._parts = [Part(self, part[0], part[1], part[2]) for part in part_data]
        # self._weld_controls = [WeldControl(self, wc[0], wc[1]) for wc in wc_data] # support prism controls here and remove weld control

    def get_parts(self) -> List[Part]:
        """  Gets the list of parts of a model. 

        Description 
        ----------- 
          Gets the list of proxy parts of a model.        

        Parameters 
        ---------- 

        Return 
        ------ 
        List[Part]
             Returns the list of parts. 
        
        Example 
        ------- 
            >>> from ansys.meshing.prime import local_model
            >>> model = local_model()
            >>> parts = model.get_parts()
        """
        return self._parts
        
    def get_part_by_name(self, name:str) -> Part:
        """  Gets the part by name. 

        Description 
        ----------- 
            Gets the part by name. Returns None if part doesn't exist for the given name.            

        Parameters 
        ---------- 
        name : str
            Name of the part. 

        Return 
        ------ 
        Part
            Returns the part. 
        
        Example 
        ------- 
            >>> from ansys.meshing.prime import local_model
            >>> model = local_model()
            >>> part = model.get_part_by_name("part.1")
        """
        for part in self._parts:
            if(part.name == name):
                return part
        return None
    
    def get_part(self, id : int) -> Part:
        """  Gets the part by id. 

        Description 
        ----------- 
            Gets the part by id. Returns None if part doesn't exist for the given id.            

        Parameters 
        ---------- 
        id : int
            Id of the part. 

        Return 
        ------ 
        Part
            Returns the part. 
        
        Example 
        ------- 
            >>> from ansys.meshing.prime import local_model
            >>> model = local_model()
            >>> part = model.get_part(2)
        """
        for part in self._parts:
            if(part.id == id):
                return part
        return None
    
    def __str__(self):
        """ Prints the summary of the model. 

        Description 
        ----------- 
            Prints the summary of the model.            

        Parameters 
        ----------
        
        Return 
        ------ 
        str
            Returns the summary of the model.

        Example 
        ------- 
        >>> from ansys.meshing.prime import local_model
        >>> model = local_model()
        >>> print(model)
        """
        result = ""
        result += "Part Summary:\n"
        for part in self._parts:
            result += part.__str__() + "\n"
        return result

    @property
    def python_logger(self):
        """Get PRIME's Logger instance

        PRIME's Logger instance can be used to control the verbosity
        of messages printed by PRIME

        Returns
        -------
        Logger
             Returns logging.Logger instance

        Examples
        --------
        Set log level to debug.

        >>> model.python_logger.setLevel(logging.DEBUG)

        """
        return self._logger
