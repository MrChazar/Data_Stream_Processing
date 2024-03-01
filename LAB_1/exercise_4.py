import scipy as scp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


"""
Zad. 4 Korzystając z funkcji rand i randn, które dostępne są w bibliotece NumPy, wygeneruj
przebiegi czasowe. Wyznacz histogramy dla tych przebiegów.
"""

x = np.zeros(1000)
for i in range(1000):
    x[i] = np.random.rand()
plt.hist(x, bins=20)
plt.show()
