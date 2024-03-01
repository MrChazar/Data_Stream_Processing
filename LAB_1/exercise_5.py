import scipy as scp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Korzystając z funkcji random.normal, która dostępna jest w bibliotece NumPy,
wygeneruj kilka przebiegów czasowych dla wybranych parametrów. Wyznacz histogramy dla
tych przebiegów.
"""
loc = 0
scale = 1
x = np.zeros(1000)
for i in range(1000):
    x[i] = np.random.normal(loc, scale)

plt.hist(x, bins=20)
plt.show()