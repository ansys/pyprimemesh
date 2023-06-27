"""Wrapper module for Communicator class."""
from ansys.meshing.prime.internals.communicator import Communicator


class CommunicationManager:
    """Provides the wrapper class for the communicator.

    Parameters
    ----------
    comm : Communicator
        Wrapped ``Communicator`` class.
    """

    def __init__(self, comm: Communicator):
        """Initialize the communicator."""
        self._comm = comm

    @property
    def _communicator(self):
        """Getter for the communicator.

        Returns
        -------
        Communicator
            Wrapped communicator.
        """
        return self._comm
