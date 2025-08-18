# Plot of e^-x

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
y = np.exp(-x)
dy = -np.exp(-x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$e^{-x}$')
plt.plot(x, dy, label=r"Derivative: $-e^{-x}$", linestyle='--')
plt.title(r'Plot of $e^{-x}$ and its derivative')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
