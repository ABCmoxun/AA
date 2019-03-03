# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([10, 20, 30, 40, 50])
print(a)
b = a.clip(min=15, max=45)
print(b)
c = a.compress((15 <= a) & (a <= 45))
print(c)
d = a.prod()
print(d)
e = a.cumprod()
print(e)


def jiecheng(n):
    return n if n == 1 else n * jiecheng(n - 1)

n = 5
print(jiecheng(n))
jc = 1
for i in range(2, n + 1):
    jc *= i
print(jc)
print(np.arange(2, n + 1).prod())
