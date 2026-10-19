import numpy as np

# Creating an array
sales = np.array([1200, 1500, 900, 1800, 1600])

# Slicing array elements
print("First Three Elements:", sales[0:3])
print("Elements from Index 2:", sales[2:])
print("Elements from Index 1 to 3:", sales[1:4])
print("Last Two Elements:", sales[-2:])