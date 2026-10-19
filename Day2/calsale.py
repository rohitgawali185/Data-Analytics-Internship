product = input("Enter product name: ")
price = float(input("Enter price per unit: "))
quantity = int(input("Enter quantity sold: "))

total_sales = price * quantity

print("Product:", product)
print("Total Sales:", round(total_sales, 2))