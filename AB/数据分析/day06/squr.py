# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp


def squarewave(n):
    k = np.arange(1, n + 1)

    def fun(x):
        return np.sum(4 / ((2 * k - 1) * np.pi) *
                      np.sin((2 * k - 1) * x))

    return np.frompyfunc(fun, 1, 1)


x = np.linspace(0, 2 * np.pi, 201)
y1 = squarewave(1)(x)
y2 = squarewave(2)(x)
y3 = squarewave(3)(x)
y4 = squarewave(10)(x)
y5 = squarewave(100)(x)
y6 = squarewave(1000)(x)
mp.figure('Squarewave', facecolor='lightgray')
mp.title('Squarewave', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y1, label='n=1')
mp.plot(x, y2, label='n=2')
mp.plot(x, y3, label='n=3')
mp.plot(x, y4, label='n=10')
mp.plot(x, y5, label='n=100')
mp.plot(x, y6, label='n=1000')
mp.legend()
mp.show()
