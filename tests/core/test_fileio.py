import os

import pytest

import ansys.meshing.prime as prime
from ansys.meshing.prime import ErrorCode, PrimeRuntimeError


def test_io_file_not_found_error(get_remote_client, get_examples):
    model = get_remote_client.model
    with prime.FileIO(model) as io:
        file_name = r'/doesnotexist/file.pmdat'
        with pytest.raises(FileNotFoundError) as error:
            _ = io.read_pmdat(file_name, prime.FileReadParams(model=model))
            assert f'Given file name "{file_name}" is not found on local disk' in str(error.value)

        files = [r'/doesnotexist/file.pmdat', get_examples["elbow_lucid"]]
        error_msg = "File /doesnotexist/file.pmdat given for read is missing from local disk."
        with pytest.raises(FileNotFoundError, match=error_msg) as error:
            _ = io.import_fluent_meshing_meshes(
                files, prime.ImportFluentMeshingMeshParams(model=model)
            )


def test_io_pdmat(get_remote_client, get_examples, tmp_path):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)
    file_read_params = prime.FileReadParams(model=model)
    pmdat_path = get_examples["elbow_lucid"]

    # Wrong extension
    with pytest.raises(PrimeRuntimeError) as prime_error:
        _ = file_io.read_pmdat(
            os.path.abspath("./tests/core/test_files/file.pdmat"),
            file_read_params,
        )
        assert "file extension is not supported" in str(prime_error.value)

    # Empty file
    with pytest.raises(PrimeRuntimeError) as prime_error:
        _ = file_io.read_pmdat(
            os.path.abspath("./tests/core/test_files/file.pmdat"),
            file_read_params,
        )

    # Regular usage
    results = file_io.read_pmdat(
        pmdat_path,
        file_read_params,
    )
    assert results.error_code == ErrorCode.NOERROR

    # export
    export_path = str(tmp_path) + "/file_test.pmdat"
    results = file_io.write_pmdat(
        os.path.abspath(export_path),
        prime.FileWriteParams(model=model),
    )
    assert results.error_code == ErrorCode.NOERROR


def test_io_cdb(get_remote_client, tmp_path):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)

    # import
    import_params = prime.ImportMapdlCdbParams(model=model)
    results = file_io.import_mapdl_cdb(
        os.path.abspath("./tests/core/test_files/hex.cdb"), import_params
    )
    assert results.error_code == ErrorCode.NOERROR

    # export
    export_params = prime.ExportMapdlCdbParams(model=model)
    export_path = str(tmp_path) + "/hex_test.cdb"
    results = file_io.export_mapdl_cdb(os.path.abspath(export_path), export_params)
    assert results.error_code == ErrorCode.NOERROR


def test_io_fluent_case(get_remote_client, tmp_path):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)

    # import
    import_params = prime.ImportFluentCaseParams(model=model)
    results = file_io.import_fluent_case(
        os.path.abspath("./tests/core/test_files/hex.cas"), import_params
    )
    assert results.error_code == ErrorCode.NOERROR

    # export
    export_path = str(tmp_path) + "/hex_test.cas"
    export_params = prime.ExportFluentCaseParams(model=model)
    results = file_io.export_fluent_case(os.path.abspath(export_path), export_params)
    assert results.error_code == ErrorCode.NOERROR


def test_export_kfile(get_remote_client, get_examples, tmp_path):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)
    pmdat_path = get_examples["elbow_lucid"]

    # init mesher and load the example
    mesher = prime.lucid.Mesh(model)
    mesher.read(file_name=pmdat_path)
    export_path = str(tmp_path) + "/file_test.k"

    results = file_io.export_boundary_fitted_spline_kfile(
        os.path.abspath(export_path),
        prime.ExportBoundaryFittedSplineParams(model=model),
    )
    assert results.error_code == ErrorCode.NOERROR


def test_io_sf(get_remote_client):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)

    # import
    results = file_io.import_fluent_meshing_size_field(
        os.path.abspath("./tests/core/test_files/box.sf")
    )
    assert results.error_code == ErrorCode.NOERROR


def test_io_psf(get_remote_client, tmp_path):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)

    import_params = prime.ReadSizeFieldParams(model=model)
    results = file_io.read_size_field(
        os.path.abspath("./tests/core/test_files/box.psf"), import_params
    )
    assert results.error_code == ErrorCode.NOERROR

    export_params = prime.WriteSizeFieldParams(model=model)
    export_path = str(tmp_path) + "/box_test.psf"
    results = file_io.write_size_field(os.path.abspath(export_path), export_params)
    assert results.error_code == ErrorCode.NOERROR


def test_io_cad(get_remote_client):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)

    import_params = prime.ImportCadParams(model=model)
    results = file_io.import_cad(os.path.abspath("./tests/core/test_files/hex.fmd"), import_params)
    assert results.error_code == ErrorCode.NOERROR


def test_io_fluent_mesh(get_remote_client, tmp_path):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)

    import_params = prime.ImportFluentMeshingMeshParams(model=model)
    results = file_io.import_fluent_meshing_meshes(
        [os.path.abspath("./tests/core/test_files/hex.msh")], import_params
    )
    assert results.error_code == ErrorCode.NOERROR

    import_params = prime.ExportFluentMeshingMeshParams(model=model)
    export_path = str(tmp_path) + "/hex_test.msh"
    results = file_io.export_fluent_meshing_mesh(os.path.abspath(export_path), import_params)
    assert results.error_code == ErrorCode.NOERROR
