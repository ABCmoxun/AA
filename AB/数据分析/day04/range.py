# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
dates, highest_prices, lowest_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(1, 4, 5), dtype='U10, f8, f8',
    unpack=True)
max_price = np.max(highest_prices)
min_price = np.min(lowest_prices)
print(min_price, '~', max_price)
max_index = np.argmax(highest_prices)
min_index = np.argmin(lowest_prices)
print(dates[min_index], dates[max_index])
highest_ptp = np.ptp(highest_prices)
lowest_ptp = np.ptp(lowest_prices)
print(lowest_ptp, highest_ptp)
