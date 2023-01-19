import os

import pytest

import ansys.meshing.prime as prime
from ansys.meshing.prime.autogen.primeconfig import ErrorCode
from ansys.meshing.prime.internals.error_handling import PrimeRuntimeError


def test_read_pdmat(get_remote_client):
    model = get_remote_client.model
    file_io = prime.FileIO(model=model)
    file_read_params = prime.FileReadParams(model=model)
    pmdat_path = prime.examples.download_elbow_pmdat(
        destination=os.path.abspath(os.path.abspath("./tests/core/test_files/")), force=True
    )

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
