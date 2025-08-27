"""
Program: Temperature Conversion
Description: This program converts temperatures between Celsius and Fahrenheit.
Author: Marco Sandoval
Future Updates: Add more conversion options (e.g., Kelvin), error handling for invalid inputs, and input validation. Turn conversion into functions.
"""
unit = input("Celsius or Fahrenheit? (C/F): ").strip().upper() # Get user input, strip any leading and trailing whitespace around it, and convert to uppercase
temp = float(input("Enter the temperature: ")) # Get temperature input and convert to float

if unit == "C": # If the unit is Celsius
    temp = round((9 * temp) / 5 + 32) # Function to convert Celsius to Fahrenheit
    print(f"The temperature in Fahrenheit is: {temp}°F")

elif unit == "F": # If the unit is Fahrenheit
    temp = round((temp -32) * 5 / 9) # Function to convert Fahrenheit to Celsius
    print(f"The temperature in Celsius is: {temp}°C")

else:
    print(f"{unit} is not a valid unit. Please enter C for Celsius or F for Fahrenheit.")


