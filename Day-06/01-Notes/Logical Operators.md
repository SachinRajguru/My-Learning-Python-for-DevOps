# Logical Operations in Python

## Introduction

Logical operators in Python are used to manipulate and combine Boolean values.  
They allow you to perform logical operations such as `and`, `or`, and `not`.

## List of Logical Operators

1. **AND (`and`)** → Returns `True` if **both operands** are `True`.
2. **OR (`or`)** → Returns `True` if **at least one operand** is `True`.
3. **NOT (`not`)** → Returns the **opposite Boolean value** of the operand.

## Examples

### AND Operator (`and`)

```python
x = True
y = False

print(x and y)  # False
print(True and True)  # True
```

### OR Operator (`or`)

```python
a = True
b = False

print(a or b)  # True
print(False or False)  # False
```

### NOT Operator (`not`)

```python
flag = True

print(not flag)   # False
print(not False)  # True
```

---

## Summary

   - Logical operators work on Boolean (`True` / `False`) values.
   - `and` → True only if both conditions are True.
   - `or` → True if at least one condition is True.
   - `not` → Reverses the Boolean value.
   - Widely used in **conditions, loops, and decision-making statements**.