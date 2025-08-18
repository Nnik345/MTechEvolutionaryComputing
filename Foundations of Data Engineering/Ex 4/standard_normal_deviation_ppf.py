from scipy.stats import norm

# Central 95% interval
lower = norm.ppf(0.025)  # -x1
upper = norm.ppf(0.975)  # x1

print(f"x1 = {upper:.4f}, -x1 = {lower:.4f}")

# Central 99% interval
lower = norm.ppf(0.005) # -x2
upper = norm.ppf(0.995) # x2

print(f"x2 = {upper:.4f}, -x2 = {lower:.4f}")