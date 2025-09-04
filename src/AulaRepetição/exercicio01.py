while True:
    number = int(input("Enter a number (enter -999 to quit): "))
    if number == -999:
        print("Program finished. Goodbye!")
        break
    print(f"The triple of {number} is {number * 3}")
