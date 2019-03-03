# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.mat('1 -2 1; 0 2 -8; -4 5 9')
b = np.mat('0; 8; -9')
x = np.linalg.solve(a, b)
print(x)
x = np.linalg.lstsq(a, b)[0]
print(x)
