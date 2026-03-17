"""
Project: Rock Paper Scissors Game

Description:
Create a Rock-Paper-Scissors game where the user plays against the computer.

Requirements:
1. Ask the user to choose:
   R for Rock
   P for Paper
   S for Scissors
2. The computer should randomly select its choice.
3. Display both choices using emojis if possible.
4. Determine the winner based on the rules.
5. Allow the user to play multiple rounds until they exit.

Sample Output:

Choose (R/P/S): R
You chose: Rock 🪨
Computer chose: Scissors ✂️
You win!
""" 
import random

choices = {
    'R': ("Rock", "🪨"),
    'P': ("Paper", "📄"),
    'S': ("Scissors", "✂️")
}
