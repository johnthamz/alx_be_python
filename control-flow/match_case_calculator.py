#Python script named match_case_calculator.py. This calculator will prompt the user to enter two numbers and select an operation.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

#Use match case to perform the selected operation
match operation:
    case "+":
        result = num1 + num2  #addition
        print(f"The result is {result}")
    case "-":
        result = num1 - num2    #subtraction
        print(f"The rsult is {result}")
    case "*":
        result = num1 * num2   #multiplication
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation. Please choose +, - * or /")




