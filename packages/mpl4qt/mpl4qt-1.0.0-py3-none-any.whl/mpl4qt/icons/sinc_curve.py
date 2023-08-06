#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
ax.set_alpha(0.1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('y')

x = np.linspace(-1, 1, 400)
y = np.sin(15 * x) / x

line, = ax.plot(x, y)
line.set_color('m')
line.set_alpha(0.8)
line.set_lw(2)

ax.fill_between(x, y, alpha=0.8, color='m')

plt.savefig('mplcurve-logo.png', transparent=False)

plt.show()
