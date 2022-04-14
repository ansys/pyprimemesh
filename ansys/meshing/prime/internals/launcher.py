import os
import sys
import subprocess
from typing import Optional
import logging

from ansys.meshing.prime.internals.client import Client
import ansys.meshing.prime.internals.defaults as defaults

__all__ = [ 'launch_prime', 'launch_server_process' ]

def get_install_locations():
    pyprime_root = os.environ.get('PYPRIME_ROOT', '')
    if os.path.isdir(pyprime_root):
        return { 'standalone': pyprime_root }

    supported_versions = [ '222' ]
    awp_roots = {
                 ver: os.environ.get(f'AWP_ROOT{ver}', '')
                 for ver in supported_versions
                }
    installed_versions = {
                          ver: os.path.join(path, 'meshing', 'pyprime')
                          for ver, path in awp_roots.items()
                          if path and os.path.isdir(path)
                         }
    installed_versions = {
                          ver: path
                          for ver, path in installed_versions.items()
                          if path and os.path.isdir(path)
                         }
    if installed_versions:
        return installed_versions


def port_in_use(port, host):
    """Returns True when a port is in use at the given host.
    Must actually "bind" the address.  Just checking if we can create
    a socket is insufficient as it's possible to run into permission
    errors like:
    - An attempt was made to access a socket in a way forbidden by its
      access permissions.
    """
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind((host, port))
            return False
        except:
            return True

def get_pyprime_root():
    available_versions = get_install_locations()
    if not available_versions:
        return None

    # If available versions contains standalone, this means PYPRIME_ROOT
    # was set and hence we prefer PYRPIME_ROOT versions
    if 'standalone' in available_versions:
        version = 'standalone'
        pyprime_root = available_versions['standalone']
    else:
        version = max(available_versions.keys())
        pyprime_root = available_versions[version]
        return pyprime_root

def launch_server_process(pyprime_root: Optional[str]=None,
                          ip: str=defaults.ip(),
                          port: int=defaults.port(),
                          n_procs: Optional[int]=None,
                          **kw) -> subprocess.Popen:
    '''Launch a server process for PyPRIME Server.

    Parameters
    ----------
    pyprime_root: Optional[str]
        Root directory which contains the PyPRIME server.
    ip: str
        IP address to start the server at. Default = 127.0.0.1.
    port: int
        Port at which the server is started. Default = 50055.
    n_procs: Optional[int]
        If running in distributed mode, specify the number of distributed
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
        If there is an error in file paths used to launch the server.
    '''
    if pyprime_root is None:
        pyprime_root = get_pyprime_root()
        if pyprime_root is None:
            raise FileNotFoundError('No valid PyPrime server found to launch.')
    else: # verify if the file exists
        if not os.path.isdir(pyprime_root):
            raise FileNotFoundError('Invalid exec_file path.')

    script_ext = 'bat' if os.name == 'nt' else 'sh'
    run_prime_script = f'runPrime.{script_ext}'

    exec_path = os.path.join(pyprime_root, run_prime_script)
    if not os.path.isfile(exec_path):
        raise FileNotFoundError(f'{run_prime_script} not found in {pyprime_root}')

    if kw is None:
        kw = {}

    enable_cpp_server = kw.get('cpp_server', None)
    if enable_cpp_server is None:
        server_path = os.path.join(pyprime_root, 'scripts', 'PrimeGRPC.py')
        if not os.path.isfile(server_path):
            script_dir = os.path.join(pyprime_root, 'scripts')
            raise FileNotFoundError(f'PrimeGRPC.py not found in {script_dir}')
    else:
        if not isinstance(enable_cpp_server, str):
            raise ValueError('Hidden option to run C++ server needs to be a string.'
                             'Potential options are: Debug, Release')
        if enable_cpp_server.lower() not in ('debug', 'release'):
            raise ValueError('cpp_server option needs to be either release or debug.')

    server_args = [ exec_path, 'server' ]
    if enable_cpp_server is not None:
        server_args.append('-cpp')
        if enable_cpp_server.lower() == 'debug':
            server_args.append('-debug')

    server_args.append(f'--ip={ip}')
    server_args.append(f'--port={port}')
    if n_procs is not None and isinstance(n_procs, int):
        server_args.append(f'-np={n_procs}')

    kwargs = {
        'stdin': subprocess.DEVNULL,
        'stdout': subprocess.DEVNULL,
        'stderr': subprocess.DEVNULL,
    }
    if sys.platform.startswith('win32'):
        kwargs['creationflags'] = subprocess.CREATE_NEW_PROCESS_GROUP

    logging.getLogger('PyPrime').info('Launching PyPrime Server')
    server = subprocess.Popen(server_args, **kwargs)
    return server

def launch_prime(pyprime_root: Optional[str]=None,
                 ip: str=defaults.ip(),
                 port: int=defaults.port(),
                 timeout: float=defaults.connection_timeout(),
                 n_procs: Optional[int]=None, **kwargs):
    '''Launch an instance of PyPRIME server and get a client for it

    Parameters
    ----------
    pyprime_root: Optional[str]
        Root directory which contains the PyPRIME server.
    ip: str
        IP address to start the server at. Default = 127.0.0.1.
    port: int
        Port at which the server is started. Default = 50055.
    timeout: float
        Maximum time in seconds to wait for the client to connect to the server.
        Default = 10.0 seconds
    n_procs: Optional[int]
        If running in distributed mode, specify the number of distributed
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
        If there is an error in file paths used to launch the server.
    ConnectionError
        If there is an error in connecting to the GRPC server.
    '''
    server = launch_server_process(pyprime_root=pyprime_root,
                                   ip=ip,
                                   port=port,
                                   n_procs=n_procs,
                                   **kwargs)

    return Client(server_process=server, ip=ip, port=port, timeout=timeout)
