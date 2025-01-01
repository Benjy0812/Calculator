import os
import sys


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def calculator():
    while True:
        print("\nThis is a calculator")

        num1 = input("Enter the first number: ")

        num2 = input("Enter the second number: ")

        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        operation = input("Enter operation: ")

        clear_console()

        try:
            num_1 = float(num1)
            num_2 = float(num2)
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        if operation == "1":
            print(f"The result is: {num_1 + num_2}")
        elif operation == "2":
            print(f"The result is: {num_1 - num_2}")
        elif operation == "3":
            print(f"The result is: {num_1 * num_2}")
        elif operation == "4":
            if num_2 != 0:
                print(f"The result is: {num_1 / num_2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice! Please try again.\n")

        exit = input("\nDo you want to perform another calculation? (yes/no)")
        if exit.lower() == 'no':
            sys.exit()


calculator()
