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
medios = np.convolve(
    closing_prices, weights[::-1], 'valid')
stds = np.zeros(medios.size)
for i in range(stds.size):
    stds[i] = closing_prices[i:i + 5].std()
stds *= 2
lowers = medios - stds
uppers = medios + stds
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
mp.plot(dates[4:], medios, c='dodgerblue',
        label='Medio')
mp.plot(dates[4:], lowers, c='limegreen',
        label='Lower')
mp.plot(dates[4:], uppers, c='orangered',
        label='Upper')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
