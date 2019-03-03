# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(11, 20).reshape(3, 3)
print(a)
b = a + 10
print(b)
c = np.vstack((a, b))
print(c)
d = np.concatenate((a, b), axis=0)
print(d)
e, f = np.vsplit(c, 2)
print(e, f, sep='\n')
g, h = np.split(d, 2, axis=0)
print(g, h, sep='\n')
i = np.hstack((a, b))
print(i)
j = np.concatenate((a, b), axis=1)
print(j)
k, l = np.hsplit(i, 2)
print(k, l, sep='\n')
m, n = np.split(i, 2, axis=1)
print(m, n, sep='\n')
o = np.dstack((a, b))
print(o)
p, q = np.dsplit(o, 2)
print(p.T[0].T, q.T[0].T, sep='\n')
a, b = a.ravel(), b.ravel()
print(a, b)
#r = np.vstack((a, b))
r = np.row_stack((a, b))
print(r)
#s = np.hstack((a, b))
s = np.column_stack((a, b))
print(s)
