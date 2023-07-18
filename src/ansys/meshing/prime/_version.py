"""Version of PyPrimeMesh Library."""
# Version
# ------------------------------------------------------------------------------

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:  # pragma: no cover
    import importlib_metadata  # type: ignore

__version__ = importlib_metadata.version("ansys-meshing-prime")

# ------------------------------------------------------------------------------
