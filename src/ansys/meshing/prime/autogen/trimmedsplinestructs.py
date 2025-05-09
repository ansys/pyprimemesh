# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
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

""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class TrimmedSolidSplineCutMode(enum.IntEnum):
    """Types of Cut modes used to generate Cartesian grid representing subdomains of trimmed solid spline.
    """
    HYBRID = 0
    """This is faster mode and may defeature the input mesh to represent each subdomain.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    EXACT = 1
    """This mode guarantees to represent the exact input mesh for each subdomain without any defeaturing.

    **This is a beta parameter**. **The behavior and name may change in the future**."""

class TetMeshSplineParams(CoreObject):
    """Parameters for meshing the solid spline.

    Parameters
    ----------
    model: Model
        Model to create a ``TetMeshSplineParams`` object with default parameters.
    feature_angle: float, optional
        Feature angle used in meshing of the solid spline.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    mode: TrimmedSolidSplineCutMode, optional
        Cut mode to specify rule for mesh cell selection in the volume mesh.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    decimation_factor: float, optional
        Decimation factor used in meshing of the solid spline.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``TetMeshSplineParams`` object with provided parameters.

    Examples
    --------
    >>> tet_mesh_spline_params = prime.TetMeshSplineParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            feature_angle: float,
            mode: TrimmedSolidSplineCutMode,
            decimation_factor: float):
        self._feature_angle = feature_angle
        self._mode = TrimmedSolidSplineCutMode(mode)
        self._decimation_factor = decimation_factor

    def __init__(
            self,
            model: CommunicationManager=None,
            feature_angle: float = None,
            mode: TrimmedSolidSplineCutMode = None,
            decimation_factor: float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``TetMeshSplineParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``TetMeshSplineParams`` object with default parameters.
        feature_angle: float, optional
            Feature angle used in meshing of the solid spline.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        mode: TrimmedSolidSplineCutMode, optional
            Cut mode to specify rule for mesh cell selection in the volume mesh.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        decimation_factor: float, optional
            Decimation factor used in meshing of the solid spline.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``TetMeshSplineParams`` object with provided parameters.

        Examples
        --------
        >>> tet_mesh_spline_params = prime.TetMeshSplineParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["featureAngle"] if "featureAngle" in json_data else None,
                TrimmedSolidSplineCutMode(json_data["mode"] if "mode" in json_data else None),
                json_data["decimationFactor"] if "decimationFactor" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [feature_angle, mode, decimation_factor])
            if all_field_specified:
                self.__initialize(
                    feature_angle,
                    mode,
                    decimation_factor)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "TetMeshSplineParams")
                    json_data = param_json["TetMeshSplineParams"] if "TetMeshSplineParams" in param_json else {}
                    self.__initialize(
                        feature_angle if feature_angle is not None else ( TetMeshSplineParams._default_params["feature_angle"] if "feature_angle" in TetMeshSplineParams._default_params else (json_data["featureAngle"] if "featureAngle" in json_data else None)),
                        mode if mode is not None else ( TetMeshSplineParams._default_params["mode"] if "mode" in TetMeshSplineParams._default_params else TrimmedSolidSplineCutMode(json_data["mode"] if "mode" in json_data else None)),
                        decimation_factor if decimation_factor is not None else ( TetMeshSplineParams._default_params["decimation_factor"] if "decimation_factor" in TetMeshSplineParams._default_params else (json_data["decimationFactor"] if "decimationFactor" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            feature_angle: float = None,
            mode: TrimmedSolidSplineCutMode = None,
            decimation_factor: float = None):
        """Set the default values of the ``TetMeshSplineParams`` object.

        Parameters
        ----------
        feature_angle: float, optional
            Feature angle used in meshing of the solid spline.
        mode: TrimmedSolidSplineCutMode, optional
            Cut mode to specify rule for mesh cell selection in the volume mesh.
        decimation_factor: float, optional
            Decimation factor used in meshing of the solid spline.
        """
        args = locals()
        [TetMeshSplineParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``TetMeshSplineParams`` object.

        Examples
        --------
        >>> TetMeshSplineParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in TetMeshSplineParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._feature_angle is not None:
            json_data["featureAngle"] = self._feature_angle
        if self._mode is not None:
            json_data["mode"] = self._mode
        if self._decimation_factor is not None:
            json_data["decimationFactor"] = self._decimation_factor
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "feature_angle :  %s\nmode :  %s\ndecimation_factor :  %s" % (self._feature_angle, self._mode, self._decimation_factor)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def feature_angle(self) -> float:
        """Feature angle used in meshing of the solid spline.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._feature_angle

    @feature_angle.setter
    def feature_angle(self, value: float):
        self._feature_angle = value

    @property
    def mode(self) -> TrimmedSolidSplineCutMode:
        """Cut mode to specify rule for mesh cell selection in the volume mesh.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._mode

    @mode.setter
    def mode(self, value: TrimmedSolidSplineCutMode):
        self._mode = value

    @property
    def decimation_factor(self) -> float:
        """Decimation factor used in meshing of the solid spline.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._decimation_factor

    @decimation_factor.setter
    def decimation_factor(self, value: float):
        self._decimation_factor = value

class RefineTetMeshParams(CoreObject):
    """Parameters for meshing the solid spline.

    Parameters
    ----------
    model: Model
        Model to create a ``RefineTetMeshParams`` object with default parameters.
    nisr: int, optional
        Interpolation elements in the local r-direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    niss: int, optional
        Interpolation elements in the local s-direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    nist: int, optional
        Interpolation elements in the local t-direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    tolerance: float, optional
        Tolerance for boundary refinement.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``RefineTetMeshParams`` object with provided parameters.

    Examples
    --------
    >>> refine_tet_mesh_params = prime.RefineTetMeshParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            nisr: int,
            niss: int,
            nist: int,
            tolerance: float):
        self._nisr = nisr
        self._niss = niss
        self._nist = nist
        self._tolerance = tolerance

    def __init__(
            self,
            model: CommunicationManager=None,
            nisr: int = None,
            niss: int = None,
            nist: int = None,
            tolerance: float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``RefineTetMeshParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``RefineTetMeshParams`` object with default parameters.
        nisr: int, optional
            Interpolation elements in the local r-direction.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        niss: int, optional
            Interpolation elements in the local s-direction.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        nist: int, optional
            Interpolation elements in the local t-direction.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        tolerance: float, optional
            Tolerance for boundary refinement.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``RefineTetMeshParams`` object with provided parameters.

        Examples
        --------
        >>> refine_tet_mesh_params = prime.RefineTetMeshParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nisr"] if "nisr" in json_data else None,
                json_data["niss"] if "niss" in json_data else None,
                json_data["nist"] if "nist" in json_data else None,
                json_data["tolerance"] if "tolerance" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [nisr, niss, nist, tolerance])
            if all_field_specified:
                self.__initialize(
                    nisr,
                    niss,
                    nist,
                    tolerance)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "RefineTetMeshParams")
                    json_data = param_json["RefineTetMeshParams"] if "RefineTetMeshParams" in param_json else {}
                    self.__initialize(
                        nisr if nisr is not None else ( RefineTetMeshParams._default_params["nisr"] if "nisr" in RefineTetMeshParams._default_params else (json_data["nisr"] if "nisr" in json_data else None)),
                        niss if niss is not None else ( RefineTetMeshParams._default_params["niss"] if "niss" in RefineTetMeshParams._default_params else (json_data["niss"] if "niss" in json_data else None)),
                        nist if nist is not None else ( RefineTetMeshParams._default_params["nist"] if "nist" in RefineTetMeshParams._default_params else (json_data["nist"] if "nist" in json_data else None)),
                        tolerance if tolerance is not None else ( RefineTetMeshParams._default_params["tolerance"] if "tolerance" in RefineTetMeshParams._default_params else (json_data["tolerance"] if "tolerance" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            nisr: int = None,
            niss: int = None,
            nist: int = None,
            tolerance: float = None):
        """Set the default values of the ``RefineTetMeshParams`` object.

        Parameters
        ----------
        nisr: int, optional
            Interpolation elements in the local r-direction.
        niss: int, optional
            Interpolation elements in the local s-direction.
        nist: int, optional
            Interpolation elements in the local t-direction.
        tolerance: float, optional
            Tolerance for boundary refinement.
        """
        args = locals()
        [RefineTetMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``RefineTetMeshParams`` object.

        Examples
        --------
        >>> RefineTetMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in RefineTetMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._nisr is not None:
            json_data["nisr"] = self._nisr
        if self._niss is not None:
            json_data["niss"] = self._niss
        if self._nist is not None:
            json_data["nist"] = self._nist
        if self._tolerance is not None:
            json_data["tolerance"] = self._tolerance
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "nisr :  %s\nniss :  %s\nnist :  %s\ntolerance :  %s" % (self._nisr, self._niss, self._nist, self._tolerance)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def nisr(self) -> int:
        """Interpolation elements in the local r-direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._nisr

    @nisr.setter
    def nisr(self, value: int):
        self._nisr = value

    @property
    def niss(self) -> int:
        """Interpolation elements in the local s-direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._niss

    @niss.setter
    def niss(self, value: int):
        self._niss = value

    @property
    def nist(self) -> int:
        """Interpolation elements in the local t-direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._nist

    @nist.setter
    def nist(self, value: int):
        self._nist = value

    @property
    def tolerance(self) -> float:
        """Tolerance for boundary refinement.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, value: float):
        self._tolerance = value

class UniformSolidSplineCreationParams(CoreObject):
    """Parameters to define the uniform solid spline.

    Parameters
    ----------
    model: Model
        Model to create a ``UniformSolidSplineCreationParams`` object with default parameters.
    n_control_points_u: int, optional
        Number of control points in u direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    n_control_points_v: int, optional
        Number of control points in v direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    n_control_points_w: int, optional
        Number of control points in w direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    degree_u: int, optional
        Degree in u direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    degree_v: int, optional
        Degree in v direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    degree_w: int, optional
        Degree in w direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``UniformSolidSplineCreationParams`` object with provided parameters.

    Examples
    --------
    >>> uniform_solid_spline_creation_params = prime.UniformSolidSplineCreationParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            n_control_points_u: int,
            n_control_points_v: int,
            n_control_points_w: int,
            degree_u: int,
            degree_v: int,
            degree_w: int):
        self._n_control_points_u = n_control_points_u
        self._n_control_points_v = n_control_points_v
        self._n_control_points_w = n_control_points_w
        self._degree_u = degree_u
        self._degree_v = degree_v
        self._degree_w = degree_w

    def __init__(
            self,
            model: CommunicationManager=None,
            n_control_points_u: int = None,
            n_control_points_v: int = None,
            n_control_points_w: int = None,
            degree_u: int = None,
            degree_v: int = None,
            degree_w: int = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``UniformSolidSplineCreationParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``UniformSolidSplineCreationParams`` object with default parameters.
        n_control_points_u: int, optional
            Number of control points in u direction.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        n_control_points_v: int, optional
            Number of control points in v direction.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        n_control_points_w: int, optional
            Number of control points in w direction.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        degree_u: int, optional
            Degree in u direction.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        degree_v: int, optional
            Degree in v direction.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        degree_w: int, optional
            Degree in w direction.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``UniformSolidSplineCreationParams`` object with provided parameters.

        Examples
        --------
        >>> uniform_solid_spline_creation_params = prime.UniformSolidSplineCreationParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nControlPointsU"] if "nControlPointsU" in json_data else None,
                json_data["nControlPointsV"] if "nControlPointsV" in json_data else None,
                json_data["nControlPointsW"] if "nControlPointsW" in json_data else None,
                json_data["degreeU"] if "degreeU" in json_data else None,
                json_data["degreeV"] if "degreeV" in json_data else None,
                json_data["degreeW"] if "degreeW" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [n_control_points_u, n_control_points_v, n_control_points_w, degree_u, degree_v, degree_w])
            if all_field_specified:
                self.__initialize(
                    n_control_points_u,
                    n_control_points_v,
                    n_control_points_w,
                    degree_u,
                    degree_v,
                    degree_w)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "UniformSolidSplineCreationParams")
                    json_data = param_json["UniformSolidSplineCreationParams"] if "UniformSolidSplineCreationParams" in param_json else {}
                    self.__initialize(
                        n_control_points_u if n_control_points_u is not None else ( UniformSolidSplineCreationParams._default_params["n_control_points_u"] if "n_control_points_u" in UniformSolidSplineCreationParams._default_params else (json_data["nControlPointsU"] if "nControlPointsU" in json_data else None)),
                        n_control_points_v if n_control_points_v is not None else ( UniformSolidSplineCreationParams._default_params["n_control_points_v"] if "n_control_points_v" in UniformSolidSplineCreationParams._default_params else (json_data["nControlPointsV"] if "nControlPointsV" in json_data else None)),
                        n_control_points_w if n_control_points_w is not None else ( UniformSolidSplineCreationParams._default_params["n_control_points_w"] if "n_control_points_w" in UniformSolidSplineCreationParams._default_params else (json_data["nControlPointsW"] if "nControlPointsW" in json_data else None)),
                        degree_u if degree_u is not None else ( UniformSolidSplineCreationParams._default_params["degree_u"] if "degree_u" in UniformSolidSplineCreationParams._default_params else (json_data["degreeU"] if "degreeU" in json_data else None)),
                        degree_v if degree_v is not None else ( UniformSolidSplineCreationParams._default_params["degree_v"] if "degree_v" in UniformSolidSplineCreationParams._default_params else (json_data["degreeV"] if "degreeV" in json_data else None)),
                        degree_w if degree_w is not None else ( UniformSolidSplineCreationParams._default_params["degree_w"] if "degree_w" in UniformSolidSplineCreationParams._default_params else (json_data["degreeW"] if "degreeW" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            n_control_points_u: int = None,
            n_control_points_v: int = None,
            n_control_points_w: int = None,
            degree_u: int = None,
            degree_v: int = None,
            degree_w: int = None):
        """Set the default values of the ``UniformSolidSplineCreationParams`` object.

        Parameters
        ----------
        n_control_points_u: int, optional
            Number of control points in u direction.
        n_control_points_v: int, optional
            Number of control points in v direction.
        n_control_points_w: int, optional
            Number of control points in w direction.
        degree_u: int, optional
            Degree in u direction.
        degree_v: int, optional
            Degree in v direction.
        degree_w: int, optional
            Degree in w direction.
        """
        args = locals()
        [UniformSolidSplineCreationParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``UniformSolidSplineCreationParams`` object.

        Examples
        --------
        >>> UniformSolidSplineCreationParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in UniformSolidSplineCreationParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._n_control_points_u is not None:
            json_data["nControlPointsU"] = self._n_control_points_u
        if self._n_control_points_v is not None:
            json_data["nControlPointsV"] = self._n_control_points_v
        if self._n_control_points_w is not None:
            json_data["nControlPointsW"] = self._n_control_points_w
        if self._degree_u is not None:
            json_data["degreeU"] = self._degree_u
        if self._degree_v is not None:
            json_data["degreeV"] = self._degree_v
        if self._degree_w is not None:
            json_data["degreeW"] = self._degree_w
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_control_points_u :  %s\nn_control_points_v :  %s\nn_control_points_w :  %s\ndegree_u :  %s\ndegree_v :  %s\ndegree_w :  %s" % (self._n_control_points_u, self._n_control_points_v, self._n_control_points_w, self._degree_u, self._degree_v, self._degree_w)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def n_control_points_u(self) -> int:
        """Number of control points in u direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._n_control_points_u

    @n_control_points_u.setter
    def n_control_points_u(self, value: int):
        self._n_control_points_u = value

    @property
    def n_control_points_v(self) -> int:
        """Number of control points in v direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._n_control_points_v

    @n_control_points_v.setter
    def n_control_points_v(self, value: int):
        self._n_control_points_v = value

    @property
    def n_control_points_w(self) -> int:
        """Number of control points in w direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._n_control_points_w

    @n_control_points_w.setter
    def n_control_points_w(self, value: int):
        self._n_control_points_w = value

    @property
    def degree_u(self) -> int:
        """Degree in u direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._degree_u

    @degree_u.setter
    def degree_u(self, value: int):
        self._degree_u = value

    @property
    def degree_v(self) -> int:
        """Degree in v direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._degree_v

    @degree_v.setter
    def degree_v(self, value: int):
        self._degree_v = value

    @property
    def degree_w(self) -> int:
        """Degree in w direction.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._degree_w

    @degree_w.setter
    def degree_w(self, value: int):
        self._degree_w = value

class TrimmedSplineResults(CoreObject):
    """Results of IGA operations.

    Parameters
    ----------
    model: Model
        Model to create a ``TrimmedSplineResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code if IGA operation is unsuccessful.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``TrimmedSplineResults`` object with provided parameters.

    Examples
    --------
    >>> trimmed_spline_results = prime.TrimmedSplineResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``TrimmedSplineResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``TrimmedSplineResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code if IGA operation is unsuccessful.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``TrimmedSplineResults`` object with provided parameters.

        Examples
        --------
        >>> trimmed_spline_results = prime.TrimmedSplineResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "TrimmedSplineResults")
                    json_data = param_json["TrimmedSplineResults"] if "TrimmedSplineResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( TrimmedSplineResults._default_params["error_code"] if "error_code" in TrimmedSplineResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of the ``TrimmedSplineResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code if IGA operation is unsuccessful.
        """
        args = locals()
        [TrimmedSplineResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``TrimmedSplineResults`` object.

        Examples
        --------
        >>> TrimmedSplineResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in TrimmedSplineResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code if IGA operation is unsuccessful.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
