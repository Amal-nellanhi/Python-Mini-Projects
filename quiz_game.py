"""
Project: Simple Quiz Game

Description:
Create a simple quiz game that asks the user a few questions and calculates the score.

Requirements:
1. Display at least 5 questions.
2. Ask the user to input their answer.
3. Check if the answer is correct.
4. Increase the score for each correct answer.
5. Display the final score at the end of the quiz.

Sample Output:

Question 1: What is the capital of France?
Your answer: Paris
Correct!

Question 2: What is 5 + 3?
Your answer: 8
Correct!

Final Score: 2/2
"""
print("Welcome to the Quiz Game")
score=0
a=input("1.What is the capital of India?")
if a.lower()=="delhi":
    print("Correct")
    score=score+1
else:
    print("wrong")
b=input("2.What is 5+3?")
if b=="8":
    print("Correct")
    score=score+1
else:
    print("Wrong")
c= input("3. Is Python a programming language ? ")
if c==programming language:
    print("Correct answer")
    score = score + 1
else:
    print("Wrong answer")


