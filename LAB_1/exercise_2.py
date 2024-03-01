import pandas as pd
import matplotlib.pyplot as plt

"""
Zad. 2 Korzystając z funkcji read_csv dostępnej w bibliotece pandas wczytaj wybrane plik
CSV z zapisem dowolnego sygnału.
"""

data_frame = pd.read_csv('signal.csv')
plt.plot(data_frame['Czas'], data_frame["Wartość_sygnału"])
plt.show()