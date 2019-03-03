# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([0, -1, 2, -3, 4, -5])
b = np.array([0, 1, 2, 3, 4, 5])
print(a, b)
# c = a ^ b
# c = a.__xor__(b)
c = np.bitwise_xor(a, b)
print(np.where(c < 0)[0])
d = np.arange(1, 21)
print(d)
# e = d & (d - 1)
# e = d.__and__(d - 1)
e = np.bitwise_and(d, d - 1)
print(e)
print(d[e == 0])
# f = d << 1
# f = d.__lshift__(1)
f = np.left_shift(d, 1)
print(f)
# g = d >> 1
# g = d.__rshift__(1)
g = np.right_shift(d, 1)
print(g)
