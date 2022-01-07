import os
import subprocess

from ansys.meshing.prime.internals.client import Client
__all__ = [ 'launch_prime', 'PrimeServerLaunchError' ]

class PrimeServerLaunchError(RuntimeError):
    def __init__(self, msg='Timed out while launching server'):
        RuntimeError.__init__(self, msg)

__LOCALHOST = '127.0.0.1'
__DEFAULT_PORT = 50055

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
        return None, 'not-found'

    # If available versions contains standalone, this means PYPRIME_ROOT
    # was set and hence we prefer PYRPIME_ROOT versions
    if 'standalone' in available_versions:
        version = 'standalone'
        pyprime_root = available_versions['standalone']
    else:
        version = max(available_versions.keys())
        pyprime_root = available_versions[version]
        return pyprime_root

def launch_prime(pyprime_root: str=None,
                 ip: str=__LOCALHOST,
                 port: int=__DEFAULT_PORT):
    if pyprime_root is None:
        pyprime_root = get_pyprime_root()
        if pyprime_root is None:
            raise FileNotFoundError('Invalid exec_file path.')
    else: # verify if the file exists
        if not os.path.isdir(pyprime_root):
            raise FileNotFoundError('Invalid exec_file path.')

    server_path = os.path.join(pyprime_root, 'scripts', 'PrimeGRPC.py')
    if not os.path.isfile(server_path):
        script_dir = os.path.join(pyprime_root, 'scripts')
        raise FileNotFoundError(f'PrimeGRPC.py not found in {script_dir}')

    script_ext = 'bat' if os.name == 'nt' else 'sh'
    run_prime_script = f'runPrime.{script_ext}'

    exec_path = os.path.join(pyprime_root, run_prime_script)
    if not os.path.isfile(exec_path):
        raise FileNotFoundError(f'{run_prime_script} not found in {pyprime_root}')

    server = subprocess.Popen(
        [
            exec_path,
            server_path,
            f'--ip={ip}',
            f'--port={port}'
        ],
    )

    return Client(server_process=server, ip=ip, port=port)
