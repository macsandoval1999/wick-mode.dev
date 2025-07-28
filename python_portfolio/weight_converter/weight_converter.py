"""
Progran: Weight Converter
Description: This program converts weight between kilograms and pounds.
Author: Marco Sandoval
Future Updates: Add more units of measurement and error handling for invalid inputs.
"""
error = True
unit = ""

while error == True:
    try:
        weight = float(input("Enter weight: "))
        error = False
    except ValueError:
        print("Invalid input. Please enter a numeric value for weight.")

while unit not in ["kg", "lb"]:
    unit = input("Enter unit (kg/lb): ").strip().lower()

    if unit == "kg":
        converted_weight = weight * 2.205
        unit = "lb"

    elif unit == "lb":
        converted_weight = weight / 2.205
        unit = "kg"

    else: 
        print("Invalid unit. Please enter 'kg' or 'lb'.")

print(f"Converted weight: {converted_weight:.2f} {unit}")