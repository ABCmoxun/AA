# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([70, 80, 60, 30, 40])
print(a)
b = a - 60
print(b)
c = np.sign(b)
print(c)
d = np.piecewise(a, [a < 60, a == 60, a > 60],
                 [-1, 0, 1])
print(d)
