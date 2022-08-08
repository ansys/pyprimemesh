# Copyright 2023 ANSYS, Inc.
# Unauthorized use, distribution, or duplication is prohibited.
import logging

# import psutil


def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


def terminate_process(process):
    import sys
    import signal

    if sys.platform.startswith('win32'):
        # process.send_signal(signal.CTRL_C_EVENT)
        process.send_signal(signal.CTRL_BREAK_EVENT)
    if process.stdin is not None:
        process.stdin.close()
    if process.stdout is not None:
        process.stdout.close()
    if process.stderr is not None:
        process.stderr.close()
    process.terminate()
    process.wait()


def print_logs_before_command(logger: logging.Logger, command: str, args):
    logger.info("Executing " + command)
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Command: " + command)
        logger.debug("Args:")
        for key in args:
            logger.debug("    " + key + ":")
            val = args[key]
            printable_str = ""
            if hasattr(val, '__str__'):
                printable_str = val.__str__()
            elif type(val) == 'str':
                printable_str = val
            else:
                printable_str = str(val)
            for line in printable_str.splitlines():
                logger.debug("        " + line)
        logger.debug("")


def print_logs_after_command(logger: logging.Logger, command: str, ret):
    logger.info("Finished " + command)
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Return: ")
        printable_str = ""
        if hasattr(ret, '__str__'):
            printable_str = ret.__str__()
        elif type(ret) == 'str':
            printable_str = ret
        else:
            printable_str = str(ret)
        for line in printable_str.splitlines():
            logger.debug("        " + line)
        logger.debug("")
