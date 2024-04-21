"""
Zad. 7 Przygotuj kod w Pythonie, który odszumi sygnał załadowany z pliku csv oraz odszumi ten
sygnał wykorzystując filtr Wienera, Savitzkyego-Golaya oraz bazującego na algorytmie EMD i
częściowej rekonstrukcji.
"""

import numpy as np
import matplotlib.pyplot as plt
import emd
import matplotlib
from scipy.signal import wiener
from matplotlib.widgets import Slider
from scipy.signal import chirp
import yfinance as yf
from scipy.signal import savgol_filter
matplotlib.use('TkAgg')

# Pobieranie danych z serwisu Yahoo Finance
data = yf.download("GME", start='2021-01-01', end='2024-01-01')

# Wyodrębnianie danych z zamknięcia akcji
y = data['Close'].values
t = np.arange(len(y))

# Tworzenie wykresu
fig, ax = plt.subplots(4, 1, figsize=(10, 8))
fig.suptitle("Porównanie Filtrów wienera, Savitzkyego-Golaya oraz bazującego na algorytmie EMD i częściowej rekonstrukcji.")
# Oryginalny sygnał
ax[0].plot(t, y, color='blue', label='Oryginalny Sygnał')
ax[0].set_title("Oryginalny Sygnał")
ax[0].set_xlabel("Czas")
ax[0].set_ylabel("Wartość")
ax[0].legend()

# Odszumianie sygnału z wykorzystaniem filtru Wienera
wiener_denoised = wiener(y, mysize=15)
ax[1].plot(t, wiener_denoised, color='green', label='Filtr Wienera')
ax[1].set_title("Odszumianie z wykorzystaniem filtru Wienera")
ax[1].set_xlabel("Czas")
ax[1].set_ylabel("Wartość")
ax[1].legend()

# Odszumianie sygnału z wykorzystaniem filtru Savitzky-Golay
window_length = 51
polyorder = 3
savgol_denoised = savgol_filter(y, window_length, polyorder)
ax[2].plot(t, savgol_denoised, color='red', label='Filtr Savitzky-Golay')
ax[2].set_title("Odszumianie z wykorzystaniem filtru Savitzky-Golay")
ax[2].set_xlabel("Czas")
ax[2].set_ylabel("Wartość")
ax[2].legend()

# Odszumianie sygnału za pomocą EMD
IMFs = emd.sift.sift(y)
ax[3].plot(np.sum(IMFs[::-5], axis=1), color='orange', label='EMD i częściowa rekonstrukcja')
ax[3].set_title("Odszumianie za pomocą EMD i częściowej rekonstrukcji")
ax[3].set_xlabel("Czas")
ax[3].set_ylabel("Wartość")
ax[3].legend()

plt.tight_layout()
plt.show()
