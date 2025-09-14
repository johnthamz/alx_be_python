# Python script that will calculate the user’s monthly savings based on inputted monthly income and expenses
#User Input for Financial Details
    #Prompt the user for their monthly income

monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

#Calculate Monthly Savings

monthly_savings = monthly_income - monthly_expenses

#Project Annual Savings
#Assume a simple annual interest rate of 5%.
#Calculate the projected savings after one year, incorporating the interest

projected_savings = monthly_savings *12 + (monthly_savings * 12 * 0.05)

#Display the results
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
