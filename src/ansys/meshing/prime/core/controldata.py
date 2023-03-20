from typing import Iterable, List

# isort: split
from ansys.meshing.prime.autogen.controldata import ControlData as _ControlData

# isort: split
from ansys.meshing.prime.autogen.commonstructs import DeleteResults
from ansys.meshing.prime.autogen.primeconfig import ErrorCode
from ansys.meshing.prime.autogen.prismcontrol import PrismControl
from ansys.meshing.prime.core.periodiccontrol import PeriodicControl
from ansys.meshing.prime.core.sizecontrol import SizeControl
from ansys.meshing.prime.core.volumecontrol import VolumeControl
from ansys.meshing.prime.core.wrappercontrol import WrapperControl
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import SizingType


class ControlData(_ControlData):
    """ControlData acts as a container for all controls (size controls, prism controls,
    wrapper controls, etc).

    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """Initializes ControlData"""
        self._model = model
        self._wrapper_controls = []
        self._size_controls = []
        self._prism_controls = []
        self._volume_controls = []
        self._periodic_controls = []
        _ControlData.__init__(self, model, id, object_id, name)

    def get_wrapper_control_by_name(self, name) -> WrapperControl:
        """Gets the wrapper control by name.


        Parameters
        ----------
        name : str
            Name of the wrapper control.

        Returns
        -------
        WrapperControl
            Returns the wrapper control.

        Examples
        --------
        >>> wrapper_control = model.control_data.get_wrapper_control_by_name("wrappercontol-1")

        """
        for wc in self._wrapper_controls:
            if wc.name == name:
                return wc
        return None

    def create_size_control(self, sizing_type: SizingType) -> SizeControl:
        """Creates size control for the given sizing type.


        Parameters
        ----------
        type : SizingType
            Sizing type used to create a size control.

        Returns
        -------
        SizeControl
            Returns the size control.

        Notes
        -----
        An empty size control is created on calling this API.

        Examples
        --------
        >>> size_control = model.control_data.create_size_control(SizingType.Curvature)

        """
        res = _ControlData.create_size_control(self, sizing_type)
        new_size_control = SizeControl(self._model, res[0], res[1], res[2])
        self._size_controls.append(new_size_control)
        return new_size_control

    def create_prism_control(self) -> PrismControl:
        """Creates a PrismControl.


        Returns
        -------
        PrismControl
            Returns PrismControl.


        Examples
        --------
        >>> prism_control = model.control_data.create_prism_control()

        """
        res = _ControlData.create_prism_control(self)
        new_prism_control = PrismControl(self._model, res[0], res[1], res[2])
        self._prism_controls.append(new_prism_control)
        return new_prism_control

    def create_wrapper_control(self) -> WrapperControl:
        """Creates wrapper control with defaults.


        Returns
        -------
        WrapperControl
            Returns the wrapper control.

        Notes
        -----
        A wrapper control with defaults is created on calling this API.

        Examples
        --------
        >>> wrapper_control = model.control_data.create_wrapper_control()

        """
        res = _ControlData.create_wrapper_control(self)
        new_control = WrapperControl(self._model, res[0], res[1], res[2])
        self._wrapper_controls.append(new_control)
        return new_control

    def get_size_control_by_name(self, name: str) -> SizeControl:
        """Gets the size control by name.


        Parameters
        ----------
        name : str
            Name of the size control.

        Returns
        -------
        SizeControl
            Returns the size control.

        Examples
        --------
        >>> size_control = model.control_data.get_size_control_by_name("SizeControl-1")

        """
        for size_control in self._size_controls:
            if size_control.name == name:
                return size_control
        return None

    def get_prism_control_by_name(self, name: str) -> PrismControl:
        """Gets the prism control by name.


        Parameters
        ----------
        name : str
            Name of the prism control.

        Returns
        -------
        PrismControl
            Returns the prism control.

        Examples
        --------
        >>> prism_control = model.control_data.get_prism_control_by_name("PrismControl-1")

        """
        for prism_control in self._prism_controls:
            if prism_control.name == name:
                return prism_control
        return None

    def delete_controls(self, control_ids: Iterable[int]) -> DeleteResults:
        """Deletes the control for the given id.


        Parameters
        ----------
        control_ids : Iterable[int]
            List of control ids.

        Returns
        -------
        DeleteResults
            Returns the DeleteResults.

        Examples
        --------
        >>> results = model.control_data.delete_controls([size_control.id, volume_control.id])

        """
        res = _ControlData.delete_controls(self, control_ids=control_ids)
        if res.error_code == ErrorCode.NOERROR:
            for id in control_ids:
                for size_control in self._size_controls:
                    if size_control.id == id:
                        self._size_controls.remove(size_control)
                        break
                for wrapper_control in self._wrapper_controls:
                    if wrapper_control.id == id:
                        self._wrapper_controls.remove(wrapper_control)
                        break
                for prism_control in self._prism_controls:
                    if prism_control.id == id:
                        self._prism_controls.remove(prism_control)
                        break
                for volume_control in self._volume_controls:
                    if volume_control.id == id:
                        self._volume_controls.remove(volume_control)
                        break
                for periodic_control in self._periodic_controls:
                    if periodic_control.id == id:
                        self._periodic_controls.remove(periodic_control)
                        break
        return res

    def _update_size_controls(self, sc_data: List):
        self._size_controls = [SizeControl(self._model, sc[0], sc[1], sc[2]) for sc in sc_data]

    def _update_prism_controls(self, sc_data: List):
        self._prism_controls = [PrismControl(self._model, sc[0], sc[1], sc[2]) for sc in sc_data]

    def _update_wrapper_controls(self, sc_data: List):
        self._wrapper_controls = [
            WrapperControl(self._model, sc[0], sc[1], sc[2]) for sc in sc_data
        ]

    def _update_volume_controls(self, sc_data: List):
        self._volume_controls = [VolumeControl(self._model, sc[0], sc[1], sc[2]) for sc in sc_data]

    def _update_periodic_controls(self, sc_data: List):
        self._periodic_controls = [
            PeriodicControl(self._model, sc[0], sc[1], sc[2]) for sc in sc_data
        ]

    def create_volume_control(self) -> VolumeControl:
        """Creates the volume control.

        Returns
        -------
        VolumeControl
            Returns the volume control.

        Examples
        --------
        >>> volume_control = model.control_data.create_volume_control()

        """
        res = _ControlData.create_volume_control(self)
        new_control = VolumeControl(self._model, res[0], res[1], res[2])
        self._volume_controls.append(new_control)
        return new_control

    def get_volume_control_by_name(self, name: str) -> VolumeControl:
        """Gets the volume control by name.


        Parameters
        ----------
        name : str
            Name of the volume control.

        Returns
        -------
        VolumeControl
            Returns the volume control.

        Examples
        --------
        >>> volume_control = model.control_data.get_volume_control_by_name("VolumeControl-1")

        """
        for volume_control in self._volume_controls:
            if volume_control.name == name:
                return volume_control
        return None

    @property
    def size_controls(self) -> List[SizeControl]:
        """Get the size controls.

        Returns
        -------
        List[SizeControl]
            Returns the list of size controls.

        Examples
        --------
            >>> size_controls = model.control_data.size_controls
        """
        return self._size_controls

    @property
    def volume_controls(self) -> List[VolumeControl]:
        """Get the volume controls.

        Returns
        -------
        List[VolumeControl]
            Returns the list of volume controls.

        Examples
        --------
            >>> volume_controls = model.control_data.volume_controls
        """
        return self._volume_controls

    @property
    def prism_controls(self) -> List[PrismControl]:
        """Get the prism controls.

        Returns
        -------
        List[PrismControl]
            Returns the list of prism controls.

        Examples
        --------
        >>> prism_control = model.control_data.prism_controls

        """
        return self._prism_controls

    @property
    def wrapper_controls(self) -> List[WrapperControl]:
        """Get the wrapper controls.

        Returns
        -------
        List[WrapperControl]
            Returns the list of wrapper controls.

        Examples
        --------
        >>> wrapper_control = model.control_data.wrapper_controls

        """
        return self._wrapper_controls

    def create_periodic_control(self) -> PeriodicControl:
        """Creates the periodic control.

        Returns
        -------
        PeriodicControl
            Returns the periodic control.

        Examples
        --------
        >>> periodic_control = model.control_data.create_periodic_control()

        """
        res = _ControlData.create_periodic_control(self)
        new_control = PeriodicControl(self._model, res[0], res[1], res[2])
        self._periodic_controls.append(new_control)
        return new_control

    def get_periodic_control_by_name(self, name: str) -> PeriodicControl:
        """Gets the periodic control by name.


        Parameters
        ----------
        name : str
            Name of the periodic control.

        Returns
        -------
        PeriodicControl
            Returns the periodic control.

        Examples
        --------
        >>> periodic_control = model.control_data.get_periodic_control_by_name("PeriodicControl-1")

        """
        for periodic_control in self._periodic_controls:
            if periodic_control.name == name:
                return periodic_control
        return None

    @property
    def periodic_controls(self) -> List[PeriodicControl]:
        """Get the periodic controls.

        Returns
        -------
        List[PeriodicControl]
            Returns the list of periodic controls.

        Examples
        --------
            >>> periodic_controls = model.control_data.periodic_controls
        """
        return self._periodic_controls
