# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma
mp.figure('Signal', facecolor='lightgray')
mp.title('Signal', fontsize=20)
mp.xlabel('Time', fontsize=14)
mp.ylabel('Signal', fontsize=14)
ax = mp.gca()
ax.set_ylim(-3, 3)
ax.set_xlim(0, 10)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 创建曲线对象
pl = mp.plot([], [], c='orangered')[0]
# 在曲线对象内部创建缓冲区，以容纳曲线上点的横纵坐标
pl.set_data([], [])


# 更新回调函数
def update(data):
    t, v = data
    # 获取曲线上当前所有的点
    x, y = pl.get_data()
    # 追加新采集到的点
    x.append(t)
    y.append(v)
    # 获取当前水平坐标范围
    x_min, x_max = ax.get_xlim()
    # 如果新点的水平坐标超过水平坐标范围
    if t >= x_max:
        # 重新设置水平坐标范围
        ax.set_xlim(t - (x_max - x_min), t)
        # 重新绘制坐标轴
        ax.figure.canvas.draw()
    # 设置曲线上的点
    pl.set_data(x, y)


# 生成器函数
def generator():
    t = 0
    while True:
        v = np.sin(2 * np.pi * t) * np.exp(
            np.sin(0.2 * np.pi * t))
        yield t, v
        t += 0.05


# 启动动画
anim = ma.FuncAnimation(
    mp.gcf(), update, generator, interval=5)
mp.show()
