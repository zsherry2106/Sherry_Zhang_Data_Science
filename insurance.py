# Sherry Sherry_Zhang_Data_Science
# 1/5/22

# Insurance Calculation

import os
os.system('cls')

#First patient
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500 
print(f"This person's insurance cost is {insurance_cost} dollars")

#Age factor
age += 4
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500 
change_in_insurane_cost = new_insurance_cost - insurance_cost
print(f"The change in cost of insurance after increasing the age by 4 years is {change_in_insurane_cost} dollars")

#BMI factor
age = 28
bmi += 3.1
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500 
change_in_insurane_cost = new_insurance_cost - insurance_cost
print(f"The change in cost of insurance after increasing BMI by 3.1 is {change_in_insurane_cost} dollars")

#Male vs Female
bmi = 26.2
sex = 1
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500 
change_in_insurane_cost = new_insurance_cost - insurance_cost
print(f"The change in cost of insurance for being male instead of female is {change_in_insurane_cost} dollars")

#Number of children
sex = 0
num_of_children = 1
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500 
change_in_insurane_cost = new_insurance_cost - insurance_cost
print(f"The change in cost of insurance for having 1 kid instead of three is {change_in_insurane_cost} dollars")

#Smoker vs Non-Smoker
num_of_children = 3
smoker = 1
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500 
change_in_insurane_cost = new_insurance_cost - insurance_cost
print(f"The change in cost of insurance for smoking instead of not smoking is {change_in_insurane_cost} dollars")
