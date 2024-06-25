#!/usr/bin/env python3

# Prompt the user for the first number
first_number = float(input("Enter the first number: "))

# Prompt the user for the second number
second_number = float(input("Enter the second number: "))

# Calculate the result of multiplication
result = first_number * second_number

# Display the multiplication result
print(f"{first_number} x {second_number} = {result}")

# Determine if the result is positive, negative, or zero
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")
