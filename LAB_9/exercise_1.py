"""
Zad. 1 Przygotuj kod w Pythonie, które wyznacza wartości następujących miar jakości
sygnałów:

gdzie: s to sygnał, n to szum, smax to maksymalna wartość sygnału, y to sygnał z zakłóceniem
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import LAB_1.exercise_1 as ex1
from matplotlib.widgets import Slider
matplotlib.use('TkAgg')


def SNR(s, n):
    signal_power = np.sum(np.abs(s))
    noise_power = np.sum(np.abs(n))
    snr = 20 * np.log10(signal_power / noise_power)
    return snr


def MSE(s, n):
    return np.square(s - n).mean()


def PSNR(s, n):
    smax = np.max(s)
    psnr = 20 * np.log10(smax/ MSE(s, n) ** 1/2)
    return psnr


fs = 1000  # Częstotliwość próbkowania
T = 1     # Czas trwania sygnału w sekundach
t = np.linspace(0, T, T*fs, endpoint=False)
f = 5 # częstotliwość sygnału


def update(val):
    freq = freq_slider.val
    noise_freq = noise_freq_slider.val
    y = ex1.sin(freq+3, t)
    noise = ex1.sin(noise_freq+12, t)
    added_sign = y + noise

    ax[0].clear()
    ax[0].plot(t, y, color='red', label='Sygnał sinusoidalny')
    ax[0].plot(t, noise, color='blue', label='Sygnał hałasu')
    ax[0].plot(t, added_sign, color='orange', label='Suma sygnału i hałasu')
    ax[0].set_title("Sygnały")
    ax[0].set_xlabel("Czas")
    ax[0].set_ylabel("Częstotliwość")
    ax[0].legend()

    ax[1].clear()
    ax[1].text(0.5, 0.5, f"SNR: {SNR(added_sign, noise)}\nPSNR: {PSNR(added_sign, noise)}\nMSE: {MSE(added_sign, noise)}",
               horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.draw()

fig, ax = plt.subplots(2, 1, figsize=(14, 10))

# Ustawianie suwaków
freq_slider_ax = plt.axes([0.2, 0.02, 0.65, 0.03])
freq_slider = Slider(freq_slider_ax, 'Częstotliwość sygnału', valmin=1, valmax=10, valinit=5)

noise_freq_slider_ax = plt.axes([0.2, 0.001, 0.65, 0.03])
noise_freq_slider = Slider(noise_freq_slider_ax, 'Częstotliwość hałasu', valmin=1, valmax=15, valinit=12)

# Obsługa zmian wartości suwaków
freq_slider.on_changed(update)
noise_freq_slider.on_changed(update)

update(None)
plt.show()