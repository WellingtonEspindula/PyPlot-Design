#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Test program which plots Van der Pol Oscillator using pastel colors style 
# Author: Wellington Espindula

# %%
from scipy.integrate import solve_ivp as sivp
import numpy as np

def diffeq(t, xy):
    mi = 3

    x = xy[0]
    y = xy[1]
    return y, mi*(1-(x**2))*y - x

solution = sivp(diffeq, [-0.001, 100.001], [1, 1], dense_output=True)
t = np.linspace(solution.t[1], solution.t[-1], 150)
x = solution.sol(t)[0]
y = solution.sol(t)[1]

# PLOT
import stylelib as st
plt, fig, ax = st.pastel("Van der Pol Oscillator")
ax.plot(t, x, linewidth=2)
ax.plot(t, y, linewidth=2)
plt.show()

# %%
