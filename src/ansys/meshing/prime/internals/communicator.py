# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
