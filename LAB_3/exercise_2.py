import numpy as np
import matplotlib.pyplot as plt
import LAB_1.exercise_1 as ex1

"""
Zad. 2 Przygotuj w Pythonie kod, który wyznaczy z definicji widmową gęstość mocy. WGM
z definicji wyznaczana jest z zależności:
"""


def power_spectral_density(signal, fs):
    N = len(signal) # Długość sygnału
    freqs = np.fft.fftfreq(N, 1/fs) # Wygenerowania wartości częstotliwości dla analizowanej transformaty Fouriera, 1/fs to odwrotność okresu próbkowania
    fft_vals = np.fft.fft(signal) # Obliczenie wartości transformaty Fouriera
    psd = np.abs(fft_vals)**2 / (fs*N) # Obliczenie wimdowej gęstości mocy (PSD)
    return freqs, psd








# Nie działa dla moich sygnałów
def power_spectral_density_(f, signal, Fs):
    t = 1 / Fs  # Sample spacing
    T = len(signal)  # Signal duration
    auto_corr = np.correlate(signal, signal, mode='full')
    s = np.cumsum([auto_corr[i] * np.exp(-1j * 2 * np.pi * f * i * t) for i in range(T)])
    return t ** 2 / T * np.abs(s) ** 2

