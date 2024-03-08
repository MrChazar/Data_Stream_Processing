import scipy as scp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Zad. 7 Przygotuj kod w języku Python, który generuje dwuwymiarowy szum czerwony
(Browna). Wyświetl wygenerowany przebieg na płaszczyźnie.
"""

time = 100
x = np.linspace(-1,1,50)
y = np.linspace(-1,1,50)
X,Y = np.meshgrid(x,y)
Z = np.zeros((50,50))
for i in range(50):
    for j in range(50):
        Z[i,j] = np.random.uniform(0,1,time).cumsum()[-1]


plt.contourf(X,Y,Z)
plt.title('2D szum czerwony')
plt.xlabel('x')
plt.ylabel('y')
plt.show()