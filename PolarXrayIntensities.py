"""
Scatter plot on a polar axis.

Intensity of diffraction peak increases radially.
"""
import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt('05APR16_0005_PSRD.txt', usecols=range(0,5), skiprows=1)
maxIntensity = data[:,4].max()
minIntensity = data[:,4].min()

theta = range(len(data))
r = range(len(data))

intensitysize = range(len(data))
intensitycolor = range(len(data))

for i in range(len(data)):

    if data[i,0] < 0:
        if data[i,1] <= 0:
            theta[i] = data[i,0] + 360
        else:
            theta[i] = data[i,0] + 180
    else:
        if data[i,1] <= 0:
            theta[i] = data[i,0] + 180
        else:
            theta[i] = data[i,0]
    if data[i,1] !=0:
        r[i] = (math.sin(math.radians(abs(data[i,1]))))/(1-math.cos(math.radians(data[i,1])))
    else:
        r[i] = data[i,1]
    intensitysize[i] = ((maxIntensity - data[i,4])/(maxIntensity - minIntensity))*100
    intensitycolor[i] = ((maxIntensity - data[i,4])/(maxIntensity - minIntensity))
    #intensitycolor[i] = data[i,4]
    
    ax = plt.subplot(111, projection='polar')
    c = plt.scatter(math.radians(theta[i]), r[i], s=intensitysize[i], c=intensitycolor[i], cmap=plt.cm.Blues, vmin=0, vmax=1)
    c.set_alpha(0.75)
    ax.set_rmax(60)



plt.show()

"""
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2 * np.random.rand(N)
colors = theta

ax = plt.subplot(111, projection='polar')
c = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.hsv)
c.set_alpha(0.75)

plt.show()
"""
