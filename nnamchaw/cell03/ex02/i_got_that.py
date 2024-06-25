#!/usr/bin/env python3

def main():
    while True:
        # Prompt user for input
        user_input = input("What you gotta say? : ")
        
        # Check if the user input is "STOP"
        if user_input.strip().upper() == "STOP":
            break
        
        # Respond to the user input
        print("I got that! Anything else? :")

if __name__ == "__main__":
    main()
