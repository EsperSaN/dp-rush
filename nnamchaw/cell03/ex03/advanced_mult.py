#!/usr/bin/env python3
import sys

def main():
    # Check for command-line arguments
    if len(sys.argv) > 1:
        print("none")
        return
    
    # Outer loop to go through each multiplication table from 0 to 10
    i = 0
    while i <= 10:
        print(f"Table de {i}: ", end="")
        
        # Inner loop to generate the multiplication values for the current table
        j = 0
        while j <= 10:
            print(i * j, end=" ")
            j += 1
        
        # Move to the next line after printing one table
        print()
        i += 1

if __name__ == "__main__":
    main()
