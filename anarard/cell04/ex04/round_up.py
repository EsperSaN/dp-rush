#!/usr/bin/python3
number = float(input("Give me a number: "))
if(number%1!=0):
    number+=0.5
    print(round(number))
else:
    print(int(number))

#number = float(input("Give me a number: "))
#print(round(num + 0.5))
    