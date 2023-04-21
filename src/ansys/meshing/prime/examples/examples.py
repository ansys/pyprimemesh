"""Examples module for PyPrimeMesh
"""
import os
from enum import Enum
from typing import Optional, Union

from .download_utilities import download_file

__all__ = ['clear_download_cache', 'get_file', 'Examples']


class Examples(Enum):
    """Contains the available PyPrimeMesh examples to download."""

    ELBOW_PMDAT = {"filename": "mixing_elbow.pmdat", "git_folder": "mixing_elbow"}
    ELBOW_FMD = {"filename": "mixing_elbow.fmd", "git_folder": "mixing_elbow"}
    ELBOW_SCDOC = {"filename": "mixing_elbow.scdoc", "git_folder": "mixing_elbow"}
    BRACKET_FMD = {"filename": "bracket_mid_surface.fmd", "git_folder": "bracket_scaffold"}
    BRACKET_SCDOC = {"filename": "bracket_mid_surface.scdoc", "git_folder": "bracket_scaffold"}
    TOY_CAR_PMDAT = {"filename": "toy_car.pmdat", "git_folder": "toy_car"}
    TOY_CAR_FMD = {"filename": "toy_car.fmd", "git_folder": "toy_car"}
    TOY_CAR_SCDOC = {"filename": "toy_car.scdoc", "git_folder": "toy_car"}
    PIPE_TEE_PMDAT = {"filename": "pipe_tee.pmdat", "git_folder": "pipe_tee"}
    PIPE_TEE_FMD = {"filename": "pipe_tee.fmd", "git_folder": "pipe_tee"}
    PIPE_TEE_SCDOC = {"filename": "pipe_tee.scdoc", "git_folder": "pipe_tee"}


_DOWNLOADS = []


def clear_download_cache():
    """Clears the cache of downloaded files"""
    [os.remove(_file) for _file in _DOWNLOADS]
    _DOWNLOADS.clear()


def get_file(
    example: Examples,
    destination: Optional[str] = None,
    force: bool = False,
) -> Union[str, os.PathLike]:
    """Downloads example files from git.

    Parameters
    ----------
    example: Examples
        Known example to download from database
    destination: Optional[str]
        Destination for the file to be downloaded.
        The default is ``None`` in which case the default path in app data is used.
    force: bool
        If true, the file is always downloaded.
        Otherwise, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file
    """
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_file(
        example.value["filename"],
        'pyprimemesh',
        example.value["git_folder"],
        destination=destination,
        force=force,
    )
    _DOWNLOADS.append(file)
    return file


def download_elbow_pmdat(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download PMDAT file for the mixing elbow example

    Parameters
    ----------
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
    force: bool
        If true, the file is always downloaded.
        If false, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     elbow = prime_examples.download_elbow_pmdat()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.read_pmdat(elbow, params=prime.FileReadParams(model))
    >>>     print(model)

    """
    return get_file(Examples.ELBOW_PMDAT, destination, force)


def download_elbow_fmd(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download FMD file for the mixing elbow example

    Parameters
    ----------
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
    force: bool
        If true, the file is always downloaded.
        If false, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     elbow = prime_examples.download_elbow_fmd()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(elbow, params=prime.ImportCADParams(model))
    >>>     print(model)

    """

    return get_file(Examples.ELBOW_FMD, destination, force)


def download_elbow_scdoc(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download SCDOC file for the mixing elbow example

    Parameters
    ----------
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
    force: bool
        If true, the file is always downloaded.
        If false, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     elbow = prime_examples.download_elbow_scdoc()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(elbow, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.ELBOW_SCDOC, destination, force)


def download_bracket_fmd(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download FMD file for the bracket scaffold example

    Parameters
    ----------
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
    force: bool
        If true, the file is always downloaded.
        If false, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     bracket = prime_examples.download_bracket_fmd()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(bracket, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.BRACKET_FMD, destination, force)


def download_bracket_scdoc(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download SCDOC file for the bracket scaffold example

    Parameters
    ----------
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
    force: bool
        If true, the file is always downloaded.
        If false, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     bracket = prime_examples.download_bracket_scdoc()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(bracket, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.BRACKET_SCDOC, destination, force)


def download_toy_car_pmdat(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download PMDAT file for the toy car example

    Parameters
    ----------
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
    force: bool
        If true, the file is always downloaded.
        If false, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     toy_car = prime_examples.download_toy_car_pmdat()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.read_pmdat(toy_car, params=prime.FileReadParams(model))
    >>>     print(model)

    """
    return get_file(Examples.TOY_CAR_PMDAT, destination, force)


def download_toy_car_fmd(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download FMD file for the toy car example

    Parameters
    ----------
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
    force: bool
        If true, the file is always downloaded.
        If false, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     toy_car = prime_examples.download_toy_car_fmd()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(toy_car, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.TOY_CAR_FMD, destination, force)


def download_toy_car_scdoc(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download SCDOC file for the toy car example

    Parameters
    ----------
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
    force: bool
        If true, the file is always downloaded.
        If false, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     toy_car = prime_examples.download_toy_car_scdoc()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(toy_car, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.TOY_CAR_SCDOC, destination, force)


def download_pipe_tee_pmdat(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download PMDAT file for the pipe tee example

    Parameters
    ----------
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
    force: bool
        If true, the file is always downloaded.
        If false, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     pipe_tee = prime_examples.download_pipe_tee_pmdat()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.read_pmdat(pipe_tee, params=prime.FileReadParams(model))
    >>>     print(model)

    """
    return get_file(Examples.PIPE_TEE_PMDAT, destination, force)


def download_pipe_tee_fmd(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download FMD file for the pipe tee example

    Parameters
    ----------
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
    force: bool
        If true, the file is always downloaded.
        If false, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     pipe_tee = prime_examples.download_pipe_tee_fmd()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(pipe_tee, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.PIPE_TEE_FMD, destination, force)


def download_pipe_tee_scdoc(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download SCDOC file for the pipe tee example

    Parameters
    ----------
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
    force: bool
        If true, the file is always downloaded.
        If false, an existing file in the cache may be re-used.

    Returns
    -------
    str
        Local path to the downloaded file

    Raises
    ------
    ValueError
        When the provided destination path does not exist on file

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     pipe_tee = prime_examples.download_pipe_tee_scdoc()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(pipe_tee, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.PIPE_TEE_SCDOC, destination, force)
