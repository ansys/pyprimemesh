from logging import Logger

from ansys.meshing.prime.internals.utils import print_logs_after_command, to_camel_case


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
