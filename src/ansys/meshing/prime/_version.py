"""Version of ansys-meshing-prime library.

On the ``main`` branch, use 'devN' to denote a development version.

Version number is modified in ``pyproject.toml`` file.

Examples
--------
Print the version

>>> from ansys.meshing import prime
>>> print(prime.__version__)
0.2.0

"""

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:  # pragma: no cover
    import importlib_metadata  # type: ignore

__version__ = importlib_metadata.version(__name__.replace(".", "-"))
