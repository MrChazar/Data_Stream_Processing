import numpy as np
import matplotlib.pyplot as plt
"""
Zad. 1 Przygotuj w Pythonie kod, który wygeneruje sygnał sinusoidalny o możliwej do zmiany
częstotliwości f oraz częstotliwości próbkowania fs. Przygotuj wykres z sygnałem i próbkami
pobranymi z zadaną częstotliwością próbkowania fs.
"""

def sinusoid(f, fs, T):
    t = np.linspace(0, T, fs, endpoint=False)
    y = np.sin(2*np.pi*f*t)
    return t, y


t,y = sinusoid(1, 10, 1)
plt.plot(t,y,'o')
plt.title('Sygnał sinusoidalny')
plt.xlabel('t')
plt.ylabel('y')
plt.show()

