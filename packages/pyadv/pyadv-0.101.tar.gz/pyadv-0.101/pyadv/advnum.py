# -*- coding: utf-8 -*-

from . import operation

class _infinity:

    def __init__(self,inftype=1):
        if type(inftype) == int:
            if inftype > 0:
                self.type = "Infinity"
            elif inftype < 0:
                self.type = "-Infinity"
            else:
                self.type = "NaN"
        elif type(inftype) == str:
            if inftype in ["Infinity","-Infinity"]:
                self.type = inftype
            else: self.type = "NaN"

    # Emulating Numeric Types
    # called when inf is self

    def __add__(self,other):
        if operation.sametype(self,other):
            if other.type == "NaN": return _infinity(0)
            else:
                if self != other: return _infinity(0)
                return operation.new(self)
        else: return operation.new(self)

    def __sub__(self,other):
        if operation.sametype(self,other):
            if other.type == "NaN": return _infinity(0)
            else:
                if self == other: return _infinity(0)
                return operation.new(self)
        else: return operation.new(self)

    def __mul__(self,other):
        if operation.sametype(self,other):
            if other.type == "NaN": return _infinity(0)
        if other < 0 and self.type != "NaN":
            if self.type == "Infinity": return _infinity(-1)
            else: return _infinity(1)
        return operation.new(self)

    def __truediv__(self,other):
        if operation.sametype(self,other):
            if other.type == "NaN": return _infinity(0)
        if other < 0 and self.type != "NaN":
            if self.type == "Infinity": return _infinity(-1)
            else: return _infinity(1)
        return operation.new(self)

    def __floordiv__(self,other):
        if operation.sametype(self,other):
            if other.type == "NaN": return _infinity(0)
        if other < 0 and self.type != "NaN":
            if self.type == "Infinity": return _infinity(-1)
            else: return _infinity(1)
        return operation.new(self)

    def __mod__(self,other):
        return _infinity(0)

    def __divmod__(self,other):
        return (self // other, self % other)

    def __pow__(self,other):
        if self.type == "-Infinity":
            if other%2: _infinity(1)
        else: return operation.new(self)

    def __lshift__(self,other):
        return operation.new(self)

    def __rshift__(self,other):
        return operation.new(self)

    def __and__(self,other):
        if self.type == "NaN": return _infinity(0)
        else: return new(other)

    def __xor__(self,other):
        if self.type == "NaN": return _infinity(0)
        else: int("{0:b}".format(other).replace("1","t").replace("0","1").replace("t","0"),2)

    def __or__(self,other):
        if self.type == "NaN": return _infinity(0)
        else: return _infinity(1)

    # Emulating Numeric Types
    # called when inf is other

    def __radd__(self,other):
        if operation.sametype(self,other):
            if other.type == "NaN": return _infinity(0)
            else:
                if self != other: return _infinity(0)
                return operation.new(self)
        else: return operation.new(self)

    def __rsub__(self,other):
        if operation.sametype(self,other):
            if other.type == "NaN": return _infinity(0)
            else:
                if self == other: return _infinity(0)
                return operation.new(self)
        else: return operation.new(self)

    def __rmul__(self,other):
        if operation.sametype(self,other):
            if other.type == "NaN": return _infinity(0)
        if other < 0 and self.type != "NaN":
            if self.type == "Infinity": return _infinity(-1)
            else: return _infinity(1)
        return operation.new(self)

    def __rtruediv__(self,other):
        if self.type == "NaN": return _infinity(0)
        else: return 0

    def __rfloordiv__(self,other):
        if self.type == "NaN": return _infinity(0)
        else: return 0

    def __rmod__(self,other):
        if self.type == "NaN": return _infinity(0)
        else: return 0

    def __rpow__(self,other):
        if self.type == "NaN": return _infinity(0)
        elif other == 1: return 1
        else:
            if self.type == "Infinity":
                if other < 1: return 0
                return _infinity(1)
            else:
                if other < 1: return _infinity(1)
                return 0

    def __rlshift__(self,other):
        if self.type == "NaN": return _infinity(0)
        return 0

    def __rrshift__(self,other):
        if self.type == "NaN": return _infinity(0)
        return 0

    def __rand__(self,other):
        if self.type == "NaN": return _infinity(0)
        else: return new(other)

    def __rxor__(self,other):
        if self.type == "NaN": return _infinity(0)
        else: int("{0:b}".format(other).replace("1","t").replace("0","1").replace("t","0"),2)

    def __ror__(self,other):
        if self.type == "NaN": return _infinity(0)
        else: return _infinity(1)

    # Emulating Numeric Types
    # others

    def __neg__(self):
        if self.type == "NaN": return _infinity(0)
        elif self.type == "Infinity": return _infinity(-1)
        else: return _infinity(1)

    def __pos__(self):
        return operation.new(self)

    def __abs__(self):
        if self.type == "NaN": return _infinity(0)
        else: return _infinity(1)

    def __invert__(self):
        if self.type == "NaN": return _infinity(0)
        elif self.type == "Infinity": return _infinity(-1)
        else: return _infinity(1)

    def __int__(self):
        return operation.new(self)

    def __float__(self):
        return operation.new(self)

    def __index__(self):
        return operation.new(self)

    def __round__(self,):
        return operation.new(self)

    def __trunc__(self):
        return operation.new(self)

    def __floor__(self):
        return operation.new(self)

    def __ceil__(self):
        return operation.new(self)

    # Compare

    def __lt__(self,other):
        if self.type == "NaN": return False
        return (self.type == "-Infinity" and self != other)

    def __gt__(self,other):
        if self.type == "NaN": return False
        return (self.type == "Infinity" and self != other)

    def __le__(self,other):
        if self.type == "NaN": return False
        return (self.type == "-Infinity")

    def __ge__(self,other):
        if self.type == "NaN": return False
        return (self.type == "Infinity")

    def __eq__(self,other):
        if operation.sametype(self,other):
            if self.type != "NaN" and other.type != "NaN":
                return self.type == other.type
        return False

    def __ne__(self,other):
        if operation.sametype(self,other):
            if self.type != "NaN" and other.type != "NaN":
                return self.type != other.type
        return True

    # Others

    def __repr__(self):
        return self.type

    def __str__(self):
        return self.type

    def __bool__(self):
        if self.type == "NaN":
            return False
        return True

    def __hash__(self):
        return hash((self.type))