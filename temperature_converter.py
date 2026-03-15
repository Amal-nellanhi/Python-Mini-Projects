"""
Project: Temperature Converter
author:Shyama c prasanth

Description:
Create a program that converts temperature between Celsius and Fahrenheit.

Requirements:
1. Display a menu with options:
   1. Celsius to Fahrenheit
   2. Fahrenheit to Celsius
   3. Exit
2. Ask the user to choose an option.
3. Ask for the temperature value.
4. Perform the conversion and display the result.

Conversion formulas:
Fahrenheit = (Celsius × 9/5) + 32
Celsius = (Fahrenheit − 32) × 5/9

Sample Output:

1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit

Enter your choice: 1
Enter temperature in Celsius: 25

Temperature in Fahrenheit: 77
"""
print("Temperature converter: ")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Exit")

choice = int(input("Enter the choice: "))

if choice == 1:
    c = float(input("Enter your temperature in Celsius: "))
    f = (c * (9/5)) + 32
    print("Temperature in Fahrenheit:", f)
elif choice == 2:
    f = float(input("Enter the temperature in Fahrenheit: "))
    c = (f - 32) * (5/9)
    print("Temperature in Celsius:", c)
elif choice == 3:
    print("Exit")
else:
    print("Invalid choice, exiting...")