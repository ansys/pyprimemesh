# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
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

"""Module for general utilities of the project."""
import logging
import os
import shutil
import subprocess
import uuid
from contextlib import contextmanager
from typing import List, Optional

import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.internals.defaults as defaults

_LOCAL_PORTS = []


def make_unique_container_name(name: str):
    """Make a unique container name.

    Parameters
    ----------
    name : str
        Original name prefix that is provided.

    Returns
    -------
    str
        Unique name with a numeric integer added as suffix.
    """
    return f'{name}-' + str(uuid.uuid4())


def to_camel_case(snake_str):
    """Transform snake_case string to camelCase.

    Parameters
    ----------
    snake_str : str
        snake_case string.

    Returns
    -------
    str
        String converted to camelCase.
    """
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


def get_child_processes(process):
    """Get child processes of a process.

    Parameters
    ----------
    process : int
        Process ID of the parent process.

    Returns
    -------
    List
        Process IDs of the processes.
    """
    children = []
    cmd = subprocess.Popen("pgrep -P %d" % process, shell=True, stdout=subprocess.PIPE)
    out = cmd.stdout.read().decode("utf-8")
    cmd.wait()
    for pid in out.split("\n")[:1]:
        if pid.strip() == '':
            break
        ps_cmd = subprocess.Popen(
            "ps -o cmd= {}".format(int(pid)), stdout=subprocess.PIPE, shell=True
        )
        ps_out = ps_cmd.stdout.read().decode("utf-8")
        ps_cmd.wait()
        cmd_name = ps_out.split()[0]
        if "AnsysPrimeServer" in cmd_name:
            children.append(int(pid))
        else:
            children += get_child_processes(int(pid))
    return children


def terminate_process(process: subprocess):
    """Terminates a process.

    Parameters
    ----------
    process : subprocess
        Process to terminate.
    """
    import signal
    import sys

    if sys.platform.startswith('win32'):
        # process.send_signal(signal.CTRL_C_EVENT)
        process.send_signal(signal.CTRL_BREAK_EVENT)
    else:
        for child in get_child_processes(process.pid):
            os.kill(child, signal.SIGTERM)

    if process.stdin is not None:
        process.stdin.close()
    if process.stdout is not None:
        process.stdout.close()
    if process.stderr is not None:
        process.stderr.close()
    process.terminate()
    process.wait()


def print_logs_before_command(logger: logging.Logger, command: str, args):
    """Print logs before running a command.

    Parameters
    ----------
    logger : logging.Logger
        Logger to print to.
    command : str
        Command to run.
    args : str
        Arguments of the command.
    """
    logger.info("Executing " + command)
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Command: " + command)
        logger.debug("Args:")
        for key in args:
            logger.debug("    " + key + ":")
            val = args[key]
            printable_str = ""
            if hasattr(val, '__str__'):
                printable_str = val.__str__()
            elif type(val) == 'str':
                printable_str = val
            else:
                printable_str = str(val)
            for line in printable_str.splitlines():
                logger.debug("        " + line)
        logger.debug("")


def print_logs_after_command(logger: logging.Logger, command: str, ret):
    """Print logs after running a command.

    Parameters
    ----------
    logger : logging.Logger
        Logger to print to.
    command : str
        Command to run.
    ret : str
        Return type of the command.
    """
    logger.info("Finished " + command)
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Return: ")
        printable_str = ""
        if hasattr(ret, '__str__'):
            printable_str = ret.__str__()
        elif type(ret) == 'str':
            printable_str = ret
        else:
            printable_str = str(ret)
        for line in printable_str.splitlines():
            logger.debug("        " + line)
        logger.debug("")


def print_beta_api_warning(logger: logging.Logger, command: str):
    """Print warning for beta API.

    Parameters
    ----------
    logger : logging.Logger
        Logger to print to.
    command : str
        Command to run.
    """
    if logger.isEnabledFor(logging.WARNING):
        logger.warning(
            f"This {command} is a beta API. The behavior and implementation may change in future."
        )


def launch_prime_github_container(
    mount_host: str = defaults.get_user_data_path(),
    mount_image: str = defaults.get_user_data_path_for_containers(),
    port: int = defaults.port(),
    name: str = "ansys-prime-server",
    version: Optional[str] = None,
):
    """Launch a container.

    Parameters
    ----------
    mount_host : str, optional
        IP address for the container to mount. The default is ``defaults.get_user_data_path()``.
    mount_image : str, optional
        Name of the path to the container to mount. The default is
        ``defaults.get_user_data_path_for_containers()``.
    port : int, optional
        Port to expose. The default is ``defaults.port()``.
    name : str, optional
        Name of the container. The default is ``"ansys-prime-server"``.
    version : str, optional
        Version of the container to retrieve. The default is ``None``.

    Raises
    ------
    ValueError
        License is not available.
    """
    license_file = os.environ.get('ANSYSLMD_LICENSE_FILE', None)
    image_name = os.environ.get('PYPRIMEMESH_IMAGE_NAME', 'ghcr.io/ansys/prime')
    if license_file is None:
        raise ValueError('Licensing information to launch container not found')
    if version is None:
        version = os.environ.get('PYPRIMEMESH_IMAGE_TAG', 'latest')
    docker_command = [
        'docker',
        'run',
        '-d',
        '--rm',
        '--name',
        f'{name}',
        '-p',
        f'{port}:{port}',
        '-v',
        f'{mount_host}:{mount_image}',
        '-e',
        f'ANSYSLMD_LICENSE_FILE={license_file}',
        f'{image_name}:{version}',
        '--port',
        f'{port}',
    ]
    subprocess.run(docker_command, stdout=subprocess.DEVNULL)


def stop_prime_github_container(name):
    """Stop a running container.

    Parameters
    ----------
    name : str
        Name of the container.
    """
    subprocess.run(['docker', 'stop', f'{name}'], stdout=subprocess.DEVNULL)


@contextmanager
def file_read_context(model, file_name: str):
    """Upload context.

    Upload context to a model.

    Parameters
    ----------
    model : Model
        Model to upload the context to.
    file_name : str
        Name of the file containing the context.

    Yields
    ------
    str
        File name of the context.
    """
    if config.file_existence_check_enabled() and not os.path.exists(file_name):
        raise FileNotFoundError(f'Given file name "{file_name}" is not found on local disk')
    if config.using_container():
        base_file_name = os.path.basename(file_name)
        temp_file_name = os.path.join(defaults.get_examples_path(), base_file_name)
        is_copy: bool = file_name != temp_file_name
        if is_copy:
            shutil.copyfile(file_name, temp_file_name)
        container_file_name = os.path.join(
            defaults.get_examples_path_for_containers(), base_file_name
        )
        container_file_name = container_file_name.replace(os.path.sep, '/')
        yield container_file_name
        if is_copy:
            os.remove(temp_file_name)
    elif config.has_pim():
        temp_file_name = os.path.basename(file_name)
        model.file_service.upload_file(file_name)
        yield temp_file_name
    else:
        yield file_name


def port_in_use(port, host=defaults.ip()):
    """Check if a port is in use on a given host.

    This method must actually check is is a "bind" of the port to the
    address. Just checking if a socket can be created is insufficient
    because it's possible to run into permission errors like this one:

    - An attempt was made to access a socket in a way forbidden by its
      access permissions.

    Parameters
    ----------
    port : int
        Port to check.
    host : str, optional
        IP address to check. The default is ``defaults.ip()``.

    Returns
    -------
    bool
        ``True`` if the port is in use, ``False`` if the port is available.
    """
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind((host, port))
            return False
        except:
            return True


def get_available_local_port(init_port: int = defaults.port()):
    """Get which ports are available and return the first one.

    Parameters
    ----------
    init_port : int, optional
        Port to start the search from. The default is ``defaults.port()```.

    Returns
    -------
    int
        First available port.
    """
    port = init_port
    import socket

    s = socket.socket()
    s.bind(("", 0))
    port = s.getsockname()[1]
    s.close()
    return port


@contextmanager
def file_read_context_list(model, file_names: List[str]):
    """Upload context.

    Upload context to a model.

    Parameters
    ----------
    model : Model
        Model to upload context to.
    file_names : List[str]
        List of files with the context.

    Yields
    ------
    List[str]
        List of context files.
    """
    if config.file_existence_check_enabled():
        for file in file_names:
            if not os.path.exists(file):
                error_msg = f"File {file} given for read is missing from local disk."
                raise FileNotFoundError(error_msg)
    if config.using_container():
        base_names = [os.path.basename(file) for file in file_names]
        temp_names = [os.path.join(defaults.get_examples_path(), base) for base in base_names]
        for file, temp in zip(file_names, temp_names):
            shutil.copyfile(file, temp)
        container_files = [
            os.path.join(defaults.get_examples_path_for_containers(), base) for base in base_names
        ]
        container_files = [file.replace(os.path.sep, '/') for file in container_files]
        yield container_files
        for temp_file in temp_names:
            os.remove(temp_file)
    elif config.has_pim():
        temp_files = [os.path.basename(file) for file in file_names]
        for file in file_names:
            model.file_service.upload_file(file)
        yield temp_files
    else:
        yield file_names


@contextmanager
def file_write_context(model, file_name: str):
    """Download context.

    Download context from a model and write it to a local file.

    Parameters
    ----------
    model : Model
        Model to download context from.
    file_name : str
        Name of the file to write the context to.

    Yields
    ------
    str
        Name of the file to which context has been written.
    """
    if config.using_container():
        base_file_name = os.path.basename(file_name)
        temp_file_name = os.path.join(defaults.get_output_path_for_containers(), base_file_name)
        temp_file_name = temp_file_name.replace(os.path.sep, '/')
        if not os.path.exists(defaults.get_output_path()):
            os.makedirs(defaults.get_output_path())
        yield temp_file_name
        # Copy temp_file_name to directory which was asked
        local_file_name = os.path.join(defaults.get_output_path(), base_file_name)
        shutil.copyfile(local_file_name, file_name)
        os.remove(local_file_name)
    elif config.has_pim():
        temp_file_name = os.path.basename(file_name)
        file_dir = os.path.dirname(file_name)
        yield temp_file_name
        model.file_service.download_file(temp_file_name, file_dir)
    else:
        yield file_name
