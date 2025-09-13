import sys  # Import sys module to access command line arguments

# Define functions for basic arithmetic operations
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

if __name__ == "__main__":
    # sys.argv[1], sys.argv[2], sys.argv[3] are command line arguments passed by the user
    # Convert the first and third arguments to int or float for numeric operations
    num1 = float(sys.argv[1])
    operation = sys.argv[2].lower()  # Convert operation to lowercase to handle case-insensitive input
    num2 = float(sys.argv[3])

    # Use conditional statements to call the appropriate function based on the operation
    if operation == "add":
        result = add(num1, num2)
    elif operation == "sub":
        result = sub(num1, num2)
    elif operation == "mul":
        result = mul(num1, num2)
    elif operation == 'div':
        # Handle division carefully (no zero division check here for simplicity)
        result = div(num1, num2)
    else:
        result = "Invalid operation"

    print("Output:", result)