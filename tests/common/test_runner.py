import unittest
from .test_result import PrimeTextTestResult

class PrimeTextTestRunner(unittest.TextTestRunner):
    resultClass = PrimeTextTestResult
    def _makeResult(self):
        return PrimeTextTestResult(self.stream, self.descriptions, self.verbosity)