import logging
import os
import subprocess
import sys
from typing import Optional

import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.internals.defaults as defaults
import ansys.meshing.prime.internals.utils as utils
from ansys.meshing.prime.internals.client import Client

try:
    import ansys.platform.instancemanagement as pypim
    from simple_upload_server.client import Client as FileClient

    config.set_has_pim(pypim.is_configured())
except ModuleNotFoundError:
    pass

__all__ = ['launch_prime', 'launch_server_process']


def get_install_locations():
    supported_versions = ['231']
    awp_roots = {ver: os.environ.get(f'AWP_ROOT{ver}', '') for ver in supported_versions}
    installed_versions = {
        ver: os.path.join(path, 'meshing', 'Prime')
        for ver, path in awp_roots.items()
        if path and os.path.isdir(path)
    }
    installed_versions = {
        ver: path for ver, path in installed_versions.items() if path and os.path.isdir(path)
    }
    if installed_versions:
        return installed_versions


def get_ansys_prime_server_root():
    available_versions = get_install_locations()
    if not available_versions:
        return None

    version = max(available_versions.keys())
    prime_root = available_versions[version]
    return prime_root


def launch_server_process(
    prime_root: Optional[str] = None,
    ip: str = defaults.ip(),
    port: int = defaults.port(),
    n_procs: Optional[int] = None,
    **kw,
) -> subprocess.Popen:
    '''Launch a server process for Ansys Prime Server.

    Parameters
    ----------
    prime_root: Optional[str]
        Root directory which contains the Ansys Prime Server.
    ip: str
        IP address to start the server at.  The default IP address is 127.0.0.1.
    port: int
        Port at which the server is started. The default port is 50055.
    n_procs: Optional[int]
        When running in distributed mode, specify the number of distributed
        processes to spawn. Process marked as Node 0 will host the GRPC
        server. If None is specified, server will be launched as the only
        process (normal mode).

    Returns
    -------
    subprocess.Popen
        The instance of the subprocess that is launched.

    Raises
    ------
    FileNotFoundError
        When there is an error in the file paths used to launch the server.
    '''
    if prime_root is None:
        prime_root = get_ansys_prime_server_root()
        if prime_root is None:
            raise FileNotFoundError('No valid Ansys Prime Server found to launch.')
    else:  # verify if the file exists
        if not os.path.isdir(prime_root):
            raise FileNotFoundError('Invalid exec_file path.')

    script_ext = 'bat' if os.name == 'nt' else 'sh'
    run_prime_script = f'runPrime.{script_ext}'

    exec_path = os.path.join(prime_root, run_prime_script)
    if not os.path.isfile(exec_path):
        raise FileNotFoundError(f'{run_prime_script} not found in {prime_root}')

    server_args = [exec_path, 'server']

    if kw is None:
        kw = {}

    enable_python_server = kw.get('server', 'release')
    if not isinstance(enable_python_server, str):
        raise ValueError(
            'Hidden option to run python server needs to be a string.'
            'Potential options are: release (default), debug and python'
        )

    enable_python_server = enable_python_server.lower()
    if enable_python_server not in ('python', 'release', 'debug'):
        raise ValueError('server option needs to be one of release, debug or python.')

    if enable_python_server == 'python':
        script_dir = os.path.join(prime_root, 'scripts')
        server_path = os.path.join(script_dir, 'PrimeGRPC.py')
        if not os.path.isfile(server_path):
            raise FileNotFoundError(f'PrimeGRPC.py not found in {script_dir}')
        server_args.append('-python')

    if enable_python_server == 'debug':
        server_args.append('-debug')

    server_args.append(f'--ip={ip}')
    server_args.append(f'--port={port}')
    if n_procs is not None and isinstance(n_procs, int):
        server_args.append(f'-np')
        server_args.append(f'{n_procs}')

    kwargs = {
        'stdin': subprocess.DEVNULL,
    }
    if "PRIME_ENABLE_VERBOSITY" not in os.environ:
        kwargs['stdout'] = subprocess.DEVNULL
        kwargs['stderr'] = subprocess.DEVNULL
    if sys.platform.startswith('win32'):
        kwargs['creationflags'] = subprocess.CREATE_NEW_PROCESS_GROUP

    logging.getLogger('PyPrimeMesh').info('Launching Ansys Prime Server')
    server = subprocess.Popen(server_args, **kwargs)
    return server


def launch_remote_prime(
    version: Optional[str] = None, timeout: float = defaults.connection_timeout()
):
    '''Create a remote instance of Prime server using PyPIM

    This method is used in case of Ansys Labs to create a remote instance of prime.
    This method also creates a file transfer service that is available on Ansys Labs
    '''
    if version is None:
        version = 'latest'

    pim = pypim.connect()
    instance = pim.create_instance(product_name='prime', product_version=version)
    instance.wait_for_ready()

    channel = instance.build_grpc_channel(
        options=[
            ('grpc.max_send_message_length', defaults.max_message_length()),
            ('grpc.max_receive_message_length', defaults.max_message_length()),
        ]
    )

    client = Client(channel=channel, timeout=timeout)
    file_service = FileClient(
        token='token',
        url=instance.services['http-simple-upload-server'].uri,
        headers=instance.services['http-simple-upload-server'].headers,
    )

    client.pim_client = pim
    client.remote_instance = instance
    model = client.model
    model._unfreeze()
    setattr(model, 'file_service', file_service)
    model._freeze()

    return client


def launch_prime(
    prime_root: Optional[str] = None,
    ip: str = defaults.ip(),
    port: int = defaults.port(),
    timeout: float = defaults.connection_timeout(),
    n_procs: Optional[int] = None,
    version: Optional[str] = None,
    **kwargs,
):
    '''Launch an instance of Ansys Prime Server and get a client for it.

    Parameters
    ----------
    prime_root: Optional[str]
        Root directory which contains the Ansys Prime Server.
    ip: str
        IP address to start the server at.  The default IP address is 127.0.0.1.
    port: int
        Port at which the server is started.  The default port is 50055.
    timeout: float
        Maximum time in seconds to wait for the client to connect to the server.
        The default is 10.0 seconds
    n_procs: Optional[int]
        When running in distributed mode, specify the number of distributed
        processes to spawn. Process marked as Node 0 will host the GRPC
        server. If None is specified, server will be launched as the only
        process (normal mode).

    Returns
    -------
    Client
        The instance of the client that is connected to the launched server.

    Raises
    ------
    FileNotFoundError
        When there is an error in file paths used to launch the server.
    ConnectionError
        When there is an error in connecting to the GRPC server.
    '''
    if config.has_pim():
        return launch_remote_prime(version=version, timeout=timeout)

    # Check for port availability on local host
    if ip == defaults.ip():
        port = utils.get_available_local_port(port)

    if 'PYPRIMEMESH_LAUNCH_CONTAINER' in os.environ:
        container_name = 'ansys-prime-server'
        utils.launch_prime_github_container(port=port, name=container_name, version=version)
        config.set_using_container(True)
        client = Client(port=port, timeout=timeout)
        client.container_name = container_name
        return client

    server = launch_server_process(
        prime_root=prime_root, ip=ip, port=port, n_procs=n_procs, **kwargs
    )

    return Client(server_process=server, ip=ip, port=port, timeout=timeout)
