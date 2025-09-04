count = 0

while True:
    number = int(input("Enter a positive number (negative number to quit): "))
    if number < 0:
        break
    count += 1

print(f"Total positive numbers entered: {count}")
