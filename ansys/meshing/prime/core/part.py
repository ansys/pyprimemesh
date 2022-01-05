from ansys.meshing.prime.autogen.model import Model
from ansys.meshing.prime.autogen.part import Part as _Part
from ansys.meshing.prime.autogen.partstructs import *

from typing import KeysView, List
import json

class Part(_Part):
    __doc__ = _Part.__doc__

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """Initialize Part 

        Parameters
        ----------
        model: ansys.meshing.prime.Model
            Model in which part is created
        id: int
            Id of the part provided by server
        object_id: int
            Object id provided by the server
        name: str
            Part name
        """
        self._model = model
        self._print_mesh = False
        self._print_id = False
        _Part.__init__(self, model, id, object_id, name)

    def __call__(self, *args: Any, **kwds: Any) -> str:
        """Callable interface of the Part. 

        Gets summary of the part using supported keyword arguments as given below.            

        Parameters 
        ----------  
        print_mesh : bool, optional
            print_mesh pass True will get the mesh summary along with part summary. The default is False. 
        peint_id : bool, optional
            print_id pass True will get id's of topo entities/zonelets along with part summary. The default is False.
        
        Returns
        -------
        str
            Returns the summary of part.

        Examples
        --------
        >>> from ansys.meshing.prime import local_model
        >>> model = local_model()
        >>> part = model.get_part_by_name("Part.1")
        >>> print(part(print_mesh=True, print_id=True))
        """
        params = PartSummaryParams(model=self._model, 
        print_id=self._print_id,
        print_mesh=self._print_mesh)
        for key, value in kwds.items():
            setattr(params, key, value)
            if(key == 'print_mesh'):
                params.print_mesh = value
            if(key == 'print_id'):
                params.print_id = value
        result = _Part.get_summary(self, params)
        return result.message
    
    def __str__(self) -> str:
        """Prints the summary of a part. 

        Uses print_mesh and print_id properties to control the the summary of a part.            

        Returns 
        -------
        str
            Returns the summary of a part.

        Examples 
        -------- 
        >>> from ansys.meshing.prime import local_model
        >>> model = local_model()
        >>> part = model.get_part_by_name("Part.1")
        >>> print(part)
        """
        params = PartSummaryParams(model=self._model)
        params.print_mesh = self._print_mesh
        params.print_id = self._print_id
        result = _Part.get_summary(self, params)
        return result.message
    
    @property
    def print_mesh(self) ->bool:
        """True will get the mesh summary along with part summary. The default is False. """
        return self._print_mesh
    
    @print_mesh.setter
    def print_mesh(self, value:bool):
        self._print_mesh = value

    @property
    def print_id(self) ->bool:
        """True will get id's of topo entities/zonelets along with part summary. The default is False. """
        return self._print_id
    
    @print_id.setter
    def print_id(self, value:bool):
        self._print_id = value

