import os


def clear():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def calculator():
    while True:
        print()

        print("This is a calculator\nEnter 'exit' to exit")

        print()

        num1 = input("Enter the first number: ")
        if num1.lower() == "exit":
            break

        num2 = input("Enter the second number: ")

        print()
        print("chose operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        operation = input("Enter operation: ")

        clear()

        try:
            num_1 = float(num1)
            num_2 = float(num2)
        except ValueError:
            print("Error: please enter valid numbers")
            continue

        print()

        if operation == "1":
            print(f"The result is: {num_1 + num_2}")
        elif operation == "2":
            print(f"The result is: {num_1 - num_2}")
        elif operation == "3":
            print(f"The result is: {num_1 * num_2}")
        elif operation == "4":
            if num2 != 0:
                print(f"The result is {num_1 / num_2}")
            else:
                print("Error: Division by zero i not allowed")
        else:
            print(
                "Invalid choice! please try again"
            )

        print()


calculator()
