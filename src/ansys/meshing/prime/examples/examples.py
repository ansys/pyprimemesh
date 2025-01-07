# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Examples module for PyPrimeMesh.
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
    "download_pipe_tee_pmdat",
    "download_pipe_tee_scdoc",
    "download_pipe_tee_dsco",
    "download_turbine_blade_cdb",
    "download_pcb_pmdat",
    "download_pcb_scdoc",
    "download_saddle_bracket_fmd",
    "download_saddle_bracket_scdoc",
    "download_saddle_bracket_dsco",
    "download_f1_rw_drs_stl",
    "download_f1_rw_enclosure_stl",
    "download_f1_rw_end_plates_stl",
    "download_f1_rw_main_plane_stl",
    "download_multi_layer_quad_mesh_pcb_dsco",
    "download_multi_layer_quad_mesh_pcb_pmdb",
    "download_multi_layer_quad_mesh_pcb_fmd",
    "download_multi_layer_quad_mesh_pcb_scdoc",
    "download_multi_layer_quad_mesh_pcb_pmdat",
    "download_block_model_scdoc",
    "download_block_model_fmd",
    "download_block_model_pmdat",
    "download_wheel_ground_scdoc",
    "download_wheel_ground_fmd",
    "download_wheel_ground_dsco",
    "download_solder_ball_fmd",
    "download_solder_ball_target_fmd",
]


class Examples(Enum):
    """Contains the PyPrimeMesh examples available for download."""

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
    PCB_SCDOC = {"filename": "pcb_stacker.scdoc", "git_folder": "pcb"}
    SADDLE_BRACKET_FMD = {"filename": "saddle_bracket.fmd", "git_folder": "saddle_bracket"}
    SADDLE_BRACKET_SCDOC = {"filename": "saddle_bracket.scdoc", "git_folder": "saddle_bracket"}
    SADDLE_BRACKET_DSCO = {"filename": "saddle_bracket.dsco", "git_folder": "saddle_bracket"}
    F1_RW_DRS_STL = {"filename": "f1_rw_drs.stl", "git_folder": "f1_rear_wing"}
    F1_RW_END_PLATES_STL = {"filename": "f1_rw_enclosure.stl", "git_folder": "f1_rear_wing"}
    F1_RW_ENCLOSURE_STL = {"filename": "f1_rw_end_plates.stl", "git_folder": "f1_rear_wing"}
    F1_RW_MAIN_PLANE_STL = {"filename": "f1_rw_main_plane.stl", "git_folder": "f1_rear_wing"}
    MULTI_LAYER_MESH_PCB_DSCO = {
        "filename": "multi_layer_quad_mesh_pcb.dsco",
        "git_folder": "multi_layer_quad_mesh_pcb",
    }
    MULTI_LAYER_MESH_PCB_PMDB = {
        "filename": "multi_layer_quad_mesh_pcb.pmdb",
        "git_folder": "multi_layer_quad_mesh_pcb",
    }
    MULTI_LAYER_MESH_PCB_FMD = {
        "filename": "multi_layer_quad_mesh_pcb.fmd",
        "git_folder": "multi_layer_quad_mesh_pcb",
    }
    MULTI_LAYER_MESH_PCB_SCDOC = {
        "filename": "multi_layer_quad_mesh_pcb.scdoc",
        "git_folder": "multi_layer_quad_mesh_pcb",
    }
    MULTI_LAYER_MESH_PCB_PMDAT = {
        "filename": "multi_layer_quad_mesh_pcb.pmdat",
        "git_folder": "multi_layer_quad_mesh_pcb",
    }
    BLOCK_MODEL_SCDOC = {"filename": "pyprime_block_import.scdoc", "git_folder": "block_model"}
    BLOCK_MODEL_FMD = {"filename": "pyprime_block_import.fmd", "git_folder": "block_model"}
    BLOCK_MODEL_PMDAT = {"filename": "pyprime_block_import.pmdat", "git_folder": "block_model"}
    WHEEL_GROUND_SCDOC = {"filename": "wheel_ground.scdoc", "git_folder": "wheel_ground"}
    WHEEL_GROUND_FMD = {"filename": "wheel_ground.fmd", "git_folder": "wheel_ground"}
    WHEEL_GROUND_DSCO = {"filename": "wheel_ground.dsco", "git_folder": "wheel_ground"}
    SOLDER_BALL_FMD = {"filename": "solder_ball.fmd", "git_folder": "solder_ball"}
    SOLDER_BALL_TARGET_FMD = {"filename": "solder_ball_target.fmd", "git_folder": "solder_ball"}


_DOWNLOADS = []


def get_file(
    example: Examples,
    destination: Optional[str] = None,
    force: bool = False,
) -> Union[str, os.PathLike]:
    """Download a PyPrimeMesh example file from the GitHub repository.

    Parameters
    ----------
    example : Examples
        Name of the example file to be downloaded.
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

    Raises
    ------
    ValueError
        When the provided destination path for the example file does not exist.
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
    """Download the PMDAT file for the mixing elbow example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the FMD file for the mixing elbow example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the SCDOC file for the mixing elbow example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the DSCO file for the mixing elbow example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the FMD file for the bracket scaffold example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the SCDOC file for the bracket scaffold example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the DSCO file for the bracket scaffold example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the PMDAT file for the toy car example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the FMD file for the toy car example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the SCDOC file for the toy car example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the DSCO file for the toy car example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the PMDAT file for the pipe tee example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the FMD file for the pipe tee example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Option to  download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the SCDOC file for the pipe tee example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the DSCO file for the pipe tee example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the FMD file for the turbine blade example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the SCDOC file for the turbine blade example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the DSCO file for the turbine blade example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the CDB file for the turbine blade example.

    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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
    """Download the PMDAT file for the PCB example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded example file.

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


def download_pcb_scdoc(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download SCDOC file for the pcb example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     pcb = prime_examples.download_pcb_scdoc()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(pcb, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.PCB_SCDOC, destination, force)


def download_saddle_bracket_fmd(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download FMD file for the saddle bracket example

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     saddle_bracket = prime_examples.download_saddle_bracket_fmd()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(saddle_bracket, params=prime.ImportCADParams(model))
    >>>     print(model)

    """

    return get_file(Examples.SADDLE_BRACKET_FMD, destination, force)


def download_saddle_bracket_scdoc(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download SCDOC file for the saddle bracket example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     saddle_bracket = prime_examples.download_saddle_bracket_scdoc()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(saddle_bracket, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.SADDLE_BRACKET_SCDOC, destination, force)


def download_saddle_bracket_dsco(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download DSCO file for the saddle bracket example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     saddle_bracket = prime_examples.download_saddle_bracket_dsco()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(saddle_bracket, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.SADDLE_BRACKET_DSCO, destination, force)


def download_f1_rw_drs_stl(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download STL file for the generic f1 rear wing example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     f1_rw_drs = prime_examples.download_f1_rw_drs_stl()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(f1_rw_drs, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.F1_RW_DRS_STL, destination, force)


def download_f1_rw_enclosure_stl(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download STL file for the generic f1 rear wing example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     f1_rw_enclosure = prime_examples.download_f1_rw_enclosure_stl()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(f1_rw_enclosure, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.F1_RW_ENCLOSURE_STL, destination, force)


def download_f1_rw_end_plates_stl(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download STL file for the generic f1 rear wing example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     f1_rw_end_plates = prime_examples.download_f1_rw_end_plates_stl()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(f1_rw_end_plates, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.F1_RW_END_PLATES_STL, destination, force)


def download_f1_rw_main_plane_stl(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download STL file for the generic f1 rear wing example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     f1_rw_main_plane = prime_examples.download_f1_rw_main_plane_stl()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(f1_rw_main_plane, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.F1_RW_MAIN_PLANE_STL, destination, force)


def download_multi_layer_quad_mesh_pcb_dsco(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download the DSCO file for the multi-layer PCB meshing example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     cad_file = prime_examples.download_multi_layer_quad_mesh_pcb_dsco()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(cad_file, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.MULTI_LAYER_MESH_PCB_DSCO, destination, force)


def download_multi_layer_quad_mesh_pcb_pmdb(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download the PMDB file for the multi-layer PCB meshing example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     cad_file = prime_examples.download_multi_layer_quad_mesh_pcb_pmdb()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(cad_file, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.MULTI_LAYER_MESH_PCB_PMDB, destination, force)


def download_multi_layer_quad_mesh_pcb_scdoc(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download the SCDOC file for the multi-layer PCB meshing example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     cad_file = prime_examples.download_multi_layer_quad_mesh_pcb_scdoc()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(cad_file, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.MULTI_LAYER_MESH_PCB_SCDOC, destination, force)


def download_multi_layer_quad_mesh_pcb_fmd(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download the FMD file for the multi-layer PCB meshing example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     cad_file = prime_examples.download_multi_layer_quad_mesh_pcb_fmd()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(cad_file, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.MULTI_LAYER_MESH_PCB_FMD, destination, force)


def download_multi_layer_quad_mesh_pcb_pmdat(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download the PMDAT file for the multi-layer PCB meshing example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     cad_file = prime_examples.download_multi_layer_quad_mesh_pcb_pmdat()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.read_pmdat(cad_file, params=prime.FileReadParams(model))
    >>>     print(model)

    """
    return get_file(Examples.MULTI_LAYER_MESH_PCB_PMDAT, destination, force)


def download_block_model_scdoc(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download CAD file for the block model example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     block_model = prime_examples.download_block_model_scdoc()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(block_model, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.BLOCK_MODEL_SCDOC, destination, force)


def download_block_model_fmd(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download CAD file for the block model example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     block_model = prime_examples.download_block_model_fmd()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(block_model, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.BLOCK_MODEL_FMD, destination, force)


def download_block_model_pmdat(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download PMDAT file for the block model example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     block_model = prime_examples.download_block_model_pmdat()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.read_pmdat(block_model, params=prime.FileReadParams(model))
    >>>     print(model)

    """
    return get_file(Examples.BLOCK_MODEL_PMDAT, destination, force)


def download_wheel_ground_scdoc(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download the SCDOC file for the wheel ground contact patch example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     wheel_ground = prime_examples.download_wheel_ground_scdoc()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(wheel_ground, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.WHEEL_GROUND_SCDOC, destination, force)


def download_wheel_ground_fmd(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download the FMD file for the wheel ground contact patch example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     wheel_ground = prime_examples.download_wheel_ground_fmd()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(wheel_ground, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.WHEEL_GROUND_FMD, destination, force)


def download_wheel_ground_dsco(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download the DSCO file for the wheel ground contact patch example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     wheel_ground = prime_examples.download_wheel_ground_dsco()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(wheel_ground, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.WHEEL_GROUND_DSCO, destination, force)


def download_solder_ball_fmd(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download a FMD file for the solder ball example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     solder_ball = prime_examples.download_solder_ball_fmd()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(solder_ball, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.SOLDER_BALL_FMD, destination, force)


def download_solder_ball_target_fmd(
    destination: Optional[str] = None, force: bool = False
) -> Union[str, os.PathLike]:
    """Download a FMD file for the solder ball example.

    Parameters
    ----------
    destination : str, optional
        Path to download the example file to. The default
        is ``None``, in which case the default path for app data
        is used.
    force : bool, optional
        Whether to download the example file. The default is
        ``False``, in which case if the example file is cached, it
        is reused.

    Returns
    -------
    str
        Local path to the downloaded file.

    Examples
    --------
    >>> import ansys.meshing.prime as prime
    >>> import ansys.meshing.prime.examples as prime_examples
    >>> with prime.launch_prime() as session:
    >>>     model = session.model
    >>>     solder_ball_target = prime_examples.download_solder_ball_target_fmd()
    >>>     with prime.FileIO(model) as io:
    >>>         _ = io.import_cad(solder_ball_target, params=prime.ImportCADParams(model))
    >>>     print(model)

    """
    return get_file(Examples.SOLDER_BALL_TARGET_FMD, destination, force)
