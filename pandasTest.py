# Sherry Sherry_Zhang_Data_Science
# 1/5/22

# Insurance Calculation

import os
import pandas as pd

os.system('cls')

df2 = pd.DataFrame([[1, 'San Diego', 100], [2, 'Los Angeles', 120], [3, 'San Fransisco', 90], [4, 'Sacramento', 115]], 
                columns=['Store #', 'Location', 'Store ID'])

print(df2)
print()

df3 = pd.DataFrame([[1, 't-skirt', 'blue'], [2, 't-skirt', 'green'], [3, 'skirt', 'red'], [4, 'skirt', 'black']],
columns=['Product ID', 'Product Name', 'Color'])

df3.to_file('wardrobe.csv')

print(df3)
print()

ins = pd.read_csv('Insurance Practice\insurance_data.csv')

ins['sex'] = ins['sex'].replace(['female'], 0)
ins['sex'] = ins['sex'].replace(['male'], 1)

ins['smoker'] = ins['smoker'].replace(['no'], 0)
ins['smoker'] = ins['smoker'].replace(['yes'], 1)

insurance_cost_total = []

for index in range(len(ins)):
    row = list(ins.iloc[index])
    insurance_cost = 250*int(row[0]) - 128*int(row[1]) + 370*float(row[2]) + 425*int(row[3]) + 24000*int(row[4]) - 12500
    insurance_cost = int(insurance_cost*100)/100
    insurance_cost_total.append(insurance_cost)

ins['Cost'] = insurance_cost_total

print(ins)
