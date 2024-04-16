"""
Zad. 1 Przygotuj kod w Pythonie, który wygeneruje spektrogramy dla sygnałów z zadania 1
na liście 1.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
from matplotlib.widgets import Slider
import matplotlib
import LAB_1.exercise_1 as ex1  # Zakładając, że funkcje w module są poprawnie zdefiniowane
matplotlib.use('TkAgg')
# Inicjalizacja parametrów
fs = 1000  # Częstotliwość próbkowania
T = 1  # Czas trwania sygnału w sekundach
t = np.linspace(0, T, T * fs, endpoint=False)
initial_freq = 5


def update(val):
    f = sfreq.val
    y_sin = ex1.sin(f, t)
    y_squ = ex1.signal_square(f, t)
    y_saw = ex1.signal_sawtooth(f, t)
    y_chir = ex1.signal_chirp(f0, f1, t, T)
    y_sup = np.sin(2 * np.pi * f * t) + np.cos(2 * np.pi * 2 * f * t)

    signals = [y_sin, y_squ, y_saw, y_chir, y_sup]

    for i, signal in enumerate(signals):
        f, t_spec, Sxx = spectrogram(signal, fs)
        axes[i].cla()
        axes[i].pcolormesh(t_spec, f, 10 * np.log10(Sxx), shading='gouraud')
        axes[i].set_ylabel('Frequency [Hz]')
        axes[i].set_title(signal_titles[i])

    fig.canvas.draw_idle()


# Generowanie sygnałów
y_sin = ex1.sin(initial_freq, t)
y_squ = ex1.signal_square(initial_freq, t)
y_saw = ex1.signal_sawtooth(initial_freq, t)
f0 = 1
f1 = 100
y_chir = ex1.signal_chirp(f0, f1, t, T)
y_sup = np.sin(2 * np.pi * initial_freq * t) + np.cos(2 * np.pi * 2 * initial_freq * t)

# Tytuły dla spektrogramów
signal_titles = ['Sinus', 'Square', 'Sawtooth', 'Chirp', 'Super pozycja']

# Tworzenie subplots dla spektrogramów
fig, axes = plt.subplots(5, 1, figsize=(14, 10))

# Plot initial spectrograms
signals = [y_sin, y_squ, y_saw, y_chir, y_sup]
for i, signal in enumerate(signals):
    f, t_spec, Sxx = spectrogram(signal, fs)
    axes[i].pcolormesh(t_spec, f, 10 * np.log10(Sxx), shading='gouraud')
    axes[i].set_ylabel('Frequency [Hz]')
    axes[i].set_title(signal_titles[i])


# Add frequency slider
axfreq = plt.axes([0.25, 0.0001, 0.50, 0.03], facecolor='lightgoldenrodyellow')
sfreq = Slider(axfreq, 'Frequency', 1, 100, valinit=initial_freq)
sfreq.on_changed(update)

plt.tight_layout()
plt.show()

