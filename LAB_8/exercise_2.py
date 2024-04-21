"""
Zad. 2 Przygotuj w Pythonie kod bazując na pakiecie emd, który dokona dekompozycji sygnału
świergotliwego (chirp) oraz wyznaczy widmo każdej mody.
"""

import emd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import scipy as scp
matplotlib.use('TkAgg')

# Parametry
fs = 1000  # Częstotliwość próbkowania
T = 1     # Czas trwania sygnału w sekundach
t = np.linspace(0, T, T*fs, endpoint=False)
f = 5 # częstotliwość sygnału
t = np.linspace(0, T, T*fs, endpoint=False)


# Generowanie sygnału będącego superpozycją funkcji sinus i cosinus
f0 = 1
f1 = 100
y = scp.signal.chirp(t, fs, T, f)

fig, ax = plt.subplots(3, 1, figsize=(12, 10))

ax[0].plot(t, y)
ax[0].set_ylabel('Amplituda')
ax[0].set_title('Sygnał Superpozycji')

# Dekompozycja sygnału za pomocą EMD
imfs = emd.sift.sift(y)
ax[1].plot(imfs)
ax[1].set_ylabel('Amplituda')
ax[1].set_title('Dekomponwany sygnał')


# Wyznaczanie widma każdej z mod
for imf in imfs:
    spectrum = np.fft.fft(imf)
    freqs = np.fft.fftfreq(len(imf), 1/fs)
    ax[2].plot(freqs, np.abs(spectrum))
    ax[2].set_ylabel('Amplituda')
    ax[2].set_title('Widma sygnału')

plt.tight_layout()
plt.show()
