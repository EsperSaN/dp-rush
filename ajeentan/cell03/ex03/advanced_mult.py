#!/usr/bin/python3
import sys
a = len(sys.argv)

if a==1 :
    i = 0
    a = 1
    while i<=10 :
        print("Table de",i,": ",end =" ")
        while a<=10 :
            print(i * a,end =" ")
            a += 1
        print(" ")
        i = i+1
        a = 0
else:
    print("none")
