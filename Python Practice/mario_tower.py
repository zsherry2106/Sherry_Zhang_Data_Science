#Sherry Zhang
#1/13/22

#Mario Tower

import os
os.system('cls')

while 1:
    while 1:
        mario_size = input("Size for Mario tower: ")

        try:
            mario_size = int(mario_size)
            space = mario_size

            if 0 < mario_size < 26:
                break

            else:
                print("Please enter a number between 1 and 25")

        except ValueError:
            print("Enter a number")
    
    if mario_size == -1:
        break

    mario_size += 1

    for i in range(mario_size):
        print(" "*space, end='')
        print("*"* int(mario_size-space), " ", end='')
        print("*"* int(mario_size-space), end='')
        space -=1
        print()

print()
