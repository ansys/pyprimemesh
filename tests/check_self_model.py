import unittest
import ansys.meshing.prime as prime
from tests import PrimeTestCase, PrimeTextTestRunner

class TestModel(PrimeTestCase):
    def test_self_model_exists(self):
        model=self._model
        self.assertTrue(model != None)

if __name__ == '__main__':
    unittest.main(testRunner=PrimeTextTestRunner, exit=False, verbosity=2)