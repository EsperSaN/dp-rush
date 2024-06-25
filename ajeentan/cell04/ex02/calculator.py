#!/usr/bin/python3
try :
    num_a = int(input("Give me the first number: "))
    num_b = int(input("Give me the second  number: "))
    print("Thank you!")
    print(num_a,"+",num_b,"=",num_a+num_b)
    print(num_a,"-",num_b,"=",num_a-num_b)
    print(num_a,"/",num_b,"=",num_a//num_b)
    print(num_a,"*",num_b,"=",num_a*num_b)
except:
   print("please enter the number")
