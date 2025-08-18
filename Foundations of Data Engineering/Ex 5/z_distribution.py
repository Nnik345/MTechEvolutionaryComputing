import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import uniform, norm

# Set style for better plots
plt.style.use('default')

def case1_uniform_uniform():
    # Random sampling
    n_samples = 100000
    x1 = np.random.uniform(0, 1, n_samples)
    x2 = np.random.uniform(0, 1, n_samples)
    z = x1 + x2
    
    # Theoretical PDF
    z_theoretical = np.linspace(0, 2, 1000)
    pdf_theoretical = np.where(z_theoretical <= 1, z_theoretical, 2 - z_theoretical)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Histogram vs theoretical
    plt.hist(z, bins=50, density=True, alpha=0.7, label='Simulation')
    plt.plot(z_theoretical, pdf_theoretical, 'r-', linewidth=2, label='Theoretical PDF')
    plt.xlabel('Z = X1 + X2')
    plt.ylabel('Density')
    plt.title('Case 1: Uniform + Uniform')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    


def case2_normal_normal():
    # Random sampling
    n_samples = 100000
    x1 = np.random.normal(0, 1, n_samples)
    x2 = np.random.normal(0, 1, n_samples)
    z = x1 + x2
    
    # Theoretical PDF
    z_theoretical = np.linspace(-6, 6, 1000)
    pdf_theoretical = stats.norm.pdf(z_theoretical, 0, np.sqrt(2))
    
    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Histogram vs theoretical
    plt.hist(z, bins=50, density=True, alpha=0.7, label='Simulation')
    plt.plot(z_theoretical, pdf_theoretical, 'r-', linewidth=2, label='Theoretical PDF')
    plt.xlabel('Z = X1 + X2')
    plt.ylabel('Density')
    plt.title('Case 2: Normal + Normal')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    


def case3_uniform_different():
    # Random sampling
    n_samples = 100000
    x1 = np.random.uniform(0, 1, n_samples)
    x2 = np.random.uniform(0, 2, n_samples)
    z = x1 + x2
    
    # Theoretical PDF
    z_theoretical = np.linspace(0, 3, 1000)
    pdf_theoretical = np.where(z_theoretical <= 1, z_theoretical/2,
                              np.where(z_theoretical <= 2, 0.5, (3-z_theoretical)/2))
    
    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Histogram vs theoretical
    plt.hist(z, bins=50, density=True, alpha=0.7, label='Simulation')
    plt.plot(z_theoretical, pdf_theoretical, 'r-', linewidth=2, label='Theoretical PDF')
    plt.xlabel('Z = X1 + X2')
    plt.ylabel('Density')
    plt.title('Case 3: Uniform[0,1] + Uniform[0,2]')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    


def theoretical_analysis():
    """Theoretical analysis for all cases"""
    pass

if __name__ == "__main__":
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Run simulations for each case
    case1_uniform_uniform()
    case2_normal_normal()
    case3_uniform_different()