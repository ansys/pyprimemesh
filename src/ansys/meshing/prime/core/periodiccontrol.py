"""Module containing classes and methods related to periodic control."""

from ansys.meshing.prime.autogen.periodiccontrol import (
    PeriodicControl as _PeriodicControl,
)

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults
from ansys.meshing.prime.autogen.periodiccontrolstructs import PeriodicControlParams


class PeriodicControl(_PeriodicControl):
    """Defines the scope and transformation for periodic surfaces.

    Parameters
    ----------
    model : CommunicationManager
        Server model to create and modify periodic controls from.
    id : int
        ID of the control.
    object_id : int
        Object ID of the control.
    name : str
        Name of the periodic control.
    local : bool, optional
        Unused. The default is ``False``.
    """

    def __init__(self, model, id, object_id, name, local=False):
        """Initialize class variables and the superclass."""
        _PeriodicControl.__init__(self, model, id, object_id, name)
        self._model = model
        self._name = name

    def __str__(self) -> str:
        """Get a representation of the class in string format.

        Returns
        -------
        str
            Class data in string format.
        """
        params = PeriodicControlParams(model=self._model)
        result = _PeriodicControl.get_summary(self, params)
        return result.message

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Set the unique name for the periodic control to a suggested name.

        Parameters
        ----------
        name : str
            Suggested name for the periodic control.

        Returns
        -------
        SetNameResults
            Newly suggested name of the periodic control.

        Examples
        --------
        >>> periodic_control.set_suggested_name("control1")

        """
        result = _PeriodicControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def name(self):
        """Get the name of the periodic control.

        Returns
        -------
        str
            Name of the periodic control.

        Examples
        --------
        >>> print(periodic_control.name)

        """
        return self._name
