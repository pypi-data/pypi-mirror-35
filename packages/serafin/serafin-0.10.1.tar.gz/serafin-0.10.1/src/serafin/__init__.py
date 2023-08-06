# -*- coding: utf-8 -*-
"""

**serafin** is a serialization system that allows flexible serialization
of any type of object according to a provided field spec. The field spec tells
the serialize which attribute/fields/members of the given object should be
serialized. This allows for a very flexible serialization system, especially in
the context of API endpoints where we can write one endpoint and allow client
to pass the field spec describing how he wants the output to be formatted.


.. autoclass:: serafin.core.Priority
    :members:


.. autoclass:: serafin.core.Serializer
    :members:


.. autofunction:: serafin.core.serialize

"""
from __future__ import absolute_import, unicode_literals
from .core.context import Context
from .core.fieldspec import Fieldspec
from .core.serializer import serialize
from .core.serializers import *     # pylint: disable=wildcard-import
__version__ = '0.10.1'


__all__ = [
    'Context',
    'Fieldspec',
    'serialize',
]
