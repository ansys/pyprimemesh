import os
from typing import Optional, Union

from .download_utilities import DownloadManager

FILE_NAMES = [
    "box.psf",
    "box.sf",
    "file.cas",
    "file.pdmat",
    "file.pmdat",
    "hex.cas",
    "hex.cdb",
    "hex.fmd",
    "hex.msh",
]


def download_test_examples(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download files necessary for unit testing.

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
    List[str]
        Local paths to the downloaded files

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     examples = prime_examples.unit_test_examples.download_test_examples()


    """

    download_manager = DownloadManager()
    unit_test_paths = [
        download_manager.download_file(
            file, 'pyprimemesh', 'unit_test_examples', destination=destination, force=force
        )
        for file in FILE_NAMES
    ]
    return unit_test_paths
