import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
import LAB_4.exercise_1 as ex1

"""
Zad. 1 Przygotuj w Pythonie kod, który wyznaczy widmo amplitudowe sygnału sinusoidalnego. 
"""

# Widmo amplitudowe
def amplitude_spectrum(t, y):
    N = len(y)
    freqs = np.fft.fftfreq(N, 1/10)
    fft_vals = np.fft.fft(y)
    amplitude = np.abs(fft_vals) / N
    return freqs, amplitude

plt.rcParams["figure.figsize"] = (10, 6)

# sygnał sinusoidalny
t, y = ex1.sinusoid(1, 100, 1)

# widmo amplitudowe
freqs, amplitude = amplitude_spectrum(t, y)


plt.plot(freqs, amplitude)
plt.title('Widmo amplitudowe')
plt.xlabel('F')
plt.ylabel('A')
plt.tight_layout()
plt.show()

