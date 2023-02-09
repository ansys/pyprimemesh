from ansys.meshing.prime.autogen.periodiccontrol import (
    PeriodicControl as _PeriodicControl,
)

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults
from ansys.meshing.prime.autogen.periodiccontrolstructs import PeriodicControlParams


class PeriodicControl(_PeriodicControl):
    """Periodic control is used to define the scope and transformation for periodic surfaces."""

    def __init__(self, model, id, object_id, name, local=False):
        """__init__(Model self, int id, int object_id, char* name)"""
        _PeriodicControl.__init__(self, model, id, object_id, name)
        self._model = model
        self._name = name

    def __str__(self) -> str:
        params = PeriodicControlParams(model=self._model)
        result = _PeriodicControl.get_summary(self, params)
        return result.message

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Sets the unique name for the periodic control based on the given suggested name.


        Parameters
        ----------
        name : str
            Suggested name for the periodic control.

        Returns
        -------
        SetNameResults
            Returns a name of the periodic control.


        Examples
        --------
        >>> periodic_control.set_suggested_name("control1")

        """
        result = _PeriodicControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def name(self):
        """Gets the name of the periodic control.

        Returns
        -------
        str
            Returns the name of the periodic control.

        Examples
        --------
        >>> print(periodic_control.name)

        """
        return self._name
