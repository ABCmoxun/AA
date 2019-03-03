# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
# 创建图形窗口
mp.figure('Locator')
# 刻度定位器列表
locators = [
    # 空定位器：不绘制刻度
    'mp.NullLocator()',
    # 最大值定位器：最多绘制nbins个刻度，
    # 每两个刻度之间的间隔从steps列表中选择
    'mp.MaxNLocator(nbins=3, steps=[1, 3, 5, 7, 9])',
    # 定点定位器：根据locs参数中的位置绘制刻度
    'mp.FixedLocator(locs=[0, 2.5, 5, 7.5, 10])',
    # 自动定位器：由系统自动选择刻度的绘制位置
    'mp.AutoLocator()',
    # 索引定位器：由offset确定起始刻
    # 度，由base确定相邻刻度的间隔
    'mp.IndexLocator(offset=0.5, base=1.5)',
    # 多点定位器：从0开始，按照参
    # 数指定的间隔(缺省1)绘制刻度
    'mp.MultipleLocator()',
    # 线性定位器：等分numticks-1
    # 份，绘制numticks个刻度
    'mp.LinearLocator(numticks=21)',
    # 对数定位器：以base为底，用subs
    # 中的元素作为指数增量，绘制刻度
    'mp.LogLocator(base=2, subs=[1.0])']
# 刻度定位器数
n_locators = len(locators)
# 遍历刻度定位器列表
for i, locator in enumerate(locators):
        # 为每个刻度定位器创建一个子图
    mp.subplot(n_locators, 1, i + 1)
    # 设置坐标范围
    mp.xlim(0, 10)
    mp.ylim(-1, 1)
    # 关闭垂直坐标轴刻度
    mp.yticks(())
    # 获取当前坐标轴
    ax = mp.gca()
    # 隐藏除底轴以外的所有坐标轴
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # 将底坐标轴调整到子图中心位置
    ax.spines['bottom'].set_position(('data', 0))
    # 设置水平坐标轴的主刻度定位器
    ax.xaxis.set_major_locator(eval(locator))
    # 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
    # 绘制一条与水平坐标轴重合的直线，无色透明
    mp.plot(np.arange(11), np.zeros(11), c='none')
    # 标记所用刻度定位器类名
    mp.text(5, 0.3, locator[3:], ha='center',
            size=12)
# 紧凑布局
mp.tight_layout()
# 显示图形
mp.show()
