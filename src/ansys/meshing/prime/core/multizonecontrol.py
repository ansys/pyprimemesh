"""Module containing classes and methods related to multi-zone control."""
from ansys.meshing.prime.autogen.multizonecontrol import (
    MultiZoneControl as _MultiZoneControl,
)
from ansys.meshing.prime.internals.comm_manager import CommunicationManager


class MultiZoneControl(_MultiZoneControl):
    """MultiZone Control to describe parameters and controls used for MultiZone meshing."""

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """Initialize class variables and the superclass."""
        self._model = model
        _MultiZoneControl.__init__(self, model, id, object_id, name)

    def __str__(self) -> str:
        """Provide a string implementation for control."""
        return "Not implemented yet"
