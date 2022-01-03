__version__ = '1.0.0'

__all__ = [
    'loads',
    'JSONDecoder', 'JSONDecodeError'
]

from .decoder import JSONDecoder, JSONDecodeError

_default_decoder = JSONDecoder(object_hook=None, object_pairs_hook=None)

def loads(
    s: bytes or bytearray, *,
    cls = None,
    object_hook = None,
    parse_int = None,
    parse_float = None,
    parse_constant = None,
    object_pairs_hook = None,
    **kw):
    if isinstance(s, str):
        import json
        return json.loads(
            s,
            cls=cls,
            object_hook=object_hook,
            parse_int=parse_int,
            parse_float=parse_float,
            parse_constant=parse_constant,
            object_pairs_hook=object_pairs_hook,
            **kw)
    if not isinstance(s, (bytes, bytearray)):
        raise TypeError(f'the JSON object must be str, bytes or bytearray, '
                        f'not {s.__class__.__name__}')
    
    if (cls is None and object_hook is None and
            parse_int is None and parse_float is None and
            parse_constant is None and object_pairs_hook is None and not kw):
        return _default_decoder.decode(s)
    if cls is None:
        cls = JSONDecoder
    if object_hook is not None:
        kw['object_hook'] = object_hook
    if object_pairs_hook is not None:
        kw['object_pairs_hook'] = object_pairs_hook
    if parse_float is not None:
        kw['parse_float'] = parse_float
    if parse_int is not None:
        kw['parse_int'] = parse_int
    if parse_constant is not None:
        kw['parse_constant'] = parse_constant
    return cls(**kw).decode(s)
