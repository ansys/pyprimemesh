import logging
import os

import ansys.meshing.prime.examples as examples
import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.internals.defaults as defaults
import ansys.meshing.prime.internals.utils as utils
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.internals.utils import terminate_process

__all__ = ['Client']


class Client(object):
    '''Client class for PyPrimeMesh.'''

    def __init__(
        self,
        *,
        server_process=None,
        ip: str = defaults.ip(),
        port: int = defaults.port(),
        timeout: float = defaults.connection_timeout(),
        credentials=None,
        **kwargs,
    ):
        self._default_model: Model = None
        local = kwargs.get('local', False)
        if local and server_process is not None:
            raise ValueError('Local client cannot be instantiated with a server process')
        self._local = local
        self._process = server_process
        self._comm = None
        if not local:
            try:
                from ansys.meshing.prime.internals.grpc_communicator import (
                    GRPCCommunicator,
                )

                channel = kwargs.get('channel', None)
                if channel is not None:
                    self._comm = GRPCCommunicator(channel=channel, timeout=timeout)
                else:
                    self._comm = GRPCCommunicator(
                        ip=ip, port=port, timeout=timeout, credentials=credentials
                    )
                    setattr(self, 'port', port)
            except ImportError as err:
                logging.getLogger('PyPrimeMesh').error(
                    f'Failed to load grpc_communicator with message: {err.msg}'
                )
                raise
            except ConnectionError:
                self.exit()

                logging.getLogger('PyPrimeMesh').error('Failed to connect to PRIME GRPC server')
                raise
        else:
            try:
                from ansys.meshing.prime.internals.prime_communicator import (
                    PrimeCommunicator,
                )

                self._comm = PrimeCommunicator()
            except ImportError as err:
                logging.getLogger('PyPrimeMesh').error(
                    f'Failed to load prime_communicator with message: {err.msg}'
                )

    @property
    def model(self):
        '''Gets model associated with the client.'''
        if self._default_model is None:
            # This assumes that the Model is always object id 1....
            self._default_model = Model(self._comm, 1, 1, "Default")
        return self._default_model

    def run_on_server(self, recipe: str):
        '''Run a recipe on server.

        Parameters
        ----------
        recipe: str
            Recipe to run on the server. This needs to be a valid
            python script.
        '''
        if self._comm is not None:
            result = self._comm.run_on_server(recipe)
            return result['Results']

    def exit(self):
        '''Close the connection with the server.

        If the client had launched the server, then this will also
        kill the server process.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> prime_client = prime.launch_prime() # This will launch a server process
        >>> model = prime_client.model
        >>> fileio = prime.FileIO(model)
        >>> result = fileio.read_pmdat('example.pmdat', prime.FileReadParams(model=model))
        >>> print(result)
        >>> prime_client.exit() # Sever connection with server and kill server
        '''
        if self._comm is not None:
            self._comm.close()
            self._comm = None
        if self._process is not None:
            assert self._local == False
            terminate_process(self._process)
            self._process = None

        if config.using_container():
            container_name = getattr(self, 'container_name')
            utils.stop_prime_github_container(container_name)
        elif config.has_pim():
            self.remote_instance.delete()
            self.pim_client.close()

        clear_examples = bool(int(os.environ.get('PYPRIMEMESH_CLEAR_EXAMPLES', '1')))
        if clear_examples:
            examples.clear_download_cache()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.exit()
