speed = int(input("Enter the car speed (km/h): "))
if speed > 80:
    fine = (speed - 80) * 5
    print("You have been fined!")
    print(f"Fine amount: ${fine:.2f}\n")
else:
    print("You are within the speed limit.\n")
