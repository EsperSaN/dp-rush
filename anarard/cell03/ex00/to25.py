#!/usr/bin/python3
#input number from user
number = int(input("Enter a number less than 25 \n"))
if(number>25): #if number is more than 25 showing Error in monitor
    print("Error")
else: #if number is less than or equal 25 showing "Inside the loop, my variable is (Value of number)"
    while number<=25: 
        print("Inside the loop, my variable is",number)
        number+=1
