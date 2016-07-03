#!/usr/bin/python

# Kevin Gilreath

import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdate

xi_start, xi_end = 2, 465
yi_start, yi_end = 2, 465

xi = np.genfromtxt('data.Montoya.txt', usecols=(1))
yi = np.genfromtxt('data.Montoya.txt', usecols=(2))

xi = xi[xi_start - 0:xi_end]
yi = yi[yi_start - 0:yi_end]
timestamp_date_xi=[datetime.datetime.fromtimestamp(xi[i]) for i in range(len(xi))]

xs_start, xs_end = 466, 1154
ys_start, ys_end = 466, 1154

xs = np.genfromtxt('data.Montoya.txt', usecols=(1))
ys = np.genfromtxt('data.Montoya.txt', usecols=(2))

xs = xs[xs_start - 0:xs_end]
ys = ys[ys_start - 0:ys_end]
timestamp_date_xs=[datetime.datetime.fromtimestamp(xs[i]) for i in range(len(xs))]

xa_start, xa_end = 1155, 1679
ya_start, ya_end = 1155, 1679

xa = np.genfromtxt('data.Montoya.txt', usecols=(1))
ya = np.genfromtxt('data.Montoya.txt', usecols=(2))

xa = xa[xa_start - 0:xa_end]
ya = ya[ya_start - 0:ya_end]
timestamp_date_xa=[datetime.datetime.fromtimestamp(xa[i]) for i in range(len(xa))]

#print ' x=', timestamp_date_xi, '\n'  #\n y=', yi

fig, ax = plt.subplots()

plt.plot(timestamp_date_xi, yi, 'r')
plt.plot(timestamp_date_xs, ys, 'b')
plt.plot(timestamp_date_xa, ya, 'g')
plt.xlabel('time')
plt.ylabel('value')
plt.ylim([0,70000])
date_fmt = '%d-%m-%y %H:%M:%S'

# Use a DateFormatter to set the data to the correct format.
date_formatter = mdate.DateFormatter(date_fmt)
ax.xaxis.set_major_formatter(date_formatter)
fig.autofmt_xdate()

plt.show()

# NOTES

#when looking at the data.Montoya
#range, min, max, etc
#data centers are of different time zones
#data recorded over span of 1 day
#Didn't know what RTB.requests meant, until day after completing this code (7/1)
#RTB stands for Real-Time Bidding, and RTB.requests refers to the number of bids for auctions (value?) and when (time)
#data centers I and S had similiar trends going accross time, so I assume they're both in the same country
#looking closely at A's graph, it appears A is on the other side of the world (somewhere in Europe?) from I and S, because it peaks whenever I and S reach their lowest points (excluding negative numbers), and A goes low when I and S go high.
#last adjustments: I have set the graph to focus on the main area and changed the epoch time to dates, and made the whole graph easier to read

# FINAL THOUGHTS

# - Findings

#   When I first analyzed data.Montoya.txt, I actually didn't know what rtb.requests were, until I Google'd it.  After learning that rtb stood for Real-time bidding, I understood what the resulting graph was trying to show, but I didn't know what "value" referred to.  My best guess is that it refers to the number of bid requests being made at certain times.  However, there were some negative values in the graph. I can only assume that these negative values represented special moments. They could be: glitchs/errors that occur (these values could be removed and have little effect on the graph as a whole), times where bids have finished and the data center(s) are restarting, or updates that require the data centers to stop until the update is applied. Overall, I learned from the graph that data centers I and S are in the same area (which explains why the graphs are similar, except for size), and data center A simply had a lower amount of activity compared to the other two.

# - Challenges

#   I had one particular challenge: choosing which programming language to use. At first, I was going to use C, but then switched to Python because I stumbled upon a graph-making tutorial on Python while trying to figure out what functions I need to make a graph for C.

# - Conclusion

#   This exercise has been the first time since college that I got to program. I have always feared that I may have forgotten how to program completely, but completing this exercise has taught me otherwise. I only wish I had more clarity about data.Montoya.txt and exactly what it is about. In conclusion, I hope this program demostrates my programming capabilities.

















