"""
Q) Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


num1 = int(input("Pick a number: "))
diviser = int(input("Pick a second number: "))
if num1 % diviser == 0:
    print(f"Your number {num1} is divisible by {diviser}. How cool!")
    if num1 % 4 == 0:
        print(f"Your first number, {num1}, is not only even but divisble by 4")
    elif num1 % 2 == 0:
            print(f"Your first number, {num1}, is also even")
    else:
        print(f"The number you chose: {num1} is Odd")
else:
    if num1 % 4 == 0:
        print(f"Your number is not only even but also divisible by 4! ")
    elif num1 % 2 == 0:
            print(f"The number you chose: {num1} is Even")
    else:
        print(f"The number you chose: {num1} is Odd")

if diviser % 4 == 0:
    print(f"Your second number, {diviser}, is not only even but divisble by 4")
elif diviser % 2 == 0:
    print(f"Your second number, {diviser}, is also even")
else:
    print(f"The second number you chose: {diviser} is Odd")