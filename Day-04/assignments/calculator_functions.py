# calculator_functions.py

# Function to add two numbers
def add(n1, n2):
    return n1 + n2

# Function to subtract two numbers
def sub(n1, n2):
    return n1 - n2

# Function to multiply two numbers
def mul(n1, n2):
    return n1 * n2

# Function to divide two numbers
def div(n1, n2):
    return n1 / n2  # Note: This will cause error if n2 is zero

# Using the functions and printing results
a = 10
b = 5

print("Addition:", add(a, b))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b))
print("Division:", div(a, b))