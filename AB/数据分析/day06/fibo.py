# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
n = 35


def fibo(n):
    return 1 if n < 3 else fibo(n - 1) + fibo(n - 2)


print(fibo(n))
fn_1, fn_2 = 0, 1
for i in range(n):
    fn = fn_1 + fn_2
    fn_1, fn_2 = fn, fn_1
print(fn)
print(int((np.mat('1. 1.; 1. 0.') ** (n - 1))[0, 0]))
r = np.sqrt(5)
print(int((((1 + r) / 2) ** n -
           ((1 - r) / 2) ** n) / r))
