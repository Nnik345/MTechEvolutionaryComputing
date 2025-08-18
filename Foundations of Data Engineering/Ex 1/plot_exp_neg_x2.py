# Plot of e^-x^2

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 400)
y = np.exp(-x**2)
dy = -2 * x * np.exp(-x**2)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$e^{-x^2}$')
plt.plot(x, dy, label=r"Derivative: $-2x e^{-x^2}$", linestyle='--')
plt.title(r'Plot of $e^{-x^2}$ and its derivative')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
