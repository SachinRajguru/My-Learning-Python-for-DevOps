# importing our module

# main.py
import calculator # importing our module - calculator.py (Module containing functions)

print("Calculator Demo")

a, b = 10, 3

print(f"{a} + {b} = {calculator.add(a, b)}")
print(f"{a} - {b} = {calculator.subtract(a, b)}")
print(f"{a} * {b} = {calculator.multiply(a, b)}")
print(f"{a} / {b} = {calculator.divide(a, b)}")
print(f"{a} % {b} = {calculator.modulus(a, b)}")


# # main.py (Using calculator module with alias)

# import calculator as calc   # alias 'calc' makes code shorter

# print("Addition:", calc.add(10, 5))
# print("Subtraction:", calc.sub(10, 5))
# print("Multiplication:", calc.mul(10, 5))
# print("Division:", calc.div(10, 5))