# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
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

"""Module for mangaging file inputs and outputs."""
import json
from typing import List

# isort: split
from ansys.meshing.prime.autogen.fileio import FileIO as _FileIO

# isort: split
import ansys.meshing.prime.core.dynaexportutils as dynaexportutils
import ansys.meshing.prime.core.mapdlcdbexportutils as mapdlcdbexportutils
import ansys.meshing.prime.internals.utils as utils
from ansys.meshing.prime.autogen.fileiostructs import (
    ExportBoundaryFittedSplineParams,
    ExportFluentCaseParams,
    ExportFluentMeshingMeshParams,
    ExportLSDynaIgaKeywordFileParams,
    ExportLSDynaIGAResults,
    ExportLSDynaKeywordFileParams,
    ExportLSDynaResults,
    ExportMapdlCdbParams,
    ExportMapdlCdbResults,
    ExportSTLParams,
    FileReadParams,
    FileReadResults,
    FileWriteParams,
    FileWriteResults,
    ImportAbaqusParams,
    ImportAbaqusResults,
    ImportCadParams,
    ImportCadResults,
    ImportFluentCaseParams,
    ImportFluentCaseResults,
    ImportFluentMeshingMeshParams,
    ImportFluentMeshingMeshResults,
    ImportMapdlCdbParams,
    ImportMapdlCdbResults,
    ReadSizeFieldParams,
    SeparateBlocksFormatType,
    SizeFieldFileReadResults,
    WriteSizeFieldParams,
)
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.params.primestructs import ErrorCode


class FileIO(_FileIO):
    """Handles reading or writing files from the disk.

    Parameters
    ----------
    model : Model
        Server model to create FileIO object.
    """

    __doc__ = _FileIO.__doc__

    def __init__(self, model: Model):
        """Initialize model and parent class."""
        self._model = model
        super().__init__(model)

    def read_pmdat(self, file_name: str, file_read_params: FileReadParams) -> FileReadResults:
        """Read a PyPrimeMesh data (PMDAT) file.

        Parameters
        ----------
        file_name : str
            Path to the data file on disk.
        file_read_params : FileReadParams
            Parameters for reading the data file.

        Returns
        -------
        FileReadResults
            Results from reading the data file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> #connect client to server and get model from it
        >>> client = prime.Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = prime.FileIO(model=model)
        >>> file_read_params = prime.FileReadParams(model=model)
        >>> results = file_io.read_pmdat("/tmp/file.pmdat", file_read_params)

        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().read_pmdat(temp_file_name, file_read_params)
            if result.error_code == ErrorCode.NOERROR:
                self._model._sync_up_model()
        return result

    def write_pmdat(self, file_name: str, file_write_params: FileWriteParams) -> FileWriteResults:
        """Write a PyPrimeMesh data (PMDAT) file.

        Parameters
        ----------
        file_name : str
            Path for writing the data file on disk.
        file_write_params : FileWriteParams
            Parameters for writing the data file.

        Returns
        -------
        FileWriteResults
            Results from writing the data file.

        Examples
        --------
        >>> results = file_io.write_pmdat("/tmp/prime_mesh_data.pmdat",
                                          prime.FileWriteParams(model=model))
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().write_pmdat(temp_file_name, file_write_params)
        return result

    def import_abaqus_inp(self, file_name: str, params: ImportAbaqusParams) -> ImportAbaqusResults:
        """(BETA FEATURE) Import a Abaqus file.

        This is a beta feature to import abaqus files as dead mesh and also store
        simulation-specific information into Prime in the form of JSON documents.

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


        Examples
        --------
        >>> results = file_io.import_abaqus(r"/tmp/file.inp")

        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().import_abaqus_inp(temp_file_name, params)
            if result.error_code == ErrorCode.NOERROR:
                self._model._sync_up_model()
        return result

    def import_fluent_meshing_size_field(self, file_name: str) -> SizeFieldFileReadResults:
        """Import a Fluent Meshing size field (SF and SF.GZ) file from disk.

        Parameters
        ----------
        file_name : str
            Path to the size field file on disk.

        Returns
        -------
        SizeFieldFileReadResults
            Results from reading the size field file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> results = file_io.import_fluent_meshing_size_field("/tmp/my_sizefield.sf")
        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().import_fluent_meshing_size_field(temp_file_name)
        return result

    def read_size_field(
        self, file_name: str, params: ReadSizeFieldParams
    ) -> SizeFieldFileReadResults:
        """Read a PyPrimeMesh size field (PSF and PSF.GZ) file from disk.

        Parameters
        ----------
        file_name : str
            Path to the size field file on disk.
        params : ReadSizeFieldParams
            Parameters for reading size field file.

        Returns
        -------
        SizeFieldFileReadResults
            Results from reading the size field file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ReadSizeFieldParams(model=model)
        >>> results = file_io.read_size_field("/tmp/my_prime_sizefield.psf", params)
        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().read_size_field(temp_file_name, params)
        return result

    def write_size_field(self, file_name: str, params: WriteSizeFieldParams) -> FileWriteResults:
        """Write a PyPrimeMesh size field (PSF) file to a file on disk.

        Parameters
        ----------
        file_name : str
            Path to the size field file on disk.
        params : WriteSizeFieldParams
            Parameters for writing the size field file.

        Returns
        -------
        FileWriteResults
            Results from writing the size field file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.WriteSizeFieldParams(model=model)
        >>> results = file_io.write_size_field("/tmp/my_prime_sizefield.psf", params)
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().write_size_field(temp_file_name, params)
        return result

    def import_mapdl_cdb(
        self, file_name: str, params: ImportMapdlCdbParams
    ) -> ImportMapdlCdbResults:
        """Import an MAPDL CDB file.

        Parameters
        ----------
        file_name : str
            Path to the CDB file on disk.
        params : ImportMapdlCdbParams
            Parameters for importing the CDB file.

        Returns
        -------
        ImportMapdlCdbResults
            Results from importing the CDB file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> # connect client to server and get model from it
        >>> client = prime.Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ImportMapdlCdbParams(model=model)
        >>> results = file_io.import_mapdl_cdb("/tmp/file.cdb", params)
        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().import_mapdl_cdb(temp_file_name, params)
            if result.error_code == ErrorCode.NOERROR:
                self._model._sync_up_model()
        return result

    def export_mapdl_cdb(
        self, file_name: str, params: ExportMapdlCdbParams
    ) -> ExportMapdlCdbResults:
        """Export an MAPDL CDB file.

        Parameters
        ----------
        file_name : str
            Path to the CDB file on disk.
        params : ExportMapdlCdbParams
            Parameters for exporting the CDB file.

        Returns
        -------
        ExportMapdlCdbResults
            Results from exporting the CDB file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> #connect client to server and get model from it
        >>> client = prime.Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ExportMapdlCdbParams(model=model)
        >>> results = file_io.export_mapdl_cdb("/tmp/file.cdb", params)
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            part_id = 1
            if len(self._model.parts) > 0:
                part_id = self._model.parts[0].id
            sim_data_str = super().get_abaqus_simulation_data(part_id)
            if params.config_settings == None:
                params.config_settings = ''
            all_mat_cmds, analysis_settings = mapdlcdbexportutils.generate_mapdl_commands(
                self._model, sim_data_str, params
            )
            params.material_properties = all_mat_cmds + params.material_properties
            params.analysis_settings = analysis_settings
            result = super().export_mapdl_cdb(temp_file_name, params)
        return result

    def initialize_cdb_export_params(
        self, params: ExportMapdlCdbParams, major_version: int, minor_version: int
    ) -> ExportMapdlCdbParams:
        """
        Initialize specific CDB export parameters based on the given version.

        This function sets the separate_blocks_format_type, export_fasteners_as_swgen and
        export_rigid_bodies_as_rbgen parameters of the provided ExportMapdlCdbParams
        object based on the given major and minor version numbers.
        Other parameters remain unchanged.

        Parameters
        ----------
        params : ExportMapdlCdbParams
            The CDB export parameters object to be modified.
        major_version : int
            The major version number.
        minor_version : int
            The minor version number.

        Returns
        -------
        ExportMapdlCdbParams
            The modified CDB export parameters object.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        The version is formed as "<major_version>r<minor_version>", e.g., "24r1", "25r2".
        If the version is greater than or equal to "25r1", write_separate_blocks is set to True
        with COMPACT format, and export_fasteners_as_swgen and export_rigid_bodies_as_rbgen
        parameters are set to True. Otherwise, they are set to False.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ExportMapdlCdbParams()
        >>> params = file_io.initialize_cdb_export_params(params, 24, 1)
        >>> params.write_separate_blocks
        False
        >>> params.export_fasteners_as_swgen
        False
        >>> params.export_rigid_bodies_as_swgen
        False

        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ExportMapdlCdbParams()
        >>> params = file_io.initialize_cdb_export_params(params, 25, 2)
        >>> params.write_separate_blocks
        True
        >>> params.separate_blocks_format_type
        SeparateBlocksFormatType.COMPACT
        >>> params.export_fasteners_as_swgen
        True
        >>> params.export_rigid_bodies_as_swgen
        True
        """
        version = f"{major_version}r{minor_version}"
        params.write_separate_blocks = version >= "25r1"
        if version >= "25r1":
            params.separate_blocks_format_type = SeparateBlocksFormatType.COMPACT
        else:
            params.separate_blocks_format_type = SeparateBlocksFormatType.STANDARD
        params.export_fasteners_as_swgen = version >= "25r1"
        params.export_rigid_bodies_as_rbgen = version >= "25r1"
        return params

    def import_fluent_meshing_meshes(
        self,
        file_names: List[str],
        import_fluent_meshing_mesh_params: ImportFluentMeshingMeshParams,
    ) -> ImportFluentMeshingMeshResults:
        """Import Fluent Meshing's mesh (MS and MSH.GZ) files from disk.

        Parameters
        ----------
        file_names : List[str]
            List of full path for the mesh files to import.
        import_fluent_meshing_mesh_params : ImportFluentMeshingMeshParams
            Parameters for importing the mesh files.

        Returns
        -------
        ImportFluentMeshingMeshResults
            Results from importing the mesh files.


        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ImportFluentMeshingMeshParams(model=model)
        >>> results = file_io.import_fluent_meshing_meshes(
                        ["/tmp/mesh.msh", "/tmp/mesh1.msh"],
                        params)

        """
        with utils.file_read_context_list(self._model, file_names) as temp_file_names:
            result = super().import_fluent_meshing_meshes(
                temp_file_names, import_fluent_meshing_mesh_params
            )
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result

    def import_fluent_case(
        self, file_name: str, import_fluent_case_params: ImportFluentCaseParams
    ) -> ImportFluentCaseResults:
        """Import a Fluent case (CAS) file from disk.

        Parameters
        ----------
        file_name : str
            Path to the case file on disk.
        import_fluent_case_params : ImportFluentCaseParams
            Parameters for importing the case file.

        Returns
        -------
        ImportFluentCaseResults
            Results from importing the case file.


        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ImportFluentCaseParams(model=model)
        >>> results = file_io.import_fluent_case("/tmp/fluent.cas", params)

        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().import_fluent_case(temp_file_name, import_fluent_case_params)
            if result.error_code == ErrorCode.NOERROR:
                self._model._sync_up_model()
        return result

    def export_fluent_case(
        self, file_name: str, export_fluent_case_params: ExportFluentCaseParams
    ) -> FileWriteResults:
        """Export a Fluent case (CAS) file.

        Parameters
        ----------
        file_name : str
            Path to the case file on disk.
        export_fluent_case_params : ExportFluentCaseParams
            Parameters for exporting the case file.

        Returns
        -------
        FileWriteResults
            Results from exporting the case file.

        Examples
        --------
        >>> file_io = FileIO(model=model)
        >>> results = file_io.export_fluent_case(
                        "/tmp/fluent.cas",
                        prime.ExportFluentCaseParams(model=model))
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_fluent_case(temp_file_name, export_fluent_case_params)
        return result

    def export_fluent_meshing_mesh(
        self, file_name: str, export_fluent_mesh_params: ExportFluentMeshingMeshParams
    ) -> FileWriteResults:
        """Export a Fluent Meshing mesh (MSH) file.

        Parameters
        ----------
        file_name : str
            Path to the mesh file on disk.
        export_fluent_mesh_params : ExportFluentMeshingMeshParams
            Parameters for exporting the mesh file.

        Returns
        -------
        FileWriteResults
            Results from exporting the mesh file.

        Examples
        --------
        >>> results = file_io.export_fluent_meshing_mesh(
                        "/tmp/fluent_meshing.msh",
                        ExportFluentMeshingMeshParams(model=model))
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_fluent_meshing_mesh(temp_file_name, export_fluent_mesh_params)
        return result

    def export_lsdyna_keyword_file(
        self, file_name: str, params: ExportLSDynaKeywordFileParams
    ) -> ExportLSDynaResults:
        """Export FEA LS-DYNA Keyword file for solid, surface mesh, or both.

        Parameters
        ----------
        file_name : str
            Name of the file.
        params : ExportLSDynaKeywordFileParams
            Parameters for FEA LS-DYNA Keyword file export.

        Returns
        -------
        ExportLSDynaResults
            Returns ExportLSDynaResults.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = file_io.export_lsdyna_keyword_file(
            file_name, ExportLSDynaKeywordFileParams(model=model)
        )

        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            part_id = 1
            if len(self._model.parts) > 0:
                part_id = self._model.parts[0].id
            sim_data = json.loads(super().get_abaqus_simulation_data(part_id))
            if sim_data is not None:
                mp = dynaexportutils.MaterialProcessor(self._model, sim_data)
                all_mat_cmds = mp.get_all_material_commands()
                params.material_properties = all_mat_cmds + params.material_properties
            result = super().export_lsdyna_keyword_file(temp_file_name, params)
        return result

    def export_lsdyna_iga_keyword_file(
        self, file_name: str, params: ExportLSDynaIgaKeywordFileParams
    ) -> ExportLSDynaIGAResults:
        """Export IGA LS-DYNA Keyword file for solid, surface splines.

        Parameters
        ----------
        file_name : str
            Name of the file.
        params : ExportLSDynaIgaKeywordFileParams
            Parameters for IGA LS-DYNA Keyword file export.

        Returns
        -------
        ExportLSDynaIGAResults
            Returns ExportLSDynaIGAResults.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = file_io.export_lsdyna_iga_keyword_file(
            file_name, ExportLSDynaIgaKeywordFileParams(model=model)
        )

        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_lsdyna_iga_keyword_file(temp_file_name, params)
        return result

    def export_boundary_fitted_spline_kfile(
        self, file_name: str, export_params: ExportBoundaryFittedSplineParams
    ) -> FileWriteResults:
        """Export the IGA LS-DYNA keyword file for a boundary fitted spline.

        Parameters
        ----------
        file_name : str
            Name of the keyword file.
        export_params : ExportBoundaryFittedSplineParams
            Parameters for exporting the keyword file.

        Returns
        -------
        FileWriteResults
            Results from exporting the keyword file.

        Examples
        --------
        >>> results = file_io.export_boundary_fitted_spline_k_file(
                        file_name,
                        ExportBoundaryFittedSplineParams(model=model))
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_boundary_fitted_spline_kfile(temp_file_name, export_params)
        return result

    def import_cad(self, file_name: str, params: ImportCadParams) -> ImportCadResults:
        r"""Import a CAD file from disk.

        Supported CAD file formats on Windows are:

        \*.scdoc \*.scdocx \*.dsco \*.fmd \*.agdb \*.pmdb \*.meshdat \*.mechdat \*.dsdb \*.cmdb
        \*.sat \*.sab \*.dwg \*.dxf \*.model \*.exp \*.CATPart \*.CATProduct \*.cgr \*.3dxml
        \*.prt\* \*.asm\* \*.iges \*.igs \*.ipt \*.iam \*.jt \*.prt \*.x_t \*.x_b \*.par \*.psm
        \*.asm \*.sldprt \*.sldasm \*.step \*.stp \*.stl \*.plmxml \*.tgf

        Supported CAD file formats on Linux are:

        \*.fmd \*.agdb \*.pmdb \*.meshdat \*.mechdat \*.dsdb \*.cmdb \*.sat \*.sab
        \*.CATPart \*.CATProduct \*.iges \*.igs \*.jt \*.x_t \*.x_b \*.step \*.stp
        \*.stl \*.plmxml \*.tgf

        Refer **Reading and writing files** section in **User guide** for a
        comprehensive list of supported formats.

        Parameters
        ----------
        file_name : str
            Path to the CAD file on disk.

        params : ImportCadParams
            Parameters for importing the CAD file.

        Returns
        -------
        ImportCadResults
            Results from importing the CAD file.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> prime_client = prime.launch_prime()
        >>> model = prime_client.model
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ImportCadParams(model=model)
        >>> results = file_io.import_cad("/tmp/my_cad.x_t", params=params)

        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            import_result = super().import_cad(temp_file_name, params)
            if import_result.error_code == ErrorCode.NOERROR:
                self._model._sync_up_model()
        return import_result

    def export_stl(self, file_name: str, params: ExportSTLParams) -> FileWriteResults:
        """Export an STL file.

        Parameters
        ----------
        file_name : str
            Path to the STL file on disk.
        params : ExportSTLParams
            Parameters for exporting the STL file.

        Returns
        -------
        FileWriteResults
            Results from exporting the STL file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> model = prime.launch_prime().model
        >>> fileio = prime.FileIO(model=model)
        >>> out_file_path = r"/tmp/output.stl"
        >>> part_ids = [part.id for part in model.parts]
        >>> export_stl_params=prime.ExportSTLParams(model=model,part_ids=part_ids)
        >>> results = fileio.export_stl(out_file_path,export_stl_params)

        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_stl(temp_file_name, params)
        return result
