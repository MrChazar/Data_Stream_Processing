import numpy as np
import matplotlib.pyplot as plt
import scipy as scp
import LAB_4.exercise_1 as ex1

"""
Zad. 2 Przygotuj w Pythonie kod, który dokona odcinkami liniowej interpolacji (np. funkcją
piecewise dostępną w pakiecie numpy) danych zebranych w zadaniu 1. Wyświetl przebieg
błędu interpolacji.
"""

t,y = ex1.sinusoid(1, 10, 1)
t_interp = np.linspace(0,1,100)
y_interp = np.interp(t_interp, t, y)
plt.scatter(t,y, c='r')
plt.plot(t_interp, y_interp, c='b')
plt.title('Interpolacja liniowa')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['Punkty', 'Interpolacja liniowa'])
plt.show()