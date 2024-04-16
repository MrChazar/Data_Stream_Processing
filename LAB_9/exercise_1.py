"""
Zad. 1 Przygotuj kod w Pythonie, które wyznacza wartości następujących miar jakości
sygnałów:

gdzie: s to sygnał, n to szum, smax to maksymalna wartość sygnału, y to sygnał z zakłóceniem
"""
import matplotlib.pyplot as plt
import numpy as np
import LAB_1.exercise_1 as ex1


def SNR(s, n):
    signal_power = np.sum(np.abs(s))
    noise_power = np.sum(np.abs(n))
    snr = 20 * np.log10(signal_power / noise_power)
    return snr

def MSE(s, n):
    return np.square(s - n).mean()

def PSNR(s, n):
    smax = np.max(s)
    psnr = 20 * np.log10(smax/ MSE(s, n) ** 1/2)
    return psnr



# paramettry
fs = 1000  # Częstotliwość próbkowania
T = 1     # Czas trwania sygnału w sekundach
t = np.linspace(0, T, T*fs, endpoint=False)
f = 5 # częstotliwość sygnału

# generowanie sygnału
# sinus
y = ex1.sin(f+3, t)

# generowanie sygnału hałasu
noise = ex1.sin(f+12, t)

added_sign = y + noise

plt.plot(t, y, color = 'red')
plt.plot(t, noise, color='blue')
plt.plot(t, added_sign, color='orange')
plt.show()

print(f"SNR wynosi: {SNR(added_sign, noise)}")
print(f"PSNR wynosi: {PSNR(added_sign, noise)}")
print(f"MSE wynosi: {MSE(added_sign, noise)}")

a = np.arange(1, 10, 1)
print(a)
b = np.arange(10, 1, -1)
print(b)
print(MSE(a, b))