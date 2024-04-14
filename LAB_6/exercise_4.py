"""
Zad. 4 Przygotuj w Pythonie kod, który wyznaczy widmo dowolnego sygnału załadowanego z
pliku np. csv.
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.widgets import Slider
from scipy.fft import fft
import yfinance as yf

matplotlib.use('TkAgg')


def amplitude_spectrum(t, y):
    N = len(y)
    freqs = np.fft.fftfreq(N, 1/10)
    fft_vals = np.fft.fft(y)
    amplitude = np.abs(fft_vals) / N
    return freqs, amplitude

data = yf.download("META", start='2023-01-01', end='2024-01-01')

y = data['Close'].values
t = np.arange(len(y))

freqs, amplitude = amplitude_spectrum(t, y)

# Wyświetlenie widma amplitudowego
fig, ax = plt.subplots(2)

plt.suptitle("Analiza widma sygnału ceny akcji META")
ax[0].plot(t, y)
ax[0].set_title('Szereg Czasowy')
ax[0].set_xlabel('Częstotliwość [Hz]')
ax[0].set_ylabel('Amplituda')

ax[1].plot(freqs, amplitude)
ax[1].set_title('Widmo Amplitudowe')
ax[1].set_xlabel('Częstotliwość [Hz]')
ax[1].set_ylabel('Amplituda')


plt.tight_layout()
plt.show()