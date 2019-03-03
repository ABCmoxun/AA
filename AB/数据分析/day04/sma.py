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
sma51 = np.zeros(closing_prices.size - 4)
for i in range(sma51.size):
    sma51[i] = closing_prices[i:i + 5].mean()
sma52 = np.convolve(
    closing_prices, np.ones(5) / 5, 'valid')
sma10 = np.convolve(
    closing_prices, np.ones(10) / 10, 'valid')
mp.figure('Simple Moving Average',
          facecolor='lightgray')
mp.title('Simple Moving Average', fontsize=20)
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
mp.plot(dates[4:], sma51, c='orangered',
        label='SMA-5(1)')
mp.plot(dates[4:], sma52, c='limegreen', alpha=0.5,
        linewidth=6, label='SMA-5(2)')
mp.plot(dates[9:], sma10, c='dodgerblue',
        label='SMA-10')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
