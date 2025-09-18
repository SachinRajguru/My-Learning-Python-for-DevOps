# Loop Control Statements (break and continue)

## Introduction

Loop control statements modify the normal flow of loops, giving you more control and flexibility during iteration.
In Python, the two most common control statements are:

- **break** → exits the loop immediately.  
- **continue** → skips the current iteration and moves to the next one.
- **pass** → does nothing (placeholder statement).

---

## `break` Statement

The `break` statement is used to exit a loop prematurely.  
It works in both `for` and `while` loops.

**Example:**

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        break       # Exit loop when number is 3
    print(number)   # Print numbers until break is triggered
```

**Output:**

```
1
2
```

- In this example, the loop **stops execution** when it reaches the number `3`.

---

## `continue` Statement

The `continue` statement skips the current iteration and jumps to the **next iteration** of the loop.

**Example:**

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        continue    # Skip printing when number is 3
    print(number)   # Print all numbers except 3
```

**Output:**

```
1
2
4
5
```

- In this case, the loop **skips 3** and continues with the next number.

## Practice Exercise – Automating Log File Analysis

In DevOps, logs are crucial for troubleshooting.  
Here’s how you can use a `for` loop with conditions to find errors in logs.

**Example:**

```python
log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)   # Print only error lines
```

**Output:**

```
ERROR: File not found
ERROR: Database connection failed
```

- The loop processes each line and **filters only error messages** – a common DevOps use case.

---

## `pass` Statement

The `pass` statement is a **do-nothing placeholder**.  
It is often used when writing code structure but leaving some parts unimplemented for now.

**Example:**
```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        pass        # Do nothing when number is 3
    else:
        print(number)
```

**Output:**
```
1
2
4
5
```

- Here, the loop **does nothing** when the number is `3`, but continues execution normally for other numbers.

**DevOps Use Case:**  

You can use `pass` in automation scripts while **drafting functions or loops**, keeping the structure ready while you decide what logic to add later.

---

## Practice Exercise – Automating Log File Analysis

In DevOps, logs are crucial for troubleshooting.  
Here’s how you can use a `for` loop with conditions to find errors in logs.

**Example:**

```python
log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)   # Print only error lines
```

**Output:**

```
ERROR: File not found
ERROR: Database connection failed
```

- The loop processes each line and **filters only error messages** – a common DevOps use case.

---

## Summary Table

| Statement   | Behavior                                    | Use Case Example                          |
|-------------|---------------------------------------------|-------------------------------------------|
| **break**   | Exits the loop immediately                  | Stop checking once a match is found        |
| **continue**| Skips current iteration, moves to next loop | Skip invalid data or unnecessary iterations|
| **pass**    | Does nothing, placeholder                   | Draft automation logic without errors      |