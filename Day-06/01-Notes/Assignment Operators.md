# Assignment Operations in Python

## Introduction

Assignment operators in Python are used to assign values to variables. They include the basic assignment operator (`=`) and various compound assignment operators that perform an operation on the variable while assigning a value.

## List of Assignment Operators

1. **Basic Assignment (`=`):** Assigns a value to a variable. 
2. **Addition Assignment (`+=`):** Adds the right operand to the left operand and assigns the result to the left operand.
3. **Subtraction Assignment (`-=`):** Subtracts the right operand from the left operand and assigns the result to the left operand.
4. **Multiplication Assignment (`*=`):** Multiplies the left operand by the right operand and assigns the result to the left operand. 
5. **Division Assignment (`/=`):** Divides the left operand by the right operand and assigns the result to the left operand. 
6. **Floor Division Assignment (`//=`):** Performs floor division on the left operand and assigns the result to the left operand. 
7. **Modulus Assignment (`%=`):** Calculates the modulus of the left operand and assigns the result to the left operand. 
8. **Exponentiation Assignment (`**=`):** Raises the left operand to the power of the right operand and assigns the result to the left operand.  

## Examples

### Basic Assignment

```python
x = 5
```

### Addition Assignment

```python
y = 10
y += 4  # Equivalent to y = y + 4
```

### Subtraction Assignment

```python
a = 20
a -= 4  # Equivalent to a = a - 4
print(a)  # Output: 16
```

### Multiplication Assignment

```python
b = 7
b *= 2  # Equivalent to b = b * 2
print(b)  # Output: 14
```

### Division Assignment

```python
c = 15
c /= 3  # Equivalent to c = c / 3
print(c)  # Output: 5.0  (always float)
```

### Floor Division Assignment

```python
d = 17
d //= 3  # Equivalent to d = d // 3
print(d)  # Output: 5
```

### Modulus Assignment

```python
e = 22
e %= 6  # Equivalent to e = e % 6
print(e)  # Output: 4
```

### Exponentiation Assignment

```python
f = 4
f **= 3  # Equivalent to f = f ** 3
print(f)  # Output: 64
```

---

## Summary

   - Assignment operators allow you to update variables directly.
   - They make the code shorter and cleaner.
   - Common in loops, counters, and calculations.