"""
Q) Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:
1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
"""
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 3, 5, 1, 8, 5, 4, 9, 11, 50, 23, 645, 34, 12, 11, 10, 2, 3, 4]
list_check = 9
index = 0
new_list = []

#  print(len(a)) #  this was just to check the count of how many items in the list
for i in a:
    a.sort()  ##  sorted the list. Otherwise the for loop would exit after it hit the first number above the <= 5
    if a[index] <= list_check:
        new_list.append(a[index])
        index +=1
print(new_list)
