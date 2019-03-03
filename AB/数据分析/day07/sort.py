# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
ages = np.array([30, 20, 30, 20])
scores = np.array([70, 60, 80, 70])
names = np.array(['zhangsan', 'lisi',
                  'wangwu', 'zhaoliu'])
# 按照成绩的升序打印姓名，成
# 绩相同的按照年龄的升序排列
print(np.take(names, np.lexsort((ages, scores))))
compleies = scores + ages * 1j
print(compleies)
sorted_compleies = np.sort_complex(compleies)
print(sorted_compleies)
#             0  1  2  3  4  5  6
a = np.array([1, 2, 4, 5, 6, 8, 9])
b = np.array([7, 3])
c = np.searchsorted(a, b)
print(c)
d = np.insert(a, c, b)
print(d)
