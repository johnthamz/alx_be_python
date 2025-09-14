#Simple Interest
#Python script that calculates the simple interest earned on an investment over a period of time

#The formula for simple interest is (I = P * R * T), 
# Where: 
       # ( I ) is the interest earned, 
       # ( P ) is the principal amount (initial investment),
       # ( R ) is the annual interest rate,
       # ( T ) is the time the money is invested for in years

principal = 1000           #represnting $1000
interest_rate = 0.05       #representing 5% annual interest rate
time = 3                   #representing 3 years

simple_interest = principal * interest_rate * time

print(f"The simple interest is {simple_interest}")

