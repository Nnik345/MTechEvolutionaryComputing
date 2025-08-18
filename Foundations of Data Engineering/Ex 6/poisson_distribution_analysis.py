import numpy as np
import scipy.stats as stats
from collections import Counter

lambda_param = 5
poisson_data = stats.poisson.rvs(mu=lambda_param, size=1000)

print("Poisson Distribution Analysis")
print("=" * 40)
print(f"Generated {len(poisson_data)} values from Poisson distribution (λ={lambda_param})")
print()

mean_value = np.mean(poisson_data)
print(f"Mean: {mean_value:.4f}")

median_value = np.median(poisson_data)
print(f"Median: {median_value:.4f}")

counter = Counter(poisson_data)
mode_value = counter.most_common(1)[0][0]
mode_frequency = counter.most_common(1)[0][1]
print(f"Mode: {mode_value} (appears {mode_frequency} times)")

print()
print("Theoretical values for Poisson(λ=5):")
print(f"Theoretical Mean: λ = {lambda_param}")
print(f"Theoretical Median: ≈ {lambda_param:.1f}")
print(f"Theoretical Mode: ≈ {lambda_param:.1f}")

print()
print("Value frequency distribution:")
for value, count in sorted(counter.items()):
    print(f"Value {value}: {count} times") 