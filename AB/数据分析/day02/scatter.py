# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
n = 1000  # 1000个样本
x = np.random.normal(0, 1, n)  # 标准正态分布
y = np.random.normal(0, 1, n)  # 标准正态分布
d = np.sqrt(x ** 2 + y ** 2)
mp.figure('Scatter', facecolor='lightgray')
mp.title('Scatter', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# jet_r: 从深红到深蓝的渐变颜色表
mp.scatter(x, y, c=d, cmap='jet_r', s=60, alpha=0.5)
mp.show()
