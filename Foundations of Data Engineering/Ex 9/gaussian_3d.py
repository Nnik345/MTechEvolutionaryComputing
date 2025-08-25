import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

mu_x, mu_y = 0, 0
sigma_x, sigma_y = 1, 1

Z = (1/(2*np.pi*sigma_x*sigma_y)) * np.exp(-(((X-mu_x)**2)/(2*sigma_x**2) + ((Y-mu_y)**2)/(2*sigma_y**2)))

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Probability Density')
ax.set_title('3D Gaussian Distribution')

plt.show()
