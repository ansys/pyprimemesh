# Copyright (C) 2026 ANSYS, Inc. and/or its affiliates.
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

"""YAML to PRIME JSON schema converter module.

Converts user-friendly YAML schema definitions to ANSYS PRIME's JSON schema format.
Supports both simple keywords (like *BOUNDARY) and complex parameter-variant keywords
(like *SURFACE). Preserves Output templates and field metadata.

Architecture:
- Simple keywords: Data -> Data_Block.Data_Fields + Output_Template
- Complex keywords: Parameters + Variants -> Data_Parameter structure with variant-specific outputs

This module is designed to be imported and used programmatically, not as a standalone script.
"""

import json
import logging
from typing import Any, Dict, List

from .yaml_parser import parse_yaml_file

# Schema JSON keys (module-level constants)
DATA_BLOCK = "Data_Block"
DATA_FIELDS = "Data_Fields"
OUTPUT_TEMPLATE = "Output_Template"
DEFAULT_PARAMETERS = "Default_Parameters"


class YamlToPrimeJsonConverter:
    """Converts YAML keyword definitions to PRIME JSON schema format."""

    def __init__(self):
        """Initialize an empty converter."""
        self.schemas = {}
        self.logger = logging.getLogger(__name__)

    def convert_yaml_file(self, yaml_file_path: str) -> Dict[str, Any]:
        """
        Convert a YAML file to PRIME JSON schema format.

        Args:
            yaml_file_path: Path to the YAML file to convert

        Returns:
            Dictionary containing the converted schemas

        Raises:
            ValueError: If the YAML file is empty or invalid
            FileNotFoundError: If the YAML file doesn't exist
        """
        yaml_data = parse_yaml_file(yaml_file_path)
        if yaml_data is None:
            raise ValueError(f"Empty or invalid YAML file: {yaml_file_path}")

        for keyword_name, keyword_def in yaml_data.items():
            if not isinstance(keyword_def, dict):
                raise ValueError(f"Invalid schema for {keyword_name}")

            if keyword_name.startswith('TranslationRulesTweaking'):
                for key, value in keyword_def.items():
                    self.schemas[key] = value
                continue

            pattern = self._extract_pattern(keyword_def)
            json_schema = self._convert_simple_keyword(keyword_def)
            self.schemas[pattern] = json_schema

        return self.schemas

    def _extract_pattern(self, keyword_def: Dict) -> str:
        """Extract and validate the pattern from a keyword definition."""
        pattern = keyword_def.get('Pattern', '')
        if not pattern:
            raise ValueError("Missing 'Pattern' in keyword definition")

        pattern = pattern.lstrip('*').upper()
        return pattern

    def _extract_default_parameters(self, parameters: List[Dict]) -> Dict:
        """Extract default parameter values."""
        return {p["name"]: p["default"] for p in parameters if "default" in p}

    def _is_array_field(self, field_type: str) -> bool:
        """Check if a field type indicates an array."""
        return "list" in field_type.lower()

    def _expand_array_fields(self, field_name, field_type) -> list:
        """Expand array field definitions into individual field names."""
        field_names = []
        field_type = field_type.replace('list', '')
        field_type = field_type.replace('[', '')
        field_type = field_type.replace(']', '')
        total_data_points = 0
        for part in map(str.strip, field_type.split(",")):
            if "*" in part:
                count, dtype = part.split("*")
                total_data_points += int(count)
            else:
                total_data_points += 1
        for i in range(total_data_points):
            array_field_name = f"{field_name}_{i+1}"
            field_names.append(array_field_name)
        return field_names

    def _convert_simple_keyword(self, keyword_def: Dict) -> Dict:
        """Convert a keyword definition to JSON schema format."""
        EXCLUDED_KEYS = {"Pattern", "Description"}
        json_schema = {}
        for key, value in keyword_def.items():
            if key in EXCLUDED_KEYS:
                continue
            if key == "OutputExpression":
                while value[-1] == "\n":
                    value = value[:-1]
            json_schema[key] = value

        return json_schema

    def get_json_string(self, indent: int = 2) -> str:
        """
        Get the converted schemas as a JSON string.

        Args:
            indent: Indentation level for JSON formatting

        Returns:
            JSON string representation of the schemas
        """
        return json.dumps(self.schemas, indent=indent)


def convert_yaml_to_json_string(yaml_file_path: str) -> str:
    """
    Convert a YAML file to a JSON string.

    Args:
        yaml_file_path: Path to the YAML file to convert

    Returns:
        JSON string representation of the converted schemas

    Raises:
        ValueError: If the YAML file is empty or invalid
        FileNotFoundError: If the YAML file doesn't exist

    Example:
        >>> json_string = convert_yaml_to_json_string("schema.yaml")
        >>> customizationSchema = json_string
    """
    converter = YamlToPrimeJsonConverter()
    converter.convert_yaml_file(yaml_file_path)
    return converter.get_json_string()
