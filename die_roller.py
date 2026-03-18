"""
Project: Dice Roller
Author:Aysha Surook k

Description:
Create a program that simulates rolling dice.

Requirements:
1. Ask the user how many dice they want to roll.
2. Ask the user if they want to roll the dice.
3. If the user enters 'yes', generate random numbers between 1 and 6.
4. Display the result for each dice.
5. If the user enters 'no', exit the program.
6. Handle invalid inputs.

Sample Input:
How many dice to roll: 3
Do you want to roll the dice? (yes/no): yes

Sample Output:
Dice 1: 4
Dice 2: 2
Dice 3: 6
"""
import random

n=int(input("How many dice to roll: "))
choice=input("Do you want to roll the dice? (yes/no): ").lower()
if choice=="yes":
    for i in range(n):
        print(f"Dice {i+1}: {random.randint(1,6)}")
elif choice=="no":
    print("Program exited.")
else:
    print("Invalid input.")