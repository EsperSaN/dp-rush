#!/usr/bin/env python3

def main():
    # Ask the user for the first number
    num1 = input("Give me the first number: ")
    
    # Ask the user for the second number
    num2 = input("Give me the second number: ")
    
    try:
        # Convert inputs to numerical values
        num1 = float(num1)
        num2 = float(num2)
        
        # Display confirmation message
        print("Thank you!")
        
        # Perform calculations and display results
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} / {num2} = {num1 / num2}")
        print(f"{num1} * {num2} = {num1 * num2}")
    
    except ValueError:
        # Handle case where inputs are not valid numerical values
        print("Error: Please enter valid numbers")

if __name__ == "__main__":
    main()
