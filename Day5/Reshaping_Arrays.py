import numpy as np

# Creating a one-dimensional array
numbers = np.arange(1, 13)

print("Original Array:")
print(numbers)

# Reshaping into 3 rows and 4 columns
matrix = numbers.reshape(3, 4)

print("Reshaped Two-Dimensional Array:")
print(matrix)

print("Array Shape:", matrix.shape)