import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
import LAB_1.exercise_1 as ex1

"""
Zad. 5 Przygotuj w Pythonie kod, który wyznaczy obwiednie dla sygnału świergotliwego (chirp
signal)
"""

# Parametry Sygałów
fs = 1000  # Częstotliwość próbkowania
T = 1     # Czas trwania sygnału w sekundach
t = np.linspace(0, T, T*fs, endpoint=False)
f = 5 # częstotliwość sygnału

# świergotliwy
f0 = 1
f1 = 100
y_chirp = ex1.signal_chirp(f0, f1, t, T)

# Obwiednia
y_envelope = np.abs(scp.signal.hilbert(y_chirp))

plt.plot(t, y_chirp)
plt.plot(t, y_envelope)
plt.title('Obwiednia sygnału świergotliwego')
plt.xlabel('t')
plt.ylabel('y')
plt.show()