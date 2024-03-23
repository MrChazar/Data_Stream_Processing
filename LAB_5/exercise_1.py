import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
import LAB_4.exercise_1 as ex1
"""
Zad. 1 Przygotuj w Pythonie kod, który wyznaczy widmo amplitudowe sygnału sinusoidalnego. 
"""

# sygnał sinusoidalny
t, y = ex1.sinusoid(1, 100, 1)

# widmo amplitudowe
N = len(y)
freqs = np.fft.fftfreq(N, 1/10)
fft_vals = np.fft.fft(y)
amplitude = np.abs(fft_vals) / N

plt.plot(freqs, amplitude)
plt.title('Widmo amplitudowe')
plt.xlabel('f')
plt.ylabel('A')
plt.show()

