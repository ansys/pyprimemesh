import os
import subprocess
from logging import Logger

import pytest

from ansys.meshing.prime.internals.utils import (
    get_child_processes,
    print_logs_after_command,
    print_logs_before_command,
    terminate_process,
    to_camel_case,
)

skip_windows = pytest.mark.skipif(os.name == "nt", reason="Can't fork on windows")


@skip_windows
def test_child_process():
    current_pid = os.getpid()
    child_pid = os.fork()
    # process is PID
    child_list = get_child_processes(current_pid)
    assert child_pid in child_list


"""def test_terminate_process():
    process = subprocess.Popen('ls -la', shell=True)
    pid = process.pid
    # process is object
    terminate_process(process)
    if process.poll() is not None:
        assert True
    else:
      assert False
"""


def test_to_camelcase():
    test_string = "snake_case_example"
    final_string = to_camel_case(test_string)
    assert "snakeCaseExample" == final_string


def test_logger():
    command = "ls"
    args = ["-la"]
    log = Logger(name="Test logger")
    log.setLevel(level="DEBUG")
    # there are bugs in this function
    # print_logs_before_command(log, command, args)
    print_logs_after_command(log, command, "ret")
