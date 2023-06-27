"""Module containing WrapperControl related classes and methods."""
from ansys.meshing.prime.autogen.wrappercontrol import WrapperControl as _WrapperControl

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults as SetNameResults
from ansys.meshing.prime.internals.comm_manager import CommunicationManager


class WrapperControl(_WrapperControl):
    """Provides all parameters and controls used for wrapping.

    Parameters
    ----------
    model : CommunicationManager
        Server model to create and modify wrapper controls from.
    id : int
        ID of the wrapper control.
    object_id : int
        Object ID of the wrapper control.
    name : str
        Name of the wrapper control
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """Initialize the superclass and the ''Model'' variable."""
        self._model = model
        _WrapperControl.__init__(self, model, id, object_id, name)

    def __str__(self) -> str:
        """Get a representation of the class in string format.

        Returns
        -------
        str
            Class data in string format.
        """
        return "Not implemented yet"

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Set the unique name for the wrapper control based on a suggested name.

        Parameters
        ----------
        name : str
            Suggested name for the wrapper control.

        Returns
        -------
        SetNameResults
            Newly assigned name of the wrapper control.


        Examples
        --------
        >>> wrapper_control.set_suggested_name("wrapper_control1")

        """
        result = _WrapperControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def name(self):
        """Get the name of the wrapper control.

        Returns
        -------
        str
            Name of the wrapper control.

        Examples
        --------
        >>> print(wrapper_control.name)

        """
        return self._name
