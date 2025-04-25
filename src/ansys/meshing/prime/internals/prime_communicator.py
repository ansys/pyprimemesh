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

"""Module for Prime Server communications."""
import PrimePyAnsysPrimeServer as Prime

import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.internals.json_utils as json
from ansys.meshing.prime.internals.communicator import Communicator
from ansys.meshing.prime.internals.error_handling import (
    communicator_error_handler,
    error_code_handler,
)

global return_value
return_value = ""


class PrimeCommunicator(Communicator):
    """Provides for communicating with Ansys Prime Server."""

    def __init__(self):
        """Initialize the communicator."""
        Prime.SetupForPyPrime_Beta(1)
        self._models = []
        message = json.loads(Prime.GetModelInfo().Get())
        if 'ServerError' in message:
            raise ConnectionError(message['ServerError'])
        elif 'Results' in message:
            self._models = message['Results']

    @error_code_handler
    @communicator_error_handler
    def serve(self, model, command, *args, **kwargs) -> dict:
        """Serve the model and send a command to the server.

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
        """
        command = {"Command": command}
        if len(args) > 0:
            command.update({"ObjectID": args[0]})
        if kwargs is not None:
            if "args" in kwargs:
                command.update({"Args": kwargs["args"]})

        if config.is_optimizing_numpy_arrays():
            return json.loads(
                Prime.ServeJsonBinary(model._object_id, json.dumps(command)).AsBytes()
            )

        return json.loads(Prime.ServeJson(model._object_id, json.dumps(command)).Get())

    def initialize_params(self, model, param_name: str) -> dict:
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
        """
        command = {
            "ParamName": param_name,
        }

        with config.numpy_array_optimization_disabled():
            res = json.loads(Prime.GetParamDefaultJson(model._object_id, json.dumps(command)).Get())

        return res

    def run_on_server(self, model, recipe: str) -> dict:
        """Run recipe on a model on the server.

        Parameters
        ----------
        model : Model
            Model to run recipe on.
        recipe : str
            Recipe to run.

        Returns
        -------
        dict
            Response from the server.
        """
        exec(recipe, globals())
        output = '{"Results" : "' + str(return_value) + '"}'
        with config.numpy_array_optimization_disabled():
            result = json.loads(output)
        return result

    def close(self):
        """Close session."""
        Prime.Finalize()

    @property
    def models(self):
        """List of models available."""
        return self._models
