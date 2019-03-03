# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def foo(arg):
    print('foo:', arg)
    return arg.sum()


a = np.arange(1, 10).reshape(3, 3)
print(a)
b = np.apply_along_axis(foo, 0, a)
print(b)
c = np.apply_along_axis(foo, 1, a)
print(c)
