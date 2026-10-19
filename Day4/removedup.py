
# Removing Duplicate Values from a List

sales = [12000, 15000, 12000, 20000, 15000, 25000, 20000]

print("ORIGINAL SALES DATA")
print("-------------------")
print(sales)

unique_sales = list(set(sales))

print("-------------------")
print("Sales After Removing Duplicates")
print(unique_sales)

print("Original Records:", len(sales))
print("Unique Records:", len(unique_sales))
print("Duplicate Records Removed:", len(sales) - len(unique_sales))
