#!/usr/bin/env python3

def main():
    # Ask the user for their age
    age = input("Please tell me your age: ")
    
    try:
        # Convert age input to an integer
        age = int(age)
        
        # Display current age
        print(f"You are currently {age} years old.")
        
        # Display age in 10, 20, and 30 years
        print(f"In 10 years, you'll be {age + 10} years old.")
        print(f"In 20 years, you'll be {age + 20} years old.")
        print(f"In 30 years, you'll be {age + 30} years old.")
    
    except ValueError:
        # Handle case where input is not a valid integer
        print("Error: Please enter a valid age")

if __name__ == "__main__":
    main()

