# Bitwise Operations in Python

## Introduction

Bitwise operators in Python are used to perform operations on individual bits of binary numbers. These operators include bitwise AND, OR, XOR, and more.

## List of Bitwise Operators

1. **Bitwise AND (`&`):** Performs a bitwise AND operation on the binary representations of the operands.  
2. **Bitwise OR (`|`):** Performs a bitwise OR operation.  
3. **Bitwise XOR (`^`):** Performs a bitwise XOR operation (exclusive OR).  
4. **Bitwise NOT (`~`):** Flips all bits of the operand, changing `0` to `1` and `1` to `0`.  
5. **Left Shift (`<<`):** Shifts the bits to the left by a specified number of positions (adds zeros on the right).  
6. **Right Shift (`>>`):** Shifts the bits to the right (discards bits on the right).  

## Examples

### Bitwise AND (`&`)

```python
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a & b  # Result: 0001 (Decimal: 1)
```

### Bitwise OR (`|`)

```python
x = 10  # Binary: 1010
y = 7   # Binary: 0111
result = x | y  # Result: 1111 (Decimal: 15)
```

### Bitwise XOR (`^`)

```python
p = 6   # Binary: 0110
q = 4   # Binary: 0100
result = p ^ q
print(result)  # Output: 2 (Binary: 0010)
```

### Bitwise NOT (`~`)

```python
n = 5   # Binary: 0101
result = ~n
print(result)  # Output: -6 (Explanation: -(n+1))
```

### Left Shift (`<<`)

```python
m = 5   # Binary: 0101
result = m << 1
print(result)  # Output: 10 (Binary: 1010)
```

### Right Shift (`>>`)

```python
k = 20  # Binary: 10100
result = k >> 2
print(result)  # Output: 5 (Binary: 0101)
```

---

## Summary

   - Bitwise operators work directly on binary digits (`0` and `1`).
   - Useful for tasks like setting flags, masking, compression, or performance optimization.
   - Common operators include `&`, `|`, `^`, `~`, `<<`, and `>>`.
