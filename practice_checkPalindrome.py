 # String lists. Check if input is palindrome. (read same backwards as forwards.)

word = input("Input a word to see if its a palindrome: ")

list_forward = list(word.lower())
list_reverse = list_forward[::-1]
print(list_forward)
print(list_reverse)

if list_reverse == list_forward:
    print("Fancy that, your word was a palindrome!")
else:
    print("Your word was not a palindrome. A palindrome is a word that reads the same both forward and backward.")
    
"""
for i in list_forward:
    if i[0] == list_reverse[0]:
        print("Fancy that your word was a palindrome!!")
        print(i)
    else:
        print("Your word was not a palindrome. A palindrome is a word that reads the same both forward and backward.")
        print(i)
""" # this little section did nothing...
