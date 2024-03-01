import scipy as scp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Zad. 3. Korzystając z funkcji to_csv dostępnej w bibliotece pandas zapisz wybrany sygnał do
pliku w formacie CSV.
"""

fs = 1000  # Częstotliwość próbkowania
T = 1     # Czas trwania sygnału w sekundach
t = np.linspace(0, T, T*fs, endpoint=False)
f_sin = 5 # częstotliwość sygnału
x = np.sin(2*np.pi*f_sin*t)
# zapis do pliku
data = pd.DataFrame({'Czas': t, 'Wartość_sygnału': x})
data.to_csv('signal_3.csv', index=False)

plt.plot(data['Czas'], data["Wartość_sygnału"])
plt.show()
