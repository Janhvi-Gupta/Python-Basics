def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(2, 4)
#more lines of code
calc_sum(45, 67)

#OR

def calc_sum(a, b):
    return a + b

sum = calc_sum(1, 2)
print(sum)
#more number of lines
sum = calc_sum(34, 67)
print(sum)

#STRING

def print_hello():
    print("hello")

print_hello()
#more number of lines
print_hello()
#mpore number of lines
print_hello()

#AVERAGE OF VALUES

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(2, 4, 6)


def calc_prod(a= 2, b= 3):
    print(a * b)
    return(a * b)

calc_prod(3)



#WAF to print the length of a list.
cities = ["delhi", "gurgaon", "mumbai", "indore", "chennai"]
def print_len(list):
    print(len(list))
    return len(list)

print_len(cities)



#WAF to print the elements of a list in a single line.
emotions = ["happy", "sad", "excited", "dissappointed"]
def print_el(list):
    for item in list:
        print(item, end=" ")

print_el(emotions)

#WAF to find the factorial of n.
def calc_fact(a):
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    print(fact)
    return(fact)
    
calc_fact(5)
calc_fact(7)
calc_fact(4)



#WAF to convert USD to INR.
def USD_INR(USD, INR= 95.11):
    print(USD * INR)
    return(USD * INR)

USD_INR(3)

#OR
def converter(usd_val):
    inr_val = usd_val * 95.11
    print(usd_val, "USD =", inr_val, "INR")

converter(3)



#WAF to check if the number is odd or even.
def odd_even(n):
    if (n % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

odd_even(7)
odd_even(46)