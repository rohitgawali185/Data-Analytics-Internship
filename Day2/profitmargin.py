sales = float(input("Enter total sales: "))
cost = float(input("Enter total cost: "))

profit = sales - cost

if sales > 0:
    profit_margin = (profit / sales) * 100
else:
    profit_margin = 0

print("Total Sales:", sales)
print("Total Cost:", cost)
print("Profit:", round(profit, 2))
print("Profit Margin:", round(profit_margin, 2), "%")