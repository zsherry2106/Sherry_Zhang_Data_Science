#Sherry Zhang
#1/13/2022

#Strings and Lists Practice

import os, random
os.system('cls')

num1 = 8
num2 = 4.5
char = 't'
flag = False
str1 = 'Hello there'
str2 = " Goodbye there"

#concatenation
print(str1 + ' ' + str2)
print(str1 + ' ' + str(num1) + str2)

print(type(num2))
print(str1[-1])
print(str1[3:7])

print('Hello \t Peter \nI am here\\or not \"Goodbye\"')

for letter in str1:
    print(letter, end = ' ')
print()

for i in range(10, 21):
    print(i, end = ' ')
print()

#convert input to int, will automatically be string
while 1:
    mario_size = input("Size for Mario tower: ")

    try:
        mario_size = int(mario_size) +1
        if mario_size < 26:
            break

    except ValueError:
        print("Enter a number between 1 and 25")

space = mario_size

while mario_size != 0:
    for i in range(mario_size):
        print(" "*space, end='')
        print("*"* int(mario_size-space), " ", end='')
        print("*"* int(mario_size-space), end='')
        space -=1
        print()
    
    while 1:
        mario_size = input("Size for Mario tower: ")

        try:
            mario_size = int(mario_size) +1
            space = mario_size

            if mario_size < 26:
                break

        except ValueError:
            print("Enter a number")

print()
