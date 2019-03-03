# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([5, 5, -5, -5])
b = np.array([2, -2, 2, -2])
print(a, b)
# c = np.remainder(a, b)
# c = np.mod(a, b)
c = a % b
print(c)
d = np.fmod(a, b)
print(d)
