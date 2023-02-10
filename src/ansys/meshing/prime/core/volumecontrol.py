from ansys.meshing.prime.autogen.volumecontrol import VolumeControl as _VolumeControl

# isort: split
from ansys.meshing.prime.autogen.commonstructs import SetNameResults
from ansys.meshing.prime.autogen.volumecontrolstructs import VolumeControlParams


class VolumeControl(_VolumeControl):
    """Volume control is used to define the scope and type of volume mesh to be generated."""

    def __init__(self, model, id, object_id, name, local=False):
        """__init__(Model self, int id, int object_id, char* name)"""
        _VolumeControl.__init__(self, model, id, object_id, name)
        self._model = model
        self._name = name

    def __str__(self) -> str:
        params = VolumeControlParams(model=self._model)
        result = _VolumeControl.get_summary(self, params)
        return result.message

    def set_suggested_name(self, name: str) -> SetNameResults:
        """Sets the unique name for the volume control based on the given suggested name.


        Parameters
        ----------
        name : str
            Suggested name for the volume control.

        Returns
        -------
        SetNameResults
            Returns a name of the volume control.


        Examples
        --------
        >>> volume_control.set_suggested_name("control1")

        """
        result = _VolumeControl.set_suggested_name(self, name)
        self._name = result.assigned_name
        return result

    @property
    def name(self):
        """Gets the name of volume control.

        Returns
        -------
        str
            Returns a name of volume control.

        Examples
        --------
        >>> print(volume_control.name)

        """
        return self._name
