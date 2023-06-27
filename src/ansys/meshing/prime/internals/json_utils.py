"""Module for JSON utility functions."""
import json
from typing import Union

import numpy as np

import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.relaxed_json as relaxed_json

__all__ = ['loads', 'dumps']


def try_process_as_iterable(obj):
    """Try if an object is an iterable and return its list.

    Parameters
    ----------
    obj : Any
        Object to test.

    Returns
    -------
    List
        List of the object.
    """
    iterable = iter(obj)
    return list(iterable)


def try_process_numpy_array(obj):
    """Try if an object is a numpy array and return its list.

    Parameters
    ----------
    obj : Any
        Object to test.

    Returns
    -------
    bool, list
        Whether the object is a numpy array and the list of the object.
    """
    if isinstance(obj, np.ndarray):
        return True, obj.tolist()
    return False, obj


class _CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        success, obj = try_process_numpy_array(obj)
        if success:
            return obj

        try:
            return try_process_as_iterable(obj)
        except TypeError:
            pass

        return super().default(obj)


class _CustomBinaryJSONEncoder(relaxed_json.JSONEncoder):
    def default(self, obj):
        try:
            return try_process_as_iterable(obj)
        except TypeError:
            pass

        return super().default(obj)


def loads(s: Union[str, bytes, bytearray], *args, **kwargs):
    """Load JSON from an input string.

    Parameters
    ----------
    s : Union[str, bytes, bytearray]
        Input string.

    Returns
    -------
    json
        Object converted to JSON.
    """
    if config.is_optimizing_numpy_arrays():
        return relaxed_json.loads(s, *args, **kwargs)
    return json.loads(s, *args, **kwargs)


def dumps(obj, *args, **kwargs):
    """Dump JSON to an object.

    Parameters
    ----------
    obj : Any
        Input object.

    Returns
    -------
    Object
        JSON converted to an object.
    """
    if config.is_optimizing_numpy_arrays():
        kwargs.setdefault('cls', _CustomBinaryJSONEncoder)
        return relaxed_json.dumps(obj, *args, **kwargs)

    kwargs.setdefault('cls', _CustomJSONEncoder)
    return json.dumps(obj, *args, **kwargs)
