# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([1, 2, 3, 4, 5])   # 被卷积序列
b = np.array([6, 7, 8])         # 卷积核序列
print(a, b)
c = np.convolve(a, b, 'full')   # 完全卷积
print(c)
d = np.convolve(a, b, 'same')   # 同维卷积
print(d)
e = np.convolve(a, b, 'valid')  # 有效卷积
print(e)
