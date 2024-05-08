"""Module containing SizeControl related classes and methods."""
from ansys.meshing.prime.autogen.sizecontrol import SizeControl as _SizeControl

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults
from ansys.meshing.prime.autogen.sizecontrolstructs import SizeControlSummaryParams


class SizeControl(_SizeControl):
    """Size control is used to compute the size field.

    The size field is computed based on the size control defined.
    Different type of size controls provide control over how the mesh size is distributed on a
    surface or within the volume.

    Parameters
    ----------
    model : Model
        Server model to create SizeControl object.
    id : int
        Id of the SizeControl.
    object_id : int
        Object id of the SizeControl.
    name : str
        Name of the SizeControl..
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
