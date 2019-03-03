# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([('123', [4, 5, 6])],
             dtype='U3, 3i4')
print(a[0]['f0'], a[0]['f1'])
b = np.array([('123', [4, 5, 6])],
             dtype=[('fa', np.str_, 3),
                    ('fb', np.int32, 3)])
print(b[0]['fa'], b[0]['fb'])
c = np.array([('123', [4, 5, 6])],
             dtype={'names': ['fa', 'fb'],
                    'formats': ['U3', '3i4']})
print(c[0]['fa'], c[0]['fb'], c.itemsize)
d = np.array([('123', [4, 5, 6])],
             dtype={'fa': ('U3', 0),
                    'fb': ('3i4', 16)})
print(d[0]['fa'], d[0]['fb'], d.itemsize)
e = np.array([0x1234],
             dtype=('>u2', {'lo': ('u1', 0),
                            'hi': ('u1', 1)}))
print('{:x}'.format(e[0]))
print('{:x} {:x}'.format(e['lo'][0], e['hi'][0]))
