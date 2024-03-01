import scipy as scp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Zad. 6 Przygotuj kod w języku Python, który generuje szum czerwony (Browna). Wyświetl
histogram dla tego szumu
"""

x = np.zeros(1000)
for i in range(1000):
    x[i] = np.random.randn(1) - 0.5
x = np.cumsum(x)


fig, ax = plt.subplots(2)
ax[0].plot(x)
ax[0].set_title('szum czerwony')

ax[1].hist(x, bins=20)
ax[1].set_title('histogram szumu czerwonego')

plt.tight_layout()
plt.show()