"""
Zad. 3 Przygotuj w Pythonie kod bazując na pakiecie emd, który dokona dekompozycji dowolnie
zbudowanego sygnału będącego superpozycją kilku funkcji sinus i cosinus. Wyznacz widmo każdej z
mod.
"""

import emd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
# Parametry
fs = 1000  # Częstotliwość próbkowania
T = 1      # Czas trwania sygnału w sekundach
t = np.linspace(0, T, T*fs, endpoint=False)
f = 5      # Częstotliwość sygnału

# Generowanie sygnału będącego superpozycją funkcji sinus i cosinus
y = np.sin(2*np.pi*f*t) + np.cos(2*np.pi*2*f*t) + np.sin(2*np.pi*f*t*3) + np.cos(2*np.pi*3.5*f*t)

fig, ax = plt.subplots(3, 1, figsize=(12, 10))

ax[0].plot(t, y)
ax[0].set_xlabel('Częstotliwość [Hz]')
ax[0].set_ylabel('Amplituda')
ax[0].set_title('Sygnał Superpozycji')

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