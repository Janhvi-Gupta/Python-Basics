#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# movie1 = input("enter your movie 1: ")
# movie2 = input("enter your movie 2: ")
# movie3 = input("enter your movie 3: ")
# movies = [movie1 , movie2 , movie3]
# print(movies)

# movies = []
# movie1 = input("enter 1st movie ")
# movie2 = input("enter 2nd movie ")
# movie3 = input("enter 3rd movie ")
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

# movies = []
# movies.append(input("enter movie 1 "))
# movies.append(input("enter movie 2 "))
# movies.append(input("enter movie 3 "))
# print(movies)


#WAP to check if a list contains a palindrome of element.
list = []
list.append(input("enter element 1: "))
list.append(input("enter element 2: "))
list.append(input("enter element 3: "))
list.append(input("enter element 4: "))
print(list)
copy_list = list.copy()
copy_list.reverse()
if (list == copy_list):
    print("PALINDROME")
else:
    print("NOT PALINDROME")