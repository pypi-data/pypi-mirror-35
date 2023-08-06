# -*- coding: utf-8 -*-

from .operation import *
from . import advnum

# define infinity and nan
infinity = advnum._infinity(1)
nan = advnum._infinity(0)
inf = advnum._infinity(1)
minf = advnum._infinity(-1)
infi = advnum._infinity(1)
minusinfinity = advnum._infinity(-1)
Infinity = advnum._infinity(1)
MinusInfinity = advnum._infinity(-1)
NaN = advnum._infinity(0)

# define others
none = type(None)()
null = type(None)()
Null = type(None)()