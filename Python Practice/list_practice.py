#Sherry Zhang
#1/22/22

#List Practice HW

import os
os.system('cls')

#Replace first occurence of 20 with 200
list1 = [15, 100, 154, 20, 253, 530, 203]
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break
print(list1)

#Remove all occurences of 20
list1 = [5, 20, 15, 20, 25, 50, 20]
list2 = []
for i in list1:
    if i != 20:
        list2.append(i)
print(list2)

#Remove empty strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list(filter(None, list1)))

#Add 7000 after occurrence of 6000
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#Add 'h', 'i', 'j'
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ['h', 'i', 'j']
for i in list2:
    list1[2][1][2].append(i)
print(list1)

#Iterate 1 list in order and one in reverse
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i in range(len(list1)):
    print(f"{list1[i]} {list2[-(i+1)]}")

#Combine 2 strs (same indexes) from lists
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])
print(list3)

#square every element in a list
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = []
for i in list1:
    list2.append(i**2)
print(list2)

#Create list with every word in str
list1 = "The best class in Greenhill is Data Science"
list2 = list1.split()
print(list2)
