"""
Zad. 4 Przygotuj kod w Pythonie, który odszumi sygnał z zadania 3 z wykorzystaniem filtru Wienera
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.widgets import Slider
from scipy.signal import wiener
matplotlib.use('TkAgg')

def chirp_signal(f0, f1, t):
    return np.sin(2 * np.pi * (f0 * t + (f1 - f0) * t**2 / 2))

def brownian_noise(amplitude, size):
    return amplitude * np.cumsum(np.random.randn(size))

def white_noise(amplitude, size):
    return amplitude * np.random.randn(size)

# Parametry
fs = 1000  # Częstotliwość próbkowania
T = 1     # Czas trwania sygnału w sekundach
t = np.linspace(0, T, int(T * fs), endpoint=False)

# Inicjalizacja wartości domyślnych
f0_default = 1
f1_default = 100
amplitude_default = 1
snr_default = 10

# Generowanie sygnału chirp
signal = chirp_signal(f0_default, f1_default, t)
brownian_noise_signal = white_noise(2, len(t))
added_sign_brownian_noise = signal + brownian_noise_signal

# Odszumianie sygnału z wykorzystaniem filtru Wienera
denoised_signal = wiener(added_sign_brownian_noise, mysize=15)

fig, ax = plt.subplots(3, 1, figsize=(16, 8))

ax[0].plot(t, signal)
ax[0].set_title("Oryginalny Sygnał")
ax[1].plot(t, added_sign_brownian_noise)
ax[1].set_title("Sygnał z szumem")
ax[2].plot(t, denoised_signal)
ax[2].set_title("Odszumiony Sygnał")

# Dodanie sliderów
axfreq0 = plt.axes([0.25, 0.03, 0.65, 0.03], facecolor='lightgoldenrodyellow')
axfreq1 = plt.axes([0.25, 0.011, 0.65, 0.03], facecolor='lightgoldenrodyellow')

sfreq0 = Slider(axfreq0, 'Częstotliwość początkowa', 0.1, 10.0, valinit=f0_default)
sfreq1 = Slider(axfreq1, 'Częstotliwość końcowa', 20.0, 200.0, valinit=f1_default)

# Funkcja aktualizacji
def update(val):
    f0 = sfreq0.val
    f1 = sfreq1.val

    signal = chirp_signal(f0, f1, t)
    brownian_noise_signal = white_noise(2, len(t))
    added_sign_brownian_noise = signal + brownian_noise_signal

    denoised_signal = wiener(added_sign_brownian_noise, mysize=15)

    ax[0].clear()
    ax[0].plot(t, signal)
    ax[0].set_title("Oryginalny Sygnał")

    ax[1].clear()
    ax[1].plot(t, added_sign_brownian_noise)
    ax[1].set_title("Sygnał z szumem")

    ax[2].clear()
    ax[2].plot(t, denoised_signal)
    ax[2].set_title("Odszumiony Sygnał")

    plt.draw()

# Rejestracja funkcji aktualizacji
sfreq0.on_changed(update)
sfreq1.on_changed(update)

plt.show()
