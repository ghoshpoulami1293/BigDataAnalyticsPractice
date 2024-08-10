import numpy as np

# Generate some synthetic data (1D)
# normal - Gaussian distribution
# loc - mean 
# scale - standard deviation
# size - number of values to generate

data = np.random.normal(loc=0, scale=1, size=100)

# Define the Parzen Window kernel (Gaussian kernel in this case)
# x =  input value where the kernel is evaluated(could be a single number or an array of numbers)
# h =  This is the bandwidth or smoothing parameter(euquivalent to sigma).

def gaussian_kernel(x, h):
    return (1 / (np.sqrt(2 * np.pi) * h)) * np.exp(-(x**2) / (2 * h**2))

# Define the point (x) for which you want to estimate the density
x_estimate = 0

# Set the bandwidth (h) for the Parzen Window
bandwidth = 0.5

# Calculate the Parzen Window estimate for x_estimate
density_estimate = np.mean(gaussian_kernel(data - x_estimate, bandwidth))

print(f"Parzen Window Density Estimate at {x_estimate}: {density_estimate:.4f}")