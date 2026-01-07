# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Module for client communication implementations."""

import logging
import os
import platform
import time
import json
from pathlib import Path
from typing import Optional

import ansys.meshing.prime.examples as examples
import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.internals.defaults as defaults
import ansys.meshing.prime.internals.utils as utils
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.internals.utils import terminate_process

__all__ = ['Client']

class Client(object):
    """Provides the ``Client`` class for PyPrimeMesh.

    Parameters
    ----------
    server_process : Any, optional
        Server process in the system. The default is ``None``.
    ip : str, optional
        IP address where the server is located. The default is ``defaults.ip()``.
    port : int, optional
        Port where the server is deployed. The default is ``defaults.port()``.
    timeout : float, optional
        Maximum time to wait for connection. The default is ``defaults.connection_timeout()``.
    credentials : Any, optional
        Credentials to connect to the server. The default is ``None``.
    uds_id : Optional[str], optional
        Id for the Unix Domain Socket (UDS). The default is ``None``.
    client_certs_dir : Optional[str]
        Directory containing client certificates for mutual TLS.
    Raises
    ------
    ValueError
        Failed to load the communicator.
    """

    def __init__(
        self,
        *,
        server_process=None,
        ip: str = defaults.ip(),
        port: int = defaults.port(),
        timeout: float = defaults.connection_timeout(),
        credentials=None,
        connection_type: config.ConnectionType = config.ConnectionType.GRPC_SECURE,
        uds_id: Optional[str] = None,
        client_certs_dir: Optional[str] = None,
        **kwargs,
    ):
        """Initialize the client."""
        self._default_model: Model = None
        local = kwargs.get('local', False)
        if local and server_process is not None:
            raise ValueError('Local client cannot be instantiated with a server process')
        
        
        if connection_type == config.ConnectionType.GRPC_INSECURE:
            print("Warning (Client): Modification of these configurations is not recommended.")
            print("Refer the documentation for your installed product for additional information.")

        self._local = local
        self._process = server_process
        self._comm = None
        self._cleanup_script_path : Path = None
        if not local:
            if connection_type == config.ConnectionType.GRPC_SECURE or \
                connection_type == config.ConnectionType.GRPC_INSECURE:
                try:
                    from ansys.meshing.prime.internals.grpc_communicator import (
                        GRPCCommunicator,
                    )

                    channel = kwargs.get('channel', None)

                    if channel is not None:
                        self._comm = GRPCCommunicator(channel=channel, timeout=timeout)
                    else:
                        transport_mode = None
                        if connection_type == config.ConnectionType.GRPC_INSECURE:
                            transport_mode = "insecure"
                        else:
                            if client_certs_dir is not None:
                                transport_mode = "mtls"
                            else:
                                if os.name == 'nt':
                                    transport_mode = "wnua"
                                else:
                                    transport_mode = "uds"
                                    
                    self._comm = GRPCCommunicator(
                        ip=ip, port=port, timeout=timeout,
                        credentials=credentials,
                        client_certs_dir=client_certs_dir,
                        transport_mode=transport_mode,
                        uds_id=uds_id)
                    
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
            elif communicator_type == "socket":
                from ansys.meshing.prime.internals.socket_communicator import (
                    SocketCommunicator,
                )

                self._comm = SocketCommunicator(ip=ip, port=port)
                setattr(self, 'port', port)
            else:
                logging.getLogger('PyPrimeMesh').error(f'Invalid server type: {communicator_type}')
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
        model = self.model
        results = json.loads(model._comm.serve(model,
                                               "PrimeMesh::Model/GetServerProcessInformation",
                                               model._object_id,
                                               args={}))
        #
        self._generate_server_term_scripts(results['hostNames'], results['pids'])

    @property
    def model(self):
        """Get model associated with the client."""
        if self._default_model is None and hasattr(self._comm, 'models'):
            if self._comm.models:
                model_info = self._comm.models[0]
                self._default_model = Model(
                    self._comm, model_info['id'], model_info['index'], "Default"
                )

        if self._default_model is None:
            # This assumes that the Model is always object id 1....
            self._default_model = Model(self._comm, 1, 1, "Default")
        return self._default_model

    def run_on_server(self, recipe: str):
        """Run a recipe on the server.

        Parameters
        ----------
        recipe: str
            Recipe to run. This must be a valid Python script.
        """
        if self._comm is not None:
            result = self._comm.run_on_server(recipe)
            return result['Results']

    def _generate_server_term_scripts(self, hostNames, pids):
        """Generates shell and batch scripts to kill processes on specified hostnames.

        Parameters
        ----------
        hostnames (list of str): A list of hostnames where processes are running.
                                    'localhost' or the current machine's name implies local.
        pids (list of int): A list of process IDs corresponding to the hostnames.

        Returns
        -------
        tuple: A tuple containing the filenames of the generated shell and batch scripts.
                (shell_script_filename, batch_script_filename)
        """
        # --- Input Validation ---
        current_hostname = platform.node().lower()
        if not hostNames or not pids or len(hostNames) != len(pids):
            logging.getLogger('PyPrimeMesh').info("Found invalid hostnames and PIDs," \
            "skipped server post kill scripts creation.")
            return None, None
        if os.name == "nt":
            script_content = "@echo off\n"
            script_content += "REM This script kills the Ansys Prime Server processes.\n"
        else:
            script_content = "#!/bin/bash\n"
            script_content += "# This script kills the Ansys Prime Server processes.\n"
        #
        for hostname, pid in zip(hostNames, pids):
            if hostname.lower() == 'localhost' or hostname.lower() == current_hostname:
                if os.name == "nt":
                    ## Windows batch script
                    script_content += f":: Check and kill PID {pid}\n"
                    script_content += f"tasklist /FI \"PID eq {pid}\" | find \"{pid}\" >nul\n"
                    script_content += f"if %errorlevel%==0 (\n"
                    script_content += f"    echo Attempting to killing process {pid}...\n"
                    script_content += f"    taskkill /F /PID {pid} >nul 2>&1\n"
                    script_content += f"    if %errorlevel%==0 (\n"
                    script_content += f"        echo Process {pid} killed successfully.\n"
                    script_content += f"    ) else (\n"
                    script_content += f"        echo Server process {pid} still running.\n"
                    script_content += f"    )\n"
                    script_content += f")\n\n"
                else:
                    ## Unix-like shell script
                    script_content += f"# --- Checking and killing PID {pid} ---\n"
                    script_content += f'if ps -p {pid} > /dev/null; then\n'
                    script_content += f'    echo "Attempting to kill process {pid}..."\n'
                    script_content += f'    kill -9 {pid} > /dev/null 2>&1\n'
                    script_content += f'    if [ $? -eq 0 ]; then\n'
                    script_content += f'        echo "Process {pid} killed successfully."\n'
                    script_content += f'    else\n'
                    script_content += f'        echo "Server process {pid} still running."\n'
                    script_content += f'    fi\n'
                    script_content += f'\n\nfi\n'
        # Timestamp and process information
        current_dir = Path(os.getcwd())
        script_base_name = f"cleanup-prime-{current_hostname}-{os.getpid()}-{int(time.time())}"
        #logging.getLogger('PyPrimeMesh').info(f"Current directory: {current_dir}")
        self._cleanup_script_path = (current_dir / f"{script_base_name}").with_suffix(
            '.bat' if os.name == "nt" else '.sh')
        # --- File Writing ---
        try:
            # Write the shell script
            if os.name == "nt":
                with open(self._cleanup_script_path, 'w') as batch_file:
                    batch_file.write(script_content)
            else:
                with open(self._cleanup_script_path, 'w') as shell_file:
                    shell_file.write(script_content)
                # Make the shell script executable on Unix-like systems
                os.chmod(self._cleanup_script_path, 0o755)
            return None, None
        except IOError as e:
            logging.getLogger('PyPrimeMesh').info(f"Error writing script files: {e}")
            return None, None
        except Exception as e:
            logging.getLogger('PyPrimeMesh').info(f"An unexpected error occurred: {e}")
            return None, None

    def exit(self):
        """Close the connection with the server.

        If the client has launched the server, this method also
        kills the server process.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> prime_client = prime.launch_prime() # This launches a server process.
        >>> model = prime_client.model
        >>> fileio = prime.FileIO(model)
        >>> result = fileio.read_pmdat('example.pmdat', prime.FileReadParams(model=model))
        >>> print(result)
        >>> prime_client.exit() # Sever connection with server and kill the server.
        """
        if self._comm is not None:
            self._comm.close()
            self._comm = None
        if self._process is not None:
            assert self._local == False
            terminate_process(self._process, self._cleanup_script_path)
            self._cleanup_script_path = None
            self._process = None
        if config.using_container():
            container_name = getattr(self, 'container_name')
            utils.stop_prime_github_container(container_name)
        elif config.has_pim():
            self.remote_instance.delete()
            self.pim_client.close()
        #
        if self._cleanup_script_path is not None:
            shell_script = self._cleanup_script_path.with_suffix(".sh")
            batch_script = self._cleanup_script_path.with_suffix(".bat")
            utils.cleanup_script_files(shell_script, batch_script)
        clear_examples = bool(int(os.environ.get('PYPRIMEMESH_CLEAR_EXAMPLES', '1')))
        if clear_examples:
            download_manager = examples.DownloadManager()
            download_manager.clear_download_cache()

    def __enter__(self):
        """Open client."""
        return self

    def __exit__(self, type, value, traceback):
        """Close communication with the server when deleting the instance."""
        self.exit()
