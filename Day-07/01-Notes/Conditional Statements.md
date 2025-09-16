# Conditional Statements in Python

Conditional statements are used to make decisions in a program. They allow you to execute different blocks of code depending on whether a condition is `True` or `False`.

In Python, we use the following types of conditional statements:
- `if`
- `if-else`
- `if-elif-else`
- Nested `if`
- Shorthand `if` (Ternary operator)

## `if` Statement

The `if` statement is used to execute a block of code if a specified condition is `True`. If the condition is `False`, the code block is skipped.

- Example:

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

## `elif` Statement

The `elif` (else-if) statement allows you to check additional conditions if the previous `if` or `elif` conditions are `False`.
You can have multiple `elif` statements after the initial `if` statement.

```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
elif condition3:
    # Code to execute if condition3 is True
# ...
else:
    # Code to execute if none of the conditions are True
```

- Example:

```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is not greater than 5")
```

## `if-else` Statement

The `else` statement is used to specify a block of code to execute when none of the previous conditions (`if` or `elif` statements) are `True`.

```python
if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False
```

- Example:

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

## Nested `if`

You can place one `if` statement inside another to check multiple layers of conditions.

```python
if condition1:
    # Code if condition1 is True
    if condition2:
        # Code if both condition1 and condition2 are True
```

- Example:

```python
x = 25
if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is also greater than 20")
```

## Shorthand if (Ternary Operator)

The shorthand if (also called a ternary operator) allows you to write conditional expressions in a single line.
This makes the code concise when you only need one simple if-else.

```python
true_value if condition else false_value
```

- Example:

```python
x = -3
print("x is positive") if x > 0 else print("x is not positive")
```

---

## Summary Table

   | Statement Type | Usage Example                        | Description                        |
| -------------- | ------------------------------------ | ---------------------------------- |
| `if`           | `if x > 5:`                          | Executes code if condition is True |
| `if-else`      | `if x > 5: ... else: ...`            | Executes alternative code if False |
| `if-elif-else` | `if ... elif ... else ...`           | Checks multiple conditions         |
| Nested `if`    | `if ...: if ...:`                    | Condition inside another condition |
| Shorthand `if` | `print("A") if cond else print("B")` | One-line conditional expression    |
