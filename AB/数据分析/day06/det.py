# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
A = np.mat('2 1; 3 4')
print(A)
print(np.linalg.det(A))
B = np.mat('3 2 1; 4 9 8; 5 6 7')
print(B)
print(np.linalg.det(B))
