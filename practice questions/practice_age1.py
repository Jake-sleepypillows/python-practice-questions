"""
Q) Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

def calc_age(age):
    return age * 365
print(calc_age(21))

def find_perimeter(length, width):
    perimiter = (length*2)+(width*2)
    return perimiter

def time_for_milk_and_cookies(month, day):
    if month == 12 and day == 24:
        return True
    else:
        return False

def sum_polygon(n):
    angle = (n - 2) * 180
    return angle