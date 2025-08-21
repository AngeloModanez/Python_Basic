salary = float(input("Enter the current salary: $"))
increase_percent = float(input("Enter the raise percentage: "))
new_salary = salary * (1 + increase_percent / 100)
print(f"New salary after raise: ${new_salary:.2f}\n")
