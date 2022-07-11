# Copyright 2023 ANSYS, Inc.
# Unauthorized use, distribution, or duplication is prohibited.
from ansys.meshing.prime.autogen.fileio import FileIO as _FileIO
from ansys.meshing.prime.autogen.fileiostructs import (
    FileReadParams,
    FileReadResults,
    ImportCadParams,
    ImportCadResults,
    ImportFluentMeshingMeshParams,
    ImportFluentMeshingMeshResults,
    ImportFluentCaseParams,
    ImportFluentCaseResults,
    ImportMapdlCdbParams,
    ImportMapdlCdbResults,
)
from ansys.meshing.prime.core.model import Model
from typing import List

from ansys.meshing.prime.params.primestructs import ErrorCode


class FileIO(_FileIO):
    __doc__ = _FileIO.__doc__

    def __init__(self, model: Model):
        """__init__(FileIO self, Model model)"""
        self._model = model
        _FileIO.__init__(self, model)

    def read_pmdat(self, file_name: str, file_read_params: FileReadParams) -> FileReadResults:
        """Function that reads PRIME's database file.

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
        result = _FileIO.read_pmdat(self, file_name, file_read_params)
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result

    def import_cad(self, file_name: str, params: ImportCadParams) -> ImportCadResults:
        """Function that imports CAD file.

        Import CAD file from disk.

        Supported formats on Windows are:

        \*.scdoc \*.fmd \*.agdb \*.pmdb \*.meshdat \*.mechdat \*.dsdb \*.cmdb \*.dbs \*.sat
        \*.sab \*.dwg \*.dxf \*.model \*.exp \*.CATPart \*.CATProduct \*.cgr \*.3dxml \*.prt\*
        \*.asm\* \*.iges \*.igs \*.ipt \*.iam \*.jt \*.prt \*.x_t \*.x_b \*.par \*.psm \*.asm
        \*.sldprt \*.sldasm \*.step \*.stp \*.stl \*.plmxml \*.tgf

        Supported formats on Linux are:

        \*.fmd \*.agdb \*.pmdb \*.meshdat \*.mechdat \*.dsdb \*.cmdb \*.dbs \*.sat \*.sab
        \*.CATPart \*.CATProduct \*.iges \*.igs \*.ipt \*.iam \*.jt \*.x_t \*.x_b \*.step
        \*.stp \*.stl \*.plmxml \*.tgf

        Parameters
        ----------
        file_name : str
             Path to file on disk.

        params : ImportCadParams
             Parameters to control CAD import options

        Returns
        -------
        ImportCadResults
             Returns ImportCadResults.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> #connect client to server and get model from it
        >>> client = prime.Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = prime.FileIO(model = model)
        >>> params = ImportCadParams(model = model)
        >>> results = file_io.import_cad(file_name="/tmp/my_cad.x_t", params = params)

        """
        import_result = _FileIO.import_cad(self, file_name, params)
        if import_result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return import_result

    def import_fluent_meshing_meshes(
        self,
        file_names: List[str],
        import_fluent_meshing_mesh_params: ImportFluentMeshingMeshParams,
    ) -> ImportFluentMeshingMeshResults:
        """Imports fluent meshing meshes of given files on disk.

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
        >>> results = file_io.import_fluent_meshing_meshes(["/tmp/mesh.msh", "/tmp/mesh1.msh"],
                                                           params)

        """
        result = _FileIO.import_fluent_meshing_meshes(
            self, file_names, import_fluent_meshing_mesh_params
        )
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result

    def import_fluent_case(
        self, file_name: str, import_fluent_case_params: ImportFluentCaseParams
    ) -> ImportFluentCaseResults:
        """Imports fluent case file on disk.

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
        This API does not support Unicode paths now.

        Examples
        --------
        >>> file_io = prime.FileIO(model = model)
        >>> params = prime.ImportFluentCaseParams(model = model)
        >>> results = file_io.import_fluent_case("/tmp/fluent.cas", params)

        """
        result = _FileIO.import_fluent_case(self, file_name, import_fluent_case_params)
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result

    def import_mapdl_cdb(
        self, file_name: str, params: ImportMapdlCdbParams
    ) -> ImportMapdlCdbResults:
        """Function that imports MAPDL CDB file(cdb).


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
        result = _FileIO.import_mapdl_cdb(self, file_name, params)
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result
