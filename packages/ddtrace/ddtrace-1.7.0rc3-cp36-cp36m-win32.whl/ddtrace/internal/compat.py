from inspect import isgeneratorfunction
import platform
import random
import re
import sys
import textwrap
import threading
from types import BuiltinFunctionType
from types import BuiltinMethodType
from types import FunctionType
from types import MethodType
from types import TracebackType
from typing import Any
from typing import AnyStr
from typing import Optional
from typing import Text
from typing import Tuple
from typing import Type
from typing import Union

import six

from ddtrace.vendor.wrapt.wrappers import BoundFunctionWrapper
from ddtrace.vendor.wrapt.wrappers import FunctionWrapper


__all__ = [
    "httplib",
    "iteritems",
    "PY2",
    "Queue",
    "stringify",
    "StringIO",
    "urlencode",
    "parse",
    "reraise",
    "maybe_stringify",
]

PYTHON_VERSION_INFO = sys.version_info
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if not PY2:
    long = int

# Infos about python passed to the trace agent through the header
PYTHON_VERSION = platform.python_version()
PYTHON_INTERPRETER = platform.python_implementation()

try:
    StringIO = six.moves.cStringIO
except ImportError:
    StringIO = six.StringIO  # type: ignore[misc]

httplib = six.moves.http_client
urlencode = six.moves.urllib.parse.urlencode
parse = six.moves.urllib.parse
Queue = six.moves.queue.Queue
iteritems = six.iteritems
reraise = six.reraise
reload_module = six.moves.reload_module

ensure_text = six.ensure_text
ensure_str = six.ensure_str
stringify = six.text_type
string_type = six.string_types[0]
text_type = six.text_type
binary_type = six.binary_type
msgpack_type = six.binary_type
# DEV: `six` doesn't have `float` in `integer_types`
numeric_types = six.integer_types + (float,)

# `six.integer_types` cannot be used for typing as we need to define a type
# alias for
# see https://mypy.readthedocs.io/en/latest/common_issues.html#variables-vs-type-aliases
if PY3:
    NumericType = Union[int, float]
else:
    NumericType = Union[long, int, float]  # noqa: F821

# Pattern class generated by `re.compile`
if PYTHON_VERSION_INFO >= (3, 7):
    pattern_type = re.Pattern
else:
    pattern_type = re._pattern_type  # type: ignore[misc,attr-defined]

try:
    from inspect import getargspec as getfullargspec

    def is_not_void_function(f, argspec):
        return argspec.args or argspec.varargs or argspec.keywords or argspec.defaults or isgeneratorfunction(f)


except ImportError:
    from inspect import getfullargspec  # type: ignore[assignment]  # noqa: F401

    def is_not_void_function(f, argspec):
        return (
            argspec.args
            or argspec.varargs
            or argspec.varkw
            or argspec.defaults
            or argspec.kwonlyargs
            or argspec.kwonlydefaults
            or isgeneratorfunction(f)
        )


def is_integer(obj):
    # type: (Any) -> bool
    """Helper to determine if the provided ``obj`` is an integer type or not"""
    # DEV: We have to make sure it is an integer and not a boolean
    # >>> type(True)
    # <class 'bool'>
    # >>> isinstance(True, int)
    # True
    return isinstance(obj, six.integer_types) and not isinstance(obj, bool)


try:
    from time import time_ns
except ImportError:
    from time import time as _time

    def time_ns():
        # type: () -> int
        return int(_time() * 10e5) * 1000


try:
    from time import monotonic
except ImportError:
    from ddtrace.vendor.monotonic import monotonic


try:
    from time import monotonic_ns
except ImportError:

    def monotonic_ns():
        # type: () -> int
        return int(monotonic() * 1e9)


try:
    from time import process_time_ns
except ImportError:
    from time import clock as _process_time  # type: ignore[attr-defined]

    def process_time_ns():
        # type: () -> int
        return int(_process_time() * 1e9)


if sys.version_info.major < 3:
    getrandbits = random.SystemRandom().getrandbits
else:
    # Use a wrapper that allows passing k as a kwargs like in Python 2
    def getrandbits(k):
        return random.getrandbits(k)


if sys.version_info.major < 3:
    if isinstance(threading.current_thread(), threading._MainThread):  # type: ignore[attr-defined]
        main_thread = threading.current_thread()
    else:
        main_thread = threading._shutdown.im_self  # type: ignore[attr-defined]
else:
    main_thread = threading.main_thread()


if PYTHON_VERSION_INFO[0:2] >= (3, 5):
    from asyncio import iscoroutinefunction

    # Execute from a string to get around syntax errors from `yield from`
    # DEV: The idea to do this was stolen from `six`
    #   https://github.com/benjaminp/six/blob/15e31431af97e5e64b80af0a3f598d382bcdd49a/six.py#L719-L737
    six.exec_(
        textwrap.dedent(
            """
    import functools
    import asyncio


    def make_async_decorator(tracer, coro, *params, **kw_params):
        \"\"\"
        Decorator factory that creates an asynchronous wrapper that yields
        a coroutine result. This factory is required to handle Python 2
        compatibilities.

        :param object tracer: the tracer instance that is used
        :param function f: the coroutine that must be executed
        :param tuple params: arguments given to the Tracer.trace()
        :param dict kw_params: keyword arguments given to the Tracer.trace()
        \"\"\"
        @functools.wraps(coro)
        async def func_wrapper(*args, **kwargs):
            with tracer.trace(*params, **kw_params):
                result = await coro(*args, **kwargs)
                return result

        return func_wrapper
    """
        )
    )
else:
    # asyncio is missing so we can't have coroutines; these
    # functions are used only to ensure code executions in case
    # of an unexpected behavior
    def iscoroutinefunction(fn):  # type: ignore
        return False

    def make_async_decorator(tracer, fn, *params, **kw_params):
        return fn


# DEV: There is `six.u()` which does something similar, but doesn't have the guard around `hasattr(s, 'decode')`
def to_unicode(s):
    # type: (AnyStr) -> Text
    """Return a unicode string for the given bytes or string instance."""
    # No reason to decode if we already have the unicode compatible object we expect
    # DEV: `six.text_type` will be a `str` for python 3 and `unicode` for python 2
    # DEV: Double decoding a `unicode` can cause a `UnicodeEncodeError`
    #   e.g. `'\xc3\xbf'.decode('utf-8').decode('utf-8')`
    if isinstance(s, six.text_type):
        return s

    # If the object has a `decode` method, then decode into `utf-8`
    #   e.g. Python 2 `str`, Python 2/3 `bytearray`, etc
    if hasattr(s, "decode"):
        return s.decode("utf-8")

    # Always try to coerce the object into the `six.text_type` object we expect
    #   e.g. `to_unicode(1)`, `to_unicode(dict(key='value'))`
    return six.text_type(s)


def get_connection_response(
    conn,  # type: httplib.HTTPConnection
):
    # type: (...) -> httplib.HTTPResponse
    """Returns the response for a connection.

    If using Python 2 enable buffering.

    Python 2 does not enable buffering by default resulting in many recv
    syscalls.

    See:
    https://bugs.python.org/issue4879
    https://github.com/python/cpython/commit/3c43fcba8b67ea0cec4a443c755ce5f25990a6cf
    """
    if PY2:
        return conn.getresponse(buffering=True)
    else:
        return conn.getresponse()


try:
    import contextvars  # noqa
except ImportError:
    from ddtrace.vendor import contextvars  # type: ignore  # noqa

    CONTEXTVARS_IS_AVAILABLE = False
else:
    CONTEXTVARS_IS_AVAILABLE = True


def maybe_stringify(obj):
    # type: (Any) -> Optional[str]
    if obj is not None:
        return stringify(obj)
    return None


NoneType = type(None)

BUILTIN_SIMPLE_TYPES = frozenset([int, float, str, bytes, bool, NoneType, type, long])
BUILTIN_CONTAINER_TYPES = frozenset([list, tuple, dict, set])
BUILTIN_TYPES = BUILTIN_SIMPLE_TYPES | BUILTIN_CONTAINER_TYPES


try:
    from types import MethodWrapperType

except ImportError:
    MethodWrapperType = object().__init__.__class__  # type: ignore[misc]

CALLABLE_TYPES = (
    BuiltinMethodType,
    BuiltinFunctionType,
    FunctionType,
    MethodType,
    MethodWrapperType,
    FunctionWrapper,
    BoundFunctionWrapper,
    property,
    classmethod,
    staticmethod,
)
BUILTIN = "__builtin__" if PY2 else "builtins"


try:
    from typing import Collection
except ImportError:
    from typing import List
    from typing import Set
    from typing import Union

    Collection = Union[List, Set, Tuple]  # type: ignore[misc,assignment]

ExcInfoType = Union[Tuple[Type[BaseException], BaseException, Optional[TracebackType]], Tuple[None, None, None]]
