# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
n = 1000
# 网格化
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(
    -x ** 2 - y ** 2)
mp.figure('Hot', facecolor='lightgray')
mp.title('Hot', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 绘制热成像图
mp.imshow(z, cmap='jet', origin='low')
mp.colorbar().set_label('z', fontsize=14)
mp.show()
