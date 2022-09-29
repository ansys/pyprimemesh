import os
import unittest
import xml.etree.ElementTree as ET

from .arm_utils import is_running_in_arm


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


class PrimeTestResult(unittest.TestResult):
    def __init__(self, stream=None, descriptions=None, verbosity=None):
        self.successes = []
        super().__init__(stream, descriptions, verbosity)

    def addSuccess(self, test):
        self.successes.append(test)
        return super().addSuccess(test)

    # def startTestRun(self) -> None:
    #     super().startTestRun()
    #     from .test_case import setupTestingModule
    #     setupTestingModule()

    def stopTestRun(self):
        super().stopTestRun()
        if is_running_in_arm():
            write_arm_scenarios(self)


class PrimeTextTestResult(PrimeTestResult, unittest.TextTestResult):
    pass
