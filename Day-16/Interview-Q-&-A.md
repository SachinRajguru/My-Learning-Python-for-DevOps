# 🐍 Python + DevOps Interview Questions (Beginner & Intermediate)

## 1. Describe a real-world example of how you used Python to solve a DevOps challenge

You can describe one of these:

- **GitHub Webhooks Project:**  
  Automated issue tracking by integrating GitHub webhooks with JIRA API using Python’s `requests` module.  
  Whenever a new commit was pushed, it automatically created or updated a JIRA issue.

- **File Operations Script:**  
  Created Python scripts to automate log file rotation and archiving using `os`, `shutil`, and `datetime` modules, reducing manual maintenance.

- **JIRA Integration Script:**  
  Used Python with REST APIs to fetch unresolved JIRA tickets and send alerts via email or Slack bot.

✅ *Impact:* Helped automate repetitive DevOps tasks and improved incident tracking efficiency.

---

## 2. Discuss the challenges you faced while using Python for DevOps and how you overcame them

**Example:**  
While working on a JIRA-GitHub integration, I faced authentication and API rate-limit issues.  
I solved this by:
- Using environment variables for secure API key handling.
- Implementing retry logic with exponential backoff using the `time` module.

---

## 3. How can you secure your Python code and scripts?

- Store sensitive data in:
  - Environment variables (`os.environ`)
  - Config files with restricted access
  - Command-line arguments or secret managers (like Azure Key Vault)
- Never hardcode credentials.
- Use `.env` files with `python-dotenv`.
- In CI/CD, store secrets in the pipeline’s secure vault.

---

## 4. Explain the difference between mutable and immutable objects

- **Mutable:** Can change after creation (e.g., `list`, `dict`, `set`)
- **Immutable:** Cannot change after creation (e.g., `tuple`, `str`, `int`)

**Example:**
```python
my_list = [1, 2, 3]
my_list[0] = 0  # Mutable

my_tuple = (1, 2, 3)
# my_tuple[0] = 0  # Immutable -> Error
```

---

## 5. Differentiate between list and tuple

| Feature | List | Tuple |
|----------|------|--------|
| Mutability | Mutable | Immutable |
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Use Case | Data that may change | Fixed data |
| Performance | Slower | Faster |

---

## 6. Explain the use of virtualenv

Virtualenv creates **isolated environments** for Python projects.

**Example:**
```bash
python -m venv myenv
source myenv/bin/activate     # Linux/macOS
myenv\Scripts\activate        # Windows
```

---

## 7. What are decorators in Python?

Decorators modify or extend function behavior without changing the function itself.

**Example:**
```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

Common use cases in DevOps:
- Logging
- Retry logic
- Authentication wrappers

---

## 8. How does exception handling work in Python?

Structure:
```python
try:
    # risky code
except ExceptionType:
    # handle error
else:
    # executes if no error
finally:
    # always executes
```

Example:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero not allowed.")
finally:
    print("Execution completed.")
```

---

## 9. What's the difference between append() and extend()?

| Method | Function |
|---------|-----------|
| `append(x)` | Adds a single element |
| `extend(iterable)` | Adds multiple elements |

**Example:**
```python
a = [1, 2, 3]
a.append(4)       # [1, 2, 3, 4]
a.extend([5, 6])  # [1, 2, 3, 4, 5, 6]
```

---

## 10. Explain the use of lambda functions in Python

Lambda functions are small, anonymous one-liners used for short operations.

**Example:**
```python
square = lambda x: x**2
print(square(5))  # Output: 25
```

Common in DevOps scripts for filtering, mapping, and sorting tasks.

---

## 11. What are the different types of loops in Python?

**For loop:**
```python
for i in range(5):
    print(i)
```

**While loop:**
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## 12. Explain the difference between == and is operators

- `==` → compares **values**
- `is` → compares **object identity**

**Example:**
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (same values)
print(a is b)  # False (different objects)
```

---

## 13. What is the use of the pass keyword?

The `pass` statement does nothing — used as a placeholder.

**Example:**
```python
def future_function():
    pass  # To be implemented later
```

---

## 14. What is the difference between global and local variables?

- **Global variable:** Defined outside functions, accessible everywhere.
- **Local variable:** Defined inside a function, only accessible there.

**Example:**
```python
global_var = 10

def my_func():
    local_var = 5
    print(global_var, local_var)
```

---

## 15. Explain the difference between open() and with open()

| Function | Description |
|-----------|--------------|
| `open()` | Must close file manually |
| `with open()` | Closes file automatically (preferred) |

**Example:**
```python
with open('example.txt', 'r') as file:
    data = file.read()
# file automatically closed
```

---

## ✅ Bonus: Python in DevOps Context

**Python is used for:**
- Automating provisioning and configuration (Terraform, Ansible)
- Writing custom monitoring scripts (Azure Monitor, CloudWatch)
- Integrating CI/CD pipelines (Jenkins, GitHub Actions)
- API integrations (JIRA, Slack, GitHub)
- File management and log analysis

---

**Tip:**  
For interviews, relate Python knowledge to **real DevOps use cases** — automation, monitoring, CI/CD, and cloud API interactions.