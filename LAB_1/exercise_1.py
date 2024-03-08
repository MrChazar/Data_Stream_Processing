import scipy as scp
import matplotlib.pyplot as plt
import numpy as np
"""
Zad. 1 Bazując na bibliotece scipy.signal dostępnej dla języka Python wygeneruj następujące
sygnały:
a) Sinus
b) Prostokątny
c) Piłokształtny
d) Świergotliwy
e) Superpozycja funkcji sinus i cosinus z samodzielnie dobranymi parametrami
f) Impuls jednostkowy
Zadanie dodatkowe: wygenerowane sygnały wyświetl w uporządkowany sposób korzystając z
funkcji subplot. 
"""

def sin(f, t):
    return np.sin(2*np.pi*f*t)


def signal_square(f, t):
    return scp.signal.square(2*np.pi*f*t)


def signal_sawtooth(f, t):
    return scp.signal.sawtooth(2*np.pi*f*t)


def signal_chirp(f0, f1, t, T):
    return scp.signal.chirp(t, f0, T, f1)


def super_position(f, t):
    return np.sin(2*np.pi*f*t) + np.cos(2*np.pi*2*f*t)


# wykres rozmiar
plt.rcParams["figure.figsize"] = (18, 10)

# paramettry
fs = 1000  # Częstotliwość próbkowania
T = 1     # Czas trwania sygnału w sekundach
t = np.linspace(0, T, T*fs, endpoint=False)
f = 5 # częstotliwość sygnału

# generowanie sygnału
# sinus
y = sin(f, t)


# prostokąt
y = signal_square(f,t)

# piłokształtny
y = signal_sawtooth(f, t)


# świergotliwy
f0 = 1
f1 = 100
y = signal_chirp(f0, f1, t, T)


# Superpozycja funkcji sinus i cosinus z samodzielnie dobranymi parametrami
y = np.sin(2*np.pi*f*t) + np.cos(2*np.pi*2*f*t)



# Impuls jednostkowy
y = scp.signal.unit_impulse(t.shape, idx='mid')



