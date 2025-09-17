# List vs Tuple in Python

| Feature        | List                  | Tuple                 |
| -------------- | --------------------- | --------------------- |
| Mutability     | Mutable (can change)  | Immutable (cannot change) |
| Syntax         | `[]` square brackets  | `()` parentheses      |
| Performance    | Slower                | Faster (due to immutability) |
| Use Cases      | Dynamic data storage  | Fixed data collections |
| Methods        | Many (append, pop, etc.) | Few (count, index) |

## Example

```python
# List example
numbers = [1, 2, 3]
numbers.append(4)   # Adding element to the end of the list is allowed
print(numbers)      # Output: [1, 2, 3, 4]

# Tuple example
coords = (10, 20)
# coords.append(30) ❌ Error: 'tuple' object has no attribute 'append'
print(coords)       # Output: (10, 20)
```

# Differences Between Tuples and Lists

Tuples and lists are both common data structures in Python, but they differ in mutability, performance, and use cases.

## 1. Mutability

**List:** Lists are **mutable**, meaning their elements can be added, removed, or modified after creation.

```python
my_list = [1, 2, 3]
my_list[0] = 10       # Modify first element
my_list.append(4)     # Add element
my_list.remove(2)     # Remove element
print(my_list)        # Output: [10, 3, 4]
```

**Tuple:** Tuples are **immutable**, meaning once created, you cannot modify their elements.

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  ❌ Error: 'tuple' object does not support item assignment
print(my_tuple)      # Output: (1, 2, 3)
```

## 2. Syntax

**List:** Created using square brackets `[ ]`.

```python
my_list = [1, 2, 3, 'apple', 'banana']
```

**Tuple:** Created using parentheses `( )`. For single-element tuples, include a comma `(5,)`.

```python
my_tuple = (1, 2, 'apple', 'banana')
single_element = (5,)
```

## 3. Performance

- **List:** Slightly slower because lists are mutable; memory may be reallocated when modified.
- **Tuple:** Faster for read-only operations due to immutability; memory usage is optimized.

## 4. Use Cases

- **List:** Use when elements may change dynamically, e.g., storing user input or temporary data.
- **Tuple:** Use when the data should remain constant, e.g., coordinates `(x, y)` or dictionary keys.

## 5. Iteration

Both lists and tuples can be iterated using a `for` loop.

```python
# List iteration
for item in my_list:
    print(item)

# Tuple iteration
for item in my_tuple:
    print(item)
```

## 6. Memory Usage

- **List:** Slightly higher memory usage due to dynamic resizing and mutability support.
- **Tuple:** Lower memory usage because the structure is immutable and optimized internally.