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

class CollapseParams(CoreObject):
    """Parameters to collapse face elements.

    Parameters
    ----------
    model: Model
        Model to create a ``CollapseParams`` object with default parameters.
    feature_type: SurfaceFeatureType, optional
        Feature type to be preserved when performing collapse.
    collapse_ratio: float, optional
        Maximum ratio of shortest face edge length to longest face edge length.
    preserve_quality: bool, optional
        Option to preserve quality of neighboring triangles when performing collapse.Collapse may lead to quality deterioration beyond target skewness. Such collapse is prevented, when the option is enabled.
    target_skewness: float, optional
        Skewness limit used as target to preserve quality. Better quality elements are skipped for collapse.
    keep_edge_connectivity: bool, optional
        Option to keep edge connectivity. The default value is false. When keep edge connectivity is true, edges that were connected to collapsed triangles will be connected to different triangles. Otherwise, edges will be disconnected from faces.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``CollapseParams`` object with provided parameters.

    Examples
    --------
    >>> collapse_params = prime.CollapseParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            feature_type: SurfaceFeatureType,
            collapse_ratio: float,
            preserve_quality: bool,
            target_skewness: float,
            keep_edge_connectivity: bool):
        self._feature_type = SurfaceFeatureType(feature_type)
        self._collapse_ratio = collapse_ratio
        self._preserve_quality = preserve_quality
        self._target_skewness = target_skewness
        self._keep_edge_connectivity = keep_edge_connectivity

    def __init__(
            self,
            model: CommunicationManager=None,
            feature_type: SurfaceFeatureType = None,
            collapse_ratio: float = None,
            preserve_quality: bool = None,
            target_skewness: float = None,
            keep_edge_connectivity: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``CollapseParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``CollapseParams`` object with default parameters.
        feature_type: SurfaceFeatureType, optional
            Feature type to be preserved when performing collapse.
        collapse_ratio: float, optional
            Maximum ratio of shortest face edge length to longest face edge length.
        preserve_quality: bool, optional
            Option to preserve quality of neighboring triangles when performing collapse.Collapse may lead to quality deterioration beyond target skewness. Such collapse is prevented, when the option is enabled.
        target_skewness: float, optional
            Skewness limit used as target to preserve quality. Better quality elements are skipped for collapse.
        keep_edge_connectivity: bool, optional
            Option to keep edge connectivity. The default value is false. When keep edge connectivity is true, edges that were connected to collapsed triangles will be connected to different triangles. Otherwise, edges will be disconnected from faces.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``CollapseParams`` object with provided parameters.

        Examples
        --------
        >>> collapse_params = prime.CollapseParams(model = model)
        """
        if json_data:
            self.__initialize(
                SurfaceFeatureType(json_data["featureType"] if "featureType" in json_data else None),
                json_data["collapseRatio"] if "collapseRatio" in json_data else None,
                json_data["preserveQuality"] if "preserveQuality" in json_data else None,
                json_data["targetSkewness"] if "targetSkewness" in json_data else None,
                json_data["keepEdgeConnectivity"] if "keepEdgeConnectivity" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [feature_type, collapse_ratio, preserve_quality, target_skewness, keep_edge_connectivity])
            if all_field_specified:
                self.__initialize(
                    feature_type,
                    collapse_ratio,
                    preserve_quality,
                    target_skewness,
                    keep_edge_connectivity)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "CollapseParams")
                    json_data = param_json["CollapseParams"] if "CollapseParams" in param_json else {}
                    self.__initialize(
                        feature_type if feature_type is not None else ( CollapseParams._default_params["feature_type"] if "feature_type" in CollapseParams._default_params else SurfaceFeatureType(json_data["featureType"] if "featureType" in json_data else None)),
                        collapse_ratio if collapse_ratio is not None else ( CollapseParams._default_params["collapse_ratio"] if "collapse_ratio" in CollapseParams._default_params else (json_data["collapseRatio"] if "collapseRatio" in json_data else None)),
                        preserve_quality if preserve_quality is not None else ( CollapseParams._default_params["preserve_quality"] if "preserve_quality" in CollapseParams._default_params else (json_data["preserveQuality"] if "preserveQuality" in json_data else None)),
                        target_skewness if target_skewness is not None else ( CollapseParams._default_params["target_skewness"] if "target_skewness" in CollapseParams._default_params else (json_data["targetSkewness"] if "targetSkewness" in json_data else None)),
                        keep_edge_connectivity if keep_edge_connectivity is not None else ( CollapseParams._default_params["keep_edge_connectivity"] if "keep_edge_connectivity" in CollapseParams._default_params else (json_data["keepEdgeConnectivity"] if "keepEdgeConnectivity" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            feature_type: SurfaceFeatureType = None,
            collapse_ratio: float = None,
            preserve_quality: bool = None,
            target_skewness: float = None,
            keep_edge_connectivity: bool = None):
        """Set the default values of the ``CollapseParams`` object.

        Parameters
        ----------
        feature_type: SurfaceFeatureType, optional
            Feature type to be preserved when performing collapse.
        collapse_ratio: float, optional
            Maximum ratio of shortest face edge length to longest face edge length.
        preserve_quality: bool, optional
            Option to preserve quality of neighboring triangles when performing collapse.Collapse may lead to quality deterioration beyond target skewness. Such collapse is prevented, when the option is enabled.
        target_skewness: float, optional
            Skewness limit used as target to preserve quality. Better quality elements are skipped for collapse.
        keep_edge_connectivity: bool, optional
            Option to keep edge connectivity. The default value is false. When keep edge connectivity is true, edges that were connected to collapsed triangles will be connected to different triangles. Otherwise, edges will be disconnected from faces.
        """
        args = locals()
        [CollapseParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``CollapseParams`` object.

        Examples
        --------
        >>> CollapseParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CollapseParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._feature_type is not None:
            json_data["featureType"] = self._feature_type
        if self._collapse_ratio is not None:
            json_data["collapseRatio"] = self._collapse_ratio
        if self._preserve_quality is not None:
            json_data["preserveQuality"] = self._preserve_quality
        if self._target_skewness is not None:
            json_data["targetSkewness"] = self._target_skewness
        if self._keep_edge_connectivity is not None:
            json_data["keepEdgeConnectivity"] = self._keep_edge_connectivity
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "feature_type :  %s\ncollapse_ratio :  %s\npreserve_quality :  %s\ntarget_skewness :  %s\nkeep_edge_connectivity :  %s" % (self._feature_type, self._collapse_ratio, self._preserve_quality, self._target_skewness, self._keep_edge_connectivity)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def feature_type(self) -> SurfaceFeatureType:
        """Feature type to be preserved when performing collapse.
        """
        return self._feature_type

    @feature_type.setter
    def feature_type(self, value: SurfaceFeatureType):
        self._feature_type = value

    @property
    def collapse_ratio(self) -> float:
        """Maximum ratio of shortest face edge length to longest face edge length.
        """
        return self._collapse_ratio

    @collapse_ratio.setter
    def collapse_ratio(self, value: float):
        self._collapse_ratio = value

    @property
    def preserve_quality(self) -> bool:
        """Option to preserve quality of neighboring triangles when performing collapse.Collapse may lead to quality deterioration beyond target skewness. Such collapse is prevented, when the option is enabled.
        """
        return self._preserve_quality

    @preserve_quality.setter
    def preserve_quality(self, value: bool):
        self._preserve_quality = value

    @property
    def target_skewness(self) -> float:
        """Skewness limit used as target to preserve quality. Better quality elements are skipped for collapse.
        """
        return self._target_skewness

    @target_skewness.setter
    def target_skewness(self, value: float):
        self._target_skewness = value

    @property
    def keep_edge_connectivity(self) -> bool:
        """Option to keep edge connectivity. The default value is false. When keep edge connectivity is true, edges that were connected to collapsed triangles will be connected to different triangles. Otherwise, edges will be disconnected from faces.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._keep_edge_connectivity

    @keep_edge_connectivity.setter
    def keep_edge_connectivity(self, value: bool):
        self._keep_edge_connectivity = value

class CollapseResults(CoreObject):
    """Results associated with collapse face elements.

    Parameters
    ----------
    model: Model
        Model to create a ``CollapseResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code associated with the failure of operation.
    n_collapsed: int, optional
        Number of face elements collapsed.
    n_splits: int, optional
        Number of face elements split.
    json_data: dict, optional
        JSON dictionary to create a ``CollapseResults`` object with provided parameters.

    Examples
    --------
    >>> collapse_results = prime.CollapseResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            n_collapsed: int,
            n_splits: int):
        self._error_code = ErrorCode(error_code)
        self._n_collapsed = n_collapsed
        self._n_splits = n_splits

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            n_collapsed: int = None,
            n_splits: int = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``CollapseResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``CollapseResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        n_collapsed: int, optional
            Number of face elements collapsed.
        n_splits: int, optional
            Number of face elements split.
        json_data: dict, optional
            JSON dictionary to create a ``CollapseResults`` object with provided parameters.

        Examples
        --------
        >>> collapse_results = prime.CollapseResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["nCollapsed"] if "nCollapsed" in json_data else None,
                json_data["nSplits"] if "nSplits" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, n_collapsed, n_splits])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    n_collapsed,
                    n_splits)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "CollapseResults")
                    json_data = param_json["CollapseResults"] if "CollapseResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( CollapseResults._default_params["error_code"] if "error_code" in CollapseResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        n_collapsed if n_collapsed is not None else ( CollapseResults._default_params["n_collapsed"] if "n_collapsed" in CollapseResults._default_params else (json_data["nCollapsed"] if "nCollapsed" in json_data else None)),
                        n_splits if n_splits is not None else ( CollapseResults._default_params["n_splits"] if "n_splits" in CollapseResults._default_params else (json_data["nSplits"] if "nSplits" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            n_collapsed: int = None,
            n_splits: int = None):
        """Set the default values of the ``CollapseResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        n_collapsed: int, optional
            Number of face elements collapsed.
        n_splits: int, optional
            Number of face elements split.
        """
        args = locals()
        [CollapseResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``CollapseResults`` object.

        Examples
        --------
        >>> CollapseResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CollapseResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._n_collapsed is not None:
            json_data["nCollapsed"] = self._n_collapsed
        if self._n_splits is not None:
            json_data["nSplits"] = self._n_splits
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nn_collapsed :  %s\nn_splits :  %s" % (self._error_code, self._n_collapsed, self._n_splits)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def n_collapsed(self) -> int:
        """Number of face elements collapsed.
        """
        return self._n_collapsed

    @n_collapsed.setter
    def n_collapsed(self, value: int):
        self._n_collapsed = value

    @property
    def n_splits(self) -> int:
        """Number of face elements split.
        """
        return self._n_splits

    @n_splits.setter
    def n_splits(self, value: int):
        self._n_splits = value
