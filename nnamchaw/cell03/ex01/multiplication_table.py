#!/usr/bin/env python3

def main():
    # Prompt user for input
    user_input = input("Enter a number: ")
    
    try:
        # Convert user input to an integer
        number = int(user_input)
        
        # Display the multiplication table for the given number
        for i in range(10):
            print(f"{i} x {number} = {i * number}")
    
    except ValueError:
        # Handle case where input is not a valid integer
        print("Error: Please enter a valid number")

if __name__ == "__main__":
    main()
