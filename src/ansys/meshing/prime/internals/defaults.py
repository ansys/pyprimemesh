'''The default configuration for the PyPrime library.
'''
# Copyright 2023 ANSYS, Inc.
# Unauthorized use, distribution, or duplication is prohibited.

__all__ = ['ip', 'port', 'connection_timeout', 'print_communicator_stats', 'max_message_length']

__DEFAULT_IP = '127.0.0.1'
__DEFAULT_PORT = 50055
__DEFAULT_CONNECTION_TIMEOUT = 10.0
__DEFAULT_COMM_LOG = False
__MAX_MESSAGE_LENGTH = 4194310


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
