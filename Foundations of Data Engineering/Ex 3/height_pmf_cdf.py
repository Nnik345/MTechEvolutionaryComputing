import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

heights = np.array([165, 170, 175, 180, 170, 165, 170, 175, 170, 160])

# Compute PMF
height_counts = Counter(heights)
unique_heights = np.array(sorted(height_counts.keys()))
pmf = np.array([height_counts[h] / len(heights) for h in unique_heights])

# Compute CDF
cdf = np.cumsum(pmf)

# Plot PMF
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.stem(unique_heights, pmf, basefmt=" ")
plt.title("PMF of Heights")
plt.xlabel("Height (cm)")
plt.ylabel("P(Height = h)")
plt.grid(True)

# Plot CDF
plt.subplot(1, 2, 2)
plt.step(unique_heights, cdf, where="post")
plt.title("CDF of Heights")
plt.xlabel("Height (cm)")
plt.ylabel("P(Height ≤ h)")
plt.grid(True)

plt.tight_layout()
plt.show()
