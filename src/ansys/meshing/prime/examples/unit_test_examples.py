import os
from typing import Optional, Union

from .download import download_file

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

    unit_test_paths = [
        download_file(
            file, 'pyprimemesh', 'unit_test_examples', destination=destination, force=force
        )
        for file in FILE_NAMES
    ]

    return unit_test_paths
