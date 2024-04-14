import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
import LAB_4.exercise_1 as ex1
import LAB_3.exercise_2 as ex2

"""
Zad. 2 Przygotuj w Pythonie kod, który wyznaczy widmo amplitudowe sygnału sinusoidalnego
w skali decybelowej.
"""


# Definicja widmo amplitudowe
def spectral_density_db(signal, fs):
    T = len(signal)
    f = np.fft.fftfreq(T, 1/fs)
    F = np.fft.fft(signal)
    return f, 20 * np.log10(np.abs(F))


# sygnał sinusoidalny
t, y = ex1.sinusoid(1, 100, 1)

# widmo amplitudowe
freqs, amplitude = spectral_density_db(y, 100)


plt.plot(freqs, amplitude)
plt.title('Widmo amplitudowe w skali decybelowej')
plt.xlabel('F')
plt.ylabel('A [dB]')
plt.show()
