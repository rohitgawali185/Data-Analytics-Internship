sales1 = float(input("Enter Monday sales: "))
sales2 = float(input("Enter Tuesday sales: "))
sales3 = float(input("Enter Wednesday sales: "))

total_sales = sales1 + sales2 + sales3
average_sales = total_sales / 3

print("Total Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))