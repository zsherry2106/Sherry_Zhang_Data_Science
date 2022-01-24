#Sherry Zhang
#1/24/22

#Prepare Dataset
#Change female/male and smoker/nonsmoker

import os, csv
os.system('cls')

file = open('insurance_data.csv')
insuranceFile = csv.reader(file)

#Next - get the next value
header = next(insuranceFile)
print(header)

insurance_data = []

for row in insuranceFile:
    insurance_data.append(row)

#Change female to 0
#Change male to 1
for row in insurance_data:
    if row[1] == 'female':
        row[1] = int(0)
    elif row[1] == 'male':
        row[1] = int(1)

#Change smokers to 1
#Change non smokers to 0
for row in insurance_data:
    if row[4] == 'no':
        row[4] = int(0)
    elif row[4] == 'yes':
        row[4] = int(1)
    
    # print(row)

for row in insurance_data:
    insurance_cost = 250*int(row[0]) - 128*int(row[1]) + 370*float(row[2]) + 425*int(row[3]) + 24000*int(row[4]) - 12500
    insurance_cost = int(insurance_cost*100)/100
    row.append(insurance_cost)

#Create new list with 4 regions insurance cost average
def region_average(region):
    count = 0
    sum_cost = 0
    for row in insurance_data:
        if row[5] == region:
            count += 1
            sum_cost += row[7]
    
    average = int(sum_cost/count*100)/100
    return average

region_average_cost = []
region_average_cost.append(['northeast', region_average('northwest')])
region_average_cost.append(['northwest', region_average('northwest')])
region_average_cost.append(['southeast', region_average('southeast')])
region_average_cost.append(['southwest', region_average('southwest')])

print(region_average_cost)

#Create with only females and one with only males
female_info = []
for row in insurance_data:
    if row[1] == 0:
        female_info.append(row)

male_info = []
for row in insurance_data:
    if row[1] == 1:
        male_info.append(row)

#Create with only smokers and one with only non smokers
smoker_info = []
for row in insurance_data:
    if row[4] == 1:
        smoker_info.append(row)

non_smoker_info = []
for row in insurance_data:
    if row[4] == 0:
        non_smoker_info.append(row)
