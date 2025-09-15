# Membership Operations in Python

## Introduction

Membership operators in Python are used to check whether a value is present in a sequence or collection,  
such as a list, tuple, set, or string. The membership operators are `in` and `not in`.

## List of Membership Operators

1. **`in`** → Returns `True` if the left operand is found in the sequence on the right.  
2. **`not in`** → Returns `True` if the left operand is **not found** in the sequence on the right.  

## Examples

#### `in` Operator

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)   # True
print("grape" in fruits)    # False
```

#### `not in` Operator

```python
colors = ["red", "green", "blue"]

print("yellow" not in colors)  # True
print("red" not in colors)     # False
```

---

## Summary

   - `in` → Checks if a value exists in a sequence.
   - `not in` → Checks if a value does not exist in a sequence.
   - Works with **lists, tuples, sets, dictionaries (keys), and strings**.
   - Very useful for **searching, filtering, and condition checks**.