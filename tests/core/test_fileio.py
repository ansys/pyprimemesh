import os

import pytest

import ansys.meshing.prime as prime
from ansys.meshing.prime.autogen.primeconfig import ErrorCode
from ansys.meshing.prime.internals.error_handling import PrimeRuntimeError


def test_io_pdmat(get_remote_client, get_examples):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)
    file_read_params = prime.FileReadParams(model=model)
    pmdat_path = get_examples["elbow_lucid"]

    # Wrong extension
    with pytest.raises(PrimeRuntimeError) as prime_error:
        _ = file_io.read_pmdat(
            "file.pdmat",
            file_read_params,
        )
        assert "file extension is not supported" in str(prime_error.value)

    # Non existent path
    with pytest.raises(PrimeRuntimeError) as prime_error:

        _ = file_io.read_pmdat(
            "/nonexistent/file.pmdat",
            file_read_params,
        )
        assert "Incorrect File Path or Name" in str(prime_error.value)

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
    results = file_io.write_pmdat(
        os.path.abspath("./tests/core/test_files/write_file.pmdat"),
        prime.FileWriteParams(model=model),
    )
    assert results.error_code == ErrorCode.NOERROR


def test_io_cdb(get_remote_client, get_examples):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)
    file_read_params = prime.FileReadParams(model=model)
    pmdat_path = get_examples["elbow_lucid"]

    # export
    params = prime.ExportMapdlCdbParams(model=model)
    results = file_io.export_mapdl_cdb(os.path.abspath("./tests/core/test_files/file.cdb"), params)
    assert results.error_code == ErrorCode.NOERROR

    results = file_io.import_mapdl_cdb(os.path.abspath("./tests/core/test_files/file.cdb"), params)


def test_io_fluent_case(get_remote_client, get_examples):
    # need appropiate file for this test
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)
    file_read_params = prime.FileReadParams(model=model)
    pmdat_path = get_examples["elbow_lucid"]
    params = prime.ExportFluentCaseParams(model=model)
    results = file_io.export_fluent_case(
        os.path.abspath("./tests/core/test_files/file.cas"), params
    )


def test_io_cbd(get_remote_client, get_examples):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)
    file_read_params = prime.FileReadParams(model=model)
    pmdat_path = get_examples["elbow_lucid"]

    # export
    params = prime.ExportMapdlCdbParams(model=model)
    results = file_io.export_mapdl_cdb(os.path.abspath("./tests/core/test_files/file.cdb"), params)
    assert results.error_code == ErrorCode.NOERROR

    # import TODO: fails
    params = prime.ImportMapdlCdbParams(model=model)
    results = file_io.import_mapdl_cdb(os.path.abspath("./tests/core/test_files/file.cdb"), params)
    assert results.error_code == ErrorCode.NOERROR


def test_export_kfile(get_remote_client, get_examples):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)
    file_read_params = prime.FileReadParams(model=model)
    pmdat_path = get_examples["elbow_lucid"]

    results = file_io.export_boundary_fitted_spline_k_file(
        os.path.abspath("./tests/core/test_files/file.kfile"),
        prime.ExportBoundaryFittedSplineParams(model=model),
    )
