import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
import LAB_4.exercise_1 as ex1
"""
Zad. 4 Przygotuj w Pythonie kod, który wyznaczy widmo fazowe sygnału sinusoidalnego
"""

def phase_amplitude(t, y):
    N = len(y)
    freqs = np.fft.fftfreq(N, 1/10)
    fft_vals = np.fft.fft(y)
    phase = np.angle(fft_vals)
    return freqs, phase

# sygnał sinusoidalny
t, y = ex1.sinusoid(1, 100, 1)

freqs, phase = phase_amplitude(t,y)


plt.plot(freqs, phase)
plt.title('Widmo fazowe')
plt.xlabel('F')
plt.ylabel('PHI')
plt.show()
