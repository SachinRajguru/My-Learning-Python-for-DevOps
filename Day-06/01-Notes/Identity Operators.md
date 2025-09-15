# Identity Operations in Python

## Introduction

Identity operators in Python are used to compare the memory locations of two objects.  
They help determine whether two variables point to the **same object** (not just equal values).  
There are two identity operators: `is` and `is not`.

## List of Identity Operators

1. **is:** Returns `True` if both operands refer to the same object.
2. **is not:** Returns `True` if both operands refer to different objects.

### Examples

#### `is` Operator

```python
x = [1, 2, 3]
y = x        # y refers to the same object as x
z = [1, 2, 3]

print(x is y)  # True (same object in memory)
print(x is z)  # False (different objects, even if values are same)
```

#### `is not` Operator

```python
a = "hello"
b = "world"
c = a

print(a is not b)  # True (different objects)
print(a is not c)  # False (same object)
```

---

## Summary

  - Identity operators compare object identity, not just equality of values.
  - `is` → True if two references point to the same object.
  - `is not` → True if two references point to different objects.
  - Useful when you want to check if two variables share the same memory reference, especially with mutable objects like lists and dictionaries.