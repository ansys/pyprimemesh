import os
import xml.etree.ElementTree as ET

import pytest

import ansys.meshing.prime as prime


class RemoteClientManager:
    """Manager class for starting and closing the remote client of
    Prime.
    """

    def __init__(self) -> None:
        self.client = None

    def start_ansys_prime_server(self, prime_root=None, ip='127.0.0.1', port=50055, n_procs=1):
        """Initialization of the Ansys Prime server.

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
        if 'PYPRIMEMESH_LAUNCH_CONTAINER' in os.environ:
            version = os.environ.get('PYPRIMEMESH_CONTAINER_TAG', None)
        if n_procs == 1:
            self.client = prime.launch_prime(
                prime_root=prime_root, ip=ip, port=port, version=version
            )
        else:
            self.client = prime.launch_prime(
                prime_root=prime_root, ip=ip, port=port, n_procs=n_procs, version=version
            )

    def start_remote_client(self):
        """Starts the Ansys Prime remote client with the default values."""
        ip = os.environ.get('PYPRIMEMESH_IP', '127.0.0.1')
        port = int(os.environ.get('PYPRIMEMESH_PORT', '50055'))
        if 'PYPRIMEMESH_EXTERNAL_SERVER' in os.environ:
            self.client = prime.Client(ip=ip, port=port)
        else:
            prime_root = os.environ.get('PYPRIMEMESH_INSTALL_ROOT', None)
            self.start_ansys_prime_server(prime_root=prime_root, ip=ip, port=port, n_procs=1)

    def stop_remote_client(self):
        """Stops the Ansys Prime client and server."""
        self.client.exit()


@pytest.fixture(scope="session", autouse=True)
def get_remote_client():
    """Initializes and starts Ansys Prime. This funtion is automatically called
    at the start of the test session and runs the code after the yield when the
    tests finish their execution.

    Yields
    ------
    Client
        Initialized remote client of Ansys prime
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

    return examples_dict


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
