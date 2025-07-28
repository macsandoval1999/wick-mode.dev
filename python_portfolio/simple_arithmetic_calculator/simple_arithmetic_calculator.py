"""
Program: Simple Arithmetic Calculator
Description: This program performs basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.
Author: Marco Sandoval
Future Updates: Add more operations, error handling for division by zero, and input validation. Make it run complex calculations like  a scientific calculator.
"""
operator = ""

while True:
    while operator not in ["+", "-", "*", "/"]:
        operator = input("Enter an operator (+, -, *, /): ")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

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


    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again == "yes":
        operator = ""
        continue
    elif again == "no":
        print("Exiting calculator...")
        break
    else:
        operator = ""
        continue
