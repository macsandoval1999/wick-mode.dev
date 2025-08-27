"""
Program: Simple Arithmetic Calculator
Description: This program performs basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.
Author: Marco Sandoval
Future Updates: Add more operations, error handling for division by zero, and input validation. Make it run complex calculations like  a scientific calculator.
"""
operator = "" # Initialize operator variable. This will store the current arithmetic operator but is initially empty so we can enter the operator try handle while loop.

while True: # Loop indefinitely until a break statement is encountered
    while operator not in ["+", "-", "*", "/"]: # Enter loop to get a valid operator. If operator isnt in list, handle invalid input and loop again
        operator = input("Enter an operator (+, -, *, /): ")
        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator. Please try again.")
            print()

    try: # Try to get valid numeric inputs
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError: # Handle invalid numeric input
        print("Invalid input. Please enter numeric values.")
        continue # Skip the rest of the loop and loop again. Because the operator is still stored, it will skip over the while not in loop and re-prompt for numbers.

    # Perform the arithmetic operation based on the operator
    if operator == "+": 
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = "Invalid operator"

    print("Result:", result)


    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower() # Ask user if they want to perform another calculation
    if again == "yes": # If user wants to continue, clear operator again and go back to the beginning of the loop
        operator = ""
        continue
    elif again == "no": # If user wants to exit, print exit message and break the loop
        print("Exiting calculator...")
        break
    else: # If user enters an invalid response, clear operator and go back to the beginning of the loop
        operator = ""
        continue
