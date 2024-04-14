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

t, y = ex1.sinusoid(5, 100, 1)

t_interp = np.linspace(0, 1, 1000)
y_interp_sinc = sinc_interp(t, y, t_interp)

t_high_res, y_high_res = ex1.sinusoid(1, 1000, 1)  # 1000 Hz to wysoka częstotliwość próbkowania

y_high_interp = np.interp(t_interp, t_high_res, y_high_res)

# Obliczanie błędu interpolacji
error_sinc = np.abs(y_interp_sinc - y_high_interp)
print(f"Błąd interpolacji wynosi: {np.mean(error_sinc)}")

fig, ax = plt.subplots(2, 1, figsize=(12, 10))

ax[0].scatter(t, y, c='r', label='Punkty oryginalne')
ax[0].plot(t_interp, y_interp_sinc, c='b', label='Interpolacja sinc')
ax[0].set_title('Interpolacja sinc')
ax[0].set_xlabel('Czas [s]')
ax[0].set_ylabel('Amplituda')
ax[0].legend()

ax[1].plot(t_interp, error_sinc, label='Błąd interpolacji sinc', color='orange')
ax[1].set_title('Błąd interpolacji sinc')
ax[1].set_xlabel('Czas [s]')
ax[1].set_ylabel('Błąd')
ax[1].legend()

plt.tight_layout()
plt.show()