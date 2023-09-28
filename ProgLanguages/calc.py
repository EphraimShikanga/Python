"""A simple calculator that greets the user and adds the two numbers they input."""

# Greet the user
user = input("Hello! What is your name? ")

# Provide the Two numbers
num1 = input("First Num: ")
num2 = input("Second Num: ")

# Add the two numbers
sum = int(num1) + int(num2)

# Print the sum
print(f"Hello {user}! The sum of {num1} and {num2} is {sum}.")
