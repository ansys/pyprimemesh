"""Module for abstract communicator."""
from abc import abstractmethod

from ansys.meshing.prime.core.model import Model


class Communicator(object):
    """Abstract class for the server communicator."""

    @abstractmethod
    def serve(self, model, command, *args, **kwargs) -> dict:
        """Serve model and commands to server.

        Parameters
        ----------
        model : Model
            Model to serve.
        command : str
            Command to send to the server.

        Returns
        -------
        dict
            Response from server.
        """
        pass

    @abstractmethod
    def initialize_params(self, model, param_name: str, *args) -> dict:
        """Initialize parameters in server side.

        Parameters
        ----------
        model : Model
            Model in which to initialize params.
        param_name : str
            Parameter to initialize

        Returns
        -------
        dict
            Response from server.
        """
        pass

    @abstractmethod
    def run_on_server(self, model, recipe: str) -> dict:
        """Initialize parameters in server side.

        Parameters
        ----------
        model : Model
            Model in which to initialize params.
        param_name : str
            Parameter to initialize

        Returns
        -------
        dict
            Response from server.
        """
        pass

    @abstractmethod
    def import_cad(self, model: Model, file_name: str, *args) -> dict:
        """Import CAD file from local.

        Parameters
        ----------
        model : Model
            Model to which import.
        file_name : str
            Name of the CAD file.

        Returns
        -------
        dict
            Response from the server.
        """
        pass

    @abstractmethod
    def close(self):
        """Close communication when deleting the instance."""
        pass
