"""
Project: Number Guessing Game

Description:
Create a game where the user tries to guess a randomly generated number.

Requirements:
1. Generate a random number between 1 and 100.
2. Ask the user to guess the number.
3. If the guess is too high, display "Too high".
4. If the guess is too low, display "Too low".
5. Continue until the user guesses the correct number.

Sample Output:

Guess the number between 1 and 100
Enter your guess: 50
Too high

Enter your guess: 20
Too low

Enter your guess: 35
Congratulations! You guessed the number.
"""
import random
number=random.randint(1,100)
print("Guess the number between 1 and 100")