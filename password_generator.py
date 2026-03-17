"""
Project: Password Generator

Description:
Create a Python program that generates a random password for the user.

Requirements:
1. Ask the user to enter the desired password length.
2. The password should contain a mix of:
   - uppercase letters
   - lowercase letters
   - numbers
   - symbols
3. Use Python's random module to generate the password.
4. Display the generated password to the user.

Sample Input:
Enter password length: 10

Sample Output:
Generated Password: A7#kL9@pQ2
"""
 import random
 print("Password generator")
 characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
 length=int(input("enter the password length:"))
