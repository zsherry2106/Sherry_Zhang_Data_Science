#Sherry Zhang
#1/26/22

#Diversity data code analysis/prep

import os, csv
os.system('cls')

file = open('diversity_school.csv')
divFile = csv.reader(file)

header = next(divFile)

div_data = []

for row in divFile:
    div_data.append(row)

file.close()

#Create dict with states
states = {}

#For loop to add states to dict
for row in div_data:
    if row[3] == 'Total Minority' and row[2] not in states.keys():
        states[row[2]] = 0



#Dict to add number of minoirites for each state
states_minority = states.copy()

#Add value from 'Total Minority' to dict with states
for row in div_data:
    if row[3] == 'Total Minority':
        states_minority[row[2]] += int(row[4])

print(states_minority)



#Dict to add number of colleges per state
states_college_num = states.copy()
for row in div_data:
    if row[3] == 'Total Minority':
        states_college_num[row[2]] += 1

print(states_college_num)



#Create dict to check greatest ethnic group per state
ethnic_groups_state = {}

#Use for loop to create states and then have empty dict as value
for row in div_data:
    if row[3] == 'Total Minority' and row[2] not in ethnic_groups_state.keys():
        ethnic_groups_state[row[2]] = {}

#Create dict to compare largest ethnic groups in each state
greatest_ethnic_state = ethnic_groups_state.copy()

#Add ethnic groups data to each state, don't include list below
non_groups = ['Women', 'Total Minority', 'Unknown', 'Non-Resident Foreign']
for row in div_data:
    if row[3] not in ethnic_groups_state[row[2]].keys() and row[3] not in non_groups:
        ethnic_groups_state[row[2]][row[3]] = int(row[4])

    elif row[3] in ethnic_groups_state[row[2]].keys() and row[3] not in non_groups:
        ethnic_groups_state[row[2]][row[3]] += int(row[4])
# print(ethnic_groups_state)

#Use dict to compare what ethnic group has the most amt of ppl per state
for state in ethnic_groups_state:
    largest_group = 0
    num = 0
    for group in ethnic_groups_state[state]:
        if ethnic_groups_state[state][group] > num:
            largest_group = group
            num = ethnic_groups_state[state][group]
    
    greatest_ethnic_state[state] = {largest_group: num}

print(greatest_ethnic_state)

#Add percentage column to list of data
for row in div_data:
    row.append(round(int(row[4])/int(row[1])*100, 2))
        
header.append('percentage')


out_file = open("div_percentage.csv", "w", newline = '')
writer = csv.writer(out_file)
writer.writerow(header)

for row in div_data:
    writer.writerow(row)

out_file.close()
