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

"""Module for gRPC utilities."""
import ansys.meshing.prime.internals.defaults as defaults


def get_default_channel_args():
    """Get default channel arguments for gRPC.

    Returns
    -------
    List
        List with channel parameters.
    """
    import os

    return (
        [
            # ('grpc.keepalive_time_ms', 60000), # 1 minute
            ('grpc.keepalive_timeout_ms', 60000),  # 60 seconds
            ('grpc.keepalive_permit_without_calls', True),
            ('grpc.http2.max_pings_without_data', 0),  # Disable
            ('grpc.max_send_message_length', defaults.max_message_length()),
            ('grpc.max_receive_message_length', defaults.max_message_length()),
        ]
        if "PYPRIMEMESH_DEVELOPER_MODE" not in os.environ
        else [
            ('grpc.max_send_message_length', defaults.max_message_length()),
            ('grpc.max_receive_message_length', defaults.max_message_length()),
        ]
    )
