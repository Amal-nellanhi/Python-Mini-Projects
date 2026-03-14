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

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        
        try:
            choice = input("\nEnter your choice: ")
            
            if choice == '1':
                celsius = float(input("Enter temperature in Celsius: "))
                print(f"\nTemperature in Fahrenheit: {celsius_to_fahrenheit(celsius):.2f}")
            elif choice == '2':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print(f"\nTemperature in Celsius: {fahrenheit_to_celsius(fahrenheit):.2f}")
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numerical value for temperature.")

if __name__ == "__main__":
    main()
