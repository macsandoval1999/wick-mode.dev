"""
Progran: Weight Converter
Description: This program converts weight between kilograms and pounds.
Author: Marco Sandoval
Future Updates: Add more units of measurement and error handling for invalid inputs. Turn conversion into functions.
"""
error = True # Initialize error variable. Needed to enter while loop that handles invalid weight input
unit = "" # Initialize unit variable. Needed to enter while loop that handles invalid unit input

while error == True: # Loop until valid weight is entered
    try: # Try to get a valid weight input
        weight = float(input("Enter weight being converted: "))
        error = False # Valid weight entered. While loop condition no longer true so exit loop
    except ValueError: # Handle invalid weight input
        print("Invalid input. Please enter a numeric value for weight.")
        print()

while unit not in ["kg", "lb"]: # Loop until valid unit is entered
    unit = input("Enter unit being converted(kg/lb): ").strip().lower() # Get user input, strip whitespace, and convert to lowercase

    if unit == "kg": # If the unit is kilograms convert to pounds
        converted_weight = weight * 2.205
        new_unit = "lb"

    elif unit == "lb": # If the unit is pounds convert to kilograms
        converted_weight = weight / 2.205
        new_unit = "kg"

    else: # If the unit is neither kg nor lb, handle invalid unit input
        print("Invalid unit. Please enter 'kg' or 'lb'.")
    print()

print(f"Original weight: {weight} {unit} \nConverted weight: {converted_weight:.2f} {new_unit}") # Display the original and converted weight