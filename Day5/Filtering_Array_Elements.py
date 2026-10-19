import numpy as np

# Creating an array
sales = np.array([1200, 1500, 900, 1800, 1600])

# Filtering elements using conditions
high_sales = sales[sales > 1300]
print("Sales Greater Than 1300:", high_sales)

low_sales = sales[sales < 1500]
print("Sales Less Than 1500:", low_sales)

# Filtering elements greater than or equal to 1500
selected_sales = sales[sales >= 1500]
print("Sales Greater Than or Equal to 1500:", selected_sales)