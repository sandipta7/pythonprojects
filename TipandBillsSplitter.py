bill = float(input("Enter the total bill amount: "))
tip_percent = float(input("Enter the tip percentage: "))
people = int(input("Enter the headcount of people: "))

tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount

print(f"\nThe Total amount is ${total_bill:.2f}")
print(f"The Tip amount is ${tip_amount:.2f}")

if people <= 0:
    print("Error: Headcount must be at least 1!")
else:
    bill_split = total_bill / people
    print(f"The bill to be split for each person is ${bill_split:.2f}")