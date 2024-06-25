#!/usr/bin/python3
Original_array = [2, 8, 9, 48, 8, 22, -12, 2]
#This line is for checking each element in array for and + 2 in each element and collect in New_array variable
New_array = [x+2 for x in Original_array]
print(f"Original Array: {Original_array}")
print(f"New array: {New_array}")