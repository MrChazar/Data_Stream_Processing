import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
import LAB_1.exercise_1 as ex1

"""
Zad. 3 Przygotuj w Pythonie kod, który wyznaczy widmo amplitudowe sygnałów z zadania 1
na liście 1.
"""

def amplitude_spectrum(t, y):
    N = len(y)
    freqs = np.fft.fftfreq(N, 1/10)
    fft_vals = np.fft.fft(y)
    amplitude = np.abs(fft_vals) / N
    return freqs, amplitude


# Parametry Sygałów
fs = 1000  # Częstotliwość próbkowania
T = 1     # Czas trwania sygnału w sekundach
t = np.linspace(0, T, T*fs, endpoint=False)
f = 5 # częstotliwość sygnału

# Generowanie sygnału
# sinus
y_sin = ex1.sin(f, t)
# prostokąt
y_square = ex1.signal_square(f,t)
# piłokształtny
y_sawtooth = ex1.signal_sawtooth(f, t)
# świergotliwy
f0 = 1
f1 = 100
y_chirp = ex1.signal_chirp(f0, f1, t, T)
# Superpozycja funkcji sinus i cosinus z samodzielnie dobranymi parametrami
y_super_position = ex1.super_position(f, t)
# Impuls jednostkowy
y_impulse = scp.signal.unit_impulse(fs, 'mid')

# Widmo amplitudowe
freqs_sin, amplitude_sin = amplitude_spectrum(t, y_sin)
freqs_square, amplitude_square = amplitude_spectrum(t, y_square)
freqs_sawtooth, amplitude_sawtooth = amplitude_spectrum(t, y_sawtooth)
freqs_chirp, amplitude_chirp = amplitude_spectrum(t, y_chirp)
freqs_super_position, amplitude_super_position = amplitude_spectrum(t, y_super_position)
freqs_impulse, amplitude_impulse = amplitude_spectrum(t, y_impulse)

fig, ax = plt.subplots(3, 2)
fig.suptitle('Widmo amplitudowe')
ax[0][0].plot(freqs_sin, amplitude_sin)
ax[0][0].set_title('sinus')
ax[0][0].set_xlabel('F')
ax[0][0].set_ylabel('A')

ax[0][1].plot(freqs_square, amplitude_square)
ax[0][1].set_title('prostokątny')
ax[0][1].set_xlabel('F')
ax[0][1].set_ylabel('A')

ax[1][0].plot(freqs_sawtooth, amplitude_sawtooth)
ax[1][0].set_title('piłokształtny')
ax[1][0].set_xlabel('F')
ax[1][0].set_ylabel('A')

ax[1][1].plot(freqs_chirp, amplitude_chirp)
ax[1][1].set_title('świergotliwy')
ax[1][1].set_xlabel('F')
ax[1][1].set_ylabel('A')

ax[2][0].plot(freqs_super_position, amplitude_super_position)
ax[2][0].set_title('superpozycja')
ax[2][0].set_xlabel('F')
ax[2][0].set_ylabel('A')

ax[2][1].plot(freqs_impulse, amplitude_impulse)
ax[2][1].set_title('impuls jednostkowy')
ax[2][1].set_xlabel('F')
ax[2][1].set_ylabel('A')

plt.tight_layout()
plt.show()

