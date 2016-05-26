"""
Scatter plot on a polar axis.

Intensity of diffraction peak increases radially.
"""
import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt('05APR16_PSRD.txt', usecols=range(0,14), skiprows=1)
maxIntensity = data[:,4].max()
minIntensity = data[:,13].min()

theta = range(len(data))
r = range(len(data))

intensitysize1 = range(len(data))
intensitycolor1 = range(len(data))

intensitysize2 = range(len(data))
intensitycolor2 = range(len(data))

intensitysize3 = range(len(data))
intensitycolor3 = range(len(data))

intensitysize4 = range(len(data))
intensitycolor4 = range(len(data))

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
        r[i] = (math.sin(math.radians(45-abs(data[i,1]))))/(1-math.cos(math.radians((45-abs(data[i,1])))))
    else:
        r[i] = data[i,1]
    intensitysize1[i] = ((data[i,4]-minIntensity)/(maxIntensity - minIntensity))*50
    intensitycolor1[i] = ((data[i,4]-minIntensity)/(maxIntensity - minIntensity))
    
    intensitysize2[i] = ((data[i,7]-minIntensity)/(maxIntensity - minIntensity))*50
    intensitycolor2[i] = ((data[i,7]-minIntensity)/(maxIntensity - minIntensity))
    
    intensitysize3[i] = ((data[i,10]-minIntensity)/(maxIntensity - minIntensity))*50
    intensitycolor3[i] = ((data[i,10]-minIntensity)/(maxIntensity - minIntensity))
    
    intensitysize4[i] = ((data[i,13]-minIntensity)/(maxIntensity - minIntensity))*50
    intensitycolor4[i] = ((data[i,13]-minIntensity)/(maxIntensity - minIntensity))
    #intensitycolor[i] = data[i,4]
    
    plt.subplot(1,4,1, projection='polar')
    plt.title('0005')
    plt.scatter(math.radians(theta[i]), r[i], s=intensitysize1[i], c=intensitycolor1[i], cmap=plt.cm.Blues, vmin=0, vmax=1)
    plt.subplot(1,4,2, projection='polar')
    plt.title('0006')
    plt.scatter(math.radians(theta[i]), r[i], s=intensitysize2[i], c=intensitycolor2[i], cmap=plt.cm.Blues, vmin=0, vmax=1)
    plt.subplot(1,4,3, projection='polar')
    plt.title('0007')
    plt.scatter(math.radians(theta[i]), r[i], s=intensitysize3[i], c=intensitycolor3[i], cmap=plt.cm.Blues, vmin=0, vmax=1)
    plt.subplot(1,4,4, projection='polar')
    plt.title('0008')
    plt.scatter(math.radians(theta[i]), r[i], s=intensitysize4[i], c=intensitycolor4[i], cmap=plt.cm.Blues, vmin=0, vmax=1)
    
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
