"""
Created on Tue Nov 13 22:05:46 2022

@author: Ahmet Efe BAŞOL
@school number: 1306191431
"""

# import the library pulp as p
from pulp import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Construct lines
x = np.linspace(0, 20, 2000)


def amac(x, y):
    print(y)
    print(x)
    z = x + (2 * y)
    print(z)
    return z


# Kısıt fonksiyonlarımızın tanımlanması
y1 = (3 - x) / 3
y2 = 2 - 2 * x
y3 = 3 - 3 * x

# Make plot
plt.plot(x, y1, label=r'$y\geq2$')
plt.plot(x, y2, label=r'$2y\leq25-x$')
plt.plot(x, y3, label=r'$4y\geq 2x - 8$')
plt.xlim((0, 4))
plt.ylim((0, 4))
plt.xlabel(r'$x1$')
plt.ylabel(r'$x2$')

# Fill feasible region
y5 = np.minimum(y1, y2)
y6 = np.minimum(y3, y5)
plt.plot(x, y6, label=r'$4y\geq 2x - 8$')
plt.fill_between(x, y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()



