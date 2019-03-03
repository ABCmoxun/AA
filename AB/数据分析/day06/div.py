# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([5, 5, -5, -5])
b = np.array([2, -2, 2, -2])
print(a, b)
# c = np.true_divide(a, b)
# c = np.divide(a, b)
c = a / b
print(c)
# d = np.floor_divide(a, b)
d = a // b
print(d)
e = np.ceil(a / b).astype(int)
print(e)
f = np.trunc(a / b).astype(int)
print(f)
