__version__ = '1.0.0'

__all__ = ['loads', 'dumps', 'JSONEncoder', 'JSONDecoder', 'JSONDecodeError']

from .decoder import JSONDecodeError, JSONDecoder
from .encoder import JSONEncoder

_default_encoder = JSONEncoder(
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    separators=None,
    default=None,
)

_default_decoder = JSONDecoder(object_hook=None, object_pairs_hook=None)


def dumps(
    obj,
    *,
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    cls=None,
    separators=None,
    default=None,
    sort_keys=False,
    **kw,
):
    """Serialize an object to a JSON-formatted string.

    If ``skipkeys`` is ``True``, ``dict`` keys that are not basic types
    (``str``, ``int``, ``float``, ``bool``, and ``None``) are skipped
    instead of raising a ``TypeError``.

    If ``ensure_ascii`` is ``False``, the return value can contain non-ASCII
    characters if they appear in strings contained in the object. Otherwise, all
    such characters are escaped in JSON strings.

    If ``check_circular`` is ``False``, the circular reference check
    for container types is skipped and a circular reference
    results in an ``RecursionError`` (or worse).

    If ``allow_nan`` is ``False``, it is a ``ValueError`` to
    serialize out-of-range float values (``nan``, ``inf``, and ``-inf``) in
    strict compliance of the JSON specification, instead of using the
    JavaScript equivalents (``NaN``, ``Infinity``, and ``-Infinity``).

    If specified, ``separators`` should be an ``(item_separator, key_separator)``
    tuple. The default is ``(', ', ': ')`` if *indent* is ``None`` and
    ``(',', ': ')`` otherwise. To get the most compact JSON representation,
    you should specify ``(',', ':')`` to eliminate whitespace.

    ``default(obj)`` is a function that should return a serializable version
    of the object or raise a ``TypeError``. The default simply raises a
    ``TypeError``.

    If ``sort_keys`` is ``True`` rather than the default of ``False``, the
    output of the dictionaries are sorted by key.

    To use a custom ``JSONEncoder`` subclass (one that overrides the
    ``.default()`` method to serialize additional types), specify it with
    the ``cls`` kwarg. Otherwise ``JSONEncoder`` is used.

    """
    # cached encoder
    if (
        not skipkeys
        and ensure_ascii
        and check_circular
        and allow_nan
        and cls is None
        and separators is None
        and default is None
        and not sort_keys
        and not kw
    ):
        return _default_encoder.encode(obj)
    if cls is None:
        cls = JSONEncoder
    return cls(
        skipkeys=skipkeys,
        ensure_ascii=ensure_ascii,
        check_circular=check_circular,
        allow_nan=allow_nan,
        separators=separators,
        default=default,
        sort_keys=sort_keys,
        **kw,
    ).encode(obj)


def loads(
    s: bytes or bytearray,
    *,
    cls=None,
    object_hook=None,
    parse_int=None,
    parse_float=None,
    parse_constant=None,
    object_pairs_hook=None,
    **kw,
):
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
            **kw,
        )
    if not isinstance(s, (bytes, bytearray)):
        raise TypeError(
            f'the JSON object must be str, bytes or bytearray, ' f'not {s.__class__.__name__}'
        )

    if (
        cls is None
        and object_hook is None
        and parse_int is None
        and parse_float is None
        and parse_constant is None
        and object_pairs_hook is None
        and not kw
    ):
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
