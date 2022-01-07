import logging
from ansys.meshing.prime.internals.utils import terminate_child_processes
from ansys.meshing.prime.core.model import Model

class Client(object):
    def __init__(self,
                 local: bool=False,
                 server_process=None,
                 ip: str="localhost",
                 port: int=50052,
                 credentials=None):
        self._default_model: Model = None
        if local and server_process is not None:
            raise ValueError("Local client cannot be instantiated with a server process")
        self._local = local
        self._process = server_process
        self._comm = None
        if not local:
            try:
                from ansys.meshing.prime.internals.grpc_communicator import GRPCCommunicator
                self._comm = GRPCCommunicator(ip, port, credentials=credentials)
            except ImportError as err:
                print(f"Failed to load grpc_communicator with message: {err.msg}")
            except ConnectionError:
                if self._process is not None:
                    self._process.terminate()
                    self._process = None

                logging.error('Failed to connect to PRIME GRPC server')
                raise
        else:
            try:
                from ansys.meshing.prime.internals.prime_communicator import PrimeCommunicator
                self._comm = PrimeCommunicator()
            except ImportError as err:
                print(f"Failed to load prime_communicator with message: {err.msg}")

    @property
    def model(self):
        if self._default_model is None:
            self._default_model = Model(self._comm, 1, 1, "Default")
        return self._default_model

    def run_on_server(self, recipe : str):
        if self._comm is not None:
            result = self._comm.run_on_server(recipe)
            return result["Results"]

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self._process is not None:
            assert self._local == False
            terminate_child_processes(self._process.pid)
            self._process.terminate()
        else:
            logging.info('Context exit is a no-op when running locally')
