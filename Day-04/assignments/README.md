# Day 4 Topics

- Functions  
- Modules  
- Packages  
- Virtual Environments (Python Workspaces)  

---

## 1. Functions in Python

### What is a Function?
- A function is a reusable block of code that performs a specific task.  
- Functions improve readability, modularity, and reusability of code.  
- Functions help in debugging by isolating logic.  

### Example: Calculator Program
Without functions (linear code):

```python
n1 = 10
n2 = 5

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
```

Problems:
- Less readable for large programs.  
- Not modular or reusable.  
- Difficult to debug.  

### Writing Functions
Syntax:
```python
def function_name(parameters):
    # function logic
    return result
```

Example:
```python
def addition(n1, n2):
    return n1 + n2
```

Calling functions:
```python
print(addition(10, 5))
```

### Advantages of Using Functions
- Readability: Easier to understand and maintain.  
- Reusability: Functions can be reused across different parts of the program.  
- Debugging: Easier to isolate and fix issues.  

### DevOps Use Cases for Functions
- Automating AWS resource creation (for example, S3 buckets, EC2 instances).  
- Interacting with APIs like Jira, GitHub.  
- Organizing scripts for automation and infrastructure management.  

---

## 2. Modules in Python

### What is a Module?
- A module is a Python file (.py) containing a collection of functions and variables.  
- Helps organize code into reusable components.  

Example:
```python
# calculator.py
def add(n1, n2):
    return n1 + n2
```

### Using Modules
```python
import calculator
print(calculator.add(10, 5))
```

With alias:
```python
import calculator as calc
print(calc.add(10, 5))
```

### Benefits of Modules
- Code reuse across multiple projects.  
- Easier maintenance and collaboration.  
- Logical separation of functionalities.  

---

## 3. Packages in Python

- A package is a collection of related modules organized in directories.  
- Helps manage large codebases by grouping modules.  

DevOps Context:  
- Engineers mostly consume packages rather than write them.  
- Examples:  
  - boto3 for AWS SDK  
  - jira for Jira API  
  - github for GitHub API  
  - requests for HTTP requests  

### Python Package Index (PyPI)
- Official repository for Python packages.  

Install with pip:
```bash
pip install package_name
```

List installed packages:
```bash
pip list
```

---

## 4. Virtual Environments in Python

### Why Virtual Environments?
- Different projects may require different versions of the same package.  
- Virtual environments create isolated spaces for dependencies.  

### Creating and Using Virtual Environments
1. Create:
```bash
python -m venv myenv
```

2. Activate:  
Linux or macOS:
```bash
source myenv/bin/activate
```
Windows:
```bash
myenv\Scripts\activate
```

3. Install packages:
```bash
pip install requests
```

4. Deactivate:
```bash
deactivate
```

---

## Summary

| Concept       | Description                              | DevOps Use Case Example               |
|---------------|------------------------------------------|----------------------------------------|
| Function      | Reusable block of code                   | Automate AWS resource creation         |
| Module        | Python file with multiple functions      | Share common functions across projects |
| Package       | Collection of modules                    | Use boto3 for AWS, jira for Jira API   |
| Virtual Env   | Isolated Python environment per project  | Manage different package versions      |

---

# Assignments

### Assignment 1: Calculator Program Using Functions (with inputs and return values)
- Write a Python program that defines functions for addition, subtraction, and multiplication.  
- Each function should:  
  1. Take two input parameters.  
  2. Perform the calculation.  
  3. Return the result.  

Then call these functions and print the results.

Example:
```python
def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

print("Add:", addition(10, 5))
print("Subtract:", subtraction(10, 5))
print("Multiply:", multiplication(10, 5))
```

---

### Assignment 2: Create and Use a Module
1. Save the above functions in a file named calculator.py.  
2. Create another file named main.py.  
3. Import the calculator module in main.py.  
4. Use the functions from the module.  

calculator.py:
```python
def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2
```

main.py:
```python
import calculator

print(calculator.addition(10, 5))
print(calculator.subtraction(10, 5))
```

Run:
```bash
python main.py
```

---

### Assignment 3: Create and Use a Virtual Environment
1. Create a virtual environment:
```bash
python -m venv myenv
```

2. Activate:  
Linux or macOS:
```bash
source myenv/bin/activate
```
Windows:
```bash
myenv\Scripts\activate
```

3. Install a package:
```bash
pip install requests
```

4. Verify:
```bash
pip list
```

5. Deactivate:
```bash
deactivate
```

---