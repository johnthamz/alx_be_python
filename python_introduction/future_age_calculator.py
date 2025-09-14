# Python script that asks the user for their current age and then calculates how old they will be in a specific future year.
#Prompt the user to input their current age with the question:
current_age = int(input("How old are you"))

#Calculate years until 2050 (2050 - 2023 = 27)
years_until_2050 = 2050 - 2023

#Compute age in 2050
age_in_2050 = current_age + years_until_2050

#Print result 
print(f"in 2050, you will be {age_in_2050} years old")

