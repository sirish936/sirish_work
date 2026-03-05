# Read input values from user
x = int(input("Enter first number (x): "))
y = int(input("Enter second number (y): "))

# Add the numbers
result = x + y

# Print the output
print(f"The sum of {x} and {y} is: {result}")

# Read input values from user
x = input("Enter first string (x): ")
y = input("Enter second string (y): ")

# Concatenate the strings
result = x + y

# Print the output
print(f"The concatenation of {x} and {y} is: {result}")

ch = input("Enter a character: ")
print("You entered: ",ch)
print("You entered: ",ch[0])

ch = input("Enter a character: ")[0]
print("You entered: ",ch)

ch = eval(input("Enter an expression: "))
print("Your result is: ",ch)

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
result = x + y
print(f"The sum of {x} and {y} is: {result}")