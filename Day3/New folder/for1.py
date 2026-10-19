# Sales Performance Analysis Using for Loop

sales = [12000, 15000, 8000, 20000, 18000, 9000, 25000]

total_sales = 0
target = 15000
target_days = 0

print("WEEKLY SALES PERFORMANCE REPORT")
print("--------------------------------")

for j in range(len(sales)):
    print("Day", j + 1, "Sales:", sales[j])

    total_sales += sales[j]

    if sales[j] >= target:
        target_days += 1

average_sales = total_sales / len(sales)

print("--------------------------------")
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Target:", target)
print("Days Target Achieved:", target_days)