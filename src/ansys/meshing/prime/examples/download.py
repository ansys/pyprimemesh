import os
import urllib.request
from typing import Optional
from urllib.parse import urljoin

import ansys.meshing.prime.internals.defaults as defaults

__all__ = ['download_file']


def _joinurl(base, *paths):
    for path in paths:
        if base[-1] != '/':
            base += '/'
        base = urljoin(base, path)
    return base


def _get_default_server_and_joiner():
    return 'https://github.com/ansys/example-data/raw/master', _joinurl


def _get_filepath_on_default_server(filename: str, *directory: str):
    server, joiner = _get_default_server_and_joiner()
    if directory:
        return joiner(server, *directory, filename)
    else:
        return joiner(server, filename)


def _retrieve_url(url, dest):
    saved_file, _ = urllib.request.urlretrieve(url, filename=dest)
    return saved_file


def _retrieve_data(url: str, filename: str, dest: str = None, force: bool = False):
    if dest is None:
        dest = defaults.get_examples_path()
    local_path = os.path.join(dest, os.path.basename(filename))
    if not force and os.path.isfile(local_path):
        return local_path
    local_path = _retrieve_url(url, local_path)
    return local_path


def download_file(
    filename: str, *directory: str, destination: Optional[str] = None, force: bool = False
):
    """Download a file from PyAnsys examples Github repo

    Parameters
    ----------
    filename: str
        Name of the file to download
    destination: Optional[str]
        Optional destination to download the directory to
    force: bool
        Flag to force download even if the file exists in cache
    directory: tuple[str]
        Path under the PyAnsys Github examples repo

    Returns
    -------
    Tuple[str, str]
        Tuple containing filepath to be used and the local filepath of the downloaded directory
        The two are different in case of containers.

    """
    url = _get_filepath_on_default_server(filename, *directory)
    local_path = _retrieve_data(url, filename, dest=destination, force=force)
    return local_path