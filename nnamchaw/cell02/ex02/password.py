#!/usr/bin/env python3

# Define the password
password = "Python is awesome"

# Prompt the user for a password
user_input = input("Enter the password: ")

# Check if the entered password matches the predefined password
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
