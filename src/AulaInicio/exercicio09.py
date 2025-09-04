minutes_lost = 0
loss_per_unit = {1: 11, 2: 5, 3: 3}

print("Choose the type of product you use:")
print("1. Cigarette 🚬")
print("2. Vape 💨")
print("3. Weed 🍃")

while True:
    try:
        product_type = int(input("Enter 1, 2, or 3: "))
        if product_type in [1, 2, 3]:
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a number (1, 2, or 3).")

while True:
    try:
        units_per_day = int(input("How many do you consume per day? "))
        if units_per_day > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        years_used = int(input("For how many years have you been consuming? "))
        if years_used >= 0:
            break
        else:
            print("Please enter a valid number of years.")
    except ValueError:
        print("Invalid input. Please enter a number.")

days_used = years_used * 365
total_units = units_per_day * days_used

minutes_lost = total_units * loss_per_unit[product_type]
days_lost = minutes_lost / (24 * 60)
years_lost = days_lost / 365

print("\n===== RESULTS =====")
print(f"Total units consumed: {total_units:,}")
print(f"Estimated life lost: {days_lost:.1f} days (~{years_lost:.1f} years)")
print("===================")
