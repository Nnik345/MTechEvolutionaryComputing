# Plot of Tanh Activation Function

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)

th = np.tanh(x)
th_derivative = 1 - th**2

plt.figure(figsize=(8, 5))
plt.plot(x, th, label='Tanh')
plt.plot(x, th_derivative, label='Derivative', linestyle='--')
plt.title('Tanh and its derivative')
plt.xlabel('x')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show() 