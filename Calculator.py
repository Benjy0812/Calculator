import os
import time


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def calculator():
    while True:
        try:
            clear_console()
            print("\nWelcome to the Python Calculator!")
            first_number = float(input("Please enter the first value: "))
            second_number = float(input("Please enter the second value: "))
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
            print(f"\nThe result is: {first_number + second_number}")
        elif operation == "2":
            print(f"\nThe result is: {first_number - second_number}")
        elif operation == "3":
            print(f"\nThe result is: {first_number * second_number}")
        elif operation == "4":
            if second_number != 0:
                print(f"\nThe result is: {first_number / second_number}")
            else:
                print("Error: Division by zero is not allowed.")

        user_exit = (
            input("\nPerform another calculation? (yes, y / no, n): ")
            .strip()
            .lower()
        )
        if user_exit in ["yes", "y"]:
            continue
        elif user_exit in ["no", "n"]:
            clear_console()
            print("Exiting the calculator. Goodbye!")
            for _ in range(5):
                print(".", end="", flush=(True))
                time.sleep(1)
            break
        else:
            clear_console()
            print("Invalid input. Please enter 'yes' or 'no'.")
            input("Press Enter to try again...")

if __name__ == "__main__":
    calculator()
