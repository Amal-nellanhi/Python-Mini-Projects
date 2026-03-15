"""
Project: BMR Calculator
Author :Meenakshi
Description:
Create a program that calculates a person's Basal Metabolic Rate (BMR).

Requirements:
1. Ask the user for:
   - Gender (Male/Female)
   - Age
   - Height (in cm)
   - Weight (in kg)
2. Use the following formulas:

For Men:
BMR = 10 × weight + 6.25 × height − 5 × age + 5

For Women:
BMR = 10 × weight + 6.25 × height − 5 × age − 161

3. Display the calculated BMR.

Sample Input:
Gender: Male
Age: 21
Height: 175
Weight: 70

Sample Output:
Your BMR is: 1673 calories/day
"""
gender = input("Enter Gender (Male/Female): ")
age = int(input("Enter Age: "))
height = float(input("Enter Height (cm): "))
weight = float(input("Enter Weight (kg): "))

if gender.lower() == "male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
elif gender.lower() == "female":
    bmr = 10 * weight + 6.25 * height - 5 * age - 161
else:
    print("Invalid gender entered")
    exit()

print("Your BMR is:", int(bmr), "calories/day")








