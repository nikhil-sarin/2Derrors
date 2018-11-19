import bilby
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import inspect

outdir = 'outdir'
label = 'line'

data = np.loadtxt('data.txt')
xobs = data[0,:]
yobs = data[1,:]
xerr = data[2,:]
yerr = data[3,:]
plt.errorbar(xobs, yobs, xerr = xerr, yerr = yerr, fmt = 'x')
plt.show()

