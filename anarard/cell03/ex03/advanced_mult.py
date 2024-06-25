#!/usr/bin/python3
import sys

count = len(sys.argv)
if count == 1:
    i=0
    while i<11:
            print(f"Table de {i}: {i*0} {i*1} {i*2} {i*3} {i*4} {i*5} {i*6} {i*7} {i*8} {i*9} {i*10}")
            i+=1
else:
    print("none")