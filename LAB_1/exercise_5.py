import scipy as scp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Korzystając z funkcji random.normal, która dostępna jest w bibliotece NumPy,
wygeneruj kilka przebiegów czasowych dla wybranych parametrów. Wyznacz histogramy dla
tych przebiegów.
"""

fig, ax = plt.subplots(3)
loc = 0
scale = 1
x = np.zeros(1000)
y = np.zeros(1000)
z = np.zeros(1000)
for i in range(1000):
    x[i] = np.random.normal(loc, scale)
    y[i] = np.random.normal(loc, scale)
    z[i] = np.random.normal(loc, scale)

ax[0].hist(x, bins=20)
ax[0].set_title('histogram random.normal 1')

ax[1].hist(y, bins=20)
ax[1].set_title('histogram random.normal 2')

ax[2].hist(z, bins=20)
ax[2].set_title('histogram random.normal 3')

plt.tight_layout()
plt.show()