"""
Zad. 6 Przygotuj kod w Pythonie, który odszumi sygnał z zadania 3 z wykorzystaniem filtru bazującego
na algorytmie EMD i częściowej rekonstrukcji.
"""
import numpy as np
import matplotlib.pyplot as plt
import emd
import matplotlib
from matplotlib.widgets import Slider
from scipy.signal import chirp
matplotlib.use('TkAgg')

def generate_chirp_signal(f0, f1, t):
    return chirp(t, f0, t[-1], f1)

def generate_brownian_noise(amplitude, size):
    return amplitude * np.cumsum(np.random.randn(size))

def generate_white_noise(amplitude, size):
    return amplitude * np.random.randn(size)

# Parametry
fs = 1000  # Częstotliwość próbkowania
T = 1     # Czas trwania sygnału w sekundach
t = np.linspace(0, T, int(T * fs), endpoint=False)

# Generowanie sygnału chirp
f0_default = 1
f1_default = 10
signal = generate_chirp_signal(f0_default, f1_default, t)
brownian_noise_signal = generate_brownian_noise(2, len(t))
white_noise_signal = generate_white_noise(2, len(t))
added_sign_brownian_noise = signal + brownian_noise_signal + white_noise_signal

# Odszumianie sygnału za pomocą EMD
IMFs = emd.sift.sift(added_sign_brownian_noise)


fig, ax = plt.subplots(3, 1, figsize=(10, 8))

ax[0].plot(t, signal)
ax[0].set_title("Oryginalny Sygnał")
ax[0].set_ylabel("Amplituda")

ax[1].plot(t, added_sign_brownian_noise)
ax[1].set_title("Sygnał z szumem")
ax[1].set_ylabel("Amplituda")

ax[2].plot(np.sum(IMFs[::-3], axis=1))
ax[2].set_title("Odszumiony Sygnał")
ax[2].set_xlabel("Czas [s]")
ax[2].set_ylabel("Amplituda")

plt.subplots_adjust(hspace=0.5)

# Dodanie sliderów
axfreq0 = plt.axes([0.25, 0.03, 0.65, 0.03], facecolor='lightgoldenrodyellow')
axfreq1 = plt.axes([0.25, 0.011, 0.65, 0.03], facecolor='lightgoldenrodyellow')

sfreq0 = Slider(axfreq0, 'Częstotliwość początkowa', 0, 2, valstep=0.1,  valinit=f0_default)
sfreq1 = Slider(axfreq1, 'Częstotliwość końcowa', 2, 10, valstep=0.1, valinit=f1_default)

# Funkcja aktualizacji
def update(val):
    f0 = sfreq0.val
    f1 = sfreq1.val

    signal = generate_chirp_signal(f0, f1, t)
    brownian_noise_signal = generate_brownian_noise(2, len(t))
    white_noise_signal = generate_white_noise(2, len(t))
    added_sign_brownian_noise = signal + brownian_noise_signal +  white_noise_signal

    IMFs= emd.sift.sift(added_sign_brownian_noise)

    ax[0].cla()
    ax[0].plot(t, signal)
    ax[0].set_title("Oryginalny Sygnał")
    ax[0].set_ylabel("Amplituda")

    ax[1].cla()
    ax[1].plot(t, added_sign_brownian_noise)
    ax[1].set_title("Sygnał z szumem")
    ax[1].set_ylabel("Amplituda")

    ax[2].cla()
    ax[2].plot(np.sum(IMFs[::-3], axis=1))
    ax[2].set_title("Odszumiony Sygnał")
    ax[2].set_xlabel("Czas [s]")
    ax[2].set_ylabel("Amplituda")

    plt.draw()

# Rejestracja funkcji aktualizacji
sfreq0.on_changed(update)
sfreq1.on_changed(update)

plt.show()
