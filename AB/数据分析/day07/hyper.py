# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
outcomes = np.random.hypergeometric(25, 1, 3, 100)
scores = [0]
for outcome in outcomes:
    if outcome == 3:
        scores.append(scores[-1] + 1)
    else:
        scores.append(scores[-1] - 6)
scores = np.array(scores)
mp.figure('Hypergeometric Distribution',
          facecolor='lightgray')
mp.title('Hypergeometric Distribution', fontsize=20)
mp.xlabel('Round', fontsize=14)
mp.ylabel('Score', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
o, h, l, c = 0, scores.argmax(), scores.argmin(), \
    scores.size - 1
if scores[o] < scores[c]:
    color = 'orangered'
elif scores[c] < scores[o]:
    color = 'limegreen'
else:
    color = 'dodgerblue'
mp.plot(scores, c=color, label='Score')
mp.axhline(y=scores[o], linestyle='--',
           color='deepskyblue', linewidth=1)
mp.axhline(y=scores[h], linestyle='--',
           color='crimson', linewidth=1)
mp.axhline(y=scores[l], linestyle='--',
           color='seagreen', linewidth=1)
mp.axhline(y=scores[c], linestyle='--',
           color='orange', linewidth=1)
mp.legend()
mp.show()
