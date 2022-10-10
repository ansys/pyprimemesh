"""Examples module for PyPrime
"""
import os
from typing import Union, Optional
from .download import download_file

__all__ = [
    'clear_download_cache',
    'download_file',
    'download_elbow_pmdat',
    'download_elbow_fmd',
    'download_elbow_scdoc',
    'download_bracket_fmd',
    'download_bracket_scdoc',
    'download_toy_car_pmdat',
    'download_toy_car_fmd',
    'download_toy_car_scdoc',
    'download_pipe_tee_pmdat',
    'download_pipe_tee_fmd',
]

_DOWNLOADS = []


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
    >>> import ansys.meshing.prime as pyprime
    >>> import ansys.meshing.prime.examples as pyprime_examples
    >>> with pyprime.launch_prime() as session:
    >>>     model = session.model
    >>>     elbow = pyprime_examples.download_elbow_pmdat()
    >>>     with pyprime.FileIO(model) as io:
    >>>         _ = io.read_pmdat(elbow, params=pyprime.FileReadParams(model))
    >>>     print(model)
    >>> pyprime_examples.clear_download_cache()
    """
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_file(
        'mixing_elbow.pmdat', 'pyprime', 'mixing_elbow', destination=destination, force=force
    )
    _DOWNLOADS.append(file)
    return file


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
    >>> import ansys.meshing.prime as pyprime
    >>> import ansys.meshing.prime.examples as pyprime_examples
    >>> with pyprime.launch_prime() as session:
    >>>     model = session.model
    >>>     elbow = pyprime_examples.download_elbow_fmd()
    >>>     with pyprime.FileIO(model) as io:
    >>>         _ = io.import_cad(elbow, params=pyprime.ImportCADParams(model))
    >>>     print(model)
    >>> pyprime_examples.clear_download_cache()
    """
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_file(
        'mixing_elbow.fmd', 'pyprime', 'mixing_elbow', destination=destination, force=force
    )
    _DOWNLOADS.append(file)
    return file


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
    >>> import ansys.meshing.prime as pyprime
    >>> import ansys.meshing.prime.examples as pyprime_examples
    >>> with pyprime.launch_prime() as session:
    >>>     model = session.model
    >>>     elbow = pyprime_examples.download_elbow_scdoc()
    >>>     with pyprime.FileIO(model) as io:
    >>>         _ = io.import_cad(elbow, params=pyprime.ImportCADParams(model))
    >>>     print(model)
    >>> pyprime_examples.clear_download_cache()
    """
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_file(
        'mixing_elbow.scdoc', 'pyprime', 'mixing_elbow', destination=destination, force=force
    )
    _DOWNLOADS.append(file)
    return file

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
    >>> import ansys.meshing.prime as pyprime
    >>> import ansys.meshing.prime.examples as pyprime_examples
    >>> with pyprime.launch_prime() as session:
    >>>     model = session.model
    >>>     bracket = pyprime_examples.download_bracket_fmd()
    >>>     with pyprime.FileIO(model) as io:
    >>>         _ = io.import_cad(bracket, params=pyprime.ImportCADParams(model))
    >>>     print(model)
    >>> pyprime_examples.clear_download_cache()
    """
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_file(
        'bracket_mid_surface.fmd', 'pyprime', 'bracket_scaffold', destination=destination, force=force
    )
    _DOWNLOADS.append(file)
    return file


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
    >>> import ansys.meshing.prime as pyprime
    >>> import ansys.meshing.prime.examples as pyprime_examples
    >>> with pyprime.launch_prime() as session:
    >>>     model = session.model
    >>>     bracket = pyprime_examples.download_bracket_scdoc()
    >>>     with pyprime.FileIO(model) as io:
    >>>         _ = io.import_cad(bracket, params=pyprime.ImportCADParams(model))
    >>>     print(model)
    >>> pyprime_examples.clear_download_cache()
    """
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_file(
        'bracket_mid_surface.scdoc', 'pyprime', 'bracket_scaffold', destination=destination, force=force
    )
    _DOWNLOADS.append(file)
    return file


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
    >>> import ansys.meshing.prime as pyprime
    >>> import ansys.meshing.prime.examples as pyprime_examples
    >>> with pyprime.launch_prime() as session:
    >>>     model = session.model
    >>>     toy_car = pyprime_examples.download_toy_car_pmdat()
    >>>     with pyprime.FileIO(model) as io:
    >>>         _ = io.read_pmdat(toy_car, params=pyprime.FileReadParams(model))
    >>>     print(model)
    >>> pyprime_examples.clear_download_cache()
    """
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_file(
        'toy_car.pmdat', 'pyprime', 'toy_car', destination=destination, force=force
    )
    _DOWNLOADS.append(file)
    return file


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
    >>> import ansys.meshing.prime as pyprime
    >>> import ansys.meshing.prime.examples as pyprime_examples
    >>> with pyprime.launch_prime() as session:
    >>>     model = session.model
    >>>     toy_car = pyprime_examples.download_toy_car_fmd()
    >>>     with pyprime.FileIO(model) as io:
    >>>         _ = io.import_cad(toy_car, params=pyprime.ImportCADParams(model))
    >>>     print(model)
    >>> pyprime_examples.clear_download_cache()
    """
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_file(
        'toy_car.fmd', 'pyprime', 'toy_car', destination=destination, force=force
    )
    _DOWNLOADS.append(file)
    return file


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
    >>> import ansys.meshing.prime as pyprime
    >>> import ansys.meshing.prime.examples as pyprime_examples
    >>> with pyprime.launch_prime() as session:
    >>>     model = session.model
    >>>     toy_car = pyprime_examples.download_toy_car_scdoc()
    >>>     with pyprime.FileIO(model) as io:
    >>>         _ = io.import_cad(toy_car, params=pyprime.ImportCADParams(model))
    >>>     print(model)
    >>> pyprime_examples.clear_download_cache()
    """
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_file(
        'toy_car.scdoc', 'pyprime', 'toy_car', destination=destination, force=force
    )
    _DOWNLOADS.append(file)
    return file


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
    >>> import ansys.meshing.prime as pyprime
    >>> import ansys.meshing.prime.examples as pyprime_examples
    >>> with pyprime.launch_prime() as session:
    >>>     model = session.model
    >>>     pipe_tee = pyprime_examples.download_pipe_tee_pmdat()
    >>>     with pyprime.FileIO(model) as io:
    >>>         _ = io.read_pmdat(pipe_tee, params=pyprime.FileReadParams(model))
    >>>     print(model)
    >>> pyprime_examples.clear_download_cache()
    """
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_file(
        'pipe_tee.pmdat', 'pyprime', 'pipe_tee', destination=destination, force=force
    )
    _DOWNLOADS.append(file)
    return file


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
    >>> import ansys.meshing.prime as pyprime
    >>> import ansys.meshing.prime.examples as pyprime_examples
    >>> with pyprime.launch_prime() as session:
    >>>     model = session.model
    >>>     pipe_tee = pyprime_examples.download_pipe_tee_fmd()
    >>>     with pyprime.FileIO(model) as io:
    >>>         _ = io.import_cad(pipe_tee, params=pyprime.ImportCADParams(model))
    >>>     print(model)
    >>> pyprime_examples.clear_download_cache()
    """
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_file(
        'pipe_tee.fmd', 'pyprime', 'pipe_tee', destination=destination, force=force
    )
    _DOWNLOADS.append(file)
    return file


def clear_download_cache():
    """Clears the cache of downloaded files"""
    [os.remove(_file) for _file in _DOWNLOADS]
    _DOWNLOADS.clear()
