# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 7)
print(a)
b = a + a
print(b)
b = np.add(a, a)
print(b)
c = np.add.reduce(a)
print(c)
d = np.add.accumulate(a)
print(d)
# 0   2   4
# 1 2 3 4 5 6
e = np.add.reduceat(a, [0, 2, 4])
print(e)
#  +  1  2  3  4  5  6
# 10 11 12 13 14 15 16
# 20 21 22 23 24 25 26
# 30 31 32 33 34 35 36
f = np.add.outer([10, 20, 30], a)
print(f)
#  x  1  2  3   4   5   6
# 10 10 20 30  40  50  60
# 20 20 40 60  80 100 120
# 30 30 60 90 120 150 180
g = np.outer([10, 20, 30], a)
print(g)
