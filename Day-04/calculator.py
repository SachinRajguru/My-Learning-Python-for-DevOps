# Module (functions live here)
# calculator.py

# --- Approach 1: Recommended (functions take parameters) ---
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

# Calling functions with arguments
print(add(10, 5))
print(sub(10, 5))
print(mul(10, 5))
print(div(10, 5))


# --- Approach 2: Not recommended (functions use fixed values) ---
# Learning Note:
# This works, but it's a bad practice because values are hardcoded.
# Functions should be reusable with parameters instead of fixed inputs.

# num1 = 10
# num2 = 5

# def add():
#     addition = num1 + num2
#     print(addition)

# def sub():
#     subtraction = num1 - num2
#     print(subtraction)

# def mul():
#     multiplication = num1 * num2
#     print(multiplication)

# def div():
#     division = num1 / num2
#     print(division)

# # Calling functions (without flexibility)
# add()
# sub()
# mul()
# div()