import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

def sinusoid(f, fs, T=1):
    t = np.linspace(0, T, fs, endpoint=False)
    y = np.sin(2 * np.pi * f * t)
    return t, y

def interpolate(t, y, T=1):
    t_interp = np.linspace(0, T, 10 * len(t))  # Zwiększenie liczby punktów do interpolacji
    y_interp = np.interp(t_interp, t, y)
    return t_interp, y_interp

# Parametry początkowe
init_f = 5
init_fs = 100
t, y = sinusoid(init_f, init_fs)
t_int, y_int = interpolate(t, y)

# Tworzenie figure i osi
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
scatter, = plt.plot(t, y, 'o', label='Original')
line_interp, = plt.plot(t_int, y_int, '-', label='Interpolated')
plt.title('Sygnał sinusoidalny')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

# Ustawienie suwaków
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axfs = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

# Tworzenie suwaków
freq_slider = Slider(ax=axfreq, label='f (Częstotliwość)', valmin=1, valmax=50, valinit=init_f)
fs_slider = Slider(ax=axfs, label='fs (Częstotliwość próbkowania)', valmin=10, valmax=500, valinit=init_fs)

# Funkcja aktualizująca dane wykresu
def update(val):
    f = freq_slider.val
    fs = int(fs_slider.val)
    t, y = sinusoid(f, fs)
    t_int, y_int = interpolate(t, y)
    scatter.set_data(t, y)
    line_interp.set_data(t_int, y_int)
    ax.relim()
    ax.autoscale_view()

# Połączenie funkcji aktualizacji z suwakami
freq_slider.on_changed(update)
fs_slider.on_changed(update)

plt.show()