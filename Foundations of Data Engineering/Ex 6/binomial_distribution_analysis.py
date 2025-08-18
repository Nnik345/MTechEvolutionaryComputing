import numpy as np
import scipy.stats as stats
from collections import Counter

n_trials = 10
p_success = 0.5
binomial_data = stats.binom.rvs(n=n_trials, p=p_success, size=1000)

print("Binomial Distribution Analysis")
print("=" * 40)
print(f"Generated {len(binomial_data)} values from Binomial distribution (n={n_trials}, p={p_success})")
print()

mean_value = np.mean(binomial_data)
print(f"Mean: {mean_value:.4f}")

median_value = np.median(binomial_data)
print(f"Median: {median_value:.4f}")

counter = Counter(binomial_data)
mode_value = counter.most_common(1)[0][0]
mode_frequency = counter.most_common(1)[0][1]
print(f"Mode: {mode_value} (appears {mode_frequency} times)")

print()
print("Theoretical values for Binomial(n=10, p=0.5):")
print(f"Theoretical Mean: n*p = {n_trials * p_success}")
print(f"Theoretical Median: ≈ {n_trials * p_success:.1f}")
print(f"Theoretical Mode: ≈ {n_trials * p_success:.1f}")

print()
print("Value frequency distribution:")
for value, count in sorted(counter.items()):
    print(f"Value {value}: {count} times") 