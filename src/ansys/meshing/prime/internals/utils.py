"""Module for general utils of the project."""
import logging
import os
import shutil
import subprocess
from contextlib import contextmanager
from typing import List, Optional

import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.internals.defaults as defaults

_LOCAL_PORTS = []


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
        PID of the parent process.

    Returns
    -------
    List
        PIDs of the processes.
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
    """Terminates the given process.

    Parameters
    ----------
    process : subprocess
        Process to kill.
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
    """Print logs before running command.

    Parameters
    ----------
    logger : logging.Logger
        Logger where to print.
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
    """Print logs after running command.

    Parameters
    ----------
    logger : logging.Logger
        Logger where to print.
    command : str
        Command to run.
    ret : str
        type of the return of the command.
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


def launch_prime_github_container(
    mount_host: str = defaults.get_user_data_path(),
    mount_image: str = defaults.get_user_data_path_for_containers(),
    port: int = defaults.port(),
    name: str = 'ansys-prime-server',
    version: Optional[str] = None,
):
    """Launch a given container.

    Parameters
    ----------
    mount_host : str, optional
        IP where to mount the container, by default defaults.get_user_data_path().
    mount_image : str, optional
        Name of the path to mount the container,
        by default defaults.get_user_data_path_for_containers().
    port : int, optional
        Port to expose, by default defaults.port().
    name : str, optional
        Name of the container, by default 'ansys-prime-server'.
    version : Optional[str], optional
        Version of the container to retrieve, by default None.

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

    Upload a context to a model.

    Parameters
    ----------
    model : Model
        Model where to upload the context.
    file_names : str
        File containing the context.

    Yields
    ------
    str
        File name of the context.
    """
    if not os.path.exists(file_name):
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
    """Return True when a port is in use.

    Returns True when a port is in use at the given host.
    Must actually "bind" the address.  Just checking if we can create
    a socket is insufficient as it's possible to run into permission
    errors like:
    - An attempt was made to access a socket in a way forbidden by its
      access permissions.

    Parameters
    ----------
    port : int
        Port you want to check.
    host : str, optional
        IP you want to check, by default defaults.ip().

    Returns
    -------
    Bool
        Whether the port is available or not.
    """
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind((host, port))
            return False
        except:
            return True


def get_available_local_port(init_port: int = defaults.port()):
    """Get available port.

    Checks which ports are available and return the first one available.

    Parameters
    ----------
    init_port : int, optional
        Port from where to start searching, by default defaults.port().

    Returns
    -------
    int
        Available port.
    """
    port = init_port
    while port_in_use(port) or port in _LOCAL_PORTS:
        port += 1
    _LOCAL_PORTS.append(port)
    return port


@contextmanager
def file_read_context_list(model, file_names: List[str]):
    """Upload context.

    Upload a context to a model.

    Parameters
    ----------
    model : Model
        Model where to upload the context.
    file_names : List[str]
        Files that compose the context.

    Yields
    ------
    List[str]
        List of the context files.
    """
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

    Download context from model and write it to a local file.

    Parameters
    ----------
    model : Model
        Model from which to download context.
    file_name : str
        Name of the file.

    Yields
    ------
    str
        File name.
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
