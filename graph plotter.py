import numpy as np 
from numpy import sqrt
import matplotlib.pyplot as plt

def plot_function(f, x_min=-10, x_max=10, y_min=-10, y_max=10, resolution=10000):
    x = np.linspace(x_min, x_max, resolution)
    y = np.array([f(xi) for xi in x])  # Vermeidung von Polstellen

    plt.figure(figsize=(6, 6))  # Quadrat
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.plot(x, y, label=f.__name__, color="blue")
    plt.legend()
    plt.show()

# Beispiel: f(x) = 1/x mit Polstelle bei x = 0
def f_halve_cirle(x):
    a =
    b =

    return a * sqrt(25 - (x * x))

plot_function(f_halve_cirle)
