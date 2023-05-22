import os
import urllib.request
from threading import Lock
from typing import Optional
from urllib.parse import urljoin

import ansys.meshing.prime.internals.defaults as defaults

__all__ = ['DownloadManager']


class DownloadManagerMeta(type):
    """
    This is a thread-safe implementation of Singleton, from
    https://refactoring.guru/design-patterns/singleton/python/example#example-1
    """

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class DownloadManager(metaclass=DownloadManagerMeta):
    """Singleton class to manage the file downloads of the module.
    Local paths are saved in this class so we can do a global cleanup when
    closing the client.
    """

    def __init__(self):
        self.downloads_list = []

    def add_file(self, file_path: str):
        """Adds downloaded file path to a list to keep track of where the downloaded
        files are. This will be used for cleaning up the downloads.

        Parameters
        ----------
        file_path : str
            Local path of the downloaded file.
        """
        self.downloads_list.append(file_path)

    def clear_download_cache(self):
        """Removes the downloaded files from the local."""
        for file in self.downloads_list:
            os.remove(file)
        self.downloads_list.clear()

    def download_file(
        self, filename: str, *directory: str, destination: Optional[str] = None, force: bool = False
    ) -> str:
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
        # if destination is not a dir create it
        if destination is not None and not os.path.isdir(destination):
            os.mkdir(destination)

        # check if it was able to create the dir
        if destination is not None and not os.path.isdir(destination):
            raise ValueError('destination directory provided does not exist')

        url = self._get_filepath_on_default_server(filename, *directory)
        local_path = self._retrieve_data(url, filename, dest=destination, force=force)

        # add path to downloaded files
        self.add_file(local_path)
        return local_path

    def _joinurl(self, base, *paths):
        for path in paths:
            if base[-1] != '/':
                base += '/'
            base = urljoin(base, path)
        return base

    def _get_default_server_and_joiner(self):
        return 'https://github.com/ansys/example-data/raw/master', self._joinurl

    def _get_filepath_on_default_server(self, filename: str, *directory: str):
        server, joiner = self._get_default_server_and_joiner()
        if directory:
            return joiner(server, *directory, filename)
        else:
            return joiner(server, filename)

    def _retrieve_url(self, url, dest):
        saved_file, _ = urllib.request.urlretrieve(url, filename=dest)
        return saved_file

    def _retrieve_data(self, url: str, filename: str, dest: str = None, force: bool = False):
        if dest is None:
            dest = defaults.get_examples_path()
        local_path = os.path.join(dest, os.path.basename(filename))
        if not force and os.path.isfile(local_path):
            return local_path
        local_path = self._retrieve_url(url, local_path)
        return local_path
