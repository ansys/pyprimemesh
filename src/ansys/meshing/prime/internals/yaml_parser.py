# Copyright (C) 2022 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

"""ANSYS PRIME standalone YAML parser.

Zero external dependencies - pure Python implementation.

Parses YAML keyword definition files following PRIME schema format.
Supports: scalars, lists, dicts, multi-line strings, comments.

Author: ANSYS PRIME Team
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union


class YamlParseError(Exception):
    """Exception raised for YAML parsing errors."""

    pass


class YamlParser:
    """
    Standalone YAML parser for ANSYS PRIME keyword schemas.

    Supports:
    - Key-value pairs (key: value)
    - Lists with '-' prefix
    - Nested dictionaries (indentation-based)
    - Multi-line strings (| and >)
    - Comments (#)
    - Quoted strings ("..." and '...')
    - Type inference (string, int, float, bool, null)

    Does NOT support (not needed for PRIME schemas):
    - Anchors/aliases (&anchor, *alias)
    - Complex flow syntax ({}, [])
    - Multiple documents (---)
    - Custom tags (!!str, !!int)
    """

    def __init__(self):
        """Initialize an empty parser state."""
        self.lines: List[str] = []
        self.line_num = 0
        self.current_indent = 0

    def parse(self, text: str) -> Dict[str, Any]:
        """
        Parse YAML text and return Python dictionary.

        Args:
            text: YAML content as string

        Returns:
            Parsed data as Python dict

        Raises:
            YamlParseError: If syntax is invalid
        """
        # Normalize line endings and split
        text = text.replace('\r\n', '\n').replace('\r', '\n')
        self.lines = text.split('\n')
        self.line_num = 0
        return self._parse_dict(0)

    def parse_file(self, filepath: str) -> Dict[str, Any]:
        """
        Parse YAML file and return Python dictionary.

        Args:
            filepath: Path to YAML file

        Returns:
            Parsed data as Python dict
        """
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"YAML file not found: {filepath}")

        with path.open('r', encoding='utf-8') as f:
            content = f.read()

        return self.parse(content)

    def _get_indent(self, line: str) -> int:
        """Count leading spaces (tabs converted to 2 spaces)."""
        expanded = line.replace('\t', '  ')
        return len(expanded) - len(expanded.lstrip(' '))

    def _strip_comment(self, line: str) -> str:
        """Remove # comments (preserving # inside quotes)."""
        result = []
        in_single_quote = False
        in_double_quote = False
        i = 0

        while i < len(line):
            char = line[i]

            # Toggle quote states
            if char == "'" and not in_double_quote:
                in_single_quote = not in_single_quote
                result.append(char)
            elif char == '"' and not in_single_quote:
                # Check if escaped
                if i > 0 and line[i - 1] == '\\':
                    result.append(char)
                else:
                    in_double_quote = not in_double_quote
                    result.append(char)
            elif char == '#' and not in_single_quote and not in_double_quote:
                # Found unquoted comment - stop here
                break
            else:
                result.append(char)

            i += 1

        return ''.join(result).rstrip()

    def _parse_value(self, value_str: str) -> Union[str, int, float, bool, None]:
        """Convert string to appropriate Python type."""
        value_str = value_str.strip()

        if not value_str:
            return None

        # Null/None
        if value_str in ('null', 'Null', 'NULL', '~', ''):
            return None

        # Boolean
        if value_str in ('true', 'True', 'TRUE'):
            return True
        if value_str in ('false', 'False', 'FALSE'):
            return False

        # Quoted string - remove quotes
        if (value_str.startswith('"') and value_str.endswith('"')) or (
            value_str.startswith("'") and value_str.endswith("'")
        ):
            # Unescape common escape sequences
            unquoted = value_str[1:-1]
            unquoted = unquoted.replace('\\n', '\n')
            unquoted = unquoted.replace('\\t', '\t')
            unquoted = unquoted.replace('\\r', '\r')
            unquoted = unquoted.replace('\\"', '"')
            unquoted = unquoted.replace("\\'", "'")
            unquoted = unquoted.replace('\\\\', '\\')
            return unquoted

        # Number (int or float)
        try:
            # Try int first
            if '.' not in value_str and 'e' not in value_str.lower():
                return int(value_str)
            # Try float
            return float(value_str)
        except ValueError:
            pass

        # Inline flow mapping: {k: v, k: v, ...}
        if value_str.startswith('{') and value_str.endswith('}'):
            return self._parse_flow_mapping(value_str)

        # Return as string
        return value_str

    def _parse_flow_mapping(self, text: str) -> dict:
        """Parse an inline YAML flow mapping of the form ``{k: v, k: v, ...}``."""
        inner = text[1:-1].strip()
        result = {}
        if not inner:
            return result
        # Split on commas NOT inside nested braces/brackets
        parts = []
        depth = 0
        current = []
        for ch in inner:
            if ch in ('{', '['):
                depth += 1
                current.append(ch)
            elif ch in ('}', ']'):
                depth -= 1
                current.append(ch)
            elif ch == ',' and depth == 0:
                parts.append(''.join(current).strip())
                current = []
            else:
                current.append(ch)
        if current:
            parts.append(''.join(current).strip())
        for part in parts:
            if ':' not in part:
                continue
            k, _, v = part.partition(':')
            result[self._parse_value(k.strip())] = self._parse_value(v.strip())
        return result

    def _peek_next_line(self, current_indent: int) -> Optional[Tuple[int, str]]:
        """
        Peek at next non-empty, non-comment line without consuming it.

        Returns:
            (indent, stripped_line) or None if no more lines
        """
        save_line_num = self.line_num

        while self.line_num < len(self.lines):
            raw_line = self.lines[self.line_num]
            line = self._strip_comment(raw_line)

            if line.strip():
                indent = self._get_indent(line)
                stripped = line.strip()
                self.line_num = save_line_num  # Restore position
                return (indent, stripped)

            self.line_num += 1

        self.line_num = save_line_num
        return None

    def _parse_dict(self, base_indent: int) -> Dict[str, Any]:
        """Parse dictionary at given indentation level."""
        result = {}

        while self.line_num < len(self.lines):
            raw_line = self.lines[self.line_num]
            line = self._strip_comment(raw_line)

            # Skip empty lines
            if not line.strip():
                self.line_num += 1
                continue

            indent = self._get_indent(line)
            stripped = line.strip()

            # Exit if dedented
            if indent < base_indent:
                break

            # Skip if more indented (will be handled by nested call)
            if indent > base_indent:
                raise YamlParseError(
                    f"Line {self.line_num + 1}: Unexpected indentation: '{stripped}'"
                )

            # Must have a colon for key-value
            if ':' not in stripped:
                raise YamlParseError(
                    f"Line {self.line_num + 1}: Expected key:value, got: '{stripped}'"
                )

            # Parse key and value
            key, _, value = stripped.partition(':')
            key = key.strip()
            value = value.strip()

            self.line_num += 1

            # Multi-line string (| or >)
            if value in ('|', '>'):
                result[key] = self._parse_multiline(base_indent, fold=(value == '>'))
                continue

            # Empty value - check next line
            if not value:
                peek = self._peek_next_line(base_indent)

                if peek is None:
                    result[key] = None
                    continue

                next_indent, next_stripped = peek

                # List follows
                if next_indent > base_indent and next_stripped.startswith('-'):
                    result[key] = self._parse_list(next_indent)
                # Nested dict follows
                elif next_indent > base_indent and ':' in next_stripped:
                    result[key] = self._parse_dict(next_indent)
                else:
                    result[key] = None
            else:
                # Inline value
                result[key] = self._parse_value(value)

        return result

    def _parse_list_item_properties(
        self, base_indent: int, initial_dict: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Parse additional properties of a list item that started with '- key: value'.

        Continues reading lines at base_indent+2 (or more) until dedented or next '-'.

        Args:
            base_indent: The indent level of the '-'
            initial_dict: Dictionary with first property already parsed

        Returns:
            Complete dictionary with all properties
        """
        result = initial_dict.copy()

        while self.line_num < len(self.lines):
            raw_line = self.lines[self.line_num]
            line = self._strip_comment(raw_line)

            if not line.strip():
                self.line_num += 1
                continue

            indent = self._get_indent(line)
            stripped = line.strip()

            # Stop if dedented to base level or below
            if indent <= base_indent:
                break

            # Stop if we hit another list item
            if stripped.startswith('-'):
                break

            # Must be a key:value at proper indent
            if ':' not in stripped:
                break

            key, _, value = stripped.partition(':')
            key = key.strip()
            value = value.strip()

            self.line_num += 1

            # Handle multi-line string
            if value in ('|', '>'):
                result[key] = self._parse_multiline(indent, fold=(value == '>'))
            # Empty value - check for nested structure
            elif not value:
                peek = self._peek_next_line(indent)
                if peek and peek[0] > indent:
                    next_indent, next_stripped = peek
                    if next_stripped.startswith('-'):
                        result[key] = self._parse_list(peek[0])
                    elif ':' in next_stripped:
                        # Parse nested dict (e.g., when: followed by TYPE: ELEMENT)
                        result[key] = self._parse_dict(peek[0])
                    else:
                        result[key] = None
                else:
                    result[key] = None
            # Simple inline value
            else:
                result[key] = self._parse_value(value)

        return result

    def _parse_list(self, base_indent: int) -> List[Any]:
        """Parse list at given indentation level."""
        result = []

        while self.line_num < len(self.lines):
            raw_line = self.lines[self.line_num]
            line = self._strip_comment(raw_line)

            if not line.strip():
                self.line_num += 1
                continue

            indent = self._get_indent(line)
            stripped = line.strip()

            # Exit if dedented below base
            if indent < base_indent:
                break

            # Must start with '-' at base indent level
            if indent == base_indent:
                if not stripped.startswith('-'):
                    # Not a list item anymore
                    break

                # Get value after '-'
                value = stripped[1:].strip()
                self.line_num += 1

                # Case 1: Inline simple value (e.g., "- item")
                if value and ':' not in value:
                    result.append(self._parse_value(value))
                    continue

                # Case 2: Inline dict (e.g., "- key: value" or "- when:")
                if value and ':' in value:
                    key, _, val = value.partition(':')
                    key = key.strip()
                    val = val.strip()

                    # Check if value is empty (e.g., "- when:")
                    if not val:
                        # Value will come from indented lines below
                        # Peek to see what follows
                        peek = self._peek_next_line(base_indent)

                        if peek and peek[0] > base_indent:
                            next_indent, next_stripped = peek

                            # Next line is indented dict content (e.g., TYPE: ELEMENT under when:)
                            if ':' in next_stripped and not next_stripped.startswith('-'):
                                # Parse the nested dict as the value for this key
                                nested_dict = self._parse_dict(peek[0])
                                item_dict = {key: nested_dict}

                                # Continue parsing other properties at same level
                                item_dict = self._parse_list_item_properties(base_indent, item_dict)
                                result.append(item_dict)
                                continue
                            # Next line is a list
                            elif next_stripped.startswith('-'):
                                nested_list = self._parse_list(peek[0])
                                item_dict = {key: nested_list}

                                # Continue parsing other properties
                                item_dict = self._parse_list_item_properties(base_indent, item_dict)
                                result.append(item_dict)
                                continue

                        # No nested structure, just empty value
                        item_dict = {key: None}
                    else:
                        # Has inline value (e.g., "- name: MPC_TYPE")
                        item_dict = {key: self._parse_value(val)}

                    # Check if more properties follow (without '-')
                    item_dict = self._parse_list_item_properties(base_indent, item_dict)
                    result.append(item_dict)
                    continue

                # Case 3: Empty after '-', check next line
                peek = self._peek_next_line(base_indent)

                if peek is None:
                    result.append(None)
                    continue

                next_indent, next_stripped = peek

                # Multi-line dict under list item (most common case)
                # Next line should be indented and be a key:value
                if (
                    next_indent > base_indent
                    and ':' in next_stripped
                    and not next_stripped.startswith('-')
                ):
                    item_dict = self._parse_dict(next_indent)
                    result.append(item_dict)
                # Nested list under list item
                elif next_indent > base_indent and next_stripped.startswith('-'):
                    result.append(self._parse_list(next_indent))
                else:
                    result.append(None)
            else:
                # Indented more than base - shouldn't happen at list level
                break

        return result

    def _parse_multiline(self, base_indent: int, fold: bool = False) -> str:
        """
        Parse multi-line string (| or >).

        Args:
            base_indent: Base indentation of parent key
            fold: If True (>), fold lines into single line. If False (|), preserve newlines.
        """
        lines = []
        min_indent = None

        while self.line_num < len(self.lines):
            raw_line = self.lines[self.line_num]

            # Empty line - keep it
            if not raw_line.strip():
                self.line_num += 1
                lines.append('')
                continue

            indent = self._get_indent(raw_line)

            # Exit if dedented to base level or less
            if indent <= base_indent:
                break

            # Track minimum indentation of content
            if min_indent is None:
                min_indent = indent

            # Remove base indentation
            content = raw_line[min_indent:] if indent >= min_indent else raw_line.lstrip()
            lines.append(content.rstrip())
            self.line_num += 1

        if fold:
            # Fold mode (>): join lines with spaces, collapse empty lines
            result = []
            current = []

            for line in lines:
                if not line:
                    if current:
                        result.append(' '.join(current))
                        current = []
                    result.append('')
                else:
                    current.append(line)

            if current:
                result.append(' '.join(current))

            return '\n'.join(result).strip()
        else:
            # Literal mode (|): preserve newlines
            return '\n'.join(lines)


def parse_yaml(text: str) -> Dict[str, Any]:
    """
    Parse YAML text and return Python dictionary.

    Args:
        text: YAML content as string

    Returns:
        Parsed data as Python dict

    Example:
        >>> yaml_text = '''
        ... MPC_Definition:
        ...   Pattern: "*MPC"
        ...   Data:
        ...     - name: MPC_TYPE
        ...       type: string
        ... '''
        >>> data = parse_yaml(yaml_text)
        >>> print(data['MPC_Definition']['Pattern'])
        *MPC
    """
    parser = YamlParser()
    return parser.parse(text)


def parse_yaml_file(filepath: str) -> Dict[str, Any]:
    """
    Parse YAML file and return Python dictionary.

    Args:
        filepath: Path to YAML file

    Returns:
        Parsed data as Python dict

    Example:
        >>> data = parse_yaml_file("YamlDoc.yaml")
        >>> keywords = list(data.keys())
        >>> print(f"Found {len(keywords)} keyword definitions")
    """
    parser = YamlParser()
    return parser.parse_file(filepath)


# Validation and conversion functions for PRIME schemas


def validate_prime_keyword_schema(data: Dict[str, Any]) -> List[str]:
    """
    Validate parsed YAML against PRIME keyword schema rules.

    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []

    for keyword_name, keyword_def in data.items():
        if not isinstance(keyword_def, dict):
            errors.append(f"Keyword '{keyword_name}' must be a dictionary")
            continue

        # Rule 1: Must have Pattern
        if 'Pattern' not in keyword_def:
            errors.append(f"Keyword '{keyword_name}' missing required 'Pattern' field")

        # Rule 2: Parameters must be list if present
        if 'Parameters' in keyword_def:
            if not isinstance(keyword_def['Parameters'], list):
                errors.append(f"'{keyword_name}' Parameters must be a list (use '-')")

        # Rule 2: Data must be list if present
        if 'Data' in keyword_def:
            if not isinstance(keyword_def['Data'], list):
                errors.append(f"'{keyword_name}' Data must be a list (use '-')")

        # Rule 2: Variants must be list if present
        if 'Variants' in keyword_def:
            if not isinstance(keyword_def['Variants'], list):
                errors.append(f"'{keyword_name}' Variants must be a list (use '-')")

            # Rule 4: Each variant must have 'when:' condition
            for i, variant in enumerate(keyword_def['Variants']):
                if 'when' not in variant:
                    errors.append(f"'{keyword_name}' Variant {i} missing 'when:' condition")

        # Rule 3: Validate field structure in Data
        if 'Data' in keyword_def and isinstance(keyword_def['Data'], list):
            for field in keyword_def['Data']:
                if not isinstance(field, dict):
                    errors.append(f"'{keyword_name}' Data field must be dictionary")
                    continue

                if 'name' not in field:
                    errors.append(f"'{keyword_name}' Data field missing 'name'")
                if 'type' not in field:
                    errors.append(
                        f"'{keyword_name}' Data field '{field.get('name', '?')}' missing 'type'"
                    )
    return errors


def convert_to_json_schema(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert parsed YAML to JSON schema format for AbaqusImpl.cpp.

    Args:
        yaml_data: Parsed YAML data

    Returns:
        JSON schema dictionary compatible with ReadPropertySectionWithSchema
    """
    json_schema = {}

    for keyword_name, keyword_def in yaml_data.items():
        if not isinstance(keyword_def, dict):
            continue

        keyword_schema = {}

        # Add Data_Block for common data fields
        if 'Data' in keyword_def and isinstance(keyword_def['Data'], list):
            data_field_names = [field['name'] for field in keyword_def['Data'] if 'name' in field]
            keyword_schema['Data_Block'] = {
                'Data_Fields': [data_field_names],
                'Object': None,
                'Repeat': None,
            }

        # Add Default_Parameters
        if 'Parameters' in keyword_def and isinstance(keyword_def['Parameters'], list):
            default_params = {}
            for param in keyword_def['Parameters']:
                if 'default' in param and param['default'] is not None:
                    default_params[param['name']] = str(param['default'])

            if default_params:
                keyword_schema['Default_Parameters'] = default_params

        # Handle Variants -> Output_Parameter structure
        if 'Variants' in keyword_def and isinstance(keyword_def['Variants'], list):
            variants = keyword_def['Variants']

            if variants:
                # Get variant parameter name (assume all use same parameter)
                first_variant = variants[0]
                if 'when' in first_variant:
                    variant_param_name = list(first_variant['when'].keys())[0]

                    output_param = {variant_param_name: {}}

                    for variant in variants:
                        if 'when' not in variant:
                            continue

                        variant_value = variant['when'].get(variant_param_name)
                        if not variant_value:
                            continue

                        output_template = {}
                        if 'Output_Expression' in variant:
                            output_template['Expression'] = variant['Output_Expression']
                        elif 'Output_Function' in variant:
                            output_template['Function'] = variant['Output_Function']

                        if output_template:
                            output_param[variant_param_name][variant_value] = {
                                'Output_Template': output_template
                            }

                    if output_param[variant_param_name]:
                        keyword_schema['Output_Parameter'] = output_param

        # Handle simple Output_Expression (no variants)
        elif 'Output_Expression' in keyword_def or 'Output_Function' in keyword_def:
            output_template = {}
            if 'Output_Expression' in keyword_def:
                output_template['Expression'] = keyword_def['Output_Expression']
            elif 'Output_Function' in keyword_def:
                output_template['Function'] = keyword_def['Output_Function']

            if output_template:
                keyword_schema['Output_Template'] = output_template

        json_schema[keyword_name] = keyword_schema

    return json_schema


# Main conversion function for workflow integration


def convert_yaml_to_json_schema(
    yaml_file: str, output_file: Optional[str] = None
) -> Dict[str, Any]:
    """
    Complete workflow: Parse YAML → Validate → Convert to JSON schema.

    Args:
        yaml_file: Path to YAML keyword definition file
        output_file: Optional path to save JSON schema (if None, only returns dict)

    Returns:
        JSON schema dictionary

    Raises:
        YamlParseError: If YAML syntax is invalid
        ValueError: If schema validation fails

    Example:
        >>> schema = convert_yaml_to_json_schema("YamlDoc.yaml", "abaqus_schema.json")
        >>> print(f"Converted {len(schema)} keywords")
    """
    # Parse YAML
    yaml_data = parse_yaml_file(yaml_file)

    # Validate against PRIME rules
    errors = validate_prime_keyword_schema(yaml_data)
    if errors:
        error_msg = "YAML schema validation failed:\n" + "\n".join(f"  - {err}" for err in errors)
        raise ValueError(error_msg)

    # Convert to JSON schema
    json_schema = convert_to_json_schema(yaml_data)

    # Save if output file specified
    if output_file:
        import json

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_schema, f, indent=2)

    return json_schema
