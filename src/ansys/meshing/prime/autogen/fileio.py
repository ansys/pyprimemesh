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
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class FileIO(CoreObject):
    """Handles reading or writing files from the disk.

    Parameters
    ----------
    model : Model
        Server model to create FileIO object.
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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(file_read_params, FileReadParams):
            raise TypeError("Invalid argument type passed for 'file_read_params'. Valid argument type is FileReadParams.")
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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(file_write_params, FileWriteParams):
            raise TypeError("Invalid argument type passed for 'file_write_params'. Valid argument type is FileWriteParams.")
        args = {"file_name" : file_name,
        "file_write_params" : file_write_params._jsonify()}
        command_name = "PrimeMesh::FileIO/WritePMDAT"
        self._model._print_logs_before_command("write_pmdat", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("write_pmdat", FileWriteResults(model = self._model, json_data = result))
        return FileWriteResults(model = self._model, json_data = result)

    def get_abaqus_simulation_data(self, partId : int) -> str:
        """ Gets simulation document generated by Abaqus import for a given part.

        This method will return the JSON Simulation Document for a part if the part exists. Otherwise,
        it returns an empty string.

        Parameters
        ----------
        partId : int
            Part Id.

        Returns
        -------
        str
            Returns the string containing a JSON document for simulation data.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> import json
        >>> simdata = json.loads(file_io.get_abaqus_simulation_data(2)

        """
        if not isinstance(partId, int):
            raise TypeError("Invalid argument type passed for 'partId'. Valid argument type is int.")
        args = {"partId" : partId}
        command_name = "PrimeMesh::FileIO/GetAbaqusSimulationData"
        self._model._print_beta_api_warning("get_abaqus_simulation_data")
        self._model._print_logs_before_command("get_abaqus_simulation_data", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_abaqus_simulation_data")
        return result

    def import_abaqus_inp(self, file_name : str, params : ImportAbaqusParams) -> ImportAbaqusResults:
        """ Import a Abaqus file.

        Import abaqus files as dead mesh and also store simulation-specific information into Prime in the form of JSON documents.

        Parameters
        ----------
        file_name : str
            Name of file to import.
        params : ImportAbaqusParams
            Parameters to specify options during import.

        Returns
        -------
        ImportAbaqusResults
            Returns the results of the abaqus database import.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = file_io.import_abaqus_inp(r"/tmp/file.inp")

        """
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(params, ImportAbaqusParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ImportAbaqusParams.")
        args = {"file_name" : file_name,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::FileIO/ImportAbaqusInp"
        self._model._print_beta_api_warning("import_abaqus_inp")
        self._model._print_logs_before_command("import_abaqus_inp", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("import_abaqus_inp", ImportAbaqusResults(model = self._model, json_data = result))
        return ImportAbaqusResults(model = self._model, json_data = result)

    def import_fluent_meshing_size_field(self, file_name : str) -> SizeFieldFileReadResults:
        """ Imports Fluent-Meshing's size field file from disk.

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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(params, ReadSizeFieldParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ReadSizeFieldParams.")
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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(params, WriteSizeFieldParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is WriteSizeFieldParams.")
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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(params, ImportMapdlCdbParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ImportMapdlCdbParams.")
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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(params, ExportMapdlCdbParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ExportMapdlCdbParams.")
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
        if not isinstance(file_names, List):
            raise TypeError("Invalid argument type passed for 'file_names'. Valid argument type is List[str].")
        if not isinstance(import_fluent_meshing_mesh_params, ImportFluentMeshingMeshParams):
            raise TypeError("Invalid argument type passed for 'import_fluent_meshing_mesh_params'. Valid argument type is ImportFluentMeshingMeshParams.")
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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(import_fluent_case_params, ImportFluentCaseParams):
            raise TypeError("Invalid argument type passed for 'import_fluent_case_params'. Valid argument type is ImportFluentCaseParams.")
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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(export_fluent_case_params, ExportFluentCaseParams):
            raise TypeError("Invalid argument type passed for 'export_fluent_case_params'. Valid argument type is ExportFluentCaseParams.")
        args = {"file_name" : file_name,
        "export_fluent_case_params" : export_fluent_case_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ExportFluentCase"
        self._model._print_logs_before_command("export_fluent_case", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("export_fluent_case", FileWriteResults(model = self._model, json_data = result))
        return FileWriteResults(model = self._model, json_data = result)

    def export_fluent_meshing_mesh(self, file_name : str, export_fluent_mesh_params : ExportFluentMeshingMeshParams) -> FileWriteResults:
        """ Exports Fluent Meshing mesh file. Fluent Meshing mesh files have .msh extension.


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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(export_fluent_mesh_params, ExportFluentMeshingMeshParams):
            raise TypeError("Invalid argument type passed for 'export_fluent_mesh_params'. Valid argument type is ExportFluentMeshingMeshParams.")
        args = {"file_name" : file_name,
        "export_fluent_mesh_params" : export_fluent_mesh_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ExportFluentMeshingMesh"
        self._model._print_logs_before_command("export_fluent_meshing_mesh", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("export_fluent_meshing_mesh", FileWriteResults(model = self._model, json_data = result))
        return FileWriteResults(model = self._model, json_data = result)

    def export_lsdyna_keyword_file(self, file_name : str, export_params : ExportLSDynaKeywordFileParams) -> ExportLSDynaResults:
        """ Export FEA LS-DYNA Keyword file for solid, surface mesh or both.


        Parameters
        ----------
        file_name : str
            Name of the file.
        export_params : ExportLSDynaKeywordFileParams
            Parameters for FEA LS-DYNA Keyword file export.

        Returns
        -------
        ExportLSDynaResults
            Returns FileWriteResults.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = file_io.export_lsdyna_keyword_file(file_name, ExportLSDynaKeywordFileParams(model = model))

        """
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(export_params, ExportLSDynaKeywordFileParams):
            raise TypeError("Invalid argument type passed for 'export_params'. Valid argument type is ExportLSDynaKeywordFileParams.")
        args = {"file_name" : file_name,
        "export_params" : export_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ExportLSDynaKeywordFile"
        self._model._print_beta_api_warning("export_lsdyna_keyword_file")
        self._model._print_logs_before_command("export_lsdyna_keyword_file", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("export_lsdyna_keyword_file", ExportLSDynaResults(model = self._model, json_data = result))
        return ExportLSDynaResults(model = self._model, json_data = result)

    def export_lsdyna_iga_keyword_file(self, file_name : str, export_params : ExportLSDynaIgaKeywordFileParams) -> ExportLSDynaIGAResults:
        """ Exports IGA LS-DYNA Keyword file for solid, surface splines, or both.


        Parameters
        ----------
        file_name : str
            Name of the file.
        export_params : ExportLSDynaIgaKeywordFileParams
            Parameters for IGA LS-DYNA Keyword file export.

        Returns
        -------
        ExportLSDynaIGAResults
            Returns FileWriteResults.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = file_io.export_lsdyna_iga_keyword_file(file_name, ExportLSDynaIgaKeywordFileParams(model = model))

        """
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(export_params, ExportLSDynaIgaKeywordFileParams):
            raise TypeError("Invalid argument type passed for 'export_params'. Valid argument type is ExportLSDynaIgaKeywordFileParams.")
        args = {"file_name" : file_name,
        "export_params" : export_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ExportLSDynaIgaKeywordFile"
        self._model._print_beta_api_warning("export_lsdyna_iga_keyword_file")
        self._model._print_logs_before_command("export_lsdyna_iga_keyword_file", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("export_lsdyna_iga_keyword_file", ExportLSDynaIGAResults(model = self._model, json_data = result))
        return ExportLSDynaIGAResults(model = self._model, json_data = result)

    def export_boundary_fitted_spline_kfile(self, file_name : str, export_params : ExportBoundaryFittedSplineParams) -> FileWriteResults:
        """ Exports IGA LS-DYNA Keyword file for boundary fitted spline.


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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(export_params, ExportBoundaryFittedSplineParams):
            raise TypeError("Invalid argument type passed for 'export_params'. Valid argument type is ExportBoundaryFittedSplineParams.")
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
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(import_cad_params, ImportCadParams):
            raise TypeError("Invalid argument type passed for 'import_cad_params'. Valid argument type is ImportCadParams.")
        args = {"file_name" : file_name,
        "import_cad_params" : import_cad_params._jsonify()}
        command_name = "PrimeMesh::FileIO/ImportCAD"
        self._model._print_logs_before_command("import_cad", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("import_cad", ImportCadResults(model = self._model, json_data = result))
        return ImportCadResults(model = self._model, json_data = result)

    def export_stl(self, file_name : str, params : ExportSTLParams) -> FileWriteResults:
        """ Exports STL file.


        Parameters
        ----------
        file_name : str
            Path to file on disk.
        params : ExportSTLParams
            Parameters for writing the file.

        Returns
        -------
        FileWriteResults
            Returns the FileWriteResults.


        Notes
        -----
        This API does not support Unicode paths now.

        Examples
        --------
        >>> fileio = prime.FileIO(model=model)
        >>> out_file_path = r"/tmp/output.stl"
        >>> part_ids = [part.id for part in model.parts]
        >>> export_stl_params=prime.ExportSTLParams(model=model,part_ids=part_ids)
        >>> results = fileio.export_stl(out_file_path,export_stl_params)

        """
        if not isinstance(file_name, str):
            raise TypeError("Invalid argument type passed for 'file_name'. Valid argument type is str.")
        if not isinstance(params, ExportSTLParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is ExportSTLParams.")
        args = {"file_name" : file_name,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::FileIO/ExportSTL"
        self._model._print_logs_before_command("export_stl", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("export_stl", FileWriteResults(model = self._model, json_data = result))
        return FileWriteResults(model = self._model, json_data = result)
