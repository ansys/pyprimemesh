import datetime

from ansys.meshing.prime.internals.logger import PrimeLogger


def test_logger(tmp_path):
    logs_path = str(tmp_path) + "/logs"
    prime_logger_setup = PrimeLogger(logger_name="Test_logger")
    prime_logger_setup.add_file_handler(logs_dir=logs_path)
    logger = prime_logger_setup.get_logger()

    logger.setLevel("INFO")
    msg = "this is an error"
    logger.error(msg)

    now = datetime.datetime.now()
    with open(logs_path + '/log_' + now.strftime("%Y-%m-%d") + '.log', 'r') as file:
        for line in file:
            pass
        last_line = line
        assert msg in last_line
