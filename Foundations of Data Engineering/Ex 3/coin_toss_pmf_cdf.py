import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Number of coin tosses
n = 100
# Probability of heads for a fair coin
p = 0.5

# Possible values for number of heads (X)
x = np.arange(0, n + 1)

# PMF: Probability Mass Function
pmf = binom.pmf(x, n, p)

# CDF: Cumulative Distribution Function
cdf = binom.cdf(x, n, p)

# Plot PMF
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.stem(x, pmf, basefmt=" ")
plt.title('PMF of Number of Heads in 100 Coin Tosses')
plt.xlabel('Number of Heads (X)')
plt.ylabel('P(X = x)')
plt.grid(True)

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf, drawstyle='steps-post')
plt.title('CDF of Number of Heads in 100 Coin Tosses')
plt.xlabel('Number of Heads (X)')
plt.ylabel('P(X ≤ x)')
plt.grid(True)

plt.tight_layout()
plt.show() 