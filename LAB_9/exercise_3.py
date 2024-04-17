"""
Zad. 3 Przygotuj kod w Pythonie, który wygeneruje sygnał świergotliwy z szumem biały oraz szumem
browna z zadanym SNR.
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.widgets import Slider
matplotlib.use('TkAgg')
def chirp_signal(f0, f1, t):
    return np.sin(2 * np.pi * (f0 * t + (f1 - f0) * t**2 / 2))

def white_noise(amplitude, size):
    return amplitude * np.random.randn(size)

def brownian_noise(amplitude, size):
    return amplitude * np.cumsum(np.random.randn(size))

def SNR(signal, noise):
    signal_power = np.sum(signal ** 2)
    noise_power = np.sum(noise ** 2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Parametry
fs = 1000  # Częstotliwość próbkowania
T = 1     # Czas trwania sygnału w sekundach
t = np.linspace(0, T, T * fs, endpoint=False)

# Inicjalizacja wartości domyślnych
f0_default = 1
f1_default = 100
amplitude_default = 1
snr_default = 10

# Generowanie sygnału chirp
signal = chirp_signal(f0_default, f1_default, t)

# Generowanie białego szumu
white_noise_amplitude_default = 0.2
white_noise_signal = white_noise(white_noise_amplitude_default, len(t))

# Generowanie szumu Browna
brownian_noise_amplitude_default = 0.05
brownian_noise_signal = brownian_noise(brownian_noise_amplitude_default, len(t))

# Dodawanie szumu do sygnału
added_sign_white_noise = signal + white_noise_signal
added_sign_brownian_noise = signal + brownian_noise_signal

# Tworzenie interaktywnego wykresu
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

ax[0].plot(t, signal, label='Sygnał chirp', color='blue')
ax[0].plot(t, added_sign_white_noise, label='Sygnał + biały szum', color='red')
ax[0].plot(t, added_sign_brownian_noise, label='Sygnał + szum Browna', color='green')
ax[0].set_title('Sygnały')
ax[0].set_xlabel('Czas [s]')
ax[0].set_ylabel('Amplituda')
ax[0].legend()

ax[1].set_title('Wartość SNR')
ax[1].set_xlabel('SNR [dB]')
ax[1].set_ylabel('Częstotliwość [Hz]')
ax[1].set_xlim(-10, 30)
ax[1].set_ylim(0, 100)
ax[1].grid(True)

plt.subplots_adjust(hspace=0.5)

# Inicjalizacja suwaków
axfreq = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
axwhite = plt.axes([0.25, 0.08, 0.65, 0.03], facecolor='lightgoldenrodyellow')
axbrown = plt.axes([0.25, 0.14, 0.65, 0.03], facecolor='lightgoldenrodyellow')

sfreq = Slider(axfreq, 'SNR [dB]', -10, 30, valinit=snr_default)
swhite = Slider(axwhite, 'Biały szum', 0, 1, valinit=white_noise_amplitude_default)
sbrown = Slider(axbrown, 'Szum Brown', 0, 1, valinit=brownian_noise_amplitude_default)

# Funkcja aktualizacji
def update(val):
    snr = sfreq.val
    white_noise_amplitude = swhite.val
    brownian_noise_amplitude = sbrown.val

    # Generowanie białego i szumu Browna z zadanym SNR
    white_noise_signal = white_noise(white_noise_amplitude, len(t))
    brownian_noise_signal = brownian_noise(brownian_noise_amplitude, len(t))
    signal_power = np.sum(signal ** 2)
    noise_power_white = np.sum(white_noise_signal ** 2)
    noise_power_brown = np.sum(brownian_noise_signal ** 2)

    # Obliczanie współczynnika proporcji między sygnałem a szumem dla zadanego SNR
    k_white = 10 ** (snr / 10) * signal_power / noise_power_white
    k_brown = 10 ** (snr / 10) * signal_power / noise_power_brown

    # Mnożenie szumu przez współczynniki
    added_sign_white_noise = signal + np.sqrt(k_white) * white_noise_signal
    added_sign_brownian_noise = signal + np.sqrt(k_brown) * brownian_noise_signal

    # Aktualizacja wykresu
    ax[0].lines[1].set_ydata(added_sign_white_noise)
    ax[0].lines[2].set_ydata(added_sign_brownian_noise)

    # Obliczanie i aktualizacja SNR na wykresie
    snr_white = SNR(signal, white_noise_signal)
    snr_brown = SNR(signal, brownian_noise_signal)
    ax[1].cla()
    ax[1].bar('Biały szum', snr_white, color='red', label=f'SNR = {snr_white:.2f} dB')
    ax[1].bar('Szum Brown', snr_brown, color='green', label=f'SNR = {snr_brown:.2f} dB')
    ax[1].legend()
    ax[1].set_title('Wartość SNR')
    ax[1].set_xlabel('Rodzaj szumu')
    ax[1].set_ylabel('SNR [dB]')

    fig.canvas.draw_idle()

# Rejestracja funkcji aktualizacji
sfreq.on_changed(update)
swhite.on_changed(update)
sbrown.on_changed(update)

plt.show()
