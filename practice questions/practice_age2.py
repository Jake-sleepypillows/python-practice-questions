"""
Q) Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
import datetime

def get_input():
    x = True
    while x == True:
        try:
            name = input("What is your name: ")
            age = int(input("How old are you? "))
            had_birthday = input("Have you already had your birthday this year? (yes or no) ")
            if had_birthday[0] == "y":
                year = now.year - age
            else:
                year = now.year - age - 1
            print(f"{name} will turn 100 in {year + 100}")

            game = int(input("Actually, pick a number: "))
            repeat = int(game)
            for a in range(repeat):
                print(f"{name} will turn 100 in {year + 100}")
            print("Gotch-ya!!")
            x = False
        except ValueError:
            get_input()
            x = False

now = datetime.datetime.now()
print(now)
get_input()