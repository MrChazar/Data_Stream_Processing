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

# wykres rozmiar
plt.rcParams["figure.figsize"] = (18, 10)

# wykres
fig, ax = plt.subplots(6)
fig.suptitle('Wykresy sygnałów')

# paramettry
fs = 1000  # Częstotliwość próbkowania
T = 1     # Czas trwania sygnału w sekundach
t = np.linspace(0, T, T*fs, endpoint=False)

# generowanie sygnału
# sinus
f_sin = 5 # częstotliwość sygnału
x = np.sin(2*np.pi*f_sin*t)
ax[0].plot(t, x)
ax[0].set_title('sinus')

# prostokąt
f_rect = 5 # częstotliwość sygnału
x = scp.signal.square(2*np.pi*f_rect*t)
ax[1].plot(t, x)
ax[1].set_title('prostokąt')

# piłokształtny
f_saw = 5 # częstotliwość sygnału
x = scp.signal.sawtooth(2*np.pi*f_saw*t)
ax[2].plot(t, x)
ax[2].set_title('piłokształtny')

# świergotliwy
f0 = 1
f1 = 100
t_chirp = np.linspace(0, T, T*fs)
x = scp.signal.chirp(t_chirp, f0, T, f1)
ax[3].plot(t, x)
ax[3].set_title('świergotliwy')

# Superpozycja funkcji sinus i cosinus z samodzielnie dobranymi parametrami
f_superpos = 3
x = np.sin(2*np.pi*f_superpos*t) + np.cos(2*np.pi*2*f_superpos*t)
ax[4].plot(t, x)
ax[4].set_title('superpozycja sinus i cosinus')

# Impuls jednostkowy
x = np.zeros_like(t)
x[0] = 1
ax[5].plot(t, x)
ax[5].set_title('impuls jednostkowy')

plt.tight_layout()
plt.show()


