# Plot of Sigmoid Activation Function

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

x = np.linspace(-8, 8, 400)
y = sigmoid(x)
dy = sigmoid_derivative(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Sigmoid')
plt.plot(x, dy, label='Derivative', linestyle='--')
plt.title('Plot of Sigmoid and its derivative')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show() 