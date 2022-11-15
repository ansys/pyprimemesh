""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class ThinVolumeControl(CoreObject):
    """ThinVolumeControl allows you to generate prisms in the space between surfaces.

    ThinVolumeControl allows you to control generation of prisms in the thin space between surfaces. Controls include setting the source face scope, target face scope and thin volume mesh parameters.
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize ThinVolumeControl """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    @property
    def id(self):
        """ Get the id of ThinVolumeControl."""
        return self._id

    @property
    def name(self):
        """ Get the name of ThinVolumeControl."""
        return self._name
