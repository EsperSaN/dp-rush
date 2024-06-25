#!/usr/bin/env python3
first_number = int(input("Please input your first number :\n"))
second_number = int(input("Please input your second number :\n"))
result_number = first_number*second_number
print(f"{first_number} x {second_number} = {result_number}")
if(result_number>0):
    print("The result is positive.")
elif(result_number<0): 
    print("The result is negative.")
else:
    print("The result is positive and negative.")
