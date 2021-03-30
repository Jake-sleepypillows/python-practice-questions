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
