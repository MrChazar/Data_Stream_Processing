"""
Zad. 3 Przygotuj w Pythonie kod, który wyznaczy widmo sygnału sinusoidalnego z
wykorzystaniem Szybkiej Transformaty Fouriera (np. pakiet SciPy oferuje funkcję fft)
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.widgets import Slider
from scipy.fft import fft
matplotlib.use('TkAgg')


def sinusoid(f, fs, T=1):
    t = np.linspace(0, T, fs, endpoint=False)
    y = np.sin(2 * np.pi * f * t)
    return t, y


def plot_fft(t, y, fs):
    n = len(y)
    f_values = np.linspace(0.0, 1.0 / (2.0 * (1 / fs)), n // 2)
    fft_values = fft(y)
    fft_mag = 2.0 / n * np.abs(fft_values[:n // 2])
    return f_values, fft_mag

# Parametry początkowe
init_f = 1
init_fs = 10
t, y = sinusoid(init_f, init_fs)

# Tworzenie figure i osi
fig, (ax1, ax2) = plt.subplots(2, 1)
plt.subplots_adjust(left=0.25, bottom=0.4)
scatter, = ax1.plot(t, y, 'o')
plt.title('Sygnał sinusoidalny i jego widmo')
plt.xlabel('t')
ax1.set_ylabel('y')

# Ustawienie suwaków
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axfs = plt.axes([0.1, 0.4, 0.0225, 0.5], facecolor=axcolor)

# Tworzenie suwaków
freq_slider = Slider(ax=axfreq, label='f (Częstotliwość)', valmin=1, valmax=50, valinit=init_f)
fs_slider = Slider(ax=axfs, label='fs (Częstotliwość próbkowania)', valmin=10, valmax=500, valinit=init_fs, orientation="vertical")

# Funkcja aktualizująca dane wykresu
def update(val):
    f = freq_slider.val
    fs = int(fs_slider.val)
    t, y = sinusoid(f, fs)
    f_values, fft_mag = plot_fft(t, y, fs)
    scatter.set_data(t, y)
    ax1.set_title("Wykres sygnału sinusoidalnego")
    ax1.set_xlim(0, 1)
    ax1.set_ylim(-1.1, 1.1)
    ax2.clear()
    ax2.set_title("Widmo Sygnału")
    ax2.plot(f_values, fft_mag)
    ax2.set_xlabel('Częstotliwość [Hz]')
    ax2.set_ylabel('Amplituda')

# Połączenie funkcji aktualizacji z suwakami
freq_slider.on_changed(update)
fs_slider.on_changed(update)

plt.show()