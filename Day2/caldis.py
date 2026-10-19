price = float(input("Enter product price: "))
discount_percent = float(input("Enter discount percentage: "))

discount_amount = price * discount_percent / 100
final_price = price - discount_amount

print("Original Price:", price)
print("Discount Amount:", round(discount_amount, 2))
print("Final Price:", round(final_price, 2))