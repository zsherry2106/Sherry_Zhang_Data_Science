#Sherry Zhang
#1/20/22

#Lists and Arrays Practice

import os
os.system('cls')

fruits = ['apples', 'oranges', 1, 7, 'banana']
print(fruits)

print(len(fruits))

for elem in fruits:
    print(type(elem))

mylist = list((3, 5, 6))
print(mylist)

fruits.append('kiwi')
fruits.insert(3, 'grapes')
print(fruits)

fruits.append(mylist)
print(fruits)
