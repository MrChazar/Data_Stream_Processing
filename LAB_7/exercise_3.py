"""
Zad. 3 Przygotuj kod w Pythonie, który dokona dekompozycji sygnału świergotliwego (chirp
signal) z wykorzystaniem trzech różnych falek. Uzyskane wyniki wyświetl w czytelnej
postaci.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pywt
from scipy.signal import chirp
from matplotlib.widgets import Slider

matplotlib.use('TkAgg')


def update(val):
    f0 = sf0.val
    f1 = sf1.val

    # Generowanie sygnału chirp
    t = np.linspace(0, 1, 1000)
    signal = chirp(t, f0=f0, f1=f1, t1=1, method='linear')

    # Dekompozycja sygnału za pomocą trzech różnych falek
    for i, wavelet_name in enumerate(wavelet_names):
        wavelet = pywt.Wavelet(wavelet_name)
        coeffs = pywt.wavedec(signal, wavelet, level=num_levels)
        # Uaktualnij efekt dekompozycji na wykresie
        for j, coeff in enumerate(coeffs):
            lines[i][j].set_ydata(coeff)

    fig.canvas.draw_idle()


# Dekompozycja sygnału za pomocą trzech różnych falek
wavelet_names = ['db1', 'sym2', 'coif1']
num_levels = 5  # Liczba poziomów dekompozycji

fig, axes = plt.subplots(len(wavelet_names), num_levels + 1, figsize=(15, 10))  # Zwiększenie wysokości figury
fig.suptitle("Dekompozycja sygnału za pomocą trzech różnych falek")
plt.subplots_adjust(bottom=0.3, hspace=0.5, wspace=0.5)  # Dostosowanie odstępów między subplotami

lines = []
# Dekompozycja sygnału za pomocą różnych falek
for i, wavelet_name in enumerate(wavelet_names):
    # Wygenerowanie oryginalnego sygnału chirp dla aktualnych wartości częstotliwości
    t = np.linspace(0, 1, 1000)
    signal = chirp(t, f0=10, f1=100, t1=1, method='linear')

    wavelet = pywt.Wavelet(wavelet_name)
    coeffs = pywt.wavedec(signal, wavelet, level=num_levels)
    lines.append([])
    for j, coeff in enumerate(coeffs):
        # Wyświetlanie efektu dekompozycji
        line, = axes[i, j].plot(t[:len(coeff)], coeff)
        lines[i].append(line)
        axes[i, j].set_ylabel("Amplituda")
        axes[i, j].set_title(f"{wavelet_name.capitalize()} Level {j}")

# Dodanie sliderów
axcolor = 'lightgoldenrodyellow'
axf0 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axf1 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

sf0 = Slider(axf0, 'Czas', 0.1, 30.0, valinit=10)
sf1 = Slider(axf1, 'Amplituda', 20.0, 200.0, valinit=100)

sf0.on_changed(update)
sf1.on_changed(update)

plt.show()
