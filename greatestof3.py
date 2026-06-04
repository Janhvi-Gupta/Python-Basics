a = int(input("Enter number 1 "))
b = int(input("Enter number 2 "))
c = int(input("Enter number 3 "))

if (a > b):
    if (a > c):
        print("greatest number is ", a)
    else:
        print("greatest number is ", c)
elif (b > a):
    if (b > c):
        print("greatest number is ", b)
    else:
        print("greatest number is ", c)