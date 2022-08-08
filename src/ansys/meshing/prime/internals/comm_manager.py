# Copyright 2023 ANSYS, Inc.
# Unauthorized use, distribution, or duplication is prohibited.
from ansys.meshing.prime.internals.communicator import Communicator


class CommunicationManager:
    def __init__(self, comm: Communicator):
        self._comm = comm

    @property
    def _communicator(self):
        return self._comm
