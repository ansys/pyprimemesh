# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
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

"""
Windows Named User Authentication (WNUA) for Python gRPC servers.

This module provides a server interceptor that authenticates clients
by verifying they run under the same Windows user account.
"""

import ctypes
import os
import re
import sys
from concurrent import futures
from ctypes import wintypes

import grpc

# Only available on Windows
if sys.platform != "win32":
    raise ImportError("WNUA (Windows Named User Authentication) is only supported on Windows")


class WNUAAuthenticator:
    """Windows Named User Authentication using FPN library.

    This class provides authentication functionality by interfacing with the
    FPN (Find Port Number) library to verify that gRPC clients are running
    under the same Windows user account as the server.
    """

    def __init__(self):
        """Initialize the WNUA authenticator with FPN library.

        Loads the FPN DLL and sets up function signatures for authentication.
        The DLL is searched in the build directory first, then in system PATH.

        Raises
        ------
        RuntimeError
            If the FPN library cannot be loaded or accessed.
        """
        # Look for the FPN DLL in the build directory - demo repository location after build
        fpn_dll_path = os.path.join(
            os.path.dirname(__file__), "..", "build", "fpn_install", "bin", "fpn.dll"
        )

        try:
            # Try to load from build directory first
            if os.path.exists(fpn_dll_path):
                self.fpn_lib = ctypes.CDLL(fpn_dll_path)
            else:
                # Fall back to searching in PATH
                self.fpn_lib = ctypes.CDLL("fpn.dll")
        except OSError as e:
            raise RuntimeError(
                f"Failed to load FPN library: {e}. \
                                Make sure fpn.dll is built and accessible."
            )

        # Define function signatures
        self.fpn_lib.fpn_remote_is_me.argtypes = [
            ctypes.c_ushort,  # port
            ctypes.POINTER(wintypes.DWORD),  # err_loc
            ctypes.POINTER(wintypes.DWORD),  # err_code
        ]
        self.fpn_lib.fpn_remote_is_me.restype = wintypes.BOOL

        self.fpn_lib.fpn_reduce_err_codes.argtypes = [
            ctypes.POINTER(wintypes.DWORD),  # err_loc
            ctypes.POINTER(wintypes.DWORD),  # err_code
        ]
        self.fpn_lib.fpn_reduce_err_codes.restype = wintypes.DWORD

        # Error constants (matching the C header)
        self.FPN_ERROR_PROCESS_PERMISSION = 1
        self.FPN_ERROR_NOT_ME = 2
        self.FPN_ERROR_NO_MATCH = 3

    def authenticate_client(self, context):
        """Authenticate a client by checking if they run under the same Windows user.

        Extracts the client's port number from the gRPC context and uses the FPN
        library to verify that the process using that port belongs to the same
        Windows user as the server process.

        Parameters
        ----------
        context : grpc.ServicerContext
            The gRPC service context containing client connection information.

        Returns
        -------
        tuple[bool, str]
            A tuple of (success, error_message). If success is True, error_message is empty.
            If success is False, error_message contains the reason for failure.
        """
        peer = context.peer()
        print(f"WNUA: Client peer: {peer}")

        # Extract port from peer string (format like "ipv4:127.0.0.1:12345")
        match = re.search(r':(\d+)$', peer)
        if not match:
            print("WNUA: Could not extract port from peer info")
            return False, "Authentication system error"

        try:
            client_port = int(match.group(1))
            print(f"WNUA: Client port: {client_port}")

            # Call FPN library to check if the client port belongs to the same user
            err_loc = wintypes.DWORD()
            err_code = wintypes.DWORD()

            is_same_user = self.fpn_lib.fpn_remote_is_me(
                ctypes.c_ushort(client_port), ctypes.byref(err_loc), ctypes.byref(err_code)
            )

            if is_same_user:
                print("WNUA: Client is same Windows user - ACCESS GRANTED")
                # Add authentication metadata
                context.set_trailing_metadata(
                    [("wnua-authenticated", "true"), ("wnua-user-verified", "same-user")]
                )
                return True, ""
            else:
                print("WNUA: Client is NOT same Windows user - ACCESS DENIED")
                reduced_error = self.fpn_lib.fpn_reduce_err_codes(
                    ctypes.byref(err_loc), ctypes.byref(err_code)
                )

                error_msg = "Authentication failed"
                if reduced_error == self.FPN_ERROR_PROCESS_PERMISSION:
                    error_msg = "Permission denied to check process"
                elif reduced_error == self.FPN_ERROR_NOT_ME:
                    error_msg = "Client is not the same Windows user"
                elif reduced_error == self.FPN_ERROR_NO_MATCH:
                    error_msg = "No process found using client port"
                else:
                    error_msg = f"Authentication error (loc: {err_loc.value},\
                    code: {err_code.value})"

                return False, error_msg

        except Exception as e:
            # This is a real error during authentication
            print(f"WNUA: Error during authentication: {e}")
            return False, "Authentication system error"


class WNUAServerInterceptor(grpc.ServerInterceptor):
    """gRPC server interceptor that enforces Windows Named User Authentication.

    This interceptor wraps all incoming RPC calls and applies WNUA authentication
    by checking that the client process runs under the same Windows user as the
    server process. Uses the FPN library to determine port ownership.

    Attributes
    ----------
    authenticator : WNUAAuthenticator
        The authenticator instance used to verify client credentials.
    """

    def __init__(self):
        """Initialize the WNUA interceptor.

        Creates a new WNUAAuthenticator instance for handling client authentication.

        Raises
        ------
        RuntimeError
            If the FPN library cannot be loaded.
        """
        self.authenticator = WNUAAuthenticator()

    def intercept_service(self, continuation, handler_call_details):
        """Intercept service calls to apply WNUA authentication.

        This method is called for each service handler registration. It wraps
        the original service handler with authentication logic that verifies
        the client's Windows user identity before allowing RPC execution.

        Supports all gRPC call patterns:
        - Unary-Unary: Single request → Single response
        - Unary-Stream: Single request → Stream of responses
        - Stream-Unary: Stream of requests → Single response
        - Stream-Stream: Stream of requests → Stream of responses

        Parameters
        ----------
        continuation : callable
            Function to get the original service handler.
        handler_call_details : grpc.HandlerCallDetails
            Details about the service call being intercepted.

        Returns
        -------
        grpc.RpcMethodHandler or None
            Modified handler with authentication wrapper for the appropriate
            call pattern, or None if no handler exists.
        """
        # Get the original handler from the continuation
        original_handler = continuation(handler_call_details)

        if original_handler is None:
            return None

        # Generic authentication wrapper that works for all call patterns
        def create_authenticated_wrapper(original_method):
            """Create an authenticated wrapper for any handler method."""

            def wrapper(*args):
                # The context is always the last argument
                context = args[-1]
                success, error_message = self.authenticator.authenticate_client(context)
                if not success:
                    # Authentication failed, abort the RPC
                    if "system error" in error_message.lower():
                        context.abort(grpc.StatusCode.INTERNAL, error_message)
                    else:
                        context.abort(grpc.StatusCode.UNAUTHENTICATED, error_message)
                    return  # This line won't be reached due to abort exception
                return original_method(*args)

            return wrapper

        # Handler type mapping: (attribute_name, handler_constructor)
        handler_types = [
            ('unary_unary', grpc.unary_unary_rpc_method_handler),
            ('unary_stream', grpc.unary_stream_rpc_method_handler),
            ('stream_unary', grpc.stream_unary_rpc_method_handler),
            ('stream_stream', grpc.stream_stream_rpc_method_handler),
        ]

        # Find the active handler type and wrap it
        for attr_name, handler_constructor in handler_types:
            original_method = getattr(original_handler, attr_name)
            if original_method is not None:
                authenticated_method = create_authenticated_wrapper(original_method)
                return handler_constructor(
                    authenticated_method,
                    request_deserializer=original_handler.request_deserializer,
                    response_serializer=original_handler.response_serializer,
                )

        # Unknown handler type, return as-is
        return original_handler


def create_wnua_server(max_workers=10):
    """Create a gRPC server with Windows Named User Authentication enabled.

    Creates a new gRPC server instance configured with the WNUA interceptor
    that enforces same-user authentication for all incoming RPC calls. This
    function is only supported on Windows platforms.

    Parameters
    ----------
    max_workers : int, optional
        Maximum number of worker threads in the server's thread pool, by default 10.

    Returns
    -------
    grpc.Server
        Configured gRPC server instance with WNUA interceptor enabled.
    """
    # Create server with WNUA interceptor
    interceptors = [WNUAServerInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=max_workers), interceptors=interceptors
    )

    return server
