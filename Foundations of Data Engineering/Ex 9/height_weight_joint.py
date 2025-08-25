import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

heights = np.array([160, 165, 170, 175, 180])
weights = np.array([50, 55, 60, 65, 70, 75, 80])

X, Y = np.meshgrid(heights, weights)

mu = [np.mean(heights), np.mean(weights)]

sigma = [[25, 15],
         [15, 50]]

rv = multivariate_normal(mean=mu, cov=sigma)
pos = np.dstack((X, Y))
Z = rv.pdf(pos)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('Height (cm)')
ax.set_ylabel('Weight (kg)')
ax.set_zlabel('Probability Density')
ax.set_title('Joint PDF of Height and Weight')

plt.show()
