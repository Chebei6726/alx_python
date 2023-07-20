#!/usr/bin/python3
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

fahrenheit_input = float(input("Enter the temperature in Fahrenheit: "))

# Call the function to convert Fahrenheit to Celsius
celsius_temperature = convert_to_celsius(fahrenheit_input)

print(f"{celsius_temperature:.2f}")
