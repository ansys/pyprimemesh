'''The default configuration for the PyPRIME library
'''

__all__ = [
    'ip',
    'port',
    'connection_timeout',
    'print_communicator_stats'
]

__DEFAULT_IP = '127.0.0.1'
__DEFAULT_PORT = 50055
__DEFAULT_CONNECTION_TIMEOUT = 10.0
__DEFAULT_COMM_LOG = False

def ip():
    '''Get the default ip address used throughout the library
    '''
    return __DEFAULT_IP

def port():
    ''' Get the default port used throughout the library
    '''
    return __DEFAULT_PORT

def connection_timeout():
    '''Get the default connection timeout used throughout the library'''
    return __DEFAULT_CONNECTION_TIMEOUT

def print_communicator_stats():
    '''INTERNAL ONLY: Get the flag to decide whether to print communicator stats'''
    return __DEFAULT_COMM_LOG
