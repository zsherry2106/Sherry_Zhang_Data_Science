#Sherry Zhang
#1/18/22

#Str practice

import os
os.system("cls")

str1 = 'test'

print(f"Casefold: {str1.casefold()}")

print(f"Count: {str1.count('t')}")

print(f"Endswith: {str1.endswith('t')}")

print(f"Find: {str1.find('e')}")

dict1 = {'x': 1, 'y': 2, 'z': 3}
print('{x} {y} {z}'.format_map(dict1))

print(f"isalnum: {str1.isalnum()}")

print(f"isdecimal: {str1.isdecimal()}")

print(f"isidentifier: {str1.isidentifier()}")

print(f"isnumeric: {str1.isnumeric()}")

print(f"isspace: {str1.isspace()}")

print(f"issuper: {str1.isupper()}")

print("ljust")
print(str1.ljust(20), 'test')

print(f"lstrip: {str1.lstrip('t')}")

print(f"partition: {str1.partition('e')}")

print(f"rfind: {str1.rfind('t')}")

print(f"rjust: {str1.rjust(20)}")

print(f"rsplit: {str1.rsplit('t')}")

print(f"split: {str1.split('e')}")

print(f"startswith: {str1.startswith('t')}")

print(f"swapcase: {str1.swapcase()}")

mydict = {115: 80}
print(f"translate: {str1.translate(mydict)}")

print(f"zfill: {str1.zfill(10)}")

print()
