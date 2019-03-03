# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd


dates, closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype='M8[D], f8', converters={1: dmy2ymd})
weights = np.exp(np.linspace(-1, 0, 5))
weights /= weights.sum()
ema5 = np.convolve(
    closing_prices, weights[::-1], 'valid')
weights = np.exp(np.linspace(-1, 0, 10))
weights /= weights.sum()
ema10 = np.convolve(
    closing_prices, weights[::-1], 'valid')
mp.figure('Exponential Moving Average',
          facecolor='lightgray')
mp.title('Exponential Moving Average', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
ax = mp.gca()
# 设置水平坐标每个星期一为主刻度
ax.xaxis.set_major_locator(md.WeekdayLocator(
    byweekday=md.MO))
# 设置水平坐标每一天为次刻度
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置水平坐标主刻度标签格式
ax.xaxis.set_major_formatter(md.DateFormatter(
    '%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, c='lightgray',
        label='Closing Price')
mp.plot(dates[4:], ema5, c='orangered',
        label='EMA-5')
mp.plot(dates[9:], ema10, c='dodgerblue',
        label='EMA-10')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
