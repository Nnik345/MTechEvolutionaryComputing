import numpy as np
import scipy.stats as stats

uniform_data = stats.uniform.rvs(size=1000)

print("Uniform Distribution Analysis")
print("=" * 40)
print(f"Generated {len(uniform_data)} values from Uniform distribution (0, 1)")
print()

mean_value = np.mean(uniform_data)
print(f"Mean: {mean_value:.4f}")

median_value = np.median(uniform_data)
print(f"Median: {median_value:.4f}")

hist, bin_edges = np.histogram(uniform_data, bins=20)
mode_bin_index = np.argmax(hist)
mode_value = (bin_edges[mode_bin_index] + bin_edges[mode_bin_index + 1]) / 2
print(f"Mode (approximate): {mode_value:.4f}")

print()
print("Theoretical values for Uniform(0,1):")
print(f"Theoretical Mean: 0.5")
print(f"Theoretical Median: 0.5")
print(f"Theoretical Mode: Any value in [0,1] (uniform distribution has no unique mode)")