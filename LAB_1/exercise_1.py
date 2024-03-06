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
f = 5 # częstotliwość sygnału

# generowanie sygnału
# sinus
y = np.sin(2*np.pi*f*t)
ax[0].plot(t, y)
ax[0].set_title('sinus')

# prostokąt
y = scp.signal.square(2*np.pi*f*t)
ax[1].plot(t, y)
ax[1].set_title('prostokąt')

# piłokształtny
y = scp.signal.sawtooth(2*np.pi*f*t)
ax[2].plot(t, y)
ax[2].set_title('piłokształtny')

# świergotliwy
f0 = 1
f1 = 100
y = scp.signal.chirp(t, f0, T, f1)
ax[3].plot(t, y)
ax[3].set_title('świergotliwy')

# Superpozycja funkcji sinus i cosinus z samodzielnie dobranymi parametrami
y = np.sin(2*np.pi*f*t) + np.cos(2*np.pi*2*f*t)
ax[4].plot(t, y)
ax[4].set_title('superpozycja sinus i cosinus')

# Impuls jednostkowy
y = scp.signal.unit_impulse(t.shape, idx='mid')
ax[5].plot(t, y)
ax[5].set_title('impuls jednostkowy')

plt.tight_layout()
plt.show()


