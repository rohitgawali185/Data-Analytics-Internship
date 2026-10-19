# Sales Analysis Using break

sales = [12000, 15000, 8000, 25000, 18000, 30000]

total_sales = 0
target = 25000

print("SALES PERFORMANCE REPORT")
print("------------------------")

for j in range(len(sales)):
    print("Day", j + 1, "Sales:", sales[j])

    total_sales += sales[j]

    if sales[j] >= target:
        print("Sales target achieved!")
        print("Stopping the loop.")
        break

print("------------------------")
print("Total Sales Processed:", total_sales)