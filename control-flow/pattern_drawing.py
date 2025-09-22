
# 1. Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# 2. Use a while loop to go through each row
row = 0
while row < size:
    # 3. Use a for loop to print stars in the current row
    for col in range(size):
        print("*", end="")  # Print star without moving to the next line
    print()  # Move to the next line after finishing one row
    row += 1
