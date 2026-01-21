# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""General fixtures to use in all test modules."""
import os
import xml.etree.ElementTree as ET

import ansys.tools.visualization_interface as viz_interface
import pytest

import ansys.meshing.prime as prime
from ansys.meshing.prime.examples import download_test_examples

viz_interface.TESTING_MODE = True


class RemoteClientManager:
    """Manager class for starting and closing the remote client of
    Prime.
    """

    def __init__(self) -> None:
        self.client = None

    def start_ansys_prime_server(self, prime_root=None, ip='127.0.0.1', port=50055, n_procs=1):
        """Initialization of Ansys Prime Server.

        Parameters
        ----------
        prime_root : str, optional
            Location of the prime installation, by default ``None``.
        ip : str, optional
            IP where the server is located, by default ``'127.0.0.1'``.
        port : int, optional
            Port where the server is running, by default ``50055``.
        n_procs : int, optional
            Number of distributed processes to spawn when running in distributed mode,
            by default ``1``.
        """
        if n_procs == 1:
            self.client = prime.launch_prime(prime_root=prime_root, ip=ip, port=port)
        else:
            self.client = prime.launch_prime(
                prime_root=prime_root, ip=ip, port=port, n_procs=n_procs
            )

    def start_remote_client(self):
        """Starts the Ansys Prime remote client with the default values."""
        ip = os.environ.get('PYPRIMEMESH_IP', '127.0.0.1')
        port = int(os.environ.get('PYPRIMEMESH_PORT', '50055'))
        if 'PYPRIMEMESH_EXTERNAL_SERVER' in os.environ:
            self.client = prime.Client(ip=ip, port=port)
        else:
            prime_root = os.environ.get('PYPRIMEMESH_INSTALL_ROOT', None)
            self.start_ansys_prime_server(prime_root=prime_root, ip=ip, port=port)

    def stop_remote_client(self):
        """Stops the Ansys Prime client and server."""
        self.client.exit()


@pytest.fixture(scope="session", autouse=True)
def get_remote_client():
    """Initializes and starts Ansys Prime Server. This function is automatically called
    at the start of the test session and runs the code after the yield when the
    tests finish their execution.

    Yields
    ------
    Client
        Initialized remote client of Ansys Prime Server.
    """
    client_manager = RemoteClientManager()
    client_manager.start_remote_client()
    yield client_manager.client

    # runs when tests are done
    client_manager.stop_remote_client()


@pytest.fixture(scope="session", autouse=True)
def get_examples():
    """Downloads the prime examples for them to be available
    in any test.
    """

    examples_dict = {}
    elbow_lucid = prime.examples.download_elbow_pmdat()
    examples_dict["elbow_lucid"] = elbow_lucid

    toy_car = prime.examples.download_toy_car_pmdat()
    examples_dict["toy_car"] = toy_car

    pipe_tee = prime.examples.download_pipe_tee_pmdat()
    examples_dict["pipe_tee"] = pipe_tee

    bracket = prime.examples.download_bracket_fmd()
    examples_dict["bracket"] = bracket

    mixing_elbow_windows = prime.examples.download_elbow_scdoc()
    examples_dict["elbow_lucid_scdoc"] = mixing_elbow_windows

    return examples_dict


@pytest.fixture(scope="session", autouse=True)
def get_testfiles():
    """Downloads unit test files"""
    if not os.path.exists("./tests/core/test_files/"):
        os.mkdir(os.path.abspath("./tests/core/test_files/"))
    download_test_examples(destination=str(os.path.abspath("./tests/core/test_files/")))


def create_scenario_element(test, id):
    testName, className = str(test).split()
    _, className = className.strip('()').split('.')
    return ET.Element('SCENARIO', ID=str(id), DESC=f'{className}/{testName}')


def write_arm_scenarios(result, scenarioLogName='scenario.log'):
    xmlFileName = os.path.join(os.getcwd(), scenarioLogName)

    scenarios = []
    for idx, test in enumerate(result.successes):
        scenarioCount = idx + 1
        scenario = create_scenario_element(test, scenarioCount)
        timeTaken = ET.SubElement(scenario, 'ELAPSED')
        timeTaken.text = str(test._timeTaken)
        testResult = ET.SubElement(scenario, 'RESULT')
        testResult.text = 'PASSED'
        scenarios.append(scenario)

    scenarioIdxOffset = len(scenarios)
    for idx, failedTest in enumerate(result.failures):
        test, msg = failedTest
        scenarioCount = scenarioIdxOffset + idx + 1
        scenario = create_scenario_element(test, scenarioCount)
        failed = ET.SubElement(scenario, 'FAIL')
        failed.text = msg.rsplit('File', 1)[-1]
        timeTaken = ET.SubElement(scenario, 'ELAPSED')
        timeTaken.text = str(test._timeTaken)
        testResult = ET.SubElement(scenario, 'RESULT')
        testResult.text = 'FAILED'
        scenarios.append(scenario)

    scenarioIdxOffset = len(scenarios)
    for idx, errorTest in enumerate(result.errors):
        test, msg = errorTest
        scenarioCount = scenarioIdxOffset + idx + 1
        scenario = create_scenario_element(test, scenarioCount)
        errored = ET.SubElement(scenario, 'ERROR')
        errored.text = msg
        timeTaken = ET.SubElement(scenario, 'ELAPSED')
        timeTaken.text = str(test._timeTaken)
        testResult = ET.SubElement(scenario, 'RESULT')
        testResult.text = 'ERROR'
        scenarios.append(scenario)

    if scenarios:
        lastScenario = scenarios[-1]
        ET.SubElement(lastScenario, 'ARM_JOURNAL_COMPLETE')

    for scenario in scenarios:
        try:
            import xml.dom.minidom as minidom

            xmlstr = minidom.parseString(ET.tostring(scenario)).toprettyxml(indent='   ')
        except:
            xmlstr = ET.tostring(scenario)

        with open(xmlFileName, 'a') as scenario_log:
            scenario_log.write(xmlstr)


def pytest_sessionfinish(session, exitstatus):
    """Cleanup generated folder."""
    tmp_path = os.path.abspath("./tests/core/test_files/")
    if os.path.exists(tmp_path):
        os.rmdir(tmp_path)
