# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 3)
print(a, a.shape)
b = np.array([[1, 2., '3'],
              [4, 5, 6]])
print(b, b.shape)
c = np.array([np.arange(1, 4),
              np.arange(4, 7),
              np.arange(7, 10)])
print(c, c.shape)
