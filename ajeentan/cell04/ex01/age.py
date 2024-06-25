#!/usr/bin/python3
try :
    age = input("Please tell me your age: ")
    age = int(age)
    print("You are currently",age,"years old.")
    print("In 10 years, you'll be",age+10,"years old.")
    print("In 20 years, you'll be",age+20,"years old.")
    print("In 30 years, you'll be",age+30,"years old.")
except:
   print("please enter the number")