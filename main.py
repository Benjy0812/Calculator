while True:    
    print("This is a calculator\nEnter quit to quit")

    num1 = input("Enter the first number: ")
    
    if num1 == 'quit':
      break
  
    num2 = input("Enter the second number: ")
    

    operation = input("chose opertation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\nEnter operation: ")
    
    num_1 = float(num1)
    num_2 = float(num2)

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
            print("Error: Division bt zero i not allowed")

    else:
        print("Invalid choice! pleasse run the program agein and choose a valid option")