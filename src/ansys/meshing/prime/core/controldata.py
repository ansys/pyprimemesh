# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Module for control data."""
from typing import Iterable, List

# isort: split
from ansys.meshing.prime.autogen.controldata import ControlData as _ControlData

# isort: split
from ansys.meshing.prime.autogen.commonstructs import DeleteResults
from ansys.meshing.prime.autogen.model import Model
from ansys.meshing.prime.autogen.multizonecontrol import MultiZoneControl
from ansys.meshing.prime.autogen.primeconfig import ErrorCode
from ansys.meshing.prime.autogen.shellblcontrol import ShellBLControl
from ansys.meshing.prime.autogen.thinvolumecontrol import ThinVolumeControl
from ansys.meshing.prime.core.periodiccontrol import PeriodicControl
from ansys.meshing.prime.core.prismcontrol import PrismControl
from ansys.meshing.prime.core.sizecontrol import SizeControl
from ansys.meshing.prime.core.volumecontrol import VolumeControl
from ansys.meshing.prime.core.wrappercontrol import WrapperControl
from ansys.meshing.prime.params.primestructs import SizingType


class ControlData(_ControlData):
    """Contains all controls.

    This class contains all controls, including size controls, prism controls, multizone controls
    and wrapper controls.

    Parameters
    ----------
    model : Model
        Server model to create ControlData object.
    id : int
        Id of the ControlData.
    object_id : int
        Object id of the ControlData.
    name : str
        Name of the ControlData.
    """

    def __init__(self, model: Model, id: int, object_id: int, name: str):
        """Initialize the ``ControlData`` class."""
        self._model = model
        self._wrapper_controls = []
        self._mz_controls = []
        self._size_controls = []
        self._prism_controls = []
        self._thin_volume_controls = []
        self._volume_controls = []
        self._periodic_controls = []
        self._shell_bl_controls = []
        _ControlData.__init__(self, model, id, object_id, name)

    def get_wrapper_control_by_name(self, name) -> WrapperControl:
        """Get the wrapper control by name.

        Parameters
        ----------
        name : str
            Name of the wrapper control.

        Returns
        -------
        WrapperControl
            Wrapper control.

        Examples
        --------
        >>> wrapper_control = model.control_data.get_wrapper_control_by_name("wrappercontrol-1")

        """
        for wc in self._wrapper_controls:
            if wc.name == name:
                return wc
        return None

    def get_multi_zone_control_by_name(self, name) -> MultiZoneControl:
        """Get the multizone control by name.

        Parameters
        ----------
        name : str
            Name of the multizone control.

        Returns
        -------
        MultiZoneControl
            Returns the multizone control.

        Examples
        --------
        >>> multi_zone_control = model.control_data.get_multi_zone_control_by_name("mzcontrol-1")

        """
        for mc in self._mz_controls:
            if mc.name == name:
                return mc
        return None

    def create_size_control(self, sizing_type: SizingType) -> SizeControl:
        """Create a size control for a sizing type.

        Parameters
        ----------
        type : SizingType
            Sizing type for creating the size control.

        Returns
        -------
        SizeControl
            Size control.

        Notes
        -----
        An empty size control is created on calling this method.

        Examples
        --------
        >>> size_control = model.control_data.create_size_control(SizingType.Curvature)

        """
        res = _ControlData.create_size_control(self, sizing_type)
        new_size_control = SizeControl(self._model, res[0], res[1], res[2])
        self._size_controls.append(new_size_control)
        return new_size_control

    def create_prism_control(self) -> PrismControl:
        """Create a prism control.

        Returns
        -------
        PrismControl
            Prism control.

        Examples
        --------
        >>> prism_control = model.control_data.create_prism_control()

        """
        res = _ControlData.create_prism_control(self)
        new_prism_control = PrismControl(self._model, res[0], res[1], res[2])
        self._prism_controls.append(new_prism_control)
        return new_prism_control

    def create_shell_bl_control(self) -> ShellBLControl:
        """Create a ShellBL control.

        Returns
        -------
        ShellBLControl
            ShellBL Control.

        Examples
        --------
        >>> shell_bl_control = model.control_data.create_shell_bl_control()

        """
        res = _ControlData.create_shell_bl_control(self)
        new_shell_bl_control = ShellBLControl(self._model, res[0], res[1], res[2])
        self._shell_bl_controls.append(new_shell_bl_control)
        return new_shell_bl_control

    def create_thin_volume_control(self) -> ThinVolumeControl:
        """Create a thin volume control.

        Returns
        -------
        ThinVolumeControl
            Thin volume control.

        Examples
        --------
        >>> thin_volume_control = model.control_data.create_thin_volume_control()

        """
        res = _ControlData.create_thin_volume_control(self)
        new_thin_volume_control = ThinVolumeControl(self._model, res[0], res[1], res[2])
        self._thin_volume_controls.append(new_thin_volume_control)
        return new_thin_volume_control

    def create_wrapper_control(self) -> WrapperControl:
        """Create a wrapper control with default values.

        Returns
        -------
        WrapperControl
            Wrapper control.

        Notes
        -----
        A wrapper control with default values is created on calling this method.

        Examples
        --------
        >>> wrapper_control = model.control_data.create_wrapper_control()

        """
        res = _ControlData.create_wrapper_control(self)
        new_control = WrapperControl(self._model, res[0], res[1], res[2])
        self._wrapper_controls.append(new_control)
        return new_control

    def create_multi_zone_control(self) -> MultiZoneControl:
        """Create multizone control with defaults.

        Returns
        -------
        multizone
            Returns the multizone control.

        Examples
        --------
        >>> multizone = model.control_data.create_wrapper_control()

        """
        res = _ControlData.create_multi_zone_control(self)
        new_control = MultiZoneControl(self._model, res[0], res[1], res[2])
        self._mz_controls.append(new_control)
        return new_control

    def get_size_control_by_name(self, name: str) -> SizeControl:
        """Get a size control by name.

        Parameters
        ----------
        name : str
            Name of the size control.

        Returns
        -------
        SizeControl
            Size control.

        Examples
        --------
        >>> size_control = model.control_data.get_size_control_by_name("SizeControl-1")

        """
        for size_control in self._size_controls:
            if size_control.name == name:
                return size_control
        return None

    def get_prism_control_by_name(self, name: str) -> PrismControl:
        """Get a prism control by name.

        Parameters
        ----------
        name : str
            Name of the prism control.

        Returns
        -------
        PrismControl
            Prism control.

        Examples
        --------
        >>> prism_control = model.control_data.get_prism_control_by_name("PrismControl-1")

        """
        for prism_control in self._prism_controls:
            if prism_control.name == name:
                return prism_control
        return None

    def get_shell_bl_control_by_name(self, name: str) -> ShellBLControl:
        """Get a shell bl control by name.

        Parameters
        ----------
        name : str
            Name of the shell bl control.

        Returns
        -------
        ShellBLControl
            Shell BL control.

        Examples
        --------
        >>> shell_bl_control = model.control_data.get_shell_bl_control_by_name("ShellBLControl-1")

        """
        for shell_bl_control in self._shell_bl_controls:
            if shell_bl_control.name == name:
                return shell_bl_control
        return None

    def get_thin_volume_control_by_name(self, name: str) -> ThinVolumeControl:
        """Get a thin volume control by name.

        Parameters
        ----------
        name : str
            Name of the thin volume control.

        Returns
        -------
        ThinVolumeControl
            Thin volume control.

        Examples
        --------
        >>> contorl_data = model.control_data
        >>> thin_volume_control = control_data.get_thin_volume_control_by_name(
                                                     "ThinVolumeControl-1")
        """
        for thin_volume_control in self._thin_volume_controls:
            if thin_volume_control.name == name:
                return thin_volume_control
        return None

    def delete_controls(self, control_ids: Iterable[int]) -> DeleteResults:
        """Delete the control for one or more IDs.

        Parameters
        ----------
        control_ids : Iterable[int]
            List of control IDs.

        Returns
        -------
        DeleteResults
            Delete results.

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
                for shell_bl_control in self._shell_bl_controls:
                    if shell_bl_control.id == id:
                        self._shell_bl_controls.remove(shell_bl_control)
                        break
                for thin_volume_control in self._thin_volume_controls:
                    if thin_volume_control.id == id:
                        self._thin_volume_controls.remove(thin_volume_control)
                        break
                for volume_control in self._volume_controls:
                    if volume_control.id == id:
                        self._volume_controls.remove(volume_control)
                        break
                for periodic_control in self._periodic_controls:
                    if periodic_control.id == id:
                        self._periodic_controls.remove(periodic_control)
                        break
                for multi_zone_control in self._mz_controls:
                    if multi_zone_control.id == id:
                        self._mz_controls.remove(multi_zone_control)
                        break
        return res

    def _update_size_controls(self, c_data: List):
        self._size_controls = [SizeControl(self._model, c[0], c[1], c[2]) for c in c_data]

    def _update_prism_controls(self, c_data: List):
        self._prism_controls = [PrismControl(self._model, c[0], c[1], c[2]) for c in c_data]

    def _update_shell_bl_controls(self, c_data: List):
        self._shell_bl_controls = [ShellBLControl(self._model, c[0], c[1], c[2]) for c in c_data]

    def _update_wrapper_controls(self, c_data: List):
        self._wrapper_controls = [WrapperControl(self._model, c[0], c[1], c[2]) for c in c_data]

    def _update_multi_zone_controls(self, c_data: List):
        self._mz_controls = [MultiZoneControl(self._model, c[0], c[1], c[2]) for c in c_data]

    def _update_volume_controls(self, c_data: List):
        self._volume_controls = [VolumeControl(self._model, c[0], c[1], c[2]) for c in c_data]

    def _update_periodic_controls(self, c_data: List):
        self._periodic_controls = [PeriodicControl(self._model, c[0], c[1], c[2]) for c in c_data]

    def _update_thin_volume_controls(self, c_data: List):
        self._thin_volume_controls = [
            ThinVolumeControl(self._model, c[0], c[1], c[2]) for c in c_data
        ]

    def create_volume_control(self) -> VolumeControl:
        """Create a volume control.

        Returns
        -------
        VolumeControl
            Volume control.

        Examples
        --------
        >>> volume_control = model.control_data.create_volume_control()

        """
        res = _ControlData.create_volume_control(self)
        new_control = VolumeControl(self._model, res[0], res[1], res[2])
        self._volume_controls.append(new_control)
        return new_control

    def get_volume_control_by_name(self, name: str) -> VolumeControl:
        """Get a volume control by name.

        Parameters
        ----------
        name : str
            Name of the volume control.

        Returns
        -------
        VolumeControl
            Volume control.

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
            List of size controls.

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
            List of volume controls.

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
            List of prism controls.

        Examples
        --------
        >>> prism_control = model.control_data.prism_controls

        """
        return self._prism_controls

    @property
    def thin_volume_controls(self) -> List[ThinVolumeControl]:
        """Get the thin volume controls.

        Returns
        -------
        List[ThinVolumeControl]
            List of thin volume controls.

        Examples
        --------
        >>> thin_volume_control = model.control_data.thin_volume_controls

        """
        return self._thin_volume_controls

    @property
    def shell_bl_controls(self) -> List[ShellBLControl]:
        """Get the shell bl controls.

        Returns
        -------
        List[ShellBLControl]
            List of shell bl controls.

        Examples
        --------
        >>> shell_bl_control = model.control_data.shell_bl_controls

        """
        return self._shell_bl_controls

    @property
    def wrapper_controls(self) -> List[WrapperControl]:
        """Get the wrapper controls.

        Returns
        -------
        List[WrapperControl]
            List of wrapper controls.

        Examples
        --------
        >>> wrapper_control = model.control_data.wrapper_controls

        """
        return self._wrapper_controls

    @property
    def multi_zone_controls(self) -> List[MultiZoneControl]:
        """Get the multizone controls.

        Returns
        -------
        List[MultiZoneControl]
            Returns the list of multizone controls.

        Examples
        --------
        >>> multi_zone_control = model.control_data.multi_zone_controls

        """
        return self._mz_controls

    def create_periodic_control(self) -> PeriodicControl:
        """Create a periodic control.

        Returns
        -------
        PeriodicControl
            Periodic control.

        Examples
        --------
        >>> periodic_control = model.control_data.create_periodic_control()

        """
        res = _ControlData.create_periodic_control(self)
        new_control = PeriodicControl(self._model, res[0], res[1], res[2])
        self._periodic_controls.append(new_control)
        return new_control

    def get_periodic_control_by_name(self, name: str) -> PeriodicControl:
        """Get a periodic control by name.

        Parameters
        ----------
        name : str
            Name of the periodic control.

        Returns
        -------
        PeriodicControl
            Periodic control.

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
            List of periodic controls.

        Examples
        --------
            >>> periodic_controls = model.control_data.periodic_controls
        """
        return self._periodic_controls
