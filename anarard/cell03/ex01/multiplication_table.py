#!/usr/bin/python3

#User input number for create Table of multiplication
number = int(input("Enter a number \n"))

#create index for knowing how was the value to multiplication is
i = 0

while i<10:
    print(f"{i} x {number} = {i*number}")
    i+=1
