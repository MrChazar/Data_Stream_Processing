"""
Zad. 4 Przygotuj w Pythonie kod bazując na pakiecie emd, który dokona dekompozycji sygnału
załadowanego z pliku np. csv. Wyznacz widmo każdej z mod.
"""

import emd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import yfinance as yf

matplotlib.use('TkAgg')

# wczytaj plik
data = yf.download("META", start='2023-01-01', end='2024-01-01')
y = data['Close'].values
t = np.arange(len(y))
delta_t = np.mean(np.diff(t))
fs = 1 / delta_t

fig, ax = plt.subplots(3, 1, figsize=(12, 10))

ax[0].plot(t, y)
ax[0].set_xlabel('Częstotliwość [Hz]')
ax[0].set_ylabel('Amplituda')
ax[0].set_title('Ceny akcji spółki "Meta"')

# Dekompozycja sygnału za pomocą EMD
imfs = emd.sift.sift(y)
ax[1].plot(imfs)
ax[1].set_xlabel('Częstotliwość [Hz]')
ax[1].set_ylabel('Amplituda')
ax[1].set_title('Dekomponwany sygnał')


# Wyznaczanie widma każdej z mod
for imf in imfs:
    spectrum = np.fft.fft(imf)
    freqs = np.fft.fftfreq(len(imf), 1/fs)
    ax[2].plot(freqs, np.abs(spectrum))
    ax[2].set_xlabel('Częstotliwość [Hz]')
    ax[2].set_ylabel('Amplituda')
    ax[2].set_title('Widma sygnału')

plt.tight_layout()
plt.show()