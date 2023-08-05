# -*- coding: utf-8 -*-

#    Copyright (C) 2015 Yahoo! Inc. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import six
from .. import wrapt
if six.PY3:
    import inspect
    Parameter = inspect.Parameter
    Signature = inspect.Signature
    get_signature = inspect.signature
else:
    # Provide an equivalent but use funcsigs instead...
    import funcsigs
    Parameter = funcsigs.Parameter
    Signature = funcsigs.Signature
    get_signature = funcsigs.signature

from . import _utils

_KWARG_UPDATED_POSTFIX_TPL = (', please update the code to explicitly set %s '
                              'as the value')
_KWARG_UPDATED_PREFIX_TPL = ('The %s argument is changing its default value '
                             'to %s')


def updated_kwarg_default_value(name, old_value, new_value, message=None,
                                version=None, stacklevel=3,
                                category=FutureWarning):

    """Decorates a kwarg accepting function to change the default value"""

    prefix = _KWARG_UPDATED_PREFIX_TPL % (name, new_value)
    postfix = _KWARG_UPDATED_POSTFIX_TPL % old_value
    out_message = _utils.generate_message(
        prefix, postfix=postfix, message=message, version=version)

    def decorator(f):
        sig = get_signature(f)
        varnames = list(six.iterkeys(sig.parameters))

        @wrapt.decorator
        def wrapper(wrapped, instance, args, kwargs):
            explicit_params = set(
                varnames[:len(args)] + list(kwargs.keys())
            )
            allparams = set(varnames)
            default_params = set(allparams - explicit_params)
            if name in default_params:
                _utils.deprecation(out_message,
                                   stacklevel=stacklevel, category=category)
            return wrapped(*args, **kwargs)

        return wrapper(f)

    return decorator
