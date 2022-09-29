import unittest
from .common import PrimeTestCase, PrimeTextTestRunner


class TestModel(PrimeTestCase):
    def test_model_exists(self):
        model = self._model
        self.assertTrue(model != None)


if __name__ == '__main__':
    unittest.main(testRunner=PrimeTextTestRunner, exit=False, verbosity=2)
