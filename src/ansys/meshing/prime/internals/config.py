"""Configuration utility for PyPrimeMesh."""

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
    'enable_log_output',
]

__DEFAULT_USE_BINARY = False
__USING_CONTAINER = False
__HAS_PIM = False
__FILE_CHECK = True

from ansys.meshing.prime.internals.logger import PrimeLogger


def _optimize_vectors():
    """Get the value of the flag for optimizing vectors."""
    return __DEFAULT_USE_BINARY


def _set_optimize_vectors(optimize_vectors: bool):
    """Set the flag for optimizing vectors.

    Parameters
    ----------
    optimize_vectors : bool
        Whether to optimize vectors.

    Raises
    ------
    ValueError
        Value is not Boolean.
    """
    global __DEFAULT_USE_BINARY
    if not isinstance(optimize_vectors, bool):
        raise ValueError(f'Value to set optimize vectors flag should be Boolean.')

    __DEFAULT_USE_BINARY = optimize_vectors


def enable_optimizing_numpy_arrays():
    """Enable optimizing numpy arrays over the wire.

    This method allows the library to optimize serialization of numpy arrays
    for faster deserialization. This can cause the data transferred
    over the network to increase slightly unless the array is of a very
    large size. Consider enabling this option to improve performance if
    your workflow is not limited by network bandwidth for performance. The
    default for optimization is always ``True``.
    """
    _set_optimize_vectors(True)


def disable_optimizing_numpy_arrays():
    """Disable optimizing numpy arrays over the wire.

    This method disables serialization optimization for numpy arrays when
    sending them over the wire. Typically, this is needed in case the
    performance is limited by a saturated network. Disabling this flag
    can provide some benefit for data transferred over the wire for
    most arrays. The default for optimization is always ``True``.
    """
    _set_optimize_vectors(False)


def is_optimizing_numpy_arrays():
    """Determine if serialization of numpy arrays is enabled.

    The default for optimization is always ``True``.

    Returns
    -------
    bool
        Boolean flag indicating if optimizing of numpy arrays is enabled.
    """
    return _optimize_vectors()


@contextmanager
def numpy_array_optimization_enabled():
    """Context helper to execute code with numpy optimization enabled."""
    old_value = _optimize_vectors()
    _set_optimize_vectors(True)
    yield
    _set_optimize_vectors(old_value)


@contextmanager
def numpy_array_optimization_disabled():
    """Context helper to execute code with numpy optimization disabled."""
    old_value = _optimize_vectors()
    _set_optimize_vectors(False)
    yield
    _set_optimize_vectors(old_value)


def set_using_container(value: bool):
    """Set the ``USING_CONTAINER`` flag to ``value``.

    Parameters
    ----------
    value : bool
        Whether to use a container.

    Returns
    -------
    bool
        Value for the ``USING_CONTAINER`` flag.
    """
    global __USING_CONTAINER
    __USING_CONTAINER = value
    return __USING_CONTAINER


def using_container():
    """Get the value for the ``USING_CONTAINER`` flag.

    Returns
    -------
    bool
        Value for the ``USING_CONTAINER`` flag.
    """
    return __USING_CONTAINER


def set_has_pim(value: bool):
    """Set the `HAS_PIM` flag.

    PIM (Product Instance Manager) provides a gRPC API that
    enables both library and app developers to start a product in
    a remote environment and communicate with its API.

    Parameters
    ----------
    value : bool
        Value for setting the ``HAS_PIM`` flag.

    Returns
    -------
    bool
        Value for the ``HAS_PIM`` flag.
    """
    global __HAS_PIM
    __HAS_PIM = value
    return __HAS_PIM


def has_pim():
    """Get the ``HAS_PIM`` flag.

    Returns
    -------
    bool
        Value for the ``HAS_PIM`` flag.
    """
    return __HAS_PIM


def file_existence_check_enabled():
    """Get config to enable checking if files exist.

    Returns
    -------
    bool
        Option to check if files exist before reading them.
    """
    return __FILE_CHECK


def set_file_existence_check(value: bool):
    """Set option to enable checking if files exist.

    Parameters
    ----------
    value : bool
        Value to set the option with.

    Returns
    -------
    bool
        Option to check if files exist before reading them.
    """
    global __FILE_CHECK
    __FILE_CHECK = value
    return __FILE_CHECK


def enable_log_output(stream=None):
    """Enable logger output to given stream.

    If stream is not specified, sys.stderr is used.

    Parameters
    ----------
    stream: TextIO, optional
        Stream to output the log output to stream
    """
    PrimeLogger().enable_output(stream)
