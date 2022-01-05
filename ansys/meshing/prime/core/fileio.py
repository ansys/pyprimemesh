from ansys.meshing.prime.autogen.fileio import FileIO as _FileIO
from ansys.meshing.prime.autogen.fileiostructs import FileReadResults
from ansys.meshing.prime.core.model import Model

from ansys.meshing.prime.params.primestructs import *

class FileIO(_FileIO):
    __doc__ = _FileIO.__doc__
    def __init__(self, model):
        """ __init__(FileIO self, Model model)"""
        self._model = model
        _FileIO.__init__(self, model)
    
    def read_pmdat(self, file_name) -> FileReadResults:
        """Function that reads PRIME's database file.

        Read PRIME's database file from disk.
        PRIME's database files have pmdat extension.
        Unicode paths are not currently supported by this API.

        Parameters 
        ---------- 
        file_name : str
             Path to file on disk.

        Returns 
        -------
        FileReadResults
             Returns FileReadResults.

        Examples 
        --------
        
        >>> from ansys.meshing.prime import FileIO
        >>> #connect client to server and get model from it
        >>> client = Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = FileIO(model = model)
        >>> results = file_io.read_pmdat("/tmp/my_prime_database.pmdat")

        """
        result = _FileIO.read_pmdat(self, file_name)
        if (result.error_code == ErrorCode.NOERROR):
            self._model._sync_up_model()
        return result
