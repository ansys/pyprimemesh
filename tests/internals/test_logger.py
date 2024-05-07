import datetime

from ansys.meshing.prime.internals.logger import PrimeLogger


def test_logger(tmp_path):
    logs_path = str(tmp_path) + "/logs"
    prime_logger_setup = PrimeLogger(logger_name="Test_logger")
    prime_logger_setup.add_file_handler(log_dir=logs_path)
    logger = prime_logger_setup.python_logger

    logger.setLevel("INFO")
    msg = "this is an error"
    logger.error(msg)

    now = datetime.datetime.now()

    # Another call to singleton, should be configured already
    prime_logger_setup_2 = PrimeLogger()
    logger_2 = prime_logger_setup_2.python_logger
    msg_2 = "this is another error"
    logger_2.error(msg_2)

    # Assert we are using a singleton.
    with open(logs_path + '/log_' + now.strftime("%Y-%m-%d") + '.log', 'r') as file:
        line_1 = file.readline()
        assert msg in line_1
        line_2 = file.readline()
        assert msg_2 in line_2
