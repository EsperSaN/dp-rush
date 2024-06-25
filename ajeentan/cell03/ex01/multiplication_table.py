#!/usr/bin/python3
try :
    number =int(input("Enter a number\n"))
    for i in range(10):
        print(i,"x",number,"=",i*number)
        i=i+1
except :
    print("pleas enter the number")