# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
samples = np.random.normal(size=10000)
mp.figure('Normal Distribution',
          facecolor='lightgray')
mp.title('Normal Distribution', fontsize=20)
mp.xlabel('Sample', fontsize=14)
mp.ylabel('Occurrence', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(axis='y', linestyle=':')
bins = mp.hist(samples, 100, normed=True,
               edgecolor='steelblue',
               facecolor='deepskyblue',
               label='Normal')[1]
probs = np.exp(-bins ** 2 / 2) / np.sqrt(2 * np.pi)
mp.plot(bins, probs, 'o-', c='orangered',
        label='Probability')
mp.legend()
mp.show()
