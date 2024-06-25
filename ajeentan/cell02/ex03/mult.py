#!/usr/bin/python3
try:
    print("Enter the first number:")
    fisrtnumber=int(input())
    print("Enter the second number:")
    lastnumber=int(input())
    print(fisrtnumber,"x",lastnumber,"=",fisrtnumber*lastnumber)
    if fisrtnumber*lastnumber>0 :
        print("The result is positive.")
    elif fisrtnumber*lastnumber<0 :
        print("The result is negative.")
    elif fisrtnumber*lastnumber==0 :
        print("The result is positive and negative.")
except:
   print("pleas enter the number")