# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
# 产生9个介于[10, 100)区间的随机数
a = np.random.randint(10, 100, 9).reshape(3, 3)
print(a)
print(np.max(a), np.min(a), np.ptp(a))
print(np.argmax(a), np.argmin(a))
b = np.random.randint(10, 100, 9).reshape(3, 3)
print(b)
print(np.maximum(a, b), np.minimum(a, b), sep='\n')
