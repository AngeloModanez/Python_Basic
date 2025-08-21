house_price = float(input("Enter the house price: $"))
salary = float(input("Enter your salary: $"))
years_to_pay = int(input("Enter the number of years to pay: "))

max_allowed = salary * 0.30
months = years_to_pay * 12
installment = house_price / months

print(f"Monthly installment: ${installment:.2f}")
print(f"30% of your salary: ${max_allowed:.2f}")
print(f"Total months: {months}")

if installment <= max_allowed:
    print("Loan approved!\n")
else:
    print("Loan denied.\n")
