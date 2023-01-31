"""Implementation of Scanner for scanning bytes or bytearrays
"""
import re
from typing import Callable, Tuple

NUMBER_RE = re.compile(
    b'(-?(?:0|[1-9]\d*))(\.\d+)?([eE][-+]?\d+)?', (re.VERBOSE | re.MULTILINE | re.DOTALL)
)


def make_scanner(context) -> Callable[[str, int], Tuple[str, int]]:
    parse_object = context.parse_object
    parse_array = context.parse_array
    parse_string = context.parse_string
    match_number = NUMBER_RE.match
    parse_float = context.parse_float
    parse_int = context.parse_int
    parse_constant = context.parse_constant
    object_hook = context.object_hook
    object_pairs_hook = context.object_pairs_hook
    parse_bytes = context.parse_bytes
    memo = context.memo

    def _scan_once(string: bytes or bytearray, idx):
        try:
            nextchar = bytes(string[idx : idx + 1])
        except IndexError:
            raise StopIteration(idx) from None

        if nextchar == b'"':
            return parse_string(string, idx + 1)
        elif nextchar == b'{':
            return parse_object((string, idx + 1), _scan_once, object_hook, object_pairs_hook, memo)
        elif nextchar == b'[':
            return parse_array((string, idx + 1), _scan_once)
        elif nextchar == b'<':
            return parse_bytes(string, idx + 1)
        elif nextchar == b'n' and string[idx : idx + 4] == b'null':
            return None, idx + 4
        elif nextchar == b't' and string[idx : idx + 4] == b'true':
            return True, idx + 4
        elif nextchar == b'f' and string[idx : idx + 5] == b'false':
            return False, idx + 5

        m = match_number(string, idx)
        if m is not None:
            integer, frac, exp = m.groups()
            if frac or exp:
                res = parse_float(
                    integer.decode('utf-8')
                    + (frac or b'').decode('utf-8')
                    + (exp or b'').decode('utf-8')
                )
            else:
                res = parse_int(integer)
            return res, m.end()
        elif nextchar == b'N' and string[idx : idx + 3] == b'NaN':
            return parse_constant('NaN'), idx + 3
        elif nextchar == b'I' and string[idx : idx + 8] == b'Infinity':
            return parse_constant('Infinity'), idx + 8
        elif nextchar == b'-' and string[idx : idx + 9] == b'-Infinity':
            return parse_constant('-Infinity'), idx + 9
        else:
            raise StopIteration(idx)

    def scan_once(string: bytes or bytearray, idx):
        try:
            return _scan_once(string, idx)
        finally:
            memo.clear()

    return scan_once
