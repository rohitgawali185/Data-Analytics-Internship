
# Sales Analysis Using continue

sales = [12000, 0, 15000, 8000, 0, 20000]
total_sales = 0

print("SALES PERFORMANCE REPORT")
print("------------------------")

for j in range(len(sales)):
    if sales[j] == 0:
        print("Day", j + 1, ": No Sales - Skipped")
        continue

    print("Day", j + 1, "Sales:", sales[j])
    total_sales += sales[j]

print("------------------------")
print("Total Sales:", total_sales)
