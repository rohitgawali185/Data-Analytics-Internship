import numpy as np

# Creating an array
sales = np.array([1200, 1500, 900, 1800, 1600])

# Performing numerical calculations
print("Sales Array:", sales)
print("Sum:", np.sum(sales))
print("Mean:", np.mean(sales))
print("Minimum:", np.min(sales))
print("Maximum:", np.max(sales))
print("Standard Deviation:", round(np.std(sales), 2))