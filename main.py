import os


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def calculator():
    while True:
        try:
            clear_console()
            print("\nThis is a calculator")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            clear_console()
            print("Invalid input. Please enter numeric values only.")
            continue

        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Enter operation (1-4): ").strip()
        if operation not in ["1", "2", "3", "4"]:
            print("\nInvalid operation. Please choose a valid option (1-4).")
            input("Press Enter to try again...")
            continue

        clear_console()
        if operation == "1":
            print(f"\nThe result is: {num1 + num2}")
        elif operation == "2":
            print(f"\nThe result is: {num1 - num2}")
        elif operation == "3":
            print(f"\nThe result is: {num1 * num2}")
        elif operation == "4":
            if num2 != 0:
                print(f"\nThe result is: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")

        user_exit = (
            input("\nDo you want to perform another calculation?" "(yes/no): ")
            .strip()
            .lower()
        )
        if user_exit == "yes":
            continue
        elif user_exit == "no":
            clear_console()
            print("Exiting the calculator. Goodbye!")
            break
        else:
            clear_console()
            print("Invalid input. Please enter 'yes' or 'no'.")
            input("Press Enter to try again...")
