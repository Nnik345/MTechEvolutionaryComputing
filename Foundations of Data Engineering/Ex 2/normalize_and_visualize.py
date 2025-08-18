# Normalizing a Dataset and Visualizing the Range with Box Plots

import pandas as pd
import matplotlib.pyplot as plt

# Load data
file = 'D:\College\Foundations of Data Engineering\Ex 2\sample_people.csv'
df = pd.read_csv(file)

# Columns to normalize
numeric_cols = ['height', 'weight', 'age', 'salary']

# Normalize using z-score
means = df[numeric_cols].mean()
stdevs = df[numeric_cols].std()
df_norm = df.copy()
df_norm[numeric_cols] = (df[numeric_cols] - means) / stdevs

# Compute range for each column before normalization
ranges_before = {}
for col in numeric_cols:
    col_min = df[col].min()
    col_max = df[col].max()
    ranges_before[col] = col_max - col_min
    print(f"Before normalization - {col}: range={ranges_before[col]:.2f}")

# Print mean, variance, standard deviation, and range before normalization
print("\nStatistics BEFORE normalization:")
for col in numeric_cols:
    mean = df[col].mean()
    var = df[col].var()
    std = df[col].std()
    col_min = df[col].min()
    col_max = df[col].max()
    col_range = col_max - col_min
    print(f"{col}: mean={mean:.2f}, variance={var:.2f}, std={std:.2f}, range={col_range:.2f}")

# Print mean, variance, standard deviation, and range after normalization
print("\nStatistics AFTER normalization:")
for col in numeric_cols:
    mean = df_norm[col].mean()
    var = df_norm[col].var()
    std = df_norm[col].std()
    col_min = df_norm[col].min()
    col_max = df_norm[col].max()
    col_range = col_max - col_min
    print(f"{col}: mean={mean:.2f}, variance={var:.2f}, std={std:.2f}, range={col_range:.2f}")

# Subplot for comparing Box plots
plt.figure(figsize=(12, 6))

# Subplot 1: Box plot of original features (before normalization)
plt.subplot(1, 2, 1)
plt.boxplot([df[col] for col in numeric_cols], labels=numeric_cols, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='blue'),
            capprops=dict(color='blue'),
            flierprops=dict(markerfacecolor='orange', marker='o', markersize=5, linestyle='none'))
plt.ylabel('Original Value')
plt.title('Box Plot of Original Features')

# Subplot 2: Box plot of normalized features (after normalization)
plt.subplot(1, 2, 2)
plt.boxplot([df_norm[col] for col in numeric_cols], labels=numeric_cols, patch_artist=True,
            boxprops=dict(facecolor='lightgreen', color='green'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='green'),
            capprops=dict(color='green'),
            flierprops=dict(markerfacecolor='orange', marker='o', markersize=5, linestyle='none'))
plt.ylabel('Normalized Value (z-score)')
plt.title('Box Plot of Normalized Features')

plt.tight_layout()
plt.show()
