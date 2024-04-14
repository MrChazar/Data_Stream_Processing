"""
Zad. 3 Przygotuj kod w Pythonie, który dokona dekompozycji sygnału świergotliwego (chirp
signal) z wykorzystaniem trzech różnych falek. Uzyskane wyniki wyświetl w czytelnej
postaci.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.signal import chirp
import pywt
from matplotlib.widgets import Slider
matplotlib.use('TkAgg')

def update(val):
    f0 = sf0.val
    f1 = sf1.val
    signal = chirp(t, f0=f0, f1=f1, t1=1, method='linear')

    # Uaktualnij oryginalny sygnał na wykresie
    line0.set_ydata(signal)

    # Uaktualnij dekompozycję dla każdej falki
    for i, wavelet_name in enumerate(wavelet_names):
        wavelet = pywt.Wavelet(wavelet_name)
        coeffs = pywt.wavedec(signal, wavelet, level=num_levels)
        reconstructed_signal = pywt.waverec(coeffs, wavelet)
        lines[i].set_ydata(reconstructed_signal)

    fig.canvas.draw_idle()


# Generowanie sygnału chirp
t = np.linspace(0, 1, 1000)
initial_f0 = 10
initial_f1 = 100
signal = chirp(t, f0=initial_f0, f1=initial_f1, t1=1, method='linear')

# Dekompozycja sygnału za pomocą trzech różnych falek
wavelet_names = ['db1', 'sym2', 'coif1']
num_levels = 5  # Liczba poziomów dekompozycji

fig, axes = plt.subplots(len(wavelet_names) + 1, 1, figsize=(10, 12))
plt.subplots_adjust(bottom=0.25)

# Wyświetlanie oryginalnego sygnału
line0, = axes[0].plot(t, signal, label="Oryginalny Sygnał")
axes[0].set_title("Oryginalny Chirp Sygnał")
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Amplitude")
axes[0].legend()
axes[0].grid(True)

lines = []
# Dekompozycja sygnału za pomocą różnych falek
for i, wavelet_name in enumerate(wavelet_names, start=1):
    wavelet = pywt.Wavelet(wavelet_name)
    coeffs = pywt.wavedec(signal, wavelet, level=num_levels)
    reconstructed_signal = pywt.waverec(coeffs, wavelet)
    line, = axes[i].plot(t, reconstructed_signal, label=f"{wavelet_name.capitalize()} Dekopomonowany")
    lines.append(line)
    axes[i].set_title(f"{wavelet_name.capitalize()} Dekomponowany sygnał")
    axes[i].set_xlabel("Time")
    axes[i].set_ylabel("Amplitude")
    axes[i].legend()
    axes[i].grid(True)

# Dodanie sliderów
axcolor = 'lightgoldenrodyellow'
axf0 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axf1 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

sf0 = Slider(axf0, 'F0', 0.1, 30.0, valinit=initial_f0)
sf1 = Slider(axf1, 'F1', 20.0, 200.0, valinit=initial_f1)

sf0.on_changed(update)
sf1.on_changed(update)

plt.show()