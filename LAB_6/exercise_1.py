"""
Zad. 1 Przygotuj w Pythonie kod, który przedstawi na wykresie okno Hamminga, Hanna,
Blackmana oraz Dirichleta oraz ich widma amplitudowe (pakiet SciPy).
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.signal as signal
from matplotlib.widgets import Slider

matplotlib.use('TkAgg')


# Widmo amplitudowe
def amplitude_spectrum(y, N):
    freqs = np.fft.fftfreq(N, 1/10)
    fft_vals = np.fft.fft(y)
    amplitude = np.abs(fft_vals) / N
    return freqs, amplitude


def plot_window(window, N):
    w = window(N)
    f, A = amplitude_spectrum(w, N)
    plt.plot(f, A)
    plt.xlabel('Częstotliwość [Hz]')
    plt.ylabel('Amplituda')
    plt.title('Widmo Amplitudowe')
    plt.grid(True)
    plt.show()


def update(val):
    N = int(slider.val)
    hamming = signal.windows.hamming(N)
    hann = signal.windows.hann(N)
    blackman = signal.windows.blackman(N)
    dirichlet = signal.windows.boxcar(N)
    f_h, a_h = amplitude_spectrum(hamming, N)
    f_han, a_han = amplitude_spectrum(hann, N)
    f_b, a_b = amplitude_spectrum(blackman, N)
    f_d, a_d = amplitude_spectrum(dirichlet, N)

    fig.suptitle("Wykres Okien Czasowych oraz Widm Amplitudowych")
    ax[0][0].clear()
    ax[0][0].plot(hamming)
    ax[0][0].set_title("Okno Hamminga")
    ax[0][0].set_xlabel("Próbki")
    ax[0][0].set_ylabel("Amplituda")

    ax[0][1].clear()
    ax[0][1].plot(f_h, a_h)
    ax[0][1].set_title("Widmo Amplitudowe")
    ax[0][1].set_xlabel("Częstotliwość")
    ax[0][1].set_ylabel("Amplituda")

    ax[1][0].clear()
    ax[1][0].plot(hann)
    ax[1][0].set_title("Okno Hann")
    ax[1][0].set_xlabel("Próbki")
    ax[1][0].set_ylabel("Amplituda")

    ax[1][1].clear()
    ax[1][1].plot(f_han, a_han)
    ax[1][1].set_title("Widmo Amplitudowe")
    ax[1][1].set_xlabel("Częstotliwość")
    ax[1][1].set_ylabel("Amplituda")

    ax[2][0].clear()
    ax[2][0].plot(blackman)
    ax[2][0].set_title("Okno Blackmana")
    ax[2][0].set_xlabel("Próbki")
    ax[2][0].set_ylabel("Amplituda")

    ax[2][1].clear()
    ax[2][1].plot(f_b, a_b)
    ax[2][1].set_title("Widmo Amplitudowe")
    ax[2][1].set_xlabel("Częstotliwość")
    ax[2][1].set_ylabel("Amplituda")

    ax[3][0].clear()
    ax[3][0].plot(dirichlet)
    ax[3][0].set_title("Okno Dirichleta")
    ax[3][0].set_xlabel("Próbki")
    ax[3][0].set_ylabel("Amplituda")

    ax[3][1].clear()
    ax[3][1].plot(f_d, a_d)
    ax[3][1].set_title("Widmo Amplitudowe")
    ax[3][1].set_xlabel("Częstotliwość")
    ax[3][1].set_ylabel("Amplituda")
    plt.tight_layout()
    plt.draw()

N = 51

fig, ax = plt.subplots(4, 2)
plt.subplots_adjust(bottom=0.25)

# Slider
ax_slider = plt.axes([0.1, 0.001, 0.8, 0.03])
slider = Slider(ax_slider, 'Ilość próbek', 10, 100, valinit=N, valstep=1)
slider.on_changed(update)

# Wyświetlanie
update(N)
plt.show()