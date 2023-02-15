from ansys.meshing.prime.autogen.sizecontrol import SizeControl as _SizeControl

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults
from ansys.meshing.prime.autogen.sizecontrolstructs import SizeControlSummaryParams


class SizeControl(_SizeControl):
    """Size control is used to compute size field for volumetric surface meshing."""

    def __init__(self, model, id, object_id, name, local=False):
        """__init__(Model self, int id, int object_id, char* name)"""
        _SizeControl.__init__(self, model, id, object_id, name)
        self._model = model
        self._name = name

    def __str__(self) -> str:
        params = SizeControlSummaryParams(model=self._model)
        result = _SizeControl.get_summary(self, params)
        return result.message

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Sets the unique name for the size control based on the given suggested name.


        Parameters
        ----------
        name : str
            Suggested name for the size control.

        Returns
        -------
        SetNameResults
            Returns a name of the size control.


        Examples
        --------
        >>> size_control.set_suggested_name("control1")

        """
        result = _SizeControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def name(self):
        """Gets the name of size control.

        Returns
        -------
        str
            Returns a name of the size control.

        Examples
        --------
        >>> print(size_control.name)

        """
        return self._name
