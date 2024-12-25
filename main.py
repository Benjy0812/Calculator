print("This is a calculator")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("chose opertation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")

if operation == '1':
    print(f"The result is: {num1 + num2}")
elif operation == '2':
    print(f"The result is: {num1 - num2}")
elif operation == '3':
    print(f"Ther result is: {num1 * num2}")
elif operation == '4':
    if num2 != 0:
        print(f"The result is {num1 / num2}")
    else:
        print("Error: Division bt zero i not allowed")

else:
    print("Invalid choice! pleasse run the program agein and choose a valid option")


