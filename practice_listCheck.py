 # Print numbers in list less than number.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 3, 5, 1, 8, 5, 4, 9, 11, 50, 23, 645, 34, 12, 11, 10, 2, 3, 4]
list_check = 9
index = 0
new_list = []

#  print(len(a)) #  this was just to check the count of how many items in the list
for i in a:
    a.sort()  ##  sorted the list. Otherwise the for loop would exit after it hit the first number above the <= 5
    if a[index] <= list_check:
        new_list.append(a[index])
        index +=1
print(new_list)
