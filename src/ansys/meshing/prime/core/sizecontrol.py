"""Module containing SizeControl related classes and methods."""
from ansys.meshing.prime.autogen.sizecontrol import SizeControl as _SizeControl

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults
from ansys.meshing.prime.autogen.sizecontrolstructs import SizeControlSummaryParams


class SizeControl(_SizeControl):
    """Compute the size field for a volumetric surface meshing.

    Parameters
    ----------
    model : CommunicationManager
        Server model to create and modify size controls from.
    id : int
        ID of the size control.
    object_id : int
        Object ID of the size control.
    name : str
        Name of the size control.
    local : bool, optional
        Unused. The default is ``False``.
    """

    def __init__(self, model, id, object_id, name, local=False):
        """Initialize class variables and the superclass."""
        _SizeControl.__init__(self, model, id, object_id, name)
        self._model = model
        self._name = name

    def __str__(self) -> str:
        """Get a representation of the class in string format.

        Returns
        -------
        str
            Class data in string format.
        """
        params = SizeControlSummaryParams(model=self._model)
        result = _SizeControl.get_summary(self, params)
        return result.message

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Set the unique name for the size control to a suggested name.

        Parameters
        ----------
        name : str
            Suggested name for the size control.

        Returns
        -------
        SetNameResults
            Newly suggested name for the size control.


        Examples
        --------
        >>> size_control.set_suggested_name("control1")

        """
        result = _SizeControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def name(self):
        """Get the name of size control.

        Returns
        -------
        str
            Name of the size control.

        Examples
        --------
        >>> print(size_control.name)

        """
        return self._name
