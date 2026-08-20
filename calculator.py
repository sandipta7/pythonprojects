


num1 = float(input("Enter Second Number: "))
num2 = float(input("Enter First Number: "))

print("Selection Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiply (*)")
print("4. Division (/)")

choice = input("Enter choice (1, 2, 3 and 4): ")

if choice =='1':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}" )

elif choice =='2':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}" )

elif choice =='3':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}" )

elif choice =='4':
    result = num1 / num2
    print(f"\nResult: {num1} / {num2} = {result}" )
else:
    print("\nInvalid Input! Please select from 1 to 4 options available.")