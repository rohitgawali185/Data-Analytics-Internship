import numpy as np

# Creating a Python list
python_values = [10, 20, 30, 40]

# Creating a NumPy array
numpy_values = np.array([10, 20, 30, 40])

# Performing calculations using Python list
python_doubled = [x * 2 for x in python_values]
print("Python List Doubled:", python_doubled)
print("Python List Sum:", sum(python_values))

# Performing calculations using NumPy array
numpy_doubled = numpy_values * 2
print("NumPy Array Doubled:", numpy_doubled)
print("NumPy Array Sum:", np.sum(numpy_values))