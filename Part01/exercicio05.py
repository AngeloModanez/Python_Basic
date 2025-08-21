price = float(input("Enter the product price: $"))
discount_percent = float(input("Enter discount percentage: "))
discount_value = price * (discount_percent / 100)
final_price = price - discount_value
print(f"Discount amount: ${discount_value:.2f}")
print(f"Final price to pay: ${final_price:.2f}\n")
