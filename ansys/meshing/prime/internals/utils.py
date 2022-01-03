import subprocess
import os
import sys
import logging
# import psutil

def start_server(prime_installdir: str=None, ip: str="localhost", port: int=50052):
    proc = None
    try:
        if "PRIME_INSTALLDIR" not in os.environ.keys() and prime_installdir is None:
            raise RuntimeError("Specify where your Prime install is present either through environment or as parameter")
        if prime_installdir is None:
            prime_installdir = os.environ["PRIME_INSTALLDIR"]
        if (sys.platform == "linux") :
            run_script = os.path.join(prime_installdir, 'runPrimeApp.sh')
        else :
            run_script = os.path.join(prime_installdir, 'RunPrime.bat')
        server_path = os.path.join(prime_installdir, 'scripts', 'PrimeGRPC.py')
        proc = subprocess.Popen([run_script, server_path, f"--ip={ip}", f"--port={port}"])
    except Exception as err:
        proc.terminate()
        print(str(err))

def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])

def terminate_child_processes(pid):
    pass
    # parent = psutil.Process(pid)
    # children = parent.children(recursive=True)
    # [ child.terminate() for child in children ]
    # gone, still_alive = psutil.wait_procs(children, timeout=2)

def print_logs_before_command(logger : logging.Logger, command : str, args):
    logger.info("Executing " + command)
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Command: " + command)
        logger.debug("Args:")
        for key in args:
            logger.debug("    " + key + ":")
            val = args[key]
            printable_str = ""
            if (hasattr(val, '__str__')):
                printable_str = val.__str__()
            elif (type(val) == 'str'):
                printable_str = val
            else:
                printable_str = str(val)
            for line in printable_str.splitlines():
                logger.debug("        " + line)
        logger.debug("")

def print_logs_after_command(logger : logging.Logger, command : str, ret):
    logger.info("Finished " + command)
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("Return: ")
        printable_str = ""
        if (hasattr(ret, '__str__')):
            printable_str = ret.__str__()
        elif (type(ret) == 'str'):
            printable_str = ret
        else:
            printable_str = str(ret)
        for line in printable_str.splitlines():
            logger.debug("        " + line)
        logger.debug("")

