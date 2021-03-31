"""
Q) Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

a = random.randint(1,10)
print(a)
b = 0
count = 0
while True:
    try:
        while b != a:
            b = int(input("Guess the number: "))
            if a - b >= 1:
                print("Higher")
                count += 1
            elif a - b <= -1:
                print("lower")
                count +=1
            else:
                if a - b == 0:
                    count += 1 
                    if count >= 2:
                        print(f"Congrats you nailed it! It took you {count} guess's")
                        break
                    else:
                        print(f"Congrats you guessed it first go!")
                        break
    except ValueError:
        print(f"Thanks for playing. You guessed {count} times")
    break