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
print("\n1. What is the capital of India?")
print("1. Mumbai")
print("2. Delhi")
print("3. Chennai")
print("4. Kolkata")
ans = input("Enter your option (1-4): ")
if ans == "2":
    print("Correct answer")
    score = score + 1
else:
    print("Wrong answer")
print("\n2. What is 5 + 3?")
print("1. 6")
print("2. 7")
print("3. 8")
print("4. 9")
ans_1 = input("Enter your option (1-4): ")
if ans_1 == "3":
    print("Correct answer")
    score = score + 1
else:
    print("Wrong answer")  
print("\n3. Which of the following is used to take input from the user in Python?")
print("1. print()")
print("2. input()")
print("3. read()")
print("4. scan()")
ans_2= input("Enter your option (1-4): ")

if ans_2 == "2":
    print("Correct answer")
    score = score + 1
else:
    print("Wrong answer") 
print("\n4. What is the square of 4?")
print("1. 8")
print("2. 12")
print("3. 16")
print("4. 20")
ans_3 = input("Enter your option (1-4): ")
if ans_3 == "3":
    print("Correct answer")
    score = score + 1
else:
    print("Wrong answer")         



