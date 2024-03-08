import scipy as scp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


"""
Zad. 4 Korzystając z funkcji rand i randn, które dostępne są w bibliotece NumPy, wygeneruj
przebiegi czasowe. Wyznacz histogramy dla tych przebiegów.
"""

fig, ax = plt.subplots(3)
x = np.zeros(1000)
for i in range(1000):
    x[i] = np.random.rand()

y = np.zeros(1000)
for i in range(1000):
    y[i] = np.random.randn(1)

ax[0].hist(x, bins=20)
ax[0].set_title('histogram rand')

ax[1].hist(y, bins=30)
ax[1].set_title('histogram randn')

ax[2].hist(z, bins=20)
ax[2].set_title('histogram rand')
plt.tight_layout()
plt.show()
