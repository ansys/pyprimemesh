'''Configuration utility for the PyPrimeMesh library
'''

from contextlib import contextmanager

__all__ = [
    'enable_optimizing_numpy_arrays',
    'disable_optimizing_numpy_arrays',
    'is_optimizing_numpy_arrays',
    'numpy_array_optimization_enabled',
    'numpy_array_optimization_disabled',
    'set_using_container',
    'using_container',
    'set_has_pim',
    'has_pim',
]

__DEFAULT_USE_BINARY = False
__USING_CONTAINER = False
__HAS_PIM = False


def _optimize_vectors():
    '''Gets the value of flag to optimize vectors.'''
    return __DEFAULT_USE_BINARY


def _set_optimize_vectors(optimize_vectors: bool):
    global __DEFAULT_USE_BINARY
    if not isinstance(optimize_vectors, bool):
        raise ValueError(f'Value to set optimize vectors flag should be Boolean.')

    __DEFAULT_USE_BINARY = optimize_vectors


def enable_optimizing_numpy_arrays():
    '''Enables optimizing numpy arrays over the wire.

    This will allow the library to optimize serialization of numpy arrays
    to allow faster deserialization. This can cause the data transferred
    over the network to increase slightly unless the array is of a very
    large size. Consider enabling this option to improve performance if
    your workflow is not limited by network bandwidth for performance. By
    default, optimization is always turned on.
    '''
    _set_optimize_vectors(True)


def disable_optimizing_numpy_arrays():
    '''Disable optimizing numpy arrays over the wire.

    This will disable serialization optimization for numpy arrays when
    sending them over the wire. Typically, this is needed in case the
    performance is limited by a saturated network. Disabling this flag
    can provide some benefit for data transferred over the wire for
    most arrays. By default, optimization is always turned on.
    '''
    _set_optimize_vectors(False)


def is_optimizing_numpy_arrays():
    '''Query if serialization of numpy arrays is turned on.

    By default, this is always turned on.

    Returns
    -------
    bool
        Boolean flag indicating if optimizing of numpy arrays is enabled.
    '''
    return _optimize_vectors()


@contextmanager
def numpy_array_optimization_enabled():
    '''Context helper to execute code with numpy optimization enabled.'''
    old_value = _optimize_vectors()
    _set_optimize_vectors(True)
    yield
    _set_optimize_vectors(old_value)


@contextmanager
def numpy_array_optimization_disabled():
    '''Context helper to execute code with numpy optimization disabled.'''
    old_value = _optimize_vectors()
    _set_optimize_vectors(False)
    yield
    _set_optimize_vectors(old_value)


def set_using_container(value: bool):
    global __USING_CONTAINER
    __USING_CONTAINER = value
    return __USING_CONTAINER


def using_container():
    return __USING_CONTAINER


def set_has_pim(value: bool):
    global __HAS_PIM
    __HAS_PIM = value
    return __HAS_PIM


def has_pim():
    return __HAS_PIM
