salary = float(input("Enter your salary: $"))
if salary > 1250:
    new_salary = salary * 1.10
else:
    new_salary = salary * 1.15
print(f"Adjusted salary: ${new_salary:.2f}\n")
