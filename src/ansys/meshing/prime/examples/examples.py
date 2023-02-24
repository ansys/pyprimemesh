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
    file_name : str
        Name of the file.
    file_extension : str
        Extension of the file.
    destination: Optional[str]
        Destination for the file to be downloaded.
        If nothing is provided, the default path in app data is used
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
