# -*- coding: utf-8 -*-

def ternary(a,b,c): return b if a else c

def sametype(a,b): return type(a) == type(b)

def new(a): return type(a)(a)

def strictSame(a,b):
    if type(a) != type(b): return False
    if dir(a) != dir(b): return False
    for key in dir(a):
        target = eval(f"a.{key}")
        ttype = str(type(target))
        if ttype.index("method") != -1 and ttype.index("function") != -1:
            continue
        else:
            if eval(f"a.{key}") != eval(f"b.{key}"):
                return False