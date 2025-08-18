import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mu = 50  # mean
sigma = 15  # standard deviation
n_samples = 1000

# Generate random numbers from a normal distribution
random_numbers = norm.rvs(loc=mu, scale=sigma, size=n_samples)

# Plot histogram (PDF) and theoretical PDF
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
count, bins, ignored = plt.hist(random_numbers, bins=30, color='skyblue', edgecolor='black', density=True, alpha=0.6, label='Empirical PDF')

# Theoretical PDF
x = np.linspace(min(bins), max(bins), 1000)
pdf = norm.pdf(x, mu, sigma)
plt.plot(x, pdf, 'r-', lw=2, label='Theoretical PDF')
plt.title('Normal Distribution (mu=50, sigma=15)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()

# Plot empirical CDF and theoretical CDF
plt.subplot(1, 2, 2)
sorted_numbers = np.sort(random_numbers)
cdf_empirical = np.arange(1, n_samples + 1) / n_samples
plt.plot(sorted_numbers, cdf_empirical, marker='.', linestyle='none', label='Empirical CDF')

# Theoretical CDF
cdf_theoretical = norm.cdf(x, mu, sigma)
plt.plot(x, cdf_theoretical, 'r-', lw=2, label='Theoretical CDF')
plt.title('CDF of Normal Distribution (mu=50, sigma=15)')
plt.xlabel('Value')
plt.ylabel('CDF')
plt.legend()

plt.tight_layout()
plt.show()
