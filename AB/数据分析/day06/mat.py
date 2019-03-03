# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([
    [1, 2, 6],
    [3, 5, 7],
    [4, 8, 9]])
print(a, type(a))
b = np.matrix(a)
print(b, type(b))
b += 10
print(b)
print(a)
c = np.matrix(a, copy=False)
print(c, type(c))
c += 10
print(c)
print(a)
d = np.mat(a)
print(d, type(d))
d -= 10
print(d)
print(a)
e = np.mat('1 2 6; 3 5 7; 4 8 9')
print(e)
f = np.bmat('b e')
print(f)
g = np.bmat('b e; e b')
print(g)
#
# 多维数组的乘法：对应位置的元素相乘
#
# 1  2  6   1  2  6    1  4 36
# 3  5  7 X 3  5  7 =  9 25 49
# 4  8  9   4  8  9   16 64 81
#
h = a * a
print(h)
#
# 矩阵的乘法：乘积矩阵的第i行第j列的元素等于
# 被乘数矩阵的第i行与乘数矩阵的第j列的点积
#
#          1   2   6
#    X---->3   5   7
#    |     4   8   9
# 1  2  6 31  60  74
# 3  5  7 46  87 116
# 4  8  9 64 120 161
#
i = e * e
print(i)
j = e.I
print(j)
print(e * j)
# a.I
k = a.dot(a)
print(k)
l = np.linalg.inv(a)
print(l)
