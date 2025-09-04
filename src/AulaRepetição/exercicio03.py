total = 0
count = 0

while True:
    number = int(input("Enter a positive number (negative number to quit): "))
    if number < 0:
        break
    total += number
    count += 1

if count > 0:
    average = total / count
    print(f"Average of entered numbers: {average:.2f}")
else:
    print("No positive numbers were entered.")
