'''Implementation of JSOnEncoder that can handle byte arrays
'''
import re

import numpy as np

ESCAPE = re.compile(r'[\x00-\x1f\\"\b\f\n\r\t]')
ESCAPE_ASCII = re.compile(r'([\\"]|[^\ -~])')
HAS_UTF8 = re.compile(b'[\x80-\xff]')
ESCAPE_DCT = {
    '\\': '\\\\',
    '"': '\\"',
    '\b': '\\b',
    '\f': '\\f',
    '\n': '\\n',
    '\r': '\\r',
    '\t': '\\t',
}
for i in range(0x20):
    ESCAPE_DCT.setdefault(chr(i), '\\u{0:04x}'.format(i))
    # ESCAPE_DCT.setdefault(chr(i), '\\u%04x' % (i,))

INFINITY = float('inf')

NUMPY_TYPEMAP = {
    np.int8: 0x11,
    np.int16: 0x12,
    np.int32: 0x13,
    np.int64: 0x14,
    np.uint8: 0x19,
    np.uint16: 0x1A,
    np.uint32: 0x1B,
    np.uint64: 0x1C,
    np.float32: 0x21,
    np.float64: 0x22,
}


def _get_numpy_dtype(current_dtype):
    if np.issubdtype(current_dtype, np.int8):
        return np.int8
    elif np.issubdtype(current_dtype, np.int16):
        return np.int16
    elif np.issubdtype(current_dtype, np.int32):
        return np.int32
    elif np.issubdtype(current_dtype, np.int64):
        return np.int64
    elif np.issubdtype(current_dtype, np.uint8):
        return np.uint8
    elif np.issubdtype(current_dtype, np.uint16):
        return np.uint16
    elif np.issubdtype(current_dtype, np.uint32):
        return np.uint32
    elif np.issubdtype(current_dtype, np.uint64):
        return np.uint64
    elif np.issubdtype(current_dtype, np.float32):
        return np.float32
    elif np.issubdtype(current_dtype, np.float64):
        return np.float64
    else:
        raise ValueError(f'Unsupported dtype {current_dtype}for ' f'numpy array optimizaation')


def _check_if_byteorder_needs_to_change(dtype_: np.dtype):
    '''Check if we need to change the byteorder of a numpy array

    The wire format for numpy arrays is always in bigendian to ensure
    cross-platform compatibility. Hence, this check ensures that we switch the
    dtype of an ndarray only when the existing dtype does not have a byteorder
    defined or if the defined byteorder is little-endian.
    '''
    import sys

    if dtype_.byteorder == '<' or dtype_.byteorder == '|':
        return True
    if dtype_.byteorder == '=' and sys.byteorder == 'little':
        return True
    return False


def py_encode_basestring(s):
    """Return a bytearray JSON representation of a Python string"""

    def replace(match):
        return ESCAPE_DCT[match.group(0)]

    return str('"' + ESCAPE.sub(replace, s) + '"').encode('utf-8')


encode_basestring = py_encode_basestring


def py_encode_basestring_ascii(s):
    """Return an ASCII-only bytearray JSON representation of a Python string"""

    def replace(match):
        s = match.group(0)
        try:
            return ESCAPE_DCT[s]
        except KeyError:
            n = ord(s)
            if n < 0x10000:
                return '\\u{0:04x}'.format(n)
                # return '\\u%04x' % (n,)
            else:
                # surrogate pair
                n -= 0x10000
                s1 = 0xD800 | ((n >> 10) & 0x3FF)
                s2 = 0xDC00 | (n & 0x3FF)
                return '\\u{0:04x}\\u{1:04x}'.format(s1, s2)

    return str('"' + ESCAPE_ASCII.sub(replace, s) + '"').encode('utf-8')


encode_basestring_ascii = py_encode_basestring_ascii


class JSONEncoder:
    item_separator = b','
    key_separator = b':'

    def __init__(
        self,
        *,
        skipkeys=False,
        ensure_ascii=True,
        check_circular=True,
        allow_nan=True,
        sort_keys=False,
        separators=None,
        default=None,
    ):
        '''Constructor of JSON Encoder'''
        self.skipkeys = skipkeys
        self.ensure_ascii = ensure_ascii
        self.check_circular = check_circular
        self.allow_nan = allow_nan
        self.sort_keys = sort_keys
        if separators is not None:
            self.item_separator, self.key_separator = separators
        if default is not None:
            self.default = default

    def default(self, obj):
        raise TypeError(f'Object of type {type(obj)} is not JSON serializable')

    def encode(self, obj):
        '''Return a bytearray containing JSON representation of
        Python Data structure, with the vector extension
        '''
        # This is for extremely simple cases and benchmarks.
        if isinstance(obj, str):
            if self.ensure_ascii:
                return encode_basestring_ascii(obj)
            else:
                return encode_basestring(obj)

        chunks = self.iterencode(obj)
        if not isinstance(chunks, (list, tuple)):
            chunks = list(chunks)

        return b''.join(chunks)

    def iterencode(self, obj):
        '''Encode the given object and yield the bytearray representation
        as available
        '''
        if self.check_circular:
            markers = {}
        else:
            markers = None
        if self.ensure_ascii:
            _encoder = encode_basestring_ascii
        else:
            _encoder = encode_basestring

        def floatstr(
            o, allow_nan=self.allow_nan, _repr=float.__repr__, _inf=INFINITY, _neginf=-INFINITY
        ):
            # Check for specials.  Note that this type of test is processor
            # and/or platform-specific, so do tests which don't depend on the
            # internals.

            if o != o:
                text = b'NaN'
            elif o == _inf:
                text = b'Infinity'
            elif o == _neginf:
                text = b'-Infinity'
            else:
                return _repr(o).encode('utf-8')

            if not allow_nan:
                raise ValueError("Out of range float values are not JSON compliant: " + repr(o))

            return text

        def intstr(o, _repr=int.__repr__):
            return _repr(o).encode('utf-8')

        def vectorstr(o: np.ndarray, _map_dtype=NUMPY_TYPEMAP):
            dtype_: np.dtype = _get_numpy_dtype(o.dtype)
            value_type = _map_dtype.get(dtype_)
            buffer = b'<'
            buffer += int(o.size * o.itemsize).to_bytes(8, byteorder='big')
            buffer += _map_dtype.get(dtype_).to_bytes(1, byteorder='big')
            if _check_if_byteorder_needs_to_change(o.dtype):
                buffer += o.astype(o.dtype.newbyteorder('>')).tobytes()
            else:
                buffer += o.tobytes()
            buffer += b'>'
            return buffer

        _iterencode = _make_iterencode(
            markers,
            self.default,
            _encoder,
            floatstr,
            self.key_separator,
            self.item_separator,
            self.sort_keys,
            self.skipkeys,
            intstr,
            vectorstr,
        )
        return _iterencode(obj)


def _make_iterencode(
    markers,
    _default,
    _encoder,
    _floatstr,
    _key_separator,
    _item_separator,
    _sort_keys,
    _skipkeys,
    _intstr,
    _vectorstr,
):
    def _iterencode_list(lst):
        if not lst:
            yield b'[]'
            return
        if markers is not None:
            markerid = id(lst)
            if markerid in markers:
                raise ValueError("Circular reference detected")
            markers[markerid] = lst
        buf = bytearray()
        buf += b'['
        separator = _item_separator
        first = True
        for value in lst:
            if first:
                first = False
            else:
                buf = separator
            if isinstance(value, str):
                yield buf + _encoder(value)
            elif value is None:
                yield buf + b'null'
            elif value is True:
                yield buf + b'true'
            elif value is False:
                yield buf + b'false'
            elif isinstance(value, int):
                # Subclasses of int/float may override __repr__, but we still
                # want to encode them as integers/floats in JSON. One example
                # within the standard library is IntEnum.
                yield buf + _intstr(value)
            elif isinstance(value, float):
                # see comment above for int
                yield buf + _floatstr(value)
            else:
                yield buf
                if isinstance(value, (list, tuple)):
                    chunks = _iterencode_list(value)
                elif isinstance(value, dict):
                    chunks = _iterencode_dict(value)
                else:
                    chunks = _iterencode(value)
                yield from chunks
        yield b']'
        if markers is not None:
            del markers[markerid]

    def _iterencode_dict(dct):
        if not dct:
            yield b'{}'
            return
        if markers is not None:
            markerid = id(dct)
            if markerid in markers:
                raise ValueError("Circular reference detected")
            markers[markerid] = dct
        yield b'{'
        item_separator = _item_separator
        first = True
        if _sort_keys:
            items = sorted(dct.items())
        else:
            items = dct.items()
        for key, value in items:
            if isinstance(key, str):
                pass
            # JavaScript is weakly typed for these, so it makes sense to
            # also allow them.  Many encoders seem to do something like this.
            elif isinstance(key, float):
                # see comment for int/float in _make_iterencode
                key = _floatstr(key)
            elif key is True:
                key = b'true'
            elif key is False:
                key = b'false'
            elif key is None:
                key = b'null'
            elif isinstance(key, int):
                # see comment for int/float in _make_iterencode
                key = _intstr(key)
            elif _skipkeys:
                continue
            else:
                raise TypeError(
                    f'keys must be str, int, float, bool or None, ' f'not {key.__class__.__name__}'
                )
            if first:
                first = False
            else:
                yield item_separator
            yield _encoder(key)
            yield _key_separator
            if isinstance(value, str):
                yield _encoder(value)
            elif value is None:
                yield b'null'
            elif value is True:
                yield b'true'
            elif value is False:
                yield b'false'
            elif isinstance(value, int):
                # see comment for int/float in _make_iterencode
                yield _intstr(value)
            elif isinstance(value, float):
                # see comment for int/float in _make_iterencode
                yield _floatstr(value)
            else:
                if isinstance(value, (list, tuple)):
                    chunks = _iterencode_list(value)
                elif isinstance(value, dict):
                    chunks = _iterencode_dict(value)
                else:
                    chunks = _iterencode(value)
                yield from chunks
        yield b'}'
        if markers is not None:
            del markers[markerid]

    def _iterencode(o):
        if isinstance(o, str):
            yield _encoder(o)
        elif o is None:
            yield b'null'
        elif o is True:
            yield b'true'
        elif o is False:
            yield b'false'
        elif isinstance(o, int):
            # see comment for int/float in _make_iterencode
            yield _intstr(o)
        elif isinstance(o, float):
            # see comment for int/float in _make_iterencode
            yield _floatstr(o)
        elif isinstance(o, np.ndarray):
            yield _vectorstr(o)
        elif isinstance(o, (list, tuple)):
            yield from _iterencode_list(o)
        elif isinstance(o, dict):
            yield from _iterencode_dict(o)
        else:
            if markers is not None:
                markerid = id(o)
                if markerid in markers:
                    raise ValueError("Circular reference detected")
                markers[markerid] = o
            o = _default(o)
            yield from _iterencode(o)
            if markers is not None:
                del markers[markerid]

    return _iterencode
