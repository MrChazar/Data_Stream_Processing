import scipy as scp
import numpy as np
import LAB_1.exercise_1 as ex1
import matplotlib.pyplot as plt
"""
Zad. 1 Dla sygnałów z zadania 1 z listy 1 napisz kod w języku Python, który wyznaczy dla
nich widmową gęstość mocy. W tym celu wykorzystaj metody: periodogram i welcha.
Metody dostępne są m.in. w bibliotece SciPy.
"""

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

# Widmowa gęstość mocy perdiodogram
f_sin, Pxx_den_sin = scp.signal.periodogram(y_sin, fs)
f_square, Pxx_den_square = scp.signal.periodogram(y_square, fs)
f_sawtooth, Pxx_den_sawtooth = scp.signal.periodogram(y_sawtooth, fs)
f_chirp, Pxx_den_chirp = scp.signal.periodogram(y_chirp, fs)
f_super_position, Pxx_den_super_position = scp.signal.periodogram(y_super_position, fs)
f_impulse, Pxx_den_impulse = scp.signal.periodogram(y_impulse, fs)

# Widmowa gęstość mocy welcha
f_sin_w, wxx_den_sin = scp.signal.welch(y_sin, fs)
f_square_w, wxx_den_square = scp.signal.welch(y_square, fs)
f_sawtooth_w, wxx_den_sawtooth = scp.signal.welch(y_sawtooth, fs)
f_chirp_w, wxx_den_chirp = scp.signal.welch(y_chirp, fs)
f_super_position_w, wxx_den_super_position = scp.signal.welch(y_super_position, fs)
f_impulse_w, wxx_den_impulse = scp.signal.welch(y_impulse, fs)

fig, ax = plt.subplots(6, 2)
fig.suptitle('Widmowa gęstość mocy')
ax[0][0].semilogy(f_sin, Pxx_den_sin)
ax[0][0].set_title('sinus Periodgram')
ax[0][1].semilogy(f_sin_w, wxx_den_sin)
ax[0][1].set_title('sinus Welch')
ax[1][0].semilogy(f_square, Pxx_den_square)
ax[1][0].set_title('prostokątny Periodgram')
ax[1][1].semilogy(f_square_w, wxx_den_square)
ax[1][1].set_title('prostokątny Welch')
ax[2][0].semilogy(f_sawtooth, Pxx_den_sawtooth)
ax[2][0].set_title('piłokształtny Periodgram')
ax[2][1].semilogy(f_sawtooth_w, wxx_den_sawtooth)
ax[2][1].set_title('piłokształtny Welch')
ax[3][0].semilogy(f_chirp, Pxx_den_chirp)
ax[3][0].set_title('świergotliwy Periodgram')
ax[3][1].semilogy(f_chirp_w, wxx_den_chirp)
ax[3][1].set_title('świergotliwy Welch')
ax[4][0].semilogy(f_super_position, Pxx_den_super_position)
ax[4][0].set_title('Superpozycja Periodgram')
ax[4][1].semilogy(f_super_position_w, wxx_den_super_position)
ax[4][1].set_title('Superpozycja Welch')
ax[5][0].semilogy(f_impulse, Pxx_den_impulse)
ax[5][0].set_title('Impuls jednostkowy Periodgram')
ax[5][1].semilogy(f_impulse_w, wxx_den_impulse)
ax[5][1].set_title('Impuls jednostkowy Welch')
plt.tight_layout()
plt.show()


