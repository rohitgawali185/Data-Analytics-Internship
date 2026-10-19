# Sales Analysis Using while Loop

sales = [12000, 15000, 8000, 20000, 18000]

j = 0
total_sales = 0
target = 15000
target_days = 0

print("WEEKLY SALES REPORT")
print("-------------------")

while j < len(sales):
    print("Day", j + 1, "Sales:", sales[j])

    total_sales += sales[j]

    if sales[j] >= target:
        target_days += 1

    j += 1

average_sales = total_sales / len(sales)

print("-------------------")
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Target:", target)
print("Target Achieved Days:", target_days)