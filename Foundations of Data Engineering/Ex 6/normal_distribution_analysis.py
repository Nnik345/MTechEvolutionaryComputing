import numpy as np
import scipy.stats as stats

normal_data = stats.norm.rvs(size=1000)

print("Normal Distribution Analysis")
print("=" * 40)
print(f"Generated {len(normal_data)} values from Normal distribution (μ=0, σ=1)")
print()

mean_value = np.mean(normal_data)
print(f"Mean: {mean_value:.4f}")

median_value = np.median(normal_data)
print(f"Median: {median_value:.4f}")

hist, bin_edges = np.histogram(normal_data, bins=20)
mode_bin_index = np.argmax(hist)
mode_value = (bin_edges[mode_bin_index] + bin_edges[mode_bin_index + 1]) / 2
print(f"Mode (approximate): {mode_value:.4f}")

print()
print("Theoretical values for Normal(0,1):")
print(f"Theoretical Mean: 0.0")
print(f"Theoretical Median: 0.0")
print(f"Theoretical Mode: 0.0")