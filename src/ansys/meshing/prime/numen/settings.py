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

import json
import logging
import sys

import ansys.meshing.prime.numen.utils.macros as macros
from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.cached_data import CachedData
from ansys.meshing.prime.numen.utils.communicator import call_method


def set_cwd(model: prime.Model, cwd_params: dict, cached_data: CachedData):
    path = macros.resolve_path(cwd_params["path"])
    model.logger.python_logger.disabled = True
    model.set_working_directory(path)
    model.logger.python_logger.disabled = False


def add_file_logging(logger: logging.Logger, log_file: str, verbosity: int):
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setLevel(verbosity)

    file_formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)


def setup_server_logging(model: prime.Model, log_file_name: str):
    if log_file_name:
        model_id = model._object_id
        logger_info = json.loads(
            call_method(model, "PrimeMesh::Model/GetChildObjectsJson", model_id, {})
        )
        log_file_settings = {
            "fileName": log_file_name,
            "overwrite": True,
            "append": False,
        }
        call_method(
            model, "PrimeMesh::Logger/StartLogFile", logger_info["Logger"], log_file_settings
        )


def set_logger_verbosity(logger: logging.Logger, verbosity: int, model: prime.Model = None):
    stream_handler = None
    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            stream_handler = handler
            break
    if stream_handler is None:
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)

    stream_handler.setLevel(verbosity)
    formatter = logging.Formatter('%(message)s')
    stream_handler.setFormatter(formatter)
    logger.setLevel(verbosity)

    if model is not None:
        model_id = model._object_id
        logger_info = json.loads(
            call_method(model, "PrimeMesh::Model/GetChildObjectsJson", model_id, {})
        )
        server_args = {"verbosityLevel": verbosity}
        call_method(
            model, "PrimeMesh::Logger/SetVerbosityLevel", logger_info["Logger"], server_args
        )


def settings(model: prime.Model, settings_params: dict, cached_data: CachedData):
    verbosity = settings_params.get("verbosity")
    base_log_file = settings_params.get("log_file_name")
    cwd = settings_params.get("cwd")
    if cwd:
        cwd_params = {"path": settings_params["cwd"]}
        set_cwd(model, cwd_params, cached_data)
    set_logger_verbosity(cached_data._logger, verbosity, model)
    if base_log_file:
        base_name, ext = (
            base_log_file.rsplit('.', 1) if '.' in base_log_file else (base_log_file, '')
        )
        server_log_file = f"{base_name}_server.{ext}"
        client_log_file = f"{base_name}_client.{ext}"
        setup_server_logging(model, server_log_file)
        add_file_logging(cached_data._logger, client_log_file, verbosity)
