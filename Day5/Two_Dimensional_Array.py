import numpy as np

# Creating a two-dimensional array
monthly_sales = np.array([
    [1200, 1400],
    [900, 1100],
    [1600, 1750]
])

print("Two-Dimensional Array:")
print(monthly_sales)

print("Element at Row 1, Column 2:", monthly_sales[0, 1])
print("Array Dimensions:", monthly_sales.ndim)
print("Array Shape:", monthly_sales.shape)