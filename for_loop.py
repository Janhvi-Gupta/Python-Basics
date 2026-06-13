tup = (1, 2, 3, 4, 5, 6)
for val in tup:
    print(val)

str = "Janhvi Gupta"
for char in str:
    print(char)

#Print the elements of the following list using a loop.
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for val in nums:
    print(val)

#search for a number x in this tuple using loop:
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 4)
#linear search

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 4)
x = 4

idx = 0
for el in nums:
    if (el == x):
        print("FOUND AT INDEX", idx)
        break 
    idx += 1

#RANGE IN PYTHON

for i in range(11):
    print(i)

#range(start?, stop, step?):
for i in range(2, 101, 2):
    print(i)

#print numbers from 1 to 100
for i in range(1, 101, 1):
    print(i)

# print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)

#print the multiplication table of a number n
n = int(input("enter a number: "))
for i in range(1, 11):
    print(n*i)

#PASS STATEMENT

for i in range(5):
    pass
print("THANKS")

#WAP to find the factorial of first n numbers.
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial =", fact)