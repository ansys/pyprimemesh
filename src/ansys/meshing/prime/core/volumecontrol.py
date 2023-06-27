"""Module containing VolumeControl related classes and methods."""
from ansys.meshing.prime.autogen.volumecontrol import VolumeControl as _VolumeControl

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults
from ansys.meshing.prime.autogen.volumecontrolstructs import VolumeControlParams


class VolumeControl(_VolumeControl):
    """Defines the scope and type of volume mesh to generate.

    Parameters
    ----------
    model : CommunicationManager
        Server model to create and modify volume controls from.
    id : int
        ID of the volume control.
    object_id : int
        Object ID of the volume control.
    name : str
        Name of the volume control.
    local : bool, optional
        Unused. The default is ``False``.
    """

    def __init__(self, model, id, object_id, name, local=False):
        """Initialize the superclass and the ``model`` variable."""
        _VolumeControl.__init__(self, model, id, object_id, name)
        self._model = model
        self._name = name

    def __str__(self) -> str:
        """Get a representation of the class in string format.

        Returns
        -------
        str
            Class data in string format.
        """
        params = VolumeControlParams(model=self._model)
        # TODO: function get_summary() not implemented
        result = _VolumeControl.get_summary(self, params)
        return result.message

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Set the unique name for the volume control based on a suggested name.

        Parameters
        ----------
        name : str
            Suggested name for the volume control.

        Returns
        -------
        SetNameResults
            Newly suggested name of the volume control.


        Examples
        --------
        >>> volume_control.set_suggested_name("control1")

        """
        result = _VolumeControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def name(self):
        """Get the name of the volume control.

        Returns
        -------
        str
            Name of the volume control.

        Examples
        --------
        >>> print(volume_control.name)

        """
        return self._name
