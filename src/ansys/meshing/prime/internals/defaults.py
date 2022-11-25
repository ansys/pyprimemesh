'''The default configuration for the PyPrimeMesh library.
'''

__all__ = [
    'ip',
    'port',
    'connection_timeout',
    'print_communicator_stats',
    'max_message_length',
    'get_examples_path',
    'get_examples_path_for_containers',
    'get_output_path',
    'get_output_path_for_containers',
]

import os

try:
    import appdirs

    USER_DATA_PATH = os.getenv(
        'PYPRIMEMESH_USER_DATA', appdirs.user_data_dir(appname='pyprimemesh', appauthor=False)
    )
except ModuleNotFoundError:
    # If appdirs is not installed, then try with tempfile.
    # NOTE: This only occurs for ADO ARM Test runs
    import tempfile

    USER_DATA_PATH = os.getenv(
        'PYPRIMEMESH_USER_DATA', os.path.join(tempfile.gettempdir(), 'pyprimemesh')
    )

if not os.path.exists(USER_DATA_PATH):  # pragma: no cover
    os.makedirs(USER_DATA_PATH)

EXAMPLES_PATH = os.path.join(USER_DATA_PATH, 'examples')
if not os.path.exists(EXAMPLES_PATH):  # pragma: no cover
    os.makedirs(EXAMPLES_PATH)

LOCAL_OUTDIR = os.path.join(USER_DATA_PATH, 'output')
if not os.path.exists(LOCAL_OUTDIR):  # pragma: no cover
    os.makedirs(LOCAL_OUTDIR)

CONTAINER_USER_DATA = '/data'
CONTAINER_EXAMPLES = os.path.join(CONTAINER_USER_DATA, 'examples')
CONTAINER_OUTDIR = os.path.join(CONTAINER_USER_DATA, 'output')

__DEFAULT_IP = '127.0.0.1'
__DEFAULT_PORT = 50055
__DEFAULT_CONNECTION_TIMEOUT = 10.0
__DEFAULT_COMM_LOG = False
__MAX_MESSAGE_LENGTH = 4194310

SPHINX_BUILD = bool(int(os.getenv('PYPRIMEMESH_SPHINX_BUILD', 0)))


def ip():
    '''Gets the default ip address used throughout the library.'''
    return __DEFAULT_IP


def port():
    '''Gets the default port used throughout the library.'''
    return __DEFAULT_PORT


def connection_timeout():
    '''Gets the default connection timeout used throughout the library.'''
    return __DEFAULT_CONNECTION_TIMEOUT


def print_communicator_stats():
    '''INTERNAL ONLY: Gets the flag to decide whether to print communicator stats.'''
    return __DEFAULT_COMM_LOG


def max_message_length():
    '''Gets the maximum message length for a grpc channel'''
    return __MAX_MESSAGE_LENGTH


def get_examples_path():
    '''Gets the client side default container path'''
    return EXAMPLES_PATH


def get_user_data_path():
    '''Gets the client side default user data path'''
    return USER_DATA_PATH


def get_user_data_path_for_containers():
    '''Gets the user data path for containers'''
    return CONTAINER_USER_DATA


def get_examples_path_for_containers():
    '''Gets the server side default container path in case of containers

    In case of a container, the user data directory is mounted within on the container image.
    '''
    return CONTAINER_EXAMPLES


def get_output_path():
    '''Gets the client side output directory used by containers'''
    return LOCAL_OUTDIR


def get_output_path_for_containers():
    '''Gets the server side output directory used by containers'''
    return CONTAINER_OUTDIR


def get_sphinx_build():
    '''Gets the flag for if sphinx build is being used'''
    return SPHINX_BUILD
