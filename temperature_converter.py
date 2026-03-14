"""
Project: Temperature Converter

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
print("temprature converter: ")
print("1. celsius to fahrenheit")
print("2.fahrenheit to celsius")
print("3.exit")
choice==int(input("enter the chioice: " ))
if choice==1:
    c=float(input("enter your temperature in celsius: "))
    f=(c*(9/5))+32
    print("temperature in fahrenheit: ",f)
elif choice==2:
        f=float(input("enter the temperature in fahrenheit: "))
        c=(f-32)*(5/9)
        print("the temperature in celsius: ",c)
elif choice==3:
            print("exit")
 else: 
            print("exit")