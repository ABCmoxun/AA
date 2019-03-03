# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([[10, 20, 30],
              [40, 50, 60]])
print(a.shape, a.size, len(a))
b = a.reshape((6,))
print(b.shape, b.size, len(b))
c = b.reshape((3, 2))
print(c.shape, c.size, len(c))
d = np.arange(1, 25).reshape((2, 3, 4))
print(d.shape, d.size, len(d))
