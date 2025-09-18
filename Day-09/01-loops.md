# Loops in Python (for and while)

## Introduction

Loops are a fundamental concept in programming that allow you to perform repetitive tasks efficiently.  
In Python, there are two primary types of loops:
- **for loop** → used for iterating over a sequence.  
- **while loop** → used for repeating a block of code while a condition is true.

---

## For Loop

The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item.

**Syntax:**

```python
for variable in sequence:
    # Code to be executed for each item in the sequence
```

**Example:**

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)   # Prints each element in the list one by one
```

**Output:**

```
apple
banana
cherry
```

---

## While Loop

The `while` loop keeps executing a block of code as long as the condition is `True`.  
It’s useful when the number of iterations is not known beforehand.

**Syntax:**

```python
while condition:
    # Code to be executed as long as the condition is True
```

**Example:**

```python
count = 0

while count < 5:
    print(count)   # Prints the current value of count
    count += 1     # Increment count to avoid infinite loop
```

**Output:**

```
0
1
2
3
4
```

---

## Summary Table

| Loop Type   | Syntax Example                      | Usage                                |
|-------------|-------------------------------------|--------------------------------------|
| **for**     | `for item in sequence:`             | Iterates over items in a sequence    |
| **while**   | `while condition:`                  | Repeats while condition is `True`    |