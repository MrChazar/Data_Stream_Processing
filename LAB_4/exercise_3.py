import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import LAB_4.exercise_1 as ex1

"""
Zad. 3 Przygotuj w Pythonie kod, który dokona interpolacji punktów z zadania 1 z
wykorzystaniem równania Whittakera–Shannona:
gdzie sinc to funkcja sinus cardinalis (funkcja sinc dostępna jest m.in. w pakiecie scipy).
Wyświetl przebieg błędu interpolacji z wykorzystaniem równania Whittakera–Shannona.
"""

def sinc_interp(t, y, t_interp):
    y_interp = np.zeros(len(t_interp))
    for i in range(len(t_interp)):
        y_interp[i] = np.sum(y * np.sinc((t_interp[i] - t) / (t[1] - t[0])))
    return y_interp

# Generowanie punktów
t, y = ex1.sinusoid(1, 10, 1)

# Interpolacja sinc
t_interp = np.linspace(0, 1, 100)
y_interp_sinc = sinc_interp(t, y, t_interp)

# Wyświetlanie interpolacji sinc
plt.scatter(t, y, c='r', label='Punkty')
plt.plot(t_interp, y_interp_sinc, c='b', label='Interpolacja sinc')
plt.title('Interpolacja sinc')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()


# Obliczanie błędu interpolacji
error_sinc = np.sum(np.abs(y_interp_sinc - t_interp))
print(f'Błąd interpolacji sinc: {error_sinc}')

# wizuwalizacja błędu interpolacji
plt.scatter(t_interp, np.abs(y_interp_sinc - t_interp), label='Błąd interpolacji sinc')
plt.title('Błąd interpolacji sinc')
plt.xlabel('t')
plt.ylabel('y')
plt.show()
plt.show()

