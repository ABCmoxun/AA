# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 10)
print(a, type(a[0]), a.dtype)
b = a.astype(float)
print(b, type(b[0]), b.dtype)
c = b.astype(str)
print(c, type(c[0]), c.dtype)
