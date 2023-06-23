"""Wrapper module for Communicator class."""
from ansys.meshing.prime.internals.communicator import Communicator


class CommunicationManager:
    """Wrapper class for communicator.

    Parameters
    ----------
    comm : Communicator
        Wrapped Communicator class.
    """

    def __init__(self, comm: Communicator):
        """Initialize Communicator."""
        self._comm = comm

    @property
    def _communicator(self):
        """Getter for communicator.

        Returns
        -------
        Communicator
            Wrapped communicator.
        """
        return self._comm
