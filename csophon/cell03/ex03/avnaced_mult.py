import sys

count = len(sys.argv)

if count == 1:
    for i in range(11):
        print(f"Table de {i} : ", end=" ")
        for x in range(11):
            re = i * x
            print(re, end=" ")
        print()
else:
    print("none")