import os
import time
import xml.etree.ElementTree as ET

import pytest

import ansys.meshing.prime as prime


@pytest.fixture(scope="session", autouse=True)
def startAnsysPrimeServer(prime_root=None, ip='127.0.0.1', port=50055, n_procs=1):
    if n_procs == 1:
        client = prime.launch_prime(prime_root=prime_root, ip=ip, port=port)
    else:
        client = prime.launch_prime(prime_root=prime_root, ip=ip, port=port, n_procs=n_procs)
    return client


@pytest.fixture(scope="session", autouse=True)
def getRemoteClient(startAnsysPrimeServer):
    ip = os.environ.get('PYPRIMEMESH_IP', '127.0.0.1')
    port = int(os.environ.get('PYPRIMEMESH_PORT', '50055'))
    if 'PYPRIMEMESH_EXTERNAL_SERVER' in os.environ:
        client = prime.Client(ip=ip, port=port)
    else:
        client = startAnsysPrimeServer
    return client


def pytest_sessionfinish(session, exitstatus):
    print("Cleaning up")

    def close_server(getRemoteClient):
        getRemoteClient.exit()



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
