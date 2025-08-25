import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm, boxcox

a = 5
data = skewnorm.rvs(a, loc=0, scale=1, size=1000, random_state=42)

data_shifted = data - np.min(data) + 1e-6

data_boxcox, lam = boxcox(data_shifted)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist(data_shifted, bins=30, color='skyblue', edgecolor='black', density=True)
axes[0].set_title("Original Skewed Data")

axes[1].hist(data_boxcox, bins=30, color='lightgreen', edgecolor='black', density=True)
axes[1].set_title(f"Box-Cox Normalized Data (λ={lam:.2f})")

plt.tight_layout()
plt.show()
