import scipy as scp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Zad. 7 Przygotuj kod w języku Python, który generuje dwuwymiarowy szum czerwony
(Browna). Wyświetl wygenerowany przebieg na płaszczyźnie.
"""
#visualize gaussian noise on a 2d linspace using matplotlib countour
time = 100
x = np.linspace(-1,1,100)
y = np.linspace(-1,1,100)
X,Y = np.meshgrid(x,y)
Z = np.zeros((100,100))
for i in range(100):
    for j in range(100):
        #each point has to be a cumsum of a random noise sequence in length of time
        Z[i,j] = np.random.uniform(0,1,time).cumsum()[-1]

#plot the contour
plt.contourf(X,Y,Z)
plt.show()