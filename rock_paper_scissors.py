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

def get_computer_choice():
    return random.choice(list(choices.keys()))
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'R' and computer == 'S') or \
         (user == 'P' and computer == 'R') or \
         (user == 'S' and computer == 'P'):
        return "You win!"
    else:
        return "Computer wins!"
def play_game():
    print("🎮 Rock-Paper-Scissors Game 🎮")
    
    while True:
        user_choice = input("\nChoose (R/P/S) or Q to quit: ").upper()
        
        if user_choice == 'Q':
            print("Thanks for playing! 👋")
            break
        
        if user_choice not in choices:
            print("Invalid choice! Please choose R, P, or S.")
            continue
        
        computer_choice = get_computer_choice()
        
        user_name, user_emoji = choices[user_choice]
        comp_name, comp_emoji = choices[computer_choice]
        
        print(f"You chose: {user_name} {user_emoji}")
        print(f"Computer chose: {comp_name} {comp_emoji}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
play_game()