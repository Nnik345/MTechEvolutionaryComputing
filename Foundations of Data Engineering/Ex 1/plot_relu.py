# Plot of ReLU Activation Function

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
y = np.maximum(0, x)
dy = np.where(x > 0, 1, 0)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='ReLU')
plt.plot(x, dy, label='Derivative', linestyle='--')
plt.title('Plot of ReLU and its derivative')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show() 