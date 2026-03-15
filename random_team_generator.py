"""
Project: Random Team Generator
Author: Avanthika

Description:
Create a program that randomly divides people into teams.

Requirements:
1. Ask the user to enter names separated by commas.
2. Ask the user for the number of teams.
3. Randomly assign the names into teams.
4. Display the teams.

Sample Input:
Enter names: Alice,Bob,John,Maya,David
Enter number of teams: 2

Sample Output:
Team 1: Alice, John, David
Team 2: Bob, Maya
"""
def random_team():
    import random
    Names=input("Enter the names seperated by coma(,) : ")
    namelist=Names.split(",")
    n=len(namelist)
    print("Number of members : ",n)
    number_of_Teams=int(input("Enter the number of teams required : "))
    random.shuffle(namelist)
    teams=[[] for _ in range(number_of_Teams)]
    for i,name in enumerate(namelist):
        teams[i%number_of_Teams].append(name)
    for i,term in enumerate(teams,start=1):
        print(f"Team {i}:{','.join(term)}")
    

random_team()

    
    
    
      