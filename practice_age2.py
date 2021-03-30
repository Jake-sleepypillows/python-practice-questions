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