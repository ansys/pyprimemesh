from typing import Any
import grpc
import json
from ansys.meshing.prime import relaxed_json
from ansys.meshing.prime.internals.error_handling import communicator_error_handler, error_code_handler
from ansys.meshing.prime.internals.communicator import Communicator
from ansys.api.meshing.prime.v1 import prime_pb2, prime_pb2_grpc

MAX_MESSAGE_LENGTH = 4194310
class GRPCCommunicator(Communicator):
    def __init__(self, ip: str, port: int, credentials = None):
        ip_addr = f"{ip}:{port}"
        self._channel = grpc.insecure_channel(ip_addr, options=[ ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH) ]) if credentials is None else grpc.secure_channel(ip_addr, credentials, options=[ ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH) ])
        try:
            grpc.channel_ready_future(self._channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            raise ConnectionError('Failed to connect to Server in given timeout of 10 secs')
        self._stub = prime_pb2_grpc.PrimeStub(self._channel)

    @error_code_handler
    @communicator_error_handler
    def serve(self, command, *args, **kwargs) -> dict:
        if self._stub:
            command = { "Command" : command }
            binary = False
            log = False
            if(len(args) > 0 ):
                command.update({ "ObjectID" : args[0]})
            if (kwargs is not None):
                command.update({ "Args" : kwargs["args"]})
                binary = kwargs.get("binary", False)
                log = kwargs.get("log", False)
                
            if binary:
                message = bytearray()
                response = self._stub.ServeJsonBinary(prime_pb2.Request(command=json.dumps(command)))
                for resp in response:
                    message += resp.output
                if log:
                    print(f'Binary Transfer: Received {len(message)} bytes')
                    # print(f'Message: {message}')
                return relaxed_json.loads(message)
            else:
                response = self._stub.ServeJson(prime_pb2.Request(command=json.dumps(command)))
                message = ''.join(str(resp.output) for resp in response)
                if log:
                    print(f'Regular Transfer: Received {len(message)} bytes')
                    # print(f'Message: {message}')
                return json.loads(message)
        else:
            raise RuntimeError("No connection with server")

    def initialize_params(self, param_name: str) -> dict:
        if self._stub:
            response = self._stub.GetParamDefaultJson(prime_pb2.Request(command=param_name))
            message = ''.join(str(resp.output) for resp in response)
            return json.loads(message)
        else:
            raise RuntimeError("No connection with server")

    def run_on_server(self, recipe: str) -> dict:
        if self._stub:
            commands = recipe
            response = self._stub.RunOnServer(prime_pb2.Request(command=commands))
            message = ''.join(str(resp.output) for resp in response)
            result = json.loads(message)
            if "Error" in result:
                raise RuntimeError(result['Error'])
            return result
        else:
            raise RuntimeError("No connection with server")
    
    def __del__(self):
        self._stub = None
        self._channel.close()
