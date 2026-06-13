# #Print the multiplication table of a number n.

n = int(input("enter a number "))
i = 1
while i <= 10:
    print(n*i)
    i+=1

#Print the elements of the following list using a loop.
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#traverse
i = 1
while i <= 10:
    print(pow(i,2))
    i+=1

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(nums):
    print(nums[i])
    i+=1

#search for a number x in this tuple using loop:
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(nums):
    print(nums[i])
    i+=1
print("Index of number is", nums.index(36))

# # # #alternate meathod
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND AT INDEX", i)
    i += 1

i = 1
while i <= 5:
    if (i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

# # #WAP to find the sum of first n natural numbers.
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum =", sum)