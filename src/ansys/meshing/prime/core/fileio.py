# Copyright (C) 2026 ANSYS, Inc. and/or its affiliates.
# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

"""Module for managing file inputs and outputs."""
import copy
import json
import logging
import traceback
from pathlib import Path

# isort: split
from ansys.meshing.prime.autogen.fileio import FileIO as _FileIO

# isort: split
import ansys.meshing.prime.core.dynaexportutils as dynaexportutils
import ansys.meshing.prime.core.fe2ansys_html_log as fe2ansys_html_log
import ansys.meshing.prime.core.mapdlcdbexportutils as mapdlcdbexportutils
import ansys.meshing.prime.internals.utils as utils
from ansys.meshing.prime.autogen.fileiostructs import (
    ExportBoundaryFittedSplineParams,
    ExportFluentCaseParams,
    ExportFluentMeshingMeshParams,
    ExportLSDynaIgaKeywordFileParams,
    ExportLSDynaIGAResults,
    ExportLSDynaKeywordFileParams,
    ExportLSDynaResults,
    ExportMapdlCdbParams,
    ExportMapdlCdbResults,
    ExportSTLParams,
    FileReadParams,
    FileReadResults,
    FileWriteParams,
    FileWriteResults,
    ImportAbaqusParams,
    ImportAbaqusResults,
    ImportCadParams,
    ImportCadResults,
    ImportFluentCaseParams,
    ImportFluentCaseResults,
    ImportFluentMeshingMeshParams,
    ImportFluentMeshingMeshResults,
    ImportMapdlCdbParams,
    ImportMapdlCdbResults,
    ReadSizeFieldParams,
    SeparateBlocksFormatType,
    SizeFieldFileReadResults,
    WriteSizeFieldParams,
)
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.internals import yaml_converter
from ansys.meshing.prime.params.primestructs import ErrorCode


class FileIO(_FileIO):
    """Handles reading or writing files from the disk.

    Parameters
    ----------
    model : Model
        Server model to create FileIO object.
    """

    __doc__ = _FileIO.__doc__

    def __init__(self, model: Model):
        """Initialize model and parent class."""
        self._model = model
        super().__init__(model)

    def _get_customization_schema_json(self, customization_file_name: str) -> str:
        """Convert custom YAML schema to JSON and return the content as a string.

        This runs on the client side before Abaqus import or MAPDL export so
        the server side C++ code can directly consume the JSON schema content.

        Parameters
        ----------
        customization_file_name : str
            Path to the YAML customization file.

        Returns
        -------
        str
            JSON string content of the converted schema, or empty string if
            no custom YAML schema is found or conversion fails.
        """
        logger = getattr(self._model, "python_logger", logging.getLogger(__name__))

        yaml_file = Path(customization_file_name)
        if not yaml_file.is_file():
            return ""

        try:
            schema_content = yaml_converter.convert_yaml_to_json_string(str(yaml_file))
            logger.info("Converted custom YAML schema to JSON: %s", yaml_file)
            return schema_content
        except FileNotFoundError as ex:
            logger.warning(
                "Custom YAML schema file not found: %s",
                ex,
            )
            return ""
        except ValueError as ex:
            logger.warning(
                "Failed to convert custom YAML schema to JSON: %s",
                ex,
            )
            return ""
        except Exception as ex:
            logger.warning(
                "Unexpected error converting custom YAML schema: %s",
                ex,
            )
            return ""

    @staticmethod
    def _build_customization_count_report(filtered_custom_translations: dict) -> dict:
        """Build per-keyword and total counts for customization instances."""
        per_keyword_instances = {}
        per_keyword_instance_ids = {}
        total_instances = 0

        def _instance_label(instance: object, idx: int) -> str:
            if isinstance(instance, dict):
                params = instance.get("Parameters")
                if isinstance(params, dict) and params:
                    ordered = sorted((str(k).upper(), str(v)) for k, v in params.items())
                    return "{" + "|".join(f"{k}={v}" for k, v in ordered) + "}"

            return f"instance_{idx + 1}"

        for keyword, instances in filtered_custom_translations.items():
            instance_count = len(instances) if isinstance(instances, list) else 0
            per_keyword_instances[keyword] = instance_count
            if isinstance(instances, list):
                per_keyword_instance_ids[keyword] = [
                    _instance_label(instance, i) for i, instance in enumerate(instances)
                ]
            else:
                per_keyword_instance_ids[keyword] = []
            total_instances += instance_count

        return {
            "KeywordsThatSkipNativeFe2AnsysTranslation": len(per_keyword_instances),
            "InstancesThatSkipNativeFe2AnsysTranslation": total_instances,
            "skipByKeyword": per_keyword_instances,
            "skipByInstances": per_keyword_instance_ids,
        }

    @staticmethod
    def _append_customization_report_to_formatted_summary(
        formatted_summary: str, customization_report: dict
    ) -> str:
        """Append customization count report to formatted MAPDL summary."""
        if not customization_report:
            return formatted_summary

        per_keyword = customization_report.get("perKeywordInstances", {})
        per_keyword_instance_ids = customization_report.get("perKeywordInstanceIds", {})
        skip_by_keyword = customization_report.get("skipByKeyword", per_keyword)
        skip_by_instances = customization_report.get("skipByInstances", per_keyword_instance_ids)
        cpp = customization_report.get("Cpp", {})
        combined = customization_report.get("Combined", {})

        lines = [
            "",
            "CUSTOMIZATION REPORT",
            "---------------------------------------------------",
        ]

        if skip_by_keyword:
            lines.append("Full Customization Breakdown:")
            for keyword in sorted(skip_by_keyword.keys()):
                lines.append(f"  - {keyword}: {int(skip_by_keyword[keyword])}")
        if skip_by_instances:
            lines.append("Full Customization Instance Breakdown:")
            for keyword in sorted(skip_by_instances.keys()):
                lines.append(f"  - {keyword}:")
                keyword_instances = skip_by_instances.get(keyword, [])
                for instance_label in keyword_instances:
                    lines.append(f"      * {instance_label}")
        if cpp or combined:
            tweaked_keywords = combined.get(
                "tweakingKeywordsTouched", cpp.get("tweakingKeywordsTouched", 0)
            )
            keyopt_updates = combined.get(
                "tweakingKeyoptUpdates", cpp.get("tweakingKeyoptUpdates", 0)
            )
            constant_updates = combined.get(
                "tweakingConstantUpdates", cpp.get("tweakingConstantUpdates", 0)
            )
            lines.extend(
                [
                    f"CPP Tweaked Keywords: {int(tweaked_keywords)}",
                    f"CPP Keyopt Tweaks Applied: {int(keyopt_updates)}",
                    f"CPP Constant Tweaks Applied: {int(constant_updates)}",
                ]
            )

        if per_keyword:
            lines.append("Per-Keyword Instances:")
            for keyword in sorted(per_keyword.keys()):
                lines.append(f"  - {keyword}: {int(per_keyword[keyword])}")
                keyword_instances = per_keyword_instance_ids.get(keyword, [])
                if keyword_instances:
                    lines.append("    Instances:")
                    for instance_label in keyword_instances:
                        lines.append(f"      * {instance_label}")

        return formatted_summary + "\n" + "\n".join(lines) + "\n"

    @staticmethod
    def _combine_python_cpp_customization_report(summary: dict, py_report: dict) -> dict:
        """Combine Python skip/customization reporting with C++ tweaking metrics."""
        counts = summary.get("Counts", {}) if isinstance(summary, dict) else {}
        cpp_customization = {}
        if isinstance(summary, dict):
            customization_root = summary.get("Customization", {})
            if isinstance(customization_root, dict):
                cpp_customization = customization_root.get("Cpp", {})
        if not isinstance(cpp_customization, dict):
            cpp_customization = {}

        cpp_tweaked_keywords = int(
            cpp_customization.get(
                "tweakingKeywordsTouched", counts.get("cpp_tweaking_keywords_touched", 0) or 0
            )
        )
        cpp_keyopt_updates = int(
            cpp_customization.get(
                "tweakingKeyoptUpdates", counts.get("cpp_tweaking_keyopt_updates", 0) or 0
            )
        )
        cpp_constant_updates = int(
            cpp_customization.get(
                "tweakingConstantUpdates", counts.get("cpp_tweaking_constant_updates", 0) or 0
            )
        )

        skip_keywords = int(py_report.get("KeywordsThatSkipNativeFe2AnsysTranslation"))
        skip_instances = int(py_report.get("InstancesThatSkipNativeFe2AnsysTranslation", 0))
        skip_by_keyword = py_report.get("skipByKeyword", py_report.get("perKeywordInstances", {}))
        if not isinstance(skip_by_keyword, dict):
            skip_by_keyword = {}
        skip_by_instances = py_report.get(
            "skipByInstances", py_report.get("perKeywordInstanceIds", {})
        )
        if not isinstance(skip_by_instances, dict):
            skip_by_instances = {}
        combined = {
            "KeywordsThatSkipNativeFe2AnsysTranslation": skip_keywords,
            "InstancesThatSkipNativeFe2AnsysTranslation": skip_instances,
            "skipByKeyword": skip_by_keyword,
            "skipByInstances": skip_by_instances,
            "tweakingKeywordsTouched": cpp_tweaked_keywords,
            "tweakingKeyoptUpdates": cpp_keyopt_updates,
            "tweakingConstantUpdates": cpp_constant_updates,
        }
        py_report["Combined"] = combined
        return py_report

    @staticmethod
    def _merge_custom_sections(merged_sections: dict, keyword_sections: dict) -> None:
        """Merge translated section text from one keyword into the final output."""
        for section_name, content in keyword_sections.items():
            mapdlcdbexportutils._append_section_text(merged_sections, section_name, content)

    @staticmethod
    def _read_custom_keyword_block(
        source_file_path: str, keyword_offset: int, keyword_size: int
    ) -> str:
        """Read one custom keyword block from the original Abaqus source file."""
        with open(source_file_path, "rb") as source_file:
            source_file.seek(keyword_offset)
            raw_bytes = source_file.read(keyword_size)
        return raw_bytes.decode("utf-8", errors="replace")

    @staticmethod
    def _parse_keyword_parameters(keyword_line: str) -> dict:
        """Parse the Abaqus keyword line into a parameters dictionary."""
        parameters = {}
        if not keyword_line:
            return parameters

        keyword_tokens = [token.strip() for token in keyword_line.lstrip("*").split(",")]
        for token in keyword_tokens[1:]:
            if not token:
                continue
            if "=" in token:
                key, value = token.split("=", 1)
                parameters[key.strip().upper()] = value.strip()
            else:
                parameters[token.strip().upper()] = True

        return parameters

    @classmethod
    def _parse_raw_keyword_block(cls, raw_keyword_block: str) -> dict:
        """Convert one raw Abaqus keyword block into keyword, parameters, and data."""
        parsed_keyword = ""
        parameters = {}
        data_lines = []

        for raw_line in raw_keyword_block.splitlines():
            stripped_line = raw_line.strip()
            if not stripped_line or stripped_line.startswith("**"):
                continue

            if not parsed_keyword and stripped_line.startswith("*"):
                keyword_tokens = [token.strip() for token in stripped_line.lstrip("*").split(",")]
                parsed_keyword = (
                    keyword_tokens[0].upper() if keyword_tokens and keyword_tokens[0] else ""
                )
                parameters = cls._parse_keyword_parameters(stripped_line)
                continue

            data_lines.append(stripped_line)

        return {
            "Keyword": parsed_keyword,
            "Parameters": parameters,
            "Data": data_lines,
        }

    def _hydrate_keyword_instances(self, keyword: str, keyword_instances: object) -> list:
        """Hydrate one keyword's instances with transient parsed source content."""
        if not isinstance(keyword_instances, list):
            return keyword_instances

        hydrated_instances = []
        for idx, instance in enumerate(keyword_instances):
            if not isinstance(instance, dict):
                hydrated_instances.append({"Parameters": {}, "Data": []})
                continue

            source_file_path = instance.get("SourceFilepath")
            keyword_offset = instance.get("KeywordOffset")
            keyword_size = instance.get("KeywordSize")
            hydrated_instance = dict(instance)
            hydrated_instance.pop("SourceFilepath", None)
            hydrated_instance.pop("KeywordOffset", None)
            hydrated_instance.pop("KeywordSize", None)
            hydrated_instance["Parameters"] = {}
            hydrated_instance["Data"] = []

            if source_file_path and keyword_offset is not None and keyword_size is not None:
                try:
                    raw_keyword_block = self._read_custom_keyword_block(
                        source_file_path,
                        int(keyword_offset),
                        int(keyword_size),
                    )
                    parsed_keyword_block = self._parse_raw_keyword_block(raw_keyword_block)
                    hydrated_instance["Parameters"] = parsed_keyword_block["Parameters"]
                    hydrated_instance["Data"] = parsed_keyword_block["Data"]
                except Exception as ex:
                    self._model.python_logger.warning(
                        "Failed to hydrate custom keyword %s instance %s from %s. Error: %s",
                        keyword,
                        idx + 1,
                        source_file_path,
                        ex,
                    )

            hydrated_instances.append(hydrated_instance)

        return hydrated_instances

    def read_pmdat(self, file_name: str, file_read_params: FileReadParams) -> FileReadResults:
        """Read a PyPrimeMesh data (PMDAT) file.

        Parameters
        ----------
        file_name : str
            Path to the data file on disk.
        file_read_params : FileReadParams
            Parameters for reading the data file.

        Returns
        -------
        FileReadResults
            Results from reading the data file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> #connect client to server and get model from it
        >>> client = prime.Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = prime.FileIO(model=model)
        >>> file_read_params = prime.FileReadParams(model=model)
        >>> results = file_io.read_pmdat("/tmp/file.pmdat", file_read_params)

        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().read_pmdat(temp_file_name, file_read_params)
            if result.error_code == ErrorCode.NOERROR:
                self._model._sync_up_model()
        return result

    def write_pmdat(self, file_name: str, file_write_params: FileWriteParams) -> FileWriteResults:
        """Write a PyPrimeMesh data (PMDAT) file.

        Parameters
        ----------
        file_name : str
            Path for writing the data file on disk.
        file_write_params : FileWriteParams
            Parameters for writing the data file.

        Returns
        -------
        FileWriteResults
            Results from writing the data file.

        Examples
        --------
        >>> results = file_io.write_pmdat("/tmp/prime_mesh_data.pmdat",
                                          prime.FileWriteParams(model=model))
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().write_pmdat(temp_file_name, file_write_params)
        return result

    def import_abaqus_inp(self, file_name: str, params: ImportAbaqusParams) -> ImportAbaqusResults:
        """(BETA FEATURE) Import a Abaqus file.

        This is a beta feature to import abaqus files as dead mesh and also store
        simulation-specific information into Prime in the form of JSON documents.

        Parameters
        ----------
        file_name : str
            Name of file to import.
        params : ImportAbaqusParams
            Parameters to specify options during import.

        Returns
        -------
        ImportAbaqusResults
            Returns the results of the abaqus database import.


        Examples
        --------
        >>> results = file_io.import_abaqus(r"/tmp/file.inp")

        """
        try:
            with utils.file_read_context(self._model, file_name) as temp_file_name:
                result = super().import_abaqus_inp(temp_file_name, params)
                if result.error_code == ErrorCode.NOERROR:
                    self._model._sync_up_model()
        except Exception as crash_exc:
            # Crash: server died during RPC; write crash report, then re-raise.
            if params.write_html_log:
                fe2ansys_html_log.write_abaqus_import_html_log(
                    self, file_name, crash_error=str(crash_exc)
                )
            raise
        # Best-effort HTML log render; never raises.
        if params.write_html_log:
            fe2ansys_html_log.write_abaqus_import_html_log(self, file_name)
        return result

    def import_fluent_meshing_size_field(self, file_name: str) -> SizeFieldFileReadResults:
        """Import a Fluent Meshing size field (SF and SF.GZ) file from disk.

        Parameters
        ----------
        file_name : str
            Path to the size field file on disk.

        Returns
        -------
        SizeFieldFileReadResults
            Results from reading the size field file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> results = file_io.import_fluent_meshing_size_field("/tmp/my_sizefield.sf")
        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().import_fluent_meshing_size_field(temp_file_name)
        return result

    def read_size_field(
        self, file_name: str, params: ReadSizeFieldParams
    ) -> SizeFieldFileReadResults:
        """Read a PyPrimeMesh size field (PSF and PSF.GZ) file from disk.

        Parameters
        ----------
        file_name : str
            Path to the size field file on disk.
        params : ReadSizeFieldParams
            Parameters for reading size field file.

        Returns
        -------
        SizeFieldFileReadResults
            Results from reading the size field file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ReadSizeFieldParams(model=model)
        >>> results = file_io.read_size_field("/tmp/my_prime_sizefield.psf", params)
        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().read_size_field(temp_file_name, params)
        return result

    def write_size_field(self, file_name: str, params: WriteSizeFieldParams) -> FileWriteResults:
        """Write a PyPrimeMesh size field (PSF) file to a file on disk.

        Parameters
        ----------
        file_name : str
            Path to the size field file on disk.
        params : WriteSizeFieldParams
            Parameters for writing the size field file.

        Returns
        -------
        FileWriteResults
            Results from writing the size field file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.WriteSizeFieldParams(model=model)
        >>> results = file_io.write_size_field("/tmp/my_prime_sizefield.psf", params)
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().write_size_field(temp_file_name, params)
        return result

    def import_mapdl_cdb(
        self, file_name: str, params: ImportMapdlCdbParams
    ) -> ImportMapdlCdbResults:
        """Import an MAPDL CDB file.

        Parameters
        ----------
        file_name : str
            Path to the CDB file on disk.
        params : ImportMapdlCdbParams
            Parameters for importing the CDB file.

        Returns
        -------
        ImportMapdlCdbResults
            Results from importing the CDB file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> # connect client to server and get model from it
        >>> client = prime.Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ImportMapdlCdbParams(model=model)
        >>> results = file_io.import_mapdl_cdb("/tmp/file.cdb", params)
        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().import_mapdl_cdb(temp_file_name, params)
            if result.error_code == ErrorCode.NOERROR:
                self._model._sync_up_model()
        return result

    def export_mapdl_cdb(
        self, file_name: str, params: ExportMapdlCdbParams
    ) -> ExportMapdlCdbResults:
        """Export an MAPDL CDB file.

        Parameters
        ----------
        file_name : str
            Path to the CDB file on disk.
        params : ExportMapdlCdbParams
            Parameters for exporting the CDB file.

        Returns
        -------
        ExportMapdlCdbResults
            Results from exporting the CDB file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> #connect client to server and get model from it
        >>> client = prime.Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ExportMapdlCdbParams(model=model)
        >>> results = file_io.export_mapdl_cdb("/tmp/file.cdb", params)
        """
        params = copy.copy(params)
        # Support hidden transport fields through custom params when these
        # members are not part of the released client API surface.
        customization_file = getattr(params, "customization_file_name", None)
        customization_file_json_format = None
        if customization_file:
            customization_file_json_format = self._get_customization_schema_json(customization_file)
            params._custom_params["customization_schema"] = customization_file_json_format
            customization_file_json_format = (
                json.loads(customization_file_json_format)
                if customization_file_json_format
                else None
            )
        customization_functions_file = getattr(params, "customization_functions_file_name", None)
        if not customization_functions_file:
            customization_functions_file = params._custom_params.get(
                "customization_functions_file_name"
            )
        try:
            with utils.file_write_context(self._model, file_name) as temp_file_name:
                # part_id = 1
                # if len(self._model.parts) > 0:
                #    part_id = self._model.parts[0].id
                args = {"partId": 0}
                command_name = "PrimeMesh::FileIO/GetAbaqusSimulationData"
                sim_data_str = self._comm.serve(
                    self._model, command_name, self._object_id, args=args
                )
                if params.config_settings is None:
                    params.config_settings = ''
                generate_mapdl_commands_error = None
                generate_mapdl_commands_traceback = None
                with utils.capture_log_records(self._model.python_logger) as collected_logs:
                    all_mat_cmds, analysis_settings = "", ""
                    try:
                        all_mat_cmds, analysis_settings = (
                            mapdlcdbexportutils.generate_mapdl_commands(
                                self._model, sim_data_str, params
                            )
                        )
                    except Exception as e:
                        generate_mapdl_commands_error = e
                        generate_mapdl_commands_traceback = traceback.format_exc()
                    if generate_mapdl_commands_error is not None:
                        self._model.python_logger.warning(
                            "Failed to generate MAPDL material/analysis commands. "
                            "Export proceeded with empty settings. \nError: %s\n%s",
                            generate_mapdl_commands_error,
                            generate_mapdl_commands_traceback,
                        )
                params.material_properties = all_mat_cmds + params.material_properties
                params.analysis_settings = analysis_settings
                params._custom_params["client_log_messages"] = json.dumps(collected_logs)
                result = super().export_mapdl_cdb(temp_file_name, params)
                sim_data_str_with_export_side_modifications = self._comm.serve(
                    self._model, command_name, self._object_id, args=args
                )
                counters = {}
                summary = None
                if result.summary_log:
                    summary = json.loads(result.summary_log)
                    counters = summary.get("Ids", {})
                customization_report = {}

                # Custom translation - user mutates counters in-place
                custom_translations_str = self._comm.serve(
                    self._model,
                    "PrimeMesh::FileIO/GetAbaqusCustomKeywordsData",
                    self._object_id,
                    args={},
                )
                json_custom_translations = json.loads(custom_translations_str or "null") or {}
                json_sim_data_str = json.loads(sim_data_str_with_export_side_modifications)

                if (
                    "FilteredCustomTranslations" in json_custom_translations
                    and json_custom_translations["FilteredCustomTranslations"]
                ):
                    customization_report = self._build_customization_count_report(
                        json_custom_translations["FilteredCustomTranslations"]
                    )
                    sections = {}
                    if mapdlcdbexportutils._translators_loaded is False:
                        mapdlcdbexportutils._load_keyword_translators(
                            customization_functions_file, customization_file_json_format
                        )
                    custom_translations = json_custom_translations["FilteredCustomTranslations"]
                    # In order to empower the user to control which custom function executes first
                    # Iterate through the customization file in definition order.
                    for kw_key, user_data in customization_file_json_format.items():
                        kw_instances = custom_translations.get(kw_key)
                        hydrated_instances = self._hydrate_keyword_instances(kw_key, kw_instances)
                        surface_payloads = {}
                        entry = mapdlcdbexportutils._keyword_translators.get(kw_key.upper())
                        if entry is None:
                            entry = None
                        if entry is not None:
                            _, template_def = entry
                            if template_def and template_def.get("MeshScopings"):
                                try:
                                    keyword_instances_json = json.dumps(hydrated_instances)
                                    schema_json = json.dumps(template_def)
                                    for part in self._model.parts:
                                        part_id = part.id
                                        payload_str = self._comm.serve(
                                            self._model,
                                            "PrimeMesh::FileIO/GetSurfaceMeshPayloadForKeyword",
                                            self._object_id,
                                            args={
                                                "part_id": part_id,
                                                "keyword_instances_json": keyword_instances_json,
                                                "schema_entry_json": schema_json,
                                            },
                                        )
                                        if payload_str:
                                            if surface_payloads.get(kw_key.upper()) is None:
                                                surface_payloads[kw_key.upper()] = json.loads(
                                                    payload_str
                                                )
                                            else:
                                                # Merge payloads returned by multiple parts.
                                                existing_payload = surface_payloads[kw_key.upper()]
                                                new_payload = json.loads(payload_str)
                                                for field, surfaces in new_payload.items():
                                                    if existing_payload.get(field) is None:
                                                        existing_payload[field] = surfaces
                                                    else:
                                                        existing_payload[field].extend(surfaces)
                                except Exception as e:
                                    self._model.python_logger.warning(
                                        "Failed to get surface mesh payload for keyword "
                                        "%s. Error: %s",
                                        kw_key,
                                        e,
                                    )

                        keyword_sections = mapdlcdbexportutils._translate_custom_keywords(
                            {kw_key: hydrated_instances},
                            json_sim_data_str,
                            self._model,
                            counters,
                            surface_payloads,
                        )
                        self._merge_custom_sections(sections, keyword_sections)
                    mapdlcdbexportutils._inject_custom_content(temp_file_name, sections)
                if summary is not None:
                    if customization_report:
                        customization_report = self._combine_python_cpp_customization_report(
                            summary, customization_report
                        )
                        counts = summary.setdefault("Counts", {})
                        counts["skip_keywords"] = int(customization_report.get("skipKeywords", 0))
                        counts["skip_instances"] = int(customization_report.get("skipInstances", 0))
                        counts["cpp_tweaking_keywords_touched"] = int(
                            customization_report.get("Cpp", {}).get("tweakingKeywordsTouched", 0)
                        )
                        counts["cpp_tweaking_keyopt_updates"] = int(
                            customization_report.get("Cpp", {}).get("tweakingKeyoptUpdates", 0)
                        )
                        counts["cpp_tweaking_constant_updates"] = int(
                            customization_report.get("Cpp", {}).get("tweakingConstantUpdates", 0)
                        )

                        customization_root = summary.get("Customization")
                        if not isinstance(customization_root, dict):
                            customization_root = {}
                        customization_root["Python"] = customization_report
                        customization_root["Cpp"] = customization_report.get("Cpp", {})
                        customization_root["Combined"] = customization_report.get("Combined", {})
                        summary["Customization"] = customization_root
                    result.summary_log = json.dumps(summary)
                    if customization_report:
                        result.formatted_summary_log = (
                            self._append_customization_report_to_formatted_summary(
                                result.formatted_summary_log,
                                customization_report,
                            )
                        )
        except Exception as crash_exc:
            # Crash: server died during RPC; write crash report, then re-raise.
            if params.write_html_log:
                fe2ansys_html_log.write_cdb_export_html_log(
                    self, file_name, crash_error=str(crash_exc)
                )
            raise
        # Best-effort HTML log render; never raises.
        if params.write_html_log:
            fe2ansys_html_log.write_cdb_export_html_log(self, file_name)
        return result
        # Support hidden transport fields through custom params when these
        # members are not part of the released client API surface.

    def initialize_cdb_export_params(
        self, params: ExportMapdlCdbParams, major_version: int, minor_version: int
    ) -> ExportMapdlCdbParams:
        """
        Initialize specific CDB export parameters based on the given version.

        This function sets the separate_blocks_format_type, export_fasteners_as_swgen and
        export_rigid_bodies_as_rbgen parameters of the provided ExportMapdlCdbParams
        object based on the given major and minor version numbers.
        Other parameters remain unchanged.

        Parameters
        ----------
        params : ExportMapdlCdbParams
            The CDB export parameters object to be modified.
        major_version : int
            The major version number.
        minor_version : int
            The minor version number.

        Returns
        -------
        ExportMapdlCdbParams
            The modified CDB export parameters object.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        The version is formed as "<major_version>r<minor_version>", e.g., "24r1", "25r2".
        If the version is greater than or equal to "25r1", write_separate_blocks is set to True
        with COMPACT format, and export_fasteners_as_swgen and export_rigid_bodies_as_rbgen
        parameters are set to True. Otherwise, they are set to False.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ExportMapdlCdbParams()
        >>> params = file_io.initialize_cdb_export_params(params, 24, 1)
        >>> params.write_separate_blocks
        False
        >>> params.export_fasteners_as_swgen
        False
        >>> params.export_rigid_bodies_as_swgen
        False

        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ExportMapdlCdbParams()
        >>> params = file_io.initialize_cdb_export_params(params, 25, 2)
        >>> params.write_separate_blocks
        True
        >>> params.separate_blocks_format_type
        SeparateBlocksFormatType.COMPACT
        >>> params.export_fasteners_as_swgen
        True
        >>> params.export_rigid_bodies_as_swgen
        True
        """
        version = f"{major_version}r{minor_version}"
        params.write_separate_blocks = version >= "25r1"
        if version >= "25r1":
            params.separate_blocks_format_type = SeparateBlocksFormatType.COMPACT
        else:
            params.separate_blocks_format_type = SeparateBlocksFormatType.STANDARD
        params.export_fasteners_as_swgen = version >= "25r1"
        params.export_rigid_bodies_as_rbgen = version >= "25r1"
        return params

    def import_fluent_meshing_meshes(
        self,
        file_names: utils.FileNameList,
        import_fluent_meshing_mesh_params: ImportFluentMeshingMeshParams,
    ) -> ImportFluentMeshingMeshResults:
        """Import Fluent Meshing's mesh (MS and MSH.GZ) files from disk.

        Parameters
        ----------
        file_names : List[str]
            List of full path for the mesh files to import.
        import_fluent_meshing_mesh_params : ImportFluentMeshingMeshParams
            Parameters for importing the mesh files.

        Returns
        -------
        ImportFluentMeshingMeshResults
            Results from importing the mesh files.


        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ImportFluentMeshingMeshParams(model=model)
        >>> results = file_io.import_fluent_meshing_meshes(
                        ["/tmp/mesh.msh", "/tmp/mesh1.msh"],
                        params)

        """
        with utils.file_read_context_list(self._model, file_names) as temp_file_names:
            result = super().import_fluent_meshing_meshes(
                temp_file_names, import_fluent_meshing_mesh_params
            )
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result

    def import_fluent_case(
        self, file_name: str, import_fluent_case_params: ImportFluentCaseParams
    ) -> ImportFluentCaseResults:
        """Import a Fluent case (CAS) file from disk.

        Parameters
        ----------
        file_name : str
            Path to the case file on disk.
        import_fluent_case_params : ImportFluentCaseParams
            Parameters for importing the case file.

        Returns
        -------
        ImportFluentCaseResults
            Results from importing the case file.


        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ImportFluentCaseParams(model=model)
        >>> results = file_io.import_fluent_case("/tmp/fluent.cas", params)

        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            result = super().import_fluent_case(temp_file_name, import_fluent_case_params)
            if result.error_code == ErrorCode.NOERROR:
                self._model._sync_up_model()
        return result

    def export_fluent_case(
        self, file_name: str, export_fluent_case_params: ExportFluentCaseParams
    ) -> FileWriteResults:
        """Export a Fluent case (CAS) file.

        Parameters
        ----------
        file_name : str
            Path to the case file on disk.
        export_fluent_case_params : ExportFluentCaseParams
            Parameters for exporting the case file.

        Returns
        -------
        FileWriteResults
            Results from exporting the case file.

        Examples
        --------
        >>> file_io = FileIO(model=model)
        >>> results = file_io.export_fluent_case(
                        "/tmp/fluent.cas",
                        prime.ExportFluentCaseParams(model=model))
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_fluent_case(temp_file_name, export_fluent_case_params)
        return result

    def export_fluent_meshing_mesh(
        self, file_name: str, export_fluent_mesh_params: ExportFluentMeshingMeshParams
    ) -> FileWriteResults:
        """Export a Fluent Meshing mesh (MSH) file.

        Parameters
        ----------
        file_name : str
            Path to the mesh file on disk.
        export_fluent_mesh_params : ExportFluentMeshingMeshParams
            Parameters for exporting the mesh file.

        Returns
        -------
        FileWriteResults
            Results from exporting the mesh file.

        Examples
        --------
        >>> results = file_io.export_fluent_meshing_mesh(
                        "/tmp/fluent_meshing.msh",
                        ExportFluentMeshingMeshParams(model=model))
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_fluent_meshing_mesh(temp_file_name, export_fluent_mesh_params)
        return result

    def export_lsdyna_keyword_file(
        self, file_name: str, params: ExportLSDynaKeywordFileParams
    ) -> ExportLSDynaResults:
        """Export FEA LS-DYNA Keyword file for solid, surface mesh, or both.

        Parameters
        ----------
        file_name : str
            Name of the file.
        params : ExportLSDynaKeywordFileParams
            Parameters for FEA LS-DYNA Keyword file export.

        Returns
        -------
        ExportLSDynaResults
            Returns ExportLSDynaResults.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = file_io.export_lsdyna_keyword_file(
            file_name, ExportLSDynaKeywordFileParams(model=model)
        )

        """
        params = copy.copy(params)
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            # part_id = 1
            # if len(self._model.parts) > 0:
            #    part_id = self._model.parts[0].id
            args = {"partId": 0}
            command_name = "PrimeMesh::FileIO/GetAbaqusSimulationData"
            sim_data_str = self._comm.serve(self._model, command_name, self._object_id, args=args)
            if not sim_data_str or sim_data_str.strip() == "":
                sim_data = None
            else:
                sim_data = json.loads(sim_data_str)
            generate_lsdyna_commands_error = None
            generate_lsdyna_commands_traceback = None
            with utils.capture_log_records(self._model.python_logger) as collected_logs:
                all_mat_cmds = ""
                try:
                    if sim_data is not None:
                        mp = dynaexportutils.MaterialProcessor(self._model, sim_data)
                        all_mat_cmds = mp.get_all_material_commands()
                except Exception as e:
                    generate_lsdyna_commands_error = e
                    generate_lsdyna_commands_traceback = traceback.format_exc()
                if generate_lsdyna_commands_error is not None:
                    self._model.python_logger.warning(
                        "Failed to generate LS-DYNA material commands. "
                        "Export proceeded with empty settings. \nError: %s\n%s",
                        generate_lsdyna_commands_error,
                        generate_lsdyna_commands_traceback,
                    )
            params.material_properties = all_mat_cmds + params.material_properties
            params._custom_params["client_log_messages"] = json.dumps(collected_logs)
            result = super().export_lsdyna_keyword_file(temp_file_name, params)
        return result

    def export_lsdyna_iga_keyword_file(
        self, file_name: str, params: ExportLSDynaIgaKeywordFileParams
    ) -> ExportLSDynaIGAResults:
        """Export IGA LS-DYNA Keyword file for solid, surface splines.

        Parameters
        ----------
        file_name : str
            Name of the file.
        params : ExportLSDynaIgaKeywordFileParams
            Parameters for IGA LS-DYNA Keyword file export.

        Returns
        -------
        ExportLSDynaIGAResults
            Returns ExportLSDynaIGAResults.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = file_io.export_lsdyna_iga_keyword_file(
            file_name, ExportLSDynaIgaKeywordFileParams(model=model)
        )

        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_lsdyna_iga_keyword_file(temp_file_name, params)
        return result

    def export_boundary_fitted_spline_kfile(
        self, file_name: str, export_params: ExportBoundaryFittedSplineParams
    ) -> FileWriteResults:
        """Export the IGA LS-DYNA keyword file for a boundary fitted spline.

        Parameters
        ----------
        file_name : str
            Name of the keyword file.
        export_params : ExportBoundaryFittedSplineParams
            Parameters for exporting the keyword file.

        Returns
        -------
        FileWriteResults
            Results from exporting the keyword file.

        Examples
        --------
        >>> results = file_io.export_boundary_fitted_spline_k_file(
                        file_name,
                        ExportBoundaryFittedSplineParams(model=model))
        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_boundary_fitted_spline_kfile(temp_file_name, export_params)
        return result

    def import_cad(self, file_name: str, params: ImportCadParams) -> ImportCadResults:
        r"""Import a CAD file from disk.

        Supported CAD file formats on Windows are:

        \*.scdoc \*.scdocx \*.dsco \*.fmd \*.agdb \*.pmdb \*.meshdat \*.mechdat \*.dsdb \*.cmdb
        \*.sat \*.sab \*.dwg \*.dxf \*.model \*.exp \*.CATPart \*.CATProduct \*.cgr \*.3dxml
        \*.prt\* \*.asm\* \*.iges \*.igs \*.ipt \*.iam \*.jt \*.prt \*.x_t \*.x_b \*.par \*.psm
        \*.asm \*.sldprt \*.sldasm \*.step \*.stp \*.stl \*.plmxml \*.tgf

        Supported CAD file formats on Linux are:

        \*.fmd \*.agdb \*.pmdb \*.meshdat \*.mechdat \*.dsdb \*.cmdb \*.sat \*.sab
        \*.CATPart \*.CATProduct \*.iges \*.igs \*.jt \*.x_t \*.x_b \*.step \*.stp
        \*.stl \*.plmxml \*.tgf

        Refer **Reading and writing files** section in **User guide** for a
        comprehensive list of supported formats.

        Parameters
        ----------
        file_name : str
            Path to the CAD file on disk.

        params : ImportCadParams
            Parameters for importing the CAD file.

        Returns
        -------
        ImportCadResults
            Results from importing the CAD file.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> prime_client = prime.launch_prime()
        >>> model = prime_client.model
        >>> file_io = prime.FileIO(model=model)
        >>> params = prime.ImportCadParams(model=model)
        >>> results = file_io.import_cad("/tmp/my_cad.x_t", params=params)

        """
        with utils.file_read_context(self._model, file_name) as temp_file_name:
            import_result = super().import_cad(temp_file_name, params)
            if import_result.error_code == ErrorCode.NOERROR:
                self._model._sync_up_model()
        return import_result

    def export_stl(self, file_name: str, params: ExportSTLParams) -> FileWriteResults:
        """Export an STL file.

        Parameters
        ----------
        file_name : str
            Path to the STL file on disk.
        params : ExportSTLParams
            Parameters for exporting the STL file.

        Returns
        -------
        FileWriteResults
            Results from exporting the STL file.

        Notes
        -----
        This method does not support Unicode paths.

        Examples
        --------
        >>> import ansys.meshing.prime as prime
        >>> model = prime.launch_prime().model
        >>> fileio = prime.FileIO(model=model)
        >>> out_file_path = r"/tmp/output.stl"
        >>> part_ids = [part.id for part in model.parts]
        >>> export_stl_params=prime.ExportSTLParams(model=model,part_ids=part_ids)
        >>> results = fileio.export_stl(out_file_path,export_stl_params)

        """
        with utils.file_write_context(self._model, file_name) as temp_file_name:
            result = super().export_stl(temp_file_name, params)
        return result
