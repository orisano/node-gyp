# coding: utf-8
import sys

try:
    import typing as _t
except ImportError:
    pass

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    string_types = basestring
    text_type = unicode
    binary_type = str

    def iteritems(d):  # type: (_t.Dict[_t._KT, _t._VT]) -> _t.Iterable[_t.Tuple[_t._KT, _t._VT]]
        return d.iteritems()
else:
    string_types = str
    text_type = str
    binary_type = bytes

    def iteritems(d):  # type: (_t.Dict[_t._KT, _t._VT]) -> _t.Iterable[_t.Tuple[_t._KT, _t._VT]]
        return iter(d.items())