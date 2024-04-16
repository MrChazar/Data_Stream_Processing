"""
Zad. 1 Przygotuj kod w Pythonie, który wyświetli następujące typy falek: Haar, Daubechies,
Symlets, Coiflets, Biortogonalna, Gaussian, Meksykański kapelusz, Morleta. W celu
rozwiązania zadania można wykorzystać pakiet pywt
"""

import numpy as np
import matplotlib.pyplot as plt
import pywt


def sinusoid(f, fs, T=1):
    t = np.linspace(0, T, fs, endpoint=False)
    y = np.sin(2 * np.pi * f * t)
    return t, y

def plot_wavelets():
    wavelet_types = ['haar', 'db1', 'sym2', 'coif1', 'bior1.1','morl', 'mexh']

    fig, ax = plt.subplots(len(wavelet_types), 1, figsize=(8, 12))

    for i, wt in enumerate(wavelet_types):
        print(f"\n{wt.upper()} Wavelet:")
        print("-" * 20)
        try:
            if wt in ['morl', 'mexh']:
                wavelet_function = pywt.ContinuousWavelet(wt).wavefun(level=5)
            else:
                wavelet = pywt.Wavelet(wt)
                wavelet_function = wavelet.wavefun()

            t = np.linspace(0, 1, len(wavelet_function[0]))

            ax[i].plot(t, wavelet_function[0], label="Aproksymacja")
            ax[i].plot(t, wavelet_function[1], label="Szczegół")
            ax[i].set_title(f"{wt.upper()} Falka")
            ax[i].set_xlabel("Czas")
            ax[i].set_ylabel("Amplituda")
            ax[i].legend()
            ax[i].grid(True)

        except ValueError:
            print(f"{wt} - This wavelet does not exist.")
        except Exception as e:
            print(f"An error occurred while processing {wt}: {e}")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_wavelets()