import os


def clear():
<<<<<<< HEAD
    if os.name == 'nt':
        os.system('cls')  # Windows
=======
    if os.name == "nt":
        os.system("cls")  # Windows
>>>>>>> 650c9f10a00c0fbe03fad65f3b91295d026d4aa6
    else:
        os.system("clear")  # macOS/Linux


def calculator():
<<<<<<< HEAD

    while True:
        print()

        print("This is a calculator\nEnter 'quit' to quit")
=======
    while True:
        print()

        print("This is a calculator\nEnter 'exit' to exit")
>>>>>>> 650c9f10a00c0fbe03fad65f3b91295d026d4aa6

        print()

        num1 = input("Enter the first number: ")
<<<<<<< HEAD
        if num1.lower() == 'quit':
            clear()
            break

        num2 = input("Enter the second number: ")

        print()

        operation = input("chose operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\nEnter operation: ")
=======
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
>>>>>>> 650c9f10a00c0fbe03fad65f3b91295d026d4aa6

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
<<<<<<< HEAD
        elif operation == '3':
            print(f"There result is: {num_1 * num_2}")
        elif operation == '4':
=======
        elif operation == "3":
            print(f"The result is: {num_1 * num_2}")
        elif operation == "4":
>>>>>>> 650c9f10a00c0fbe03fad65f3b91295d026d4aa6
            if num2 != 0:
                print(f"The result is {num_1 / num_2}")
            else:
                print("Error: Division by zero i not allowed")
        else:
<<<<<<< HEAD
            print("Invalid choice! please run the program again and choose a valid option")
=======
            print(
                "Invalid choice! please try again"
            )
>>>>>>> 650c9f10a00c0fbe03fad65f3b91295d026d4aa6

        print()


calculator()
