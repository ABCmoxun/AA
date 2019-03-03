# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def foo(x, y):
    return x + y, x - y, x * y


def hum(x):
    def fun(y):
        return x + y, x - y, x * y
    return np.frompyfunc(fun, 1, 1)


x, y = 1, 4
print(foo(x, y))
X, Y = np.array([1, 2, 3]), np.array([4, 5, 6])
bar = np.frompyfunc(foo, 2, 3)
print(bar(X, Y))
print(np.frompyfunc(foo, 2, 3)(X, Y))
print(hum(100)(X))
