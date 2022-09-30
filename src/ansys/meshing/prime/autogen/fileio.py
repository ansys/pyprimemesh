""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class FileIO(CoreObject):
    """Handles reading or writing files from the disk.

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize FileIO """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::FileIO/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for FileIO. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for FileIO. """
        command_name = "PrimeMesh::FileIO/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def read_pmdat(self, file_name : str, file_read_params : FileReadParams) -> FileReadResults:
        """ Function that reads PRIME's database file.

        PRIME's database files have pmdat extension.

        Parameters
        ----------
        file_name : str
            Path to file on disk.
        file_read_params : FileReadParams
            Parameter to read a file.

        Returns
        -------
        FileReadResults
            Returns FileReadResults.


        Notes
        -----
        This API does not support Unicode paths now.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> #connect client to server and get model from it
        >>> client = prime.Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = prime.FileIO(model = model)
        >>> file_read_params = prime.FileReadParams(model = model)
        >>> results = file_io.read_pmdat("/tmp/file.pmdat", file_read_params)

        """
        args = {"file_name" : file_name,
        "file_read_params" : file_read_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ReadPMDAT"
        self._model._print_logs_before_command("read_pmdat", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("read_pmdat", FileReadResults(model = self._model, json_data = result))
        return FileReadResults(model = self._model, json_data = result)

    def write_pmdat(self, file_name : str, file_write_params : FileWriteParams) -> FileWriteResults:
        """ Writes Prime mesh data file. Prime mesh data files have .pmdat extension.


        Parameters
        ----------
        file_name : str
            Path to write file on disk.
        file_write_params : FileWriteParams
            Parameters to write Prime mesh data file.

        Returns
        -------
        FileWriteResults
            Returns the FileWriteResults structure.


        Examples
        --------
        >>> results = file_io.write_pmdat("/tmp/prime_mesh_data.pmdat", prime.FileWriteParams(model = model))

        """
        args = {"file_name" : file_name,
        "file_write_params" : file_write_params._jsonify()}
        command_name = "PrimeMesh::FileIO/WritePMDAT"
        self._model._print_logs_before_command("write_pmdat", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("write_pmdat", FileWriteResults(model = self._model, json_data = result))
        return FileWriteResults(model = self._model, json_data = result)

    def import_fluent_meshing_size_field(self, file_name : str) -> SizeFieldFileReadResults:
        """ Import Fluent-Meshing's sizefield file from disk.

        Fluent-Meshing's sizefield files have sf and sf.gz extension.

        Parameters
        ----------
        file_name : str
            Path to file on disk

        Returns
        -------
        SizeFieldFileReadResults
            Return the SizeFieldFileReadResults.


        Notes
        -----
        This API does not support Unicode paths now.

        Examples
        --------
        >>> file_io = prime.FileIO(model = model)
        >>> results = file_io.import_fluent_meshing_size_field("/tmp/my_sizefield.sf")

        """
        args = {"file_name" : file_name}
        command_name = "PrimeMesh::FileIO/ImportFluentMeshingSizeField"
        self._model._print_logs_before_command("import_fluent_meshing_size_field", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("import_fluent_meshing_size_field", SizeFieldFileReadResults(model = self._model, json_data = result))
        return SizeFieldFileReadResults(model = self._model, json_data = result)

    def read_size_field(self, file_name : str, params : ReadSizeFieldParams) -> SizeFieldFileReadResults:
        """ Read PRIME's sizefield file from disk.

        PRIME's sizefield files have psf and psf.gz extension.

        Parameters
        ----------
        file_name : str
            Path to file on disk.
        params : ReadSizeFieldParams
            Parameters to read size field file.

        Returns
        -------
        SizeFieldFileReadResults
            Return the SizeFieldFileReadResults.


        Notes
        -----
        This API does not support Unicode paths now.

        Examples
        --------
        >>> file_io = prime.FileIO(model = model)
        >>> params = prime.ReadSizeFieldParams(model = model)
        >>> results = file_io.read_size_field("/tmp/my_prime_sizefield.psf", params)

        """
        args = {"file_name" : file_name,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::FileIO/ReadSizeField"
        self._model._print_logs_before_command("read_size_field", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("read_size_field", SizeFieldFileReadResults(model = self._model, json_data = result))
        return SizeFieldFileReadResults(model = self._model, json_data = result)

    def write_size_field(self, file_name : str, params : WriteSizeFieldParams) -> FileWriteResults:
        """ Write PRIME's sizefield (.psf) to file.


        Parameters
        ----------
        file_name : str
            Path to file on disk.
        params : WriteSizeFieldParams
            Parameters to write size field file.

        Returns
        -------
        FileWriteResults
            Return the FileWriteResults.


        Notes
        -----
        This API does not support Unicode paths now.

        Examples
        --------
        >>> file_io = prime.FileIO(model = model)
        >>> params = prime.WriteSizeFieldParams(model = model)
        >>> results = file_io.write_size_field("/tmp/my_prime_sizefield.psf", params)

        """
        args = {"file_name" : file_name,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::FileIO/WriteSizeField"
        self._model._print_logs_before_command("write_size_field", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("write_size_field", FileWriteResults(model = self._model, json_data = result))
        return FileWriteResults(model = self._model, json_data = result)

    def import_mapdl_cdb(self, file_name : str, params : ImportMapdlCdbParams) -> ImportMapdlCdbResults:
        """ Function that imports MAPDL CDB file(cdb).


        Parameters
        ----------
        file_name : str
            Path to file on disk.
        params : ImportMapdlCdbParams
            Parameter to import a CDB file.

        Returns
        -------
        ImportMapdlCdbResults
            Returns ImportMapdlCdbResults.


        Notes
        -----
        This API does not support Unicode paths now.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> #connect client to server and get model from it
        >>> client = prime.Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = prime.FileIO(model = model)
        >>> params = prime.ImportMapdlCdbParams(model = model)
        >>> results = file_io.import_mapdl_cdb("/tmp/file.cdb", params)

        """
        args = {"file_name" : file_name,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::FileIO/ImportMapdlCdb"
        self._model._print_logs_before_command("import_mapdl_cdb", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("import_mapdl_cdb", ImportMapdlCdbResults(model = self._model, json_data = result))
        return ImportMapdlCdbResults(model = self._model, json_data = result)

    def export_mapdl_cdb(self, file_name : str, params : ExportMapdlCdbParams) -> ExportMapdlCdbResults:
        """ Function that exports MAPDL CDB file(cdb).


        Parameters
        ----------
        file_name : str
            Path to file on disk.
        params : ExportMapdlCdbParams
            Parameter to export a CDB file.

        Returns
        -------
        ExportMapdlCdbResults
            Returns ExportMapdlCdbResults.


        Notes
        -----
        This API does not support Unicode paths now.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> #connect client to server and get model from it
        >>> client = prime.Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = prime.FileIO(model = model)
        >>> params = prime.ExportMapdlCdbParams(model = model)
        >>> results = file_io.export_mapdl_cdb("/tmp/file.cdb", params)

        """
        args = {"file_name" : file_name,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::FileIO/ExportMapdlCdb"
        self._model._print_logs_before_command("export_mapdl_cdb", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("export_mapdl_cdb", ExportMapdlCdbResults(model = self._model, json_data = result))
        return ExportMapdlCdbResults(model = self._model, json_data = result)

    def import_fluent_meshing_meshes(self, file_names : List[str], import_fluent_meshing_mesh_params : ImportFluentMeshingMeshParams) -> ImportFluentMeshingMeshResults:
        """ Imports fluent meshing meshes of given files on disk.

        Fluent Meshing mesh files have msh and msh.gz extension.

        Parameters
        ----------
        file_names : List[str]
            Full path of files to be imported.
        import_fluent_meshing_mesh_params : ImportFluentMeshingMeshParams
            Parameters to import fluent meshing mesh.

        Returns
        -------
        ImportFluentMeshingMeshResults
            Returns the FileReadResults.


        Notes
        -----
        This API does not support Unicode paths now.

        Examples
        --------
        >>> file_io = prime.FileIO(model = model)
        >>> params = prime.ImportFluentMeshingMeshParams(model = model)
        >>> results = file_io.import_fluent_meshing_meshes(["/tmp/mesh.msh", "/tmp/mesh1.msh"], params)

        """
        args = {"file_names" : file_names,
        "import_fluent_meshing_mesh_params" : import_fluent_meshing_mesh_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ImportFluentMeshingMeshes"
        self._model._print_logs_before_command("import_fluent_meshing_meshes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("import_fluent_meshing_meshes", ImportFluentMeshingMeshResults(model = self._model, json_data = result))
        return ImportFluentMeshingMeshResults(model = self._model, json_data = result)

    def import_fluent_case(self, file_name : str, import_fluent_case_params : ImportFluentCaseParams) -> ImportFluentCaseResults:
        """ Imports fluent case file on disk.

        Fluent case files have cas extension.

        Parameters
        ----------
        file_name : str
            Path to file on disk.
        import_fluent_case_params : ImportFluentCaseParams
            Parameters to import fluent case file.

        Returns
        -------
        ImportFluentCaseResults
            Returns the ImportFluentCaseResults.


        Notes
        -----
        This API does not support unicode paths now.

        Examples
        --------
        >>> file_io = prime.FileIO(model = model)
        >>> params = prime.ImportFluentCaseParams(model = model)
        >>> results = file_io.import_fluent_case("/tmp/fluent.cas", params)

        """
        args = {"file_name" : file_name,
        "import_fluent_case_params" : import_fluent_case_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ImportFluentCase"
        self._model._print_logs_before_command("import_fluent_case", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("import_fluent_case", ImportFluentCaseResults(model = self._model, json_data = result))
        return ImportFluentCaseResults(model = self._model, json_data = result)

    def export_fluent_case(self, file_name : str, export_fluent_case_params : ExportFluentCaseParams) -> FileWriteResults:
        """ Exports Fluent case file. Fluent case files have cas extension.


        Parameters
        ----------
        file_name : str
            Path to file on disk.
        export_fluent_case_params : ExportFluentCaseParams
            Parameters to export fluent case file.

        Returns
        -------
        FileWriteResults
            Returns the FileWriteResults structure.


        Examples
        --------
        >>> file_io = FileIO(model = model)
        >>> results = file_io.export_fluent_case("/tmp/fluent.cas", prime.ExportFluentCaseParams(model = model))

        """
        args = {"file_name" : file_name,
        "export_fluent_case_params" : export_fluent_case_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ExportFluentCase"
        self._model._print_logs_before_command("export_fluent_case", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("export_fluent_case", FileWriteResults(model = self._model, json_data = result))
        return FileWriteResults(model = self._model, json_data = result)

    def export_fluent_meshing_mesh(self, file_name : str, export_fluent_mesh_params : ExportFluentMeshingMeshParams) -> FileWriteResults:
        """ Export Fluent Meshing mesh file. Fluent Meshing mesh files have .msh extension.


        Parameters
        ----------
        file_name : str
            Path to file on disk.
        export_fluent_mesh_params : ExportFluentMeshingMeshParams
            Parameters to export Fluent Meshing mesh file.

        Returns
        -------
        FileWriteResults
            Returns the FileWriteResults structure.


        Examples
        --------
        >>> results = file_io.export_fluent_meshing_mesh("/tmp/fluent_meshing.msh", ExportFluentMeshingMeshParams(model = model))

        """
        args = {"file_name" : file_name,
        "export_fluent_mesh_params" : export_fluent_mesh_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ExportFluentMeshingMesh"
        self._model._print_logs_before_command("export_fluent_meshing_mesh", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("export_fluent_meshing_mesh", FileWriteResults(model = self._model, json_data = result))
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
        >>> results = file_io.export_boundary_fitted_spline_k_file(file_name, ExportBoundaryFittedSplineParams(model = model))

        """
        args = {"file_name" : file_name,
        "export_params" : export_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ExportBoundaryFittedSplineKFile"
        self._model._print_logs_before_command("export_boundary_fitted_spline_kfile", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("export_boundary_fitted_spline_kfile", FileWriteResults(model = self._model, json_data = result))
        return FileWriteResults(model = self._model, json_data = result)

    def import_cad(self, file_name : str, import_cad_params : ImportCadParams) -> ImportCadResults:
        """ Imports CAD file from disk.


        Parameters
        ----------
        file_name : str
            Path to file on disk.
        import_cad_params : ImportCadParams
            Parameters to control CAD import options.

        Returns
        -------
        ImportCadResults
            Returns the ImportCadResults.


        Notes
        -----
        This API does not support Unicode paths now.

        Examples
        --------
        >>> file_io = prime.FileIO(model = model)
        >>> params = prime.ImportCadParams(model = model)
        >>> results = file_io.import_cad(file_name="/tmp/my_cad.x_t", import_cad_params=params)

        """
        args = {"file_name" : file_name,
        "import_cad_params" : import_cad_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ImportCAD"
        self._model._print_logs_before_command("import_cad", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("import_cad", ImportCadResults(model = self._model, json_data = result))
        return ImportCadResults(model = self._model, json_data = result)
