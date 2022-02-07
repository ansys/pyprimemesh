""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

class FileIO(CoreObject):
    """Handles reading or writing files from the disk.

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize FileIO """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::FileIO/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for FileIO. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for FileIO. """
        command_name = "PrimeMesh::FileIO/Destruct"
        self._comm.serve(command_name, self._object_id, args={})

    def read_pmdat(self, file_name : str) -> FileReadResults:
        """ Function that reads PRIME's database file.

        Read PRIME's database file from disk.
        PRIME's database files have pmdat extension.
        Unicode paths are not currently supported by this API

        Parameters
        ----------
        file_name : str
            Path to file on disk

        Returns
        -------
        FileReadResults
            Returns FileReadResults

        Examples
        --------
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
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("read_pmdat", FileReadResults(model = self._model, json_data = result))
        return FileReadResults(model = self._model, json_data = result)

    def read_size_field(self, file_name : str) -> FileReadResults:
        """ Reads PRIME's sizefield file from disk.

        PRIME's sizefield files have sf and sf.gz extension.

        Parameters
        ----------
        file_name : str
            Path to file on disk

        Returns
        -------
        FileReadResults
            Returns the FileReadResults.


        Notes
        -----
        Unicode paths are not currently supported by this API.

        Examples
        --------
        >>> file_io = prime.FileIO(model = model)
        >>> results = file_io.read_size_field("/tmp/my_prime_sizefield.sf")

        """
        args = {"file_name" : file_name}
        command_name = "PrimeMesh::FileIO/ReadSizeField"
        self._model._print_logs_before_command("read_size_field", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("read_size_field", FileReadResults(model = self._model, json_data = result))
        return FileReadResults(model = self._model, json_data = result)

    def write_size_field(self, file_name : str) -> FileWriteResults:
        """ Writes PRIME's sizefield to file.


        Parameters
        ----------
        file_name : str
            Path to file on disk.

        Returns
        -------
        FileWriteResults
            Returns the FileWriteResults.


        Notes
        -----
        Unicode paths are not currently supported by this API.

        Examples
        --------
        >>> file_io = prime.FileIO(model = model)
        >>> results = file_io.write_size_field("/tmp/my_prime_sizefield.sf")

        """
        args = {"file_name" : file_name}
        command_name = "PrimeMesh::FileIO/WriteSizeField"
        self._model._print_logs_before_command("write_size_field", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("write_size_field", FileWriteResults(model = self._model, json_data = result))
        return FileWriteResults(model = self._model, json_data = result)

    def export_boundary_fitted_spline_kfile(self, file_name : str, export_params : ExportBoundaryFittedSplineParams) -> FileWriteResults:
        """ Export IGA LS-DYNA Keyword file for boundary fitted spline.


        Parameters
        ----------
        file_name : str
            Name of the file.
        export_params : ExportBoundaryFittedSplineParams
            Parameters for IGA LS-DYNA Keyword file export.

        Returns
        -------
        FileWriteResults
            Returns FileWriteResults.

        Examples
        --------
        >>> from ansys.meshing.prime import FileIO
        >>> #connect client to server and get model from it
        >>> client = Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = FileIO(model = model)
        >>> results = file_io.export_boundary_fitted_spline_k_file(file_name, export_params)

        """
        args = {"file_name" : file_name,
        "export_params" : export_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ExportBoundaryFittedSplineKFile"
        self._model._print_logs_before_command("export_boundary_fitted_spline_kfile", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("export_boundary_fitted_spline_kfile", FileWriteResults(model = self._model, json_data = result))
        return FileWriteResults(model = self._model, json_data = result)
