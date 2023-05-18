"""Module containing file input and output related classes and methods."""
from typing import List

# isort: split
from ansys.meshing.prime.autogen.fileio import FileIO as _FileIO

# isort: split
import ansys.meshing.prime.internals.utils as utils
from ansys.meshing.prime.autogen.fileiostructs import (
    ExportBoundaryFittedSplineParams,
    ExportFluentCaseParams,
    ExportFluentMeshingMeshParams,
    ExportMapdlCdbParams,
    ExportMapdlCdbResults,
    ExportSTLParams,
    FileReadParams,
    FileReadResults,
    FileWriteParams,
    FileWriteResults,
    ImportCadParams,
    ImportCadResults,
    ImportFluentCaseParams,
    ImportFluentCaseResults,
    ImportFluentMeshingMeshParams,
    ImportFluentMeshingMeshResults,
    ImportMapdlCdbParams,
    ImportMapdlCdbResults,
    ReadSizeFieldParams,
    SizeFieldFileReadResults,
    WriteSizeFieldParams,
)
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.params.primestructs import ErrorCode


class FileIO(_FileIO):
    """Input and output managing class.

    Parameters
    ----------
    model : Model
        Server model where to create and modify WrapperControls from.
    """

    __doc__ = _FileIO.__doc__

    def __init__(self, model: Model):
        """Initialize model and parent class."""
        self._model = model
        super().__init__(model)

    def read_pmdat(self, file_name: str, file_read_params: FileReadParams) -> FileReadResults:
        """Read PyPrimeMesh data file.

        PyPrimeMesh data files have pmdat extension.

        Parameters
        ----------
        file_name : str
            Path to file on disk.
        file_read_params : FileReadParams
            Parameter to read a file.

        Returns
        -------
        FileReadResults
            Return FileReadResults.

        Notes
        -----
        This API does not support Unicode paths now.

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
        """Write PyPrimeMesh data file. PyPrimeMesh data files have .pmdat extension.

        Parameters
        ----------
        file_name : str
            Path to write file on disk.
        file_write_params : FileWriteParams
            Parameters to write PyPrimeMesh data file.

        Returns
        -------
        FileWriteResults
            Return the FileWriteResults structure.

        Examples
        --------
        >>> results = file_io.write_pmdat("/tmp/prime_mesh_data.pmdat",
                                          prime.FileWriteParams(model=model))
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().write_pmdat(temp_file_name, file_write_params)
        return result

    def import_fluent_meshing_size_field(self, file_name: str) -> SizeFieldFileReadResults:
        """Import Fluent Meshing sizefield file from disk.

        Fluent Meshing sizefield files have sf and sf.gz extension.

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
        >>> file_io = prime.FileIO(model=model)
        >>> results = file_io.import_fluent_meshing_size_field("/tmp/my_sizefield.sf")
        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().import_fluent_meshing_size_field(temp_file_name)
        return result

    def read_size_field(
        self, file_name: str, params: ReadSizeFieldParams
    ) -> SizeFieldFileReadResults:
        """Read PyPrimeMesh sizefield file from disk.

        PyPrimeMesh sizefield files have psf and psf.gz extension.

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
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ReadSizeFieldParams(model=model)
        >>> results = file_io.read_size_field("/tmp/my_prime_sizefield.psf", params)
        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().read_size_field(temp_file_name, params)
        return result

    def write_size_field(self, file_name: str, params: WriteSizeFieldParams) -> FileWriteResults:
        """Write PyPrimeMesh sizefield (.psf) to file.

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
        """Open MAPDL CDB file(cdb).

        Parameters
        ----------
        file_name : str
            Path to file on disk.
        params : ImportMapdlCdbParams
            Parameter to import a CDB file.

        Returns
        -------
        ImportMapdlCdbResults
            Return ImportMapdlCdbResults.

        Notes
        -----
        This API does not support Unicode paths now.

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
        """Export MAPDL CDB file(cdb).

        Parameters
        ----------
        file_name : str
            Path to file on disk.
        params : ExportMapdlCdbParams
            Parameter to export a CDB file.

        Returns
        -------
        ExportMapdlCdbResults
            Return ExportMapdlCdbResults.

        Notes
        -----
        This API does not support Unicode paths now.

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
            result = super().export_mapdl_cdb(temp_file_name, params)
        return result

    def import_fluent_meshing_meshes(
        self,
        file_names: List[str],
        import_fluent_meshing_mesh_params: ImportFluentMeshingMeshParams,
    ) -> ImportFluentMeshingMeshResults:
        """Import Fluent Meshing meshes of given files on disk.

        Fluent Meshing mesh files have msh and msh.gz extension.

        Parameters
        ----------
        file_names : List[str]
            Full path of files to be imported.
        import_fluent_meshing_mesh_params : ImportFluentMeshingMeshParams
            Parameters to import Fluent Meshing mesh.

        Returns
        -------
        ImportFluentMeshingMeshResults
            Return the FileReadResults.


        Notes
        -----
        This API does not support Unicode paths now.

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
        """Import Fluent case file on disk.

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
            Return the ImportFluentCaseResults.


        Notes
        -----
        This API does not support Unicode paths now.

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
        """Export Fluent case file. Fluent case files have cas extension.

        Parameters
        ----------
        file_name : str
            Path to file on disk.
        export_fluent_case_params : ExportFluentCaseParams
            Parameters to export fluent case file.

        Returns
        -------
        FileWriteResults
            Return the FileWriteResults structure.

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
        """Export Fluent Meshing mesh file. Fluent Meshing mesh files have .msh extension.

        Parameters
        ----------
        file_name : str
            Path to file on disk.
        export_fluent_mesh_params : ExportFluentMeshingMeshParams
            Parameters to export Fluent Meshing mesh file.

        Returns
        -------
        FileWriteResults
            Return the FileWriteResults structure.

        Examples
        --------
        >>> results = file_io.export_fluent_meshing_mesh(
                        "/tmp/fluent_meshing.msh",
                        ExportFluentMeshingMeshParams(model=model))
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_fluent_meshing_mesh(temp_file_name, export_fluent_mesh_params)
        return result

    def export_boundary_fitted_spline_kfile(
        self, file_name: str, export_params: ExportBoundaryFittedSplineParams
    ) -> FileWriteResults:
        """Export IGA LS-DYNA Keyword file for boundary fitted spline.

        Parameters
        ----------
        file_name : str
            Name of the file.
        export_params : ExportBoundaryFittedSplineParams
            Parameters for IGA LS-DYNA Keyword file export.

        Returns
        -------
        FileWriteResults
            Return FileWriteResults.

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
        r"""Open CAD file.

        Import CAD file from disk.

        Supported formats on Windows are:

        \*.scdoc \*.fmd \*.agdb \*.pmdb \*.meshdat \*.mechdat \*.dsdb \*.cmdb \*.sat \*.sab
        \*.dwg \*.dxf \*.model \*.exp \*.CATPart \*.CATProduct \*.cgr \*.3dxml \*.prt\* \*.asm\*
        \*.iges \*.igs \*.ipt \*.iam \*.jt \*.prt \*.x_t \*.x_b \*.par \*.psm \*.asm \*.sldprt
        \*.sldasm \*.step \*.stp \*.stl \*.plmxml \*.tgf

        Supported formats on Linux are:

        \*.fmd \*.agdb \*.pmdb \*.meshdat \*.mechdat \*.dsdb \*.cmdb \*.sat \*.sab
        \*.CATPart \*.CATProduct \*.iges \*.igs \*.jt \*.x_t \*.x_b \*.step \*.stp
        \*.stl \*.plmxml \*.tgf

        Refer documentation for detailed list of supported formats.

        Parameters
        ----------
        file_name : str
             Path to file on disk.

        params : ImportCadParams
             Parameters to control CAD import options

        Returns
        -------
        ImportCadResults
             Return ImportCadResults.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> # connect client to server and get model from it
        >>> client = prime.Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = prime.FileIO(model=model)
        >>> params = ImportCadParams(model=model)
        >>> results = file_io.import_cad(
                        "/tmp/my_cad.x_t", params=params)

        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            import_result = super().import_cad(temp_file_name, params)
            if import_result.error_code == ErrorCode.NOERROR:
                self._model._sync_up_model()
        return import_result

    def export_stl(self, file_name: str, params: ExportSTLParams) -> FileWriteResults:
        """Export STL file.


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
        >>> import ansys.meshing.prime as prime
        >>> model = prime.local_model()
        >>> fileio = prime.FileIO(model=model)
        >>> out_file_path = r"/tmp/output.stl"
        >>> part_ids = [part.id for part in model.parts]
        >>> export_stl_params=prime.ExportSTLParams(model=model,part_ids=part_ids)
        >>> results = fileio.export_stl(out_file_path,export_stl_params)

        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_stl(temp_file_name, params)
        return result
