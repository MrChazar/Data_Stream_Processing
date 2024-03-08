import scipy as scp
import numpy as np
import LAB_1.exercise_1 as ex1
import matplotlib.pyplot as plt

"""
Przygotuj w Pythonie kod, który wyznaczy z definicji widmową gęstość mocy. WGM
z definicji wyznaczana jest z zależności:
"""

# widmowa gęstość mocy w scipy

# Obliczenie PSD
def psd(x, fs):
    # Autokorelacja sygnału
    Rxx = scp.signal.correlate(x, x, mode='same') / len(x)

    # Transformata Fouriera autokorelacji
    frequencies, Pxx = scp.signal.periodogram(Rxx, fs)

    return frequencies, Pxx
