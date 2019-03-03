# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
apples = np.array([
    30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([
    24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])
mp.figure('Bar', facecolor='lightgray')
mp.title('Bar', fontsize=20)
mp.xlabel('Month', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
mp.ylim((0, 40))
x = np.arange(len(apples))
mp.bar(x, apples, 0.4, color='dodgerblue',
       label='Apple')
mp.bar(x + 0.3, oranges, 0.4, color='orangered',
       label='Orange', alpha=0.75)
mp.xticks(x + 0.1, [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
mp.legend()
mp.show()
