# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
y = np.array([1, 10, 100, 1000, 100, 10, 1])
mp.figure('Normal & Log', facecolor='lightgray')
mp.subplot(211)
mp.title('Normal', fontsize=20)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
mp.tick_params(labelsize=10)
ax.grid(which='major', axis='both', linewidth=0.75,
        linestyle='-', color='orange')
ax.grid(which='minor', axis='both', linewidth=0.25,
        linestyle='-', color='orange')
mp.plot(y, 'o-', c='dodgerblue', label='plot')
mp.legend()
mp.subplot(212)
mp.title('Log', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
mp.tick_params(labelsize=10)
ax.grid(which='major', axis='both', linewidth=0.75,
        linestyle='-', color='orange')
ax.grid(which='minor', axis='both', linewidth=0.25,
        linestyle='-', color='orange')
mp.semilogy(y, 'o-', c='dodgerblue', label='semilogy')
mp.legend()
mp.tight_layout()
mp.show()
