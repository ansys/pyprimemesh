from ansys.meshing.prime.autogen.controldata import ControlData as _ControlData
from ansys.meshing.prime.core.sizecontrol import SizeControl
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import (SizingType)

from typing import List

class ControlData(_ControlData):
    """ControlData acts as a container for all controls (size controls, prism controls,
    wrapper controls, etc).

    """
    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initializes ControlData """
        self._model = model
        self._wrapper_controls = []
        self._size_controls = []
        self._prism_controls = []
        _ControlData.__init__(self, model, id, object_id, name)

    def create_size_control(self, sizing_type : SizingType) -> SizeControl:
        """ Creates size control for the given sizing type.


        Parameters
        ----------
        type : SizingType
            Sizing type used to create a size control.

        Returns
        -------
        SizeControl *
            Returns the size control.

        Notes
        -----
        An empty size control is created on calling this API.

        Examples
        --------
        >>> size_control = model.control_data.create_size_control(SizingType.Curvature)

        """
        #[TODO] check for requireent to pass name here
        res = _ControlData.create_size_control(self, sizing_type)
        new_size_control = SizeControl(self._model, res[0], res[1], res[2])
        self._size_controls.append(new_size_control)
        return new_size_control

    def get_size_control_by_name(self, name : str) -> SizeControl:
        """ Gets the size control by name.


        Parameters
        ----------
        name : str
            Name of the size control.

        Returns
        -------
        SizeControl *
            Returns the size control.

        Examples
        --------
        >>> size_control = model.control_data.get_size_control_by_name("SizeControl-1")

        """
        for size_control in self._size_controls:
            if(size_control.name == name):
                return size_control
        return None

    def delete_control(self, id : int):
        """ Deletes the control for the given id.


        Parameters
        ----------
        id : int
            Id of a control.

        Examples
        --------
        >>> model.control_data.delete_control(size_control.id)

        """
        _ControlData.delete_control(self, id)
        [self._size_controls.remove(size_control)
            for size_control in self._size_controls if size_control.id == id]

    def _update_size_controls(self, sc_data : List):
        self._size_controls = [SizeControl(self._model, sc[0], sc[1], sc[2]) for sc in sc_data]

    @property
    def size_controls(self) -> List[SizeControl]:
        """Gets the size controls.

        Returns
        -------
        List[SizeControl]
            Returns the list of size controls.

        Examples
        --------
            >>> size_controls = model.control_data.size_controls
        """
        return self._size_controls