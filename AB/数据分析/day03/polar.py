# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
t = np.linspace(0, 2 * np.pi, 1001)
r_spiral = 0.8 * t  # 阿基米德螺旋线
r_rose = 5 * np.sin(6 * t)  # 六元玫瑰线
mp.figure('Polar', facecolor='lightgray')
mp.gca(projection='polar')  # 设置极坐标系
mp.title('Polar', fontsize=20)
mp.xlabel(r'$\theta$', fontsize=14)
mp.ylabel(r'$\rho$', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 函数值   = f (自变量)
# 垂直坐标 = f (水平坐标)
# 极径     = f (极角)
mp.plot(t, r_spiral, c='dodgerblue',
        label=r'$\rho=0.8\theta$')
mp.plot(t, r_rose, c='orangered',
        label=r'$\rho=5sin(6\theta)$')
mp.legend()
mp.show()
