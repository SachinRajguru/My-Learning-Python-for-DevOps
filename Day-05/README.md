# Command Line Arguments & Environment Variables

## Command Line Arguments

**Why Command Line Arguments?**

   - Avoid hardcoding input values inside the program.
   - Allow users to pass inputs dynamically when running the program.
   - Example: `python calculator.py 2 add 3`
   - Similar to AWS CLI commands like `aws s3 ls`.

**How to Read Command Line Arguments in Python?**

   - Use the built-in `sys` module.
   - Import it with `import sys`.
   - Access arguments via `sys.argv` list:
       - `sys.argv[0]` is the script name.
       - `sys.argv[1]` is the first argument (e.g., number 1).
       - `sys.argv[2]` is the second argument (e.g., operation).
       - `sys.argv[3]` is the third argument (e.g., number 2).

**Important Notes:**

   - Arguments are read as `strings` by default.
   - Convert numeric inputs to `int` or `float` before calculations.
   - Use conditional statements to decide which operation to perform (`add`, `sub`, `mul`).

**Example Code Snippet for Calculator with Command Line Arguments**

```python
import sys # sys module helps us to read command line arguments

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

if __name__ == "__main__":
    num1 = float(sys.argv[1])
    operation = sys.argv[2].lower()
    num2 = float(sys.argv[3])

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
```
---

## Environment Variables (Env Vars)

**Why Use Environment Variables?**

   - To handle sensitive information like passwords, API keys, tokens.
   - Avoid exposing sensitive data in command line arguments or source code.
   - Useful in automation, CI/CD pipelines, and production environments.

**How to Set Environment Variables?**

   - In Linux/macOS terminal:
```bash
    export PASSWORD=your_password_here
    export API_TOKEN=your_api_token_here
```

   - In Windows Command Prompt:
```bash
    set PASSWORD=your_password_here
    set API_TOKEN=your_api_token_here
```

**How to Read Environment Variables in Python?**

   - Use the built-in `os` module.
   - Import it with `import os`.
   - Access variables using `os.getenv("VARIABLE_NAME")`.

**Example:**

```python
import os # os module helps us access environment variables

password = os.getenv("PASSWORD")
api_token = os.getenv("API_TOKEN")

print("Password:", password)
print("API Token:", api_token)
```

---

## Summary

| Concept                | Use Case                      | How to Access in Python     |
|-------------------------|-------------------------------|-----------------------------|
| Command Line Arguments  | Passing inputs dynamically    | `import sys` → `sys.argv`   |
| Environment Variables   | Handling sensitive info securely | `import os` → `os.getenv()` |

**Final Advice**

   - Avoid hardcoding values in your scripts.
   - Use command line arguments for general inputs.
   - Use environment variables for sensitive data.
   - Practice modifying your existing scripts to use these concepts.