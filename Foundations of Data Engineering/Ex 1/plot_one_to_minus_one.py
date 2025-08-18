# Plot of 1-x for 0<=x<=1, 1+x for -1<=x<=0, 0 for all other values of x

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 400)
y = np.piecewise(x, [x < -1, (x >= -1) & (x < 0), (x >= 0) & (x <= 1), x > 1], [lambda x: 0, lambda x: 1 + x, lambda x: 1 - x, lambda x: 0])
dy = np.piecewise(x, [x < -1, (x >= -1) & (x < 0), (x >= 0) & (x <= 1), x > 1], [lambda x: 0, lambda x: 1, lambda x: -1, lambda x: 0])

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Piecewise function')
plt.plot(x, dy, label='Derivative', linestyle='--')
plt.title('Plot of piecewise function and its derivative')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show() 