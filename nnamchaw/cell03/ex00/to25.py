#!/usr/bin/env python3

def main():
    # Prompt user for input
    user_input = input("Enter a number less than 25: ")
    
    try:
        # Convert user input to an integer
        number = int(user_input)
        
        # Check if the number is greater than 25
        if number > 25:
            print("Error")
        else:
            # Loop from the input number up to 25
            for i in range(number, 26):
                print(f"Inside the loop, my variable is {i}")
    
    except ValueError:
        # Handle case where input is not a valid integer
        print("Error: Please enter a valid number")

if __name__ == "__main__":
    main()
