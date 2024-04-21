"""
Zad. 2 Przygotuj w Pythonie kod, który wyznaczy widmo sygnału sinusoidalnego o trzech
różnych częstotliwościach przy zastosowanych oknach: Hamminga, Hanna, Blackmana oraz
Dirichleta
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.signal as signal
from matplotlib.widgets import Slider

matplotlib.use('TkAgg')

# Parametry sygnału
frequencies = [1, 2, 3]  # Częstotliwości sygnału
fs_default = 10  # Domyślna częstotliwość próbkowania
N_default = 100  # Domyślna liczba próbek

# Generowanie sygnałów sinusoidalnych
t = np.linspace(0, 1, N_default, endpoint=False)
signals = [np.sin(2 * np.pi * f * t) for f in frequencies]

# Funkcja obliczająca widmo amplitudowe
def amplitude_spectrum(signal, fs):
    freqs = np.fft.fftfreq(len(signal), 1/fs)
    fft_vals = np.fft.fft(signal)
    amplitude = np.abs(fft_vals) / len(signal)
    return freqs, amplitude

# Okna
windows = {
    "Hamming": signal.windows.hamming,
    "Hann": signal.windows.hann,
    "Blackman": signal.windows.blackman,
    "Dirichlet": signal.windows.boxcar
}

# Funkcja aktualizująca wykres
def update(val):
    freq = freq_slider.val
    N = int(N_default)
    t = np.linspace(0, 1, N, endpoint=False)
    for line, signal_data in zip(lines, signals):
        line.set_ydata(np.sin(2 * np.pi * freq * t) * window_func(N))
    fig.canvas.draw_idle()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-10, 10)

# Tworzenie wykresu
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
ax.set_xlabel('Częstotliwość [Hz]')
ax.set_ylabel('Amplituda')
ax.set_title('Widmo sygnału sinusoidalnego z różnymi oknami')

# Dodanie suwaków
axfreq = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
freq_slider = Slider(axfreq, 'Częstotliwość [Hz]', 10, 1000, valinit=frequencies[0])

# Dodanie linii na wykresie dla każdego okna
lines = []
for window_name, window_func in windows.items():
    windowed_signal = signals[0] * window_func(N_default)
    freqs, amplitude = amplitude_spectrum(windowed_signal, fs_default)
    line, = ax.plot(freqs, amplitude, label=window_name)
    lines.append(line)

# Dodanie legendy i siatki
ax.legend()
ax.grid(True)

# Podpięcie funkcji aktualizującej do suwaków
freq_slider.on_changed(update)

plt.show()