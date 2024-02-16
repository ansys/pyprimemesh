"""Module for communications with the gRPC server."""
__all__ = ['GRPCCommunicator']
from typing import Optional

import grpc
from ansys.api.meshing.prime.v1 import prime_pb2, prime_pb2_grpc

import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.internals.defaults as defaults
import ansys.meshing.prime.internals.grpc_utils as grpc_utils
import ansys.meshing.prime.internals.json_utils as json
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.internals.communicator import Communicator
from ansys.meshing.prime.internals.error_handling import (
    communicator_error_handler,
    error_code_handler,
)

# Keep some buffer for gRPC metadata that it may want to send
BUFFER_MESSAGE_LENGTH = defaults.max_message_length() - 100


def make_chunks(data, chunk_size):
    n = max(1, chunk_size)
    return (data[i : i + n] for i in range(0, len(data), n))


def request_iterator(model_id, data, message_cls, model_cls, content_cls, completion_cls):
    yield message_cls(model=model_cls(object_id=model_id))
    for chunk in make_chunks(data, BUFFER_MESSAGE_LENGTH):
        yield message_cls(content=content_cls(data=chunk))
    yield message_cls(completion_token=completion_cls())


def get_response_messages(response_generator):
    for response in response_generator:
        if response.HasField('completion_token'):
            break

        assert response.HasField('content')
        yield response.content


def get_response(response_iterator, separator):
    return separator.join(response.data for response in get_response_messages(response_iterator))


class GRPCCommunicator(Communicator):
    """Manages communication with the gRPC server.

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
        import os

        self._channel = kwargs.get('channel', None)
        self._models = []
        if self._channel is None:
            ip_addr = f"{ip}:{port}"
            channel_options = grpc_utils.get_default_channel_args()
            if credentials is None:
                self._channel = grpc.insecure_channel(ip_addr, options=channel_options)
            else:
                self._channel = grpc.secure_channel(ip_addr, credentials, options=channel_options)

        if 'PYPRIMEMESH_DEVELOPER_MODE' not in os.environ:
            timeout = None

        try:
            grpc.channel_ready_future(self._channel).result(timeout=timeout)
        except grpc.FutureTimeoutError as err:
            raise ConnectionError(
                f'Failed to connect to Server in given timeout of {timeout} secs'
            ) from err

        self._stub = prime_pb2_grpc.PrimeStub(self._channel)
        try:
            response = self._stub.Initialize(prime_pb2.InitializeRequest())
            message = json.loads(response.data)
            if 'ServerError' in message:
                raise ConnectionError(message['ServerError'])
            elif 'Results' in message:
                self._models = message['Results']
        except ConnectionError:
            raise
        except:
            pass

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
        if self._stub is not None:
            command = {"Command": command}
            if len(args) > 0:
                command.update({"ObjectID": args[0]})
            if kwargs is not None:
                if "args" in kwargs:
                    command.update({"Args": kwargs["args"]})

            if config.is_optimizing_numpy_arrays():
                response = self._stub.ServeJsonBinary(
                    request_iterator(
                        model._object_id,
                        json.dumps(command),
                        prime_pb2.BinaryMessage,
                        prime_pb2.Model,
                        prime_pb2.BinaryJsonContent,
                        prime_pb2.MessageCompletionToken,
                    )
                )
                message = get_response(response, b'')
            else:
                response = self._stub.ServeJson(
                    request_iterator(
                        model._object_id,
                        json.dumps(command),
                        prime_pb2.StringMessage,
                        prime_pb2.Model,
                        prime_pb2.StringJsonContent,
                        prime_pb2.MessageCompletionToken,
                    )
                )
                message = get_response(response, '')
            if defaults.print_communicator_stats():
                import logging

                logging.getLogger("PyPrimeMesh").info(
                    f'Data Transfer: Received {len(message)} bytes'
                )
            return json.loads(message)
        else:
            raise RuntimeError("No connection with server")

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
        if self._stub is not None:
            command = {"ParamName": param_name}
            with config.numpy_array_optimization_disabled():
                response = self._stub.GetParamDefaultJson(
                    request_iterator(
                        model._object_id,
                        json.dumps(command),
                        prime_pb2.StringMessage,
                        prime_pb2.Model,
                        prime_pb2.StringJsonContent,
                        prime_pb2.MessageCompletionToken,
                    )
                )
                message = get_response(response, '')
                result = json.loads(message)
            return result
        else:
            raise RuntimeError("No connection with server")

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
        if self._stub is not None:
            commands = recipe
            response = self._stub.RunOnServer(
                request_iterator(
                    model._object_id,
                    commands,
                    prime_pb2.StringMessage,
                    prime_pb2.Model,
                    prime_pb2.StringJsonContent,
                    prime_pb2.MessageCompletionToken,
                )
            )
            message = get_response(response, '')
            with config.numpy_array_optimization_disabled():
                result = json.loads(message)
            if "Error" in result:
                raise RuntimeError(result['Error'])
            return result
        else:
            raise RuntimeError("No connection with server")

    def close(self):
        """Close opened channels."""
        self._stub = None
        if self._channel is not None:
            self._channel.close()
            self._channel = None

    def __del__(self):
        """Close communication when deleting the instance."""
        self.close()

    @property
    def models(self):
        """List of models available."""
        return self._models
