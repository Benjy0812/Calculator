import os


def clear(): 
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # macOS/Linux

def caclulator():
    while True:
        print()
          
        print("This is a calculator\nEnter 'quit' to quit")

        print()

        num1 = input("Enter the first number: ")
        
        if num1.lower() == 'quit':
            clear()  
            break
    
        num2 = input("Enter the second number: ")
        
        print()

        operation = input("chose opertation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\nEnter operation: ")
        
        clear()
        
        try:
            num_1 = float(num1)
            num_2 = float(num2)
        except ValueError:
            print("Error: please enter valid numbers")
            continue

        print()

        if operation == '1':
            print(f"The result is: {num_1 + num_2}")
        elif operation == '2':
            print(f"The result is: {num_1 - num_2}")
        elif operation == '3':
            print(f"Ther result is: {num_1 * num_2}")
        elif operation == '4':
            if num2 != 0:
                print(f"The result is {num_1 / num_2}")
            else:
                print("Error: Division by zero i not allowed")
        else:
            print("Invalid choice! pleasse run the program again and choose a valid option")
            
        print()

caclulator()