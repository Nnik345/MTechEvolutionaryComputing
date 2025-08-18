import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mean = 0
stds = [1, 0.5, 2, 3]
colors = ['blue', 'green', 'red', 'purple']
labels = [f'std = {s}' for s in stds]

x = np.linspace(-10, 10, 1000)

plt.figure(figsize=(10, 6))

for std, color, label in zip(stds, colors, labels):
    y = norm.pdf(x, mean, std)
    plt.plot(x, y, label=label, color=color)

plt.title('Normal Distributions with Mean = 0 and Different Standard Deviations')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
