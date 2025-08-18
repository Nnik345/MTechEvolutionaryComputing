import numpy as np
import scipy.stats as stats

exponential_data = stats.expon.rvs(size=1000)

print("Exponential Distribution Analysis")
print("=" * 40)
print(f"Generated {len(exponential_data)} values from Exponential distribution (λ=1)")
print()

mean_value = np.mean(exponential_data)
print(f"Mean: {mean_value:.4f}")

median_value = np.median(exponential_data)
print(f"Median: {median_value:.4f}")

hist, bin_edges = np.histogram(exponential_data, bins=20)
mode_bin_index = np.argmax(hist)
mode_value = (bin_edges[mode_bin_index] + bin_edges[mode_bin_index + 1]) / 2
print(f"Mode (approximate): {mode_value:.4f}")

print()
print("Theoretical values for Exponential(λ=1):")
print(f"Theoretical Mean: 1.0")
print(f"Theoretical Median: ln(2) ≈ 0.693")
print(f"Theoretical Mode: 0.0")
