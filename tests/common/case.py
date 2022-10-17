import os
import time
import unittest

import ansys.meshing.prime as prime


class PrimeTestCase(unittest.TestCase):
    _client = None

    @classmethod
    def startPyPrimeServer(cls, pyprime_root=None, ip='127.0.0.1', port=50055, n_procs=1):
        if n_procs == 1:
            client = prime.launch_prime(pyprime_root=pyprime_root, ip=ip, port=port)
        else:
            client = prime.launch_prime(
                pyprime_root=pyprime_root, ip=ip, port=port, n_procs=n_procs
            )
        return client

    @classmethod
    def getRemoteClient(cls):
        ip = os.environ.get('PYPRIME_IP', '127.0.0.1')
        port = os.environ.get('PYPRIME_PORT', 50055)
        if 'PYPRIME_EXTERNAL_SERVER' in os.environ:
            client = prime.Client(ip=ip, port=port)
        else:
            pyprime_root = os.environ.get('PYPRIME_INSTALL_ROOT', None)
            client = cls.startPyPrimeServer(pyprime_root=pyprime_root, ip=ip, port=port, n_procs=1)

        return client

    @classmethod
    def setUpClass(cls) -> None:
        cls._client = cls.getRemoteClient()
        if cls._client is not None:
            cls._client.__enter__()
            cls._model = cls._client.model
        else:
            raise ValueError("Cannot launch and connect to the server")

        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        if cls._client is not None:
            cls._client.__exit__(None, None, None)
        return super().tearDownClass()

    def setUp(self):
        self._startTime = time.time()
        return super().setUp()

    def tearDown(self):
        self._endTime = time.time()
        self._timeTaken = self._endTime - self._startTime
        return super().tearDown()
