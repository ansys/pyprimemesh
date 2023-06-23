"""Examples module for PyPrimeMesh
"""
import os
from enum import Enum
from typing import Optional, Union

from .download_utilities import DownloadManager

__all__ = [
    'get_file',
    "download_bracket_dsco",
    "download_bracket_fmd",
    "download_bracket_scdoc",
    "download_deformed_blade_dsco",
    "download_deformed_blade_fmd",
    "download_deformed_blade_scdoc",
    "download_elbow_pmdat",
    "download_elbow_fmd",
    "download_elbow_scdoc",
    "download_elbow_dsco",
    "download_toy_car_fmd",
    "download_toy_car_pmdat",
    "download_toy_car_scdoc",
    "download_toy_car_dsco",
    "download_pipe_tee_fmd",
    "download_pipe_tee_fmd",
    "download_pipe_tee_dsco",
    "download_toy_car_scdoc",
    "download_pcb_pmdat",
]


class Examples(Enum):
    """Contains the available PyPrimeMesh examples to download."""

    ELBOW_PMDAT = {"filename": "mixing_elbow.pmdat", "git_folder": "mixing_elbow"}
    ELBOW_FMD = {"filename": "mixing_elbow.fmd", "git_folder": "mixing_elbow"}
    ELBOW_SCDOC = {"filename": "mixing_elbow.scdoc", "git_folder": "mixing_elbow"}
    ELBOW_DSCO = {"filename": "mixing_elbow.dsco", "git_folder": "mixing_elbow"}
    BRACKET_FMD = {"filename": "bracket_mid_surface.fmd", "git_folder": "bracket_scaffold"}
    BRACKET_SCDOC = {"filename": "bracket_mid_surface.scdoc", "git_folder": "bracket_scaffold"}
    BRACKET_DSCO = {"filename": "bracket_mid_surface.dsco", "git_folder": "bracket_scaffold"}
    TOY_CAR_PMDAT = {"filename": "toy_car.pmdat", "git_folder": "toy_car"}
    TOY_CAR_FMD = {"filename": "toy_car.fmd", "git_folder": "toy_car"}
    TOY_CAR_SCDOC = {"filename": "toy_car.scdoc", "git_folder": "toy_car"}
    TOY_CAR_DSCO = {"filename": "toy_car.dsco", "git_folder": "toy_car"}
    PIPE_TEE_PMDAT = {"filename": "pipe_tee.pmdat", "git_folder": "pipe_tee"}
    PIPE_TEE_FMD = {"filename": "pipe_tee.fmd", "git_folder": "pipe_tee"}
    PIPE_TEE_SCDOC = {"filename": "pipe_tee.scdoc", "git_folder": "pipe_tee"}
    PIPE_TEE_DSCO = {"filename": "pipe_tee.dsco", "git_folder": "pipe_tee"}
    DEFORMED_BLADE_FMD = {"filename": "blade_deformed.fmd", "git_folder": "turbine_blade"}
    DEFORMED_BLADE_SCDOC = {"filename": "blade_deformed.scdoc", "git_folder": "turbine_blade"}
    DEFORMED_BLADE_DSCO = {"filename": "blade_deformed.dsco", "git_folder": "turbine_blade"}
    TURBINE_BLADE_CDB = {"filename": "blade.cdb", "git_folder": "turbine_blade"}
    PCB_PMDAT = {"filename": "pcb_stacker.pmdat", "git_folder": "pcb"}


_DOWNLOADS = []


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
    download_manager = DownloadManager()
    if destination is not None and not os.path.isdir(destination):
        raise ValueError('destination directory provided does not exist')
    file = download_manager.download_file(
        example.value["filename"],
        'pyprimemesh',
        example.value["git_folder"],
        destination=destination,
        force=force,
    )

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


def download_elbow_dsco(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download DSCO file for the mixing elbow example

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

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     elbow = prime_examples.download_elbow_dsco()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(elbow, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.ELBOW_DSCO, destination, force)


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


def download_bracket_dsco(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download DSCO file for the bracket scaffold example

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

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     bracket = prime_examples.download_bracket_dsco()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(bracket, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.BRACKET_DSCO, destination, force)


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


def download_toy_car_dsco(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download DSCO file for the toy car example

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

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     toy_car = prime_examples.download_toy_car_dsco()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(toy_car, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.TOY_CAR_DSCO, destination, force)


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


def download_pipe_tee_dsco(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download DSCO file for the pipe tee example

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

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     pipe_tee = prime_examples.download_pipe_tee_dsco()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(pipe_tee, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.PIPE_TEE_DSCO, destination, force)


def download_deformed_blade_fmd(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download FMD file for the turbine blade example

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

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     deformed_blade = prime_examples.download_deformed_blade_fmd()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(deformed_blade, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.DEFORMED_BLADE_FMD, destination, force)


def download_deformed_blade_scdoc(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download SCDOC file for the turbine blade example

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

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     deformed_blade = prime_examples.download_deformed_blade_scdoc()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(deformed_blade, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.DEFORMED_BLADE_SCDOC, destination, force)


def download_deformed_blade_dsco(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download DSCO file for the turbine blade example

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

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     deformed_blade = prime_examples.download_deformed_blade_dsco()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(deformed_blade, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.DEFORMED_BLADE_DSCO, destination, force)


def download_turbine_blade_cdb(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download CDB file for the turbine blade example

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

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     turbine_blade_mesh = prime_examples.download_turbine_blade_cdb()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_mapdl_cdb(
    >>>             turbine_blade_mesh,
    >>>             params=prime.ImportMapdlCdbParams(model),
    >>>         )
    >>>     print(model)

    """
    return get_file(Examples.TURBINE_BLADE_CDB, destination, force)


def download_pcb_pmdat(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download PMDAT file for the pcb example

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

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     pcb = prime_examples.download_pcb_pmdat()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.read_pmdat(pcb, params=prime.FileReadParams(model))
    >>>     print(model)

    """
    return get_file(Examples.PCB_PMDAT, destination, force)
