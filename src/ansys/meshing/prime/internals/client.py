# Copyright (C) 2026 ANSYS, Inc. and/or its affiliates.
# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

import atexit
import json
import logging
import os
import platform
import re
import signal
import subprocess
from typing import Optional, Union

import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.internals.defaults as defaults
import ansys.meshing.prime.internals.utils as utils
from ansys.meshing.prime.core.model import Model

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
    client_certs_dir : str, os.PathLike, optional
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
        client_certs_dir: Optional[Union[str, os.PathLike]] = None,
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

        if client_certs_dir is not None:
            client_certs_dir = os.fspath(client_certs_dir)

        self._local = local
        self._process = server_process
        self._comm = None
        self._server_cleanup_targets = []
        self._atexit_registered = False
        if not local:
            if (
                connection_type == config.ConnectionType.GRPC_SECURE
                or connection_type == config.ConnectionType.GRPC_INSECURE
            ):
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
                        ip=ip,
                        port=port,
                        timeout=timeout,
                        credentials=credentials,
                        client_certs_dir=client_certs_dir,
                        transport_mode=transport_mode,
                        uds_id=uds_id,
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
        if self._process is not None and self._comm is not None:
            try:
                model = self.model
                results = json.loads(
                    model._comm.serve(
                        model,
                        "PrimeMesh::Model/GetServerProcessInformation",
                        model._object_id,
                        args={},
                    )
                )
                self._store_server_cleanup_targets(results.get('hostNames'), results.get('pids'))
            except Exception as err:
                logging.getLogger('PyPrimeMesh').info(
                    f"Skipped server cleanup target collection: {err}"
                )

    @property
    def model(self):
        """Get model associated with the client."""
        from ansys.meshing import prime

        if self._default_model is None and hasattr(self._comm, 'models'):
            if self._comm.models:
                model_info = self._comm.models[0]
                self._default_model = prime.Model(
                    self._comm, model_info['id'], model_info['index'], "Default"
                )

        if self._default_model is None:
            # This assumes that the Model is always object id 1....
            self._default_model = prime.Model(self._comm, 1, 1, "Default")
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

    def _store_server_cleanup_targets(self, hostNames, pids):
        """Store launched server host/PID pairs for later in-process cleanup.

        Parameters
        ----------
        hostNames : list of str
            Hostnames where server processes are running.
        pids : list of int
            Process IDs corresponding to the hostnames.
        """
        logger = logging.getLogger('PyPrimeMesh')
        self._server_cleanup_targets = []
        if not hostNames or not pids or len(hostNames) != len(pids):
            logger.info("Found invalid hostnames and PIDs, skipped server cleanup targets.")
            return

        owner_pid = os.getpid()
        hostname_re = re.compile(r'^[A-Za-z0-9._-]+$')
        seen = set()
        targets = []
        for hostname, pid in zip(hostNames, pids):
            try:
                pid = int(pid)
            except (TypeError, ValueError):
                continue
            if pid <= 0 or pid == owner_pid:
                continue
            if not isinstance(hostname, str) or not hostname_re.match(hostname):
                continue
            key = (hostname.lower(), pid)
            if key in seen:
                continue
            seen.add(key)
            targets.append((hostname, pid))

        if not targets:
            logger.info("No server PIDs to kill, skipped server cleanup targets.")
            return

        self._server_cleanup_targets = targets
        if not self._atexit_registered:
            atexit.register(self.exit)
            self._atexit_registered = True

    def _is_local_host(self, hostname):
        host = hostname.lower()
        if host in ('localhost', '127.0.0.1', '::1'):
            return True
        return host == platform.node().lower()

    def _is_prime_server_process(self, pid):
        try:
            if os.name == "nt":
                result = subprocess.run(
                    ["tasklist", "/FI", f"PID eq {pid}", "/FO", "CSV", "/NH"],
                    capture_output=True,
                    text=True,
                    timeout=5,
                )
                return "AnsysPrimeServer" in result.stdout
            exe = os.readlink(f"/proc/{pid}/exe")
            return "AnsysPrimeServer" in os.path.basename(exe)
        except Exception:
            return False

    def _kill_server_cleanup_targets(self):
        logger = logging.getLogger('PyPrimeMesh')
        for hostname, pid in self._server_cleanup_targets:
            try:
                if self._is_local_host(hostname):
                    if not self._is_prime_server_process(pid):
                        continue
                    if os.name == "nt":
                        subprocess.run(
                            ["taskkill", "/F", "/PID", str(pid)],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                        )
                    else:
                        os.kill(pid, signal.SIGKILL)
                else:
                    if os.name == "nt":
                        remote = (
                            f'tasklist /FI "PID eq {pid}" /FO CSV /NH | '
                            f"findstr /I AnsysPrimeServer >nul && "
                            f"taskkill /F /PID {pid} >nul 2>&1"
                        )
                    else:
                        remote = (
                            f'exe=$(readlink /proc/{pid}/exe 2>/dev/null); '
                            f'case "$exe" in *AnsysPrimeServer*) kill -9 {pid};; esac'
                        )
                    subprocess.run(
                        [
                            "ssh",
                            "-o",
                            "BatchMode=yes",
                            "-o",
                            "ConnectTimeout=5",
                            hostname,
                            remote,
                        ],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                    )
            except ProcessLookupError:
                pass
            except Exception as err:
                logger.info(f"Failed to kill server process {pid} on {hostname}: {err}")
        self._server_cleanup_targets = []

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
        if self._comm is None and self._process is None and not self._server_cleanup_targets:
            return
        if self._comm is not None:
            # close() issues the Finalize RPC to the server, which triggers a graceful, in-process
            # shutdown (gRPC server Shutdown -> PrimeMesh::Finalize). On a distributed (n_procs > 1)
            # server this also broadcasts the exit to all MPI worker ranks and calls MPI_Finalize.
            # We rely on this cooperative path instead of raising an OS termination signal at the
            # launched process, which does not reach the MPI-spawned worker ranks and left them
            # behind.
            self._comm.close()
            self._comm = None
        if self._process is not None:
            assert self._local == False  # nosec B101
            # Do not signal/kill the launched process. The Finalize RPC above tears the server (and
            # its distributed workers) down cleanly; just wait for the launched process to exit and
            # reap it so it does not linger as a zombie.
            try:
                self._process.wait(timeout=min(5.0, defaults.connection_timeout()))
            except Exception:
                # Graceful shutdown did not finish in time or the process was already gone; force
                # termination so it is not orphaned when no cleanup targets were collected.
                utils.terminate_process(self._process)
            self._process = None
        if self._server_cleanup_targets:
            self._kill_server_cleanup_targets()
        if config.using_container():
            container_name = getattr(self, 'container_name', None)
            if container_name:
                utils.stop_prime_github_container(container_name)
        elif config.has_pim():
            self.remote_instance.delete()
            self.pim_client.close()
        self._server_cleanup_targets = []
        clear_examples = bool(int(os.environ.get('PYPRIMEMESH_CLEAR_EXAMPLES', '1')))
        if clear_examples:
            try:
                DownloadManager = utils._get_download_manager()
                download_manager = DownloadManager()
                download_manager.clear_download_cache()
            except FileNotFoundError:
                # examples download to a shared temporary directory, so a concurrent
                # session may have cleared the same files first. Cleanup is best
                # effort and must not bring down an otherwise successful session.
                pass
            except ImportError:
                # The 'ansys-tools-common' package is optional and only needed for
                # example downloads. Its absence must not bring down an otherwise
                # successful session.
                pass

    def __enter__(self):
        """Open client."""
        return self

    def __exit__(self, type, value, traceback):
        """Close communication with the server when deleting the instance."""
        self.exit()
