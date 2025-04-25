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

"""Module for communications with the socket server."""
__all__ = ['SocketCommunicator']
import json
import socket
from typing import Optional

import numpy as np

import ansys.meshing.prime.internals.json_utils as json
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.internals.communicator import Communicator
from ansys.meshing.prime.internals.error_handling import (
    communicator_error_handler,
    error_code_handler,
)


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)


class SocketCommunicator(Communicator):
    """Manages communication with the socket server.

    Parameters
    ----------
    ip : Optional[str], optional
        IP address where the server is located. The default is ``None``.
    port : Optional[int], optional
        Port where the server is deployed. The default is ``None``.
    timeout : float, optional
        Maximum time to wait for connection. The default is ``10.0``.
    credentials : Any, optional
        Credentials for connecting to the server. The default is ``None``.

    Raises
    ------
    ConnectionError
        Could not connect to server.
    """

    def __init__(
        self,
        ip: Optional[str] = None,
        port: Optional[int] = None,
        timeout: float = 10.0,
        credentials=None,
        **kwargs,
    ):
        """Initialize the server connection."""
        self._models = []
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(('', port))
        self._socket.listen(5)
        self._communicator, self._address = self._socket.accept()

    @error_code_handler
    @communicator_error_handler
    def serve(self, model: Model, command: str, *args, **kwargs) -> dict:
        """Serve model and send a command to the server.

        Parameters
        ----------
        model : Model
            Model to serve.
        command : str
            Command to send.

        Returns
        -------
        dict
            Response from the server.

        Raises
        ------
        RuntimeError
            Can not connect to server.
        """
        self._send_string("ServeJson")
        command = {"Command": command}
        if len(args) > 0:
            command.update({"ObjectID": args[0]})
        if kwargs is not None:
            if "args" in kwargs:
                command.update({"Args": kwargs["args"]})
        self._send_string(json.dumps(command, cls=NumpyEncoder))
        return json.loads(self._recv_string())

    def _send_string(self, data):
        byte_string = (data + '\0').encode('utf-8')
        string_length = len(byte_string).to_bytes(4, 'little')
        self._communicator.send(string_length)
        self._communicator.send(byte_string)

    def _recv_string(self):
        result_len = int.from_bytes(self._communicator.recv(4), byteorder="little")
        result = ""
        if result_len > 0:
            result = self._communicator.recv(result_len).decode("utf-8")
        return result

    def initialize_params(self, model: Model, param_name: str, *args) -> dict:
        """Initialize parameters on the server side.

        Parameters
        ----------
        model : Model
            Model to initialize parameters on.
        param_name : str
            Parameter to initialize.

        Returns
        -------
        dict
            Response from the server.

        Raises
        ------
        RuntimeError
            Can not connect to server.
        """
        self._send_string("GetParamDefaultJSon")
        self._send_string(json.dumps({"ParamName": param_name}))
        return json.loads(self._recv_string())

    def run_on_server(self, model: Model, recipe: str) -> dict:
        """Run commands on the server.

        Run commands on a model on the server.

        Parameters
        ----------
        model : core.Model
            Model to run commands on.
        recipe : str
            Commands to run.

        Returns
        -------
        dict
            Result from the server side.

        Raises
        ------
        RuntimeError
            Bad response from server.
        RuntimeError
            Can not connect to server.
        """
        pass

    def close(self):
        """Close opened channels."""
        self._communicator.close()

    def __del__(self):
        """Close communication when deleting the instance."""
        self.close()

    @property
    def models(self):
        """List of models available."""
        return None
