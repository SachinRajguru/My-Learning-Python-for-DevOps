# Precedence of Operations in Python

## Introduction

Precedence of operations in Python defines the order in which different types of operators are evaluated in an expression.
Operators with **higher precedence** are evaluated before those with **lower precedence**.
When operators have the same precedence, **associativity** (usually left to right) decides the order.

## Examples

### Arithmetic Precedence

```python
result = 5 + 3 * 2
# Multiplication has higher precedence, so result is 11, not 16
```

Examples
### Arithmetic Precedence

```python
result = 5 + 3 * 2
print(result)  # Output: 11 (Multiplication happens before addition)
```

### Using Parentheses to Change Precedence

```python
result = (5 + 3) * 2
print(result)  # Output: 16 (Parentheses evaluated first)
```

### Exponentiation vs Multiplication

```python
result = 2 ** 3 * 2
print(result)  # Output: 16 (Exponentiation has higher precedence than multiplication)
```

### Mixed Example
```python
result = 10 - 3 + 2
print(result)  # Output: 9 (Operators with same precedence are evaluated left to right)
```

---

## Summary

   - Operators with higher precedence are evaluated first.
   - Exponentiation (`**`) has higher precedence than multiplication, division, addition, and subtraction.
   - Multiplication (`*`), Division (`/`), Floor Division (`//`), Modulus (`%`) come before addition and subtraction.
   - Parentheses (`()`) can be used to override default precedence.
   - When operators have the same precedence, evaluation happens **from left to right**, except for exponentiation (**) which is right to left.