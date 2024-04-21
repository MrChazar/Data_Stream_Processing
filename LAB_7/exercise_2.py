"""
Zad. 2 Przygotuj kod w Pythonie, który wyświetli falkę Daubechies w różnych wersjach (db1,
db2, itd.) i dla różnych parametrów.
"""

import numpy as np
import matplotlib.pyplot as plt
import pywt
import matplotlib
matplotlib.use('TkAgg')

def plot_daubechies_wavelets():
    wavelet_family = 'db'
    wavelet_versions = [1, 2, 3, 4, 5]  # Różne wersje falki Daubechies (db1, db2, itd.)
    scales = [1, 2, 3]  # Różne parametry skali (rozmiaru okna)

    fig, axes = plt.subplots(len(wavelet_versions), len(scales), figsize=(12, 8))

    for i, version in enumerate(wavelet_versions):
        for j, scale in enumerate(scales):
            wavelet_name = f"{wavelet_family}{version}"
            try:
                wavelet = pywt.Wavelet(wavelet_name)
                wavelet_function = wavelet.wavefun(level=scale)
                t = np.linspace(0, 1, len(wavelet_function[0]))

                axes[i, j].plot(t, wavelet_function[0], label="Aproksymacja")
                axes[i, j].plot(t, wavelet_function[1], label="Detale")
                axes[i, j].set_title(f"{wavelet_name} (Skala={scale})")
                axes[i, j].set_xlabel("Czas")
                axes[i, j].set_ylabel("Amplituda")
                axes[i, j].legend()
                axes[i, j].grid(True)

            except ValueError:
                print(f"{wavelet_name} - This wavelet does not exist.")
            except Exception as e:
                print(f"An error occurred while processing {wavelet_name}: {e}")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_daubechies_wavelets()

