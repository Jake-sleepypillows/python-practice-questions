"""
Create a program that asks the user for a number and then prints out a list
 of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

while True:
    try:
        new_list = [] #this is the list that gets created when a number divides evenly by the input
        num1 = int(input("Pick a number: "))
        for num in range(1,num1 + 1):
            if num1 % num == 0:
                print(num)  # possible to do without making a list... but who doesnt love a list!
                new_list.append(num) # this appends the number to the list.
        print(new_list)
        break
    except ValueError:
        print("Please select a number. :-)")
