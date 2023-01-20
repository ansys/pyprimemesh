"""Implementation of Relaxed JSON Decoder
"""
import re
from typing import Any, Callable, Dict, Tuple

import numpy as np

from . import scanner

__all__ = ['JSONDecoder', 'JSONDecodeError']

FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL

NaN = float('nan')
PosInf = float('inf')
NegInf = float('-inf')

_CONSTANTS = {
    b'-Infinity': NegInf,
    b'Infinity': PosInf,
    b'NaN': NaN,
}


class JSONDecodeError(ValueError):
    def __init__(self, msg: str, document: bytes or bytearray, pos: int):
        lineno = document.count(b'\n', 0, pos) + 1
        colno = pos - document.rfind(b'\n', 0, pos)
        error_msg = f"{msg}: line {lineno} column {colno} (char {pos})"
        ValueError.__init__(self, error_msg)
        self.error_msg = error_msg
        self.lineno = lineno
        self.colno = colno
        self.pos = pos


WHITESPACE = re.compile(r'[ \t\n\r]*'.encode("utf-8"), FLAGS)
WHITESPACE_STR = b' \t\n\r'

STRINGCHUNK = re.compile(r'(.*?)(["\\])'.encode('utf-8'), FLAGS)
BACKSLASH = {
    '"': b'"',
    '\\': b'\\',
    '/': b'/',
    'b': b'\b',
    'f': b'\f',
    'n': b'\n',
    'r': b'\r',
    't': b'\t',
}


def then(first, continuation):
    def _then(dct):
        dct = first(dct)
        return continuation(dct)

    return _then


TYPEMAP = {
    0x11: np.uint8,
    0x12: np.int16,
    0x13: np.int32,
    0x14: np.int64,
    0x19: np.uint8,
    0x1A: np.uint16,
    0x1B: np.uint32,
    0x1C: np.uint64,
    0x21: np.float32,
    0x22: np.float64,
}

TYPEDATA = {
    'int32': {'type': int, 'object_size': 4, 'signed': True},
    'int64': {'type': int, 'object_size': 8, 'signed': True},
    'uint32': {'type': int, 'object_size': 4, 'signed': False},
    'uint64': {'type': int, 'object_size': 8, 'signed': True},
    'double': {'type': float, 'object_size': 8},
}


def scan_string(str: bytes or bytearray, end: int, _b=BACKSLASH, _m=STRINGCHUNK.match):
    """Scan the string s for a JSON string. End is the index of the
    character in s after the quote that started the JSON string.
    Unescapes all valid JSON string escape sequences and raises ValueError
    on attempt to decode an invalid string. If strict is False then literal
    control characters are allowed in the string.

    Returns a tuple of the decoded string and the index of the character in s
    after the end quote."""
    chunks = bytearray()
    begin = end - 1
    while 1:
        chunk = _m(str, end)
        if chunk is None:
            raise JSONDecodeError("Unterminated string starting at", str, begin)
        end = chunk.end()
        content, terminator = chunk.groups()
        # Content is contains zero or more unescaped string characters
        if content:
            chunks += content
        # Terminator is the end of string, a literal control character,
        # or a backslash denoting that an escape sequence follows
        if terminator == b'"':
            break
        elif terminator != b'\\':
            chunks += terminator
            continue
        try:
            esc = str[end : end + 1]
        except IndexError:
            raise JSONDecodeError("Unterminated string starting at", str, begin) from None
        # If not a unicode escape sequence, must be in the lookup table
        if esc == b'u':
            raise JSONDecodeError("Unicode not supported", str, end)
        else:
            try:
                char: bytes or bytearray = _b[esc.decode('utf-8')]
            except KeyError:
                msg = "Invalid \\escape: {0!r}".format(esc.decode('utf-8'))
                raise JSONDecodeError(msg, str, end)
            end += 1
        chunks += char

    try:
        chunks = chunks.decode('utf-8')
    except:
        raise JSONDecodeError("String needs to be utf-8 encoded", str, begin)
    return chunks, end


def decode_bytes(s, end):
    begin = end - 1
    size = int.from_bytes(bytes(s[end : end + 8]), byteorder='big')
    end += 8
    type = int.from_bytes(s[end : end + 1], byteorder='big')
    end += 1
    value = bytes(s[end : end + size])
    end += size

    if s[end : end + 1] != b'>':
        raise JSONDecodeError("Unterminated bytes object starting at", str, begin) from None
    end += 1  # '>' character

    dtype = TYPEMAP.get(type, None)
    if dtype is None:
        raise JSONDecodeError(f'Invalid type ({type}) decoded while reading bytes', s, end)
    dtype = np.dtype(dtype)
    data = np.frombuffer(value, dtype=dtype.newbyteorder('>'))
    return np.array(data, dtype=dtype), end


def decode_object(
    str_and_idx: Tuple[str, int],
    scan_once: Callable[[str, int], Tuple[str, int]],
    object_hook: Callable[[Dict[str, Any]], Any],
    object_pairs_hook,
    memo,
    _w=WHITESPACE.match,
    _ws=WHITESPACE_STR,
):
    s, end = str_and_idx
    pairs = []
    pairs_append = pairs.append
    # Backwards compatibility
    if memo is None:
        memo = {}
    memo_get = memo.setdefault
    # Use a slice to prevent IndexError from being raised, the following
    # check will raise a more specific ValueError if the string is empty
    nextchar = bytes(s[end : end + 1])
    # Normally we expect nextchar == '"'
    if nextchar != b'"':
        if nextchar in _ws:
            end = _w(s, end).end()
            nextchar = bytes(s[end : end + 1])
        # Trivial empty object
        if nextchar == b'}':
            if object_pairs_hook is not None:
                result = object_pairs_hook(pairs)
                return result, end + 1
            pairs = {}
            if object_hook is not None:
                pairs = object_hook(pairs)
            return pairs, end + 1
        elif nextchar != b'"':
            raise JSONDecodeError("Expecting property name enclosed in double quotes", s, end)
    end += 1
    while True:
        key, end = scan_string(s, end)
        key = memo_get(key, key)
        # To skip some function call overhead we optimize the fast paths where
        # the JSON key separator is ": " or just ":".
        if s[end : end + 1] != b':':
            end = _w(s, end).end()
            if s[end : end + 1] != b':':
                raise JSONDecodeError("Expecting ':' delimiter", s, end)
        end += 1

        try:
            if s[end : end + 1] in _ws:
                end += 1
                if s[end : end + 1] in _ws:
                    end = _w(s, end + 1).end()
        except IndexError:
            pass

        try:
            value, end = scan_once(s, end)
        except StopIteration as err:
            raise JSONDecodeError("Expecting value", s, err.value) from None
        pairs_append((key, value))
        try:
            nextchar = bytes(s[end : end + 1])
            if nextchar in _ws:
                end = _w(s, end + 1).end()
                nextchar = bytes(s[end : end + 1])
        except IndexError:
            nextchar = b''
        end += 1

        if nextchar == b'}':
            break
        elif nextchar != b',':
            raise JSONDecodeError("Expecting ',' delimiter", s, end - 1)
        end = _w(s, end).end()
        nextchar = s[end : end + 1]
        end += 1
        if nextchar != b'"':
            raise JSONDecodeError("Expecting property name enclosed in double quotes", s, end - 1)
    if object_pairs_hook is not None:
        result = object_pairs_hook(pairs)
        return result, end
    pairs = dict(pairs)
    if object_hook is not None:
        pairs = object_hook(pairs)
    return pairs, end


def decode_array(
    str_and_idx: Tuple[str, int],
    scan_once: Callable[[str, int], Tuple[str, int]],
    _w=WHITESPACE.match,
    _ws=WHITESPACE_STR,
):
    s, end = str_and_idx
    values = []
    nextchar = bytes(s[end : end + 1])
    if nextchar in _ws:
        end = _w(s, end + 1).end()
        nextchar = s[end : end + 1]
    # Look-ahead for trivial empty array
    if nextchar == b']':
        return values, end + 1
    _append = values.append
    while True:
        try:
            value, end = scan_once(s, end)
        except StopIteration as err:
            raise JSONDecodeError("Expecting value", s, err.value) from None
        _append(value)
        nextchar = bytes(s[end : end + 1])
        if nextchar in _ws:
            end = _w(s, end + 1).end()
            nextchar = s[end : end + 1]
        end += 1
        if nextchar == b']':
            break
        elif nextchar != b',':
            raise JSONDecodeError("Expecting ',' delimiter", s, end - 1)
        try:
            if bytes(s[end : end + 1]) in _ws:
                end += 1
                if bytes(s[end : end + 1]) in _ws:
                    end = _w(s, end + 1).end()
        except IndexError:
            pass

    return values, end


class JSONDecoder:
    def __init__(
        self,
        *,
        object_hook=None,
        parse_float=None,
        parse_int=None,
        parse_constant=None or _CONSTANTS.__getitem__,
        strict=True,
        object_pairs_hook=None,
    ):
        self.object_hook = object_hook or None
        self.parse_float = parse_float or float
        self.parse_int = parse_int or int
        self.parse_constant = parse_constant
        self.object_pairs_hook = object_pairs_hook
        self.parse_string = scan_string
        self.parse_array = decode_array
        self.parse_object = decode_object
        self.parse_bytes = decode_bytes
        self.strict = strict
        self.memo = {}
        self.scan_once = scanner.make_scanner(self)

    def raw_decode(self, s: bytes or bytearray, idx: int) -> Tuple[Any, int]:
        try:
            obj, end = self.scan_once(s, idx)
        except StopIteration as err:
            raise JSONDecodeError("Expecting value", s, err.value) from None
        return obj, end

    def decode(self, s: bytes or bytearray, _w=WHITESPACE.match) -> Any:
        obj, end = self.raw_decode(s, _w(s, 0).end())
        end = _w(s, end).end()
        if end != len(s):
            raise JSONDecodeError("Extra data at end of document", s, end)
        return obj.decode('utf-8') if isinstance(obj, (bytes, bytearray)) else obj
