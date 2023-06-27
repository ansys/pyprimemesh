"""Module for abstract communicator."""
from abc import abstractmethod


class Communicator(object):
    """Provides the abstract class for the server communicator."""

    @abstractmethod
    def serve(self, model, command, *args, **kwargs) -> dict:
        """Serve the model and send a command to the server.

        Parameters
        ----------
        model : Model
            Model to serve.
        command : str
            Command to send to the server.

        Returns
        -------
        dict
            Response from the server.
        """
        pass

    @abstractmethod
    def initialize_params(self, model, param_name: str, *args) -> dict:
        """Initialize parameters on the server side.

        Parameters
        ----------
        model : Model
            Model to initialize parameter on.
        param_name : str
            Parameter to initialize.

        Returns
        -------
        dict
            Response from the server.
        """
        pass

    @abstractmethod
    def run_on_server(self, model, recipe: str) -> dict:
        """Run the command on the server side.

        Parameters
        ----------
        model : Model
            Model to run commands on.
        recipe : str
            Command to run.

        Returns
        -------
        dict
            Response from the server.
        """
        pass

    @abstractmethod
    def import_cad(self, model, file_name: str, *args) -> dict:
        """Import a CAD file from local.

        Parameters
        ----------
        model : Model
            Model to import.
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
