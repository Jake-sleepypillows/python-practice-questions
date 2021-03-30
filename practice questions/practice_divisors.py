 # Divisors. Takes a number, returns all divisors. Prints new list.
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
