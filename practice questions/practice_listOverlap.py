"""
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:
1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

# List overlap. Check if an element exists in both list a and list b. These lists are randomly generate.
import random

list_a = []
list_b = []

def list_creation(list):
    for i in range(0,random.randint(10,50)):
        n = random.randint(1,50)
        list.append(n)
    #list.sort()
    print(list)


def list_check(a, b):
    lm = []
    for i in range(len(a)):
        if i in b:
            lm.append(a[i])
            lm = list(dict.fromkeys(lm))
            lm.sort()
    print(f"\nThe following numbers were in both lists: A total of {len(lm)} numbers.\n{lm}")

list_creation(list_a)
list_creation(list_b)
list_check(list_a, list_b) # this calls the list check function.


# this is a single line function to print the results from two lists. !!!Figure out how it works!!!
#print([k for k in {*(int(i) for i in list_a)}.intersection({*(int(i) for i in list_b)})]) 
