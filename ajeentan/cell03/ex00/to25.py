#!/usr/bin/python3
try :
    i = int(input("Enter the number less than 25\n"))
    if i<=25 :
        while i<=25 :
            print("Inside the loop, my variable is",i)
            i=i+1
    else :
        print("error")
except:
   print("pleas enter the number")