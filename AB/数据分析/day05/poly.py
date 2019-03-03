# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd


dates, bhp_closing_prices = np.loadtxt(
    '../../data/bhp.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype='M8[D], f8', converters={1: dmy2ymd})
vale_closing_prices = np.loadtxt(
    '../../data/vale.csv', delimiter=',',
    usecols=(6), unpack=True)
diff_closing_prices = bhp_closing_prices - \
    vale_closing_prices
days = dates.astype(int)
p = np.polyfit(days, diff_closing_prices, 4)
poly_closing_prices = np.polyval(p, days)
q = np.polyder(p)
roots_x = np.roots(q)
roots_y = np.polyval(p, roots_x)
mp.figure('Polynomial Fitting', facecolor='lightgray')
mp.title('Polynomial Fitting', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Difference Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(
    byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter(
    '%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, poly_closing_prices, c='limegreen',
        linewidth=3, label='Polynomial Fitting')
mp.scatter(dates, diff_closing_prices, c='dodgerblue',
           alpha=0.5, s=60, label='Difference Price')
roots_x = roots_x.astype(int).astype(
    'M8[D]').astype(md.datetime.datetime)
mp.scatter(roots_x, roots_y, marker='^', s=80,
           c='orangered', label='Peek', zorder=4)
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
