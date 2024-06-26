
"""
Zad. 1 Przygotuj w Pythonie kod, który wygeneruje sygnał sinusoidalny o możliwej do zmiany
częstotliwości f oraz częstotliwości próbkowania fs. Przygotuj wykres z sygnałem i próbkami
pobranymi z zadaną częstotliwością próbkowania fs.
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.widgets import Slider
matplotlib.use('TkAgg')

def sinusoid(f, fs, T=1):
    t = np.linspace(0, T, fs, endpoint=False)
    y = np.sin(2 * np.pi * f * t)
    return t, y
"""

# Parametry początkowe
init_f = 5
init_fs = 100
t, y = sinusoid(init_f, init_fs)

# Tworzenie figure i osi
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
scatter, = plt.plot(t, y, 'o')
plt.title('Sygnał sinusoidalny')
plt.xlabel('t')
plt.ylabel('y')

# Ustawienie suwaków
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axfs = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor=axcolor)

# Tworzenie suwaków
freq_slider = Slider(ax=axfreq, label='f (Częstotliwość)', valmin=1, valmax=50, valinit=init_f)
fs_slider = Slider(ax=axfs, label='fs (Częstotliwość próbkowania)', valmin=10, valmax=500, valinit=init_fs, orientation="vertical")

# Funkcja aktualizująca dane wykresu
def update(val):
    f = freq_slider.val
    fs = int(fs_slider.val)
    t, y = sinusoid(f, fs)
    scatter.set_data(t, y)
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.1, 1.1)


# Połączenie funkcji aktualizacji z suwakami
freq_slider.on_changed(update)
fs_slider.on_changed(update)


plt.show()
"""