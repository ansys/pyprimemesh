"""Examples module for PyPrimeMesh
"""
import os
from typing import Optional, Union

from .download_utilities import download_file

__all__ = ['clear_download_cache', 'get_file']

_DOWNLOADS = []


def clear_download_cache():
    """Clears the cache of downloaded files"""
    [os.remove(_file) for _file in _DOWNLOADS]
    _DOWNLOADS.clear()


def get_file(
    file_name: str,
    file_extension: str,
    git_folder_name: str,
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
    file_full_name = file_name + '.' + file_extension
    file = download_file(
        file_full_name, 'pyprimemesh', git_folder_name, destination=destination, force=force
    )
    _DOWNLOADS.append(file)
    return file
