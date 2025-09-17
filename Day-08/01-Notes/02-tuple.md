# Python Tuples

A **tuple** in Python is an ordered, immutable collection that can hold elements of different data types.

## Characteristics of Tuples

- Ordered (elements maintain insertion order)
- Immutable (cannot change elements once created)
- Allow duplicates
- Elements can be of mixed types

## Creating Tuples

```python
# Creating a tuple with numbers
numbers = (1, 2, 3, 4, 5)  # Tuple of integers

# Mixed data types
mixed = (10, "hello", 3.14, True)  # Integer, string, float, boolean

# Tuple with one element (note the comma)
single = (5,)  # Single-element tuple
```

## Accessing Elements

```python
colors = ("red", "green", "blue")

print(colors[0])   # Access first element -> "red"
print(colors[1])   # Access second element -> "green"
print(colors[-1])  # Access last element -> "blue"
```

## Tuple Packing & Unpacking

```python
# Packing multiple values into a tuple
person = ("Alice", 25, "Engineer")

# Unpacking tuple into separate variables
name, age, profession = person
print(name)       # Output -> Alice
print(age)        # Output -> 25
print(profession) # Output -> Engineer
```

## Tuple Methods

```python
nums = (1, 2, 2, 3, 4, 2)

print(nums.count(2))   # Count occurrences of 2 -> 3
print(nums.index(3))   # Find index of value 3 -> 3
```

## Concatenating Tuples

```python
tuple1 = (1, 2)
tuple2 = (3, 4)

combined = tuple1 + tuple2  # Concatenate two tuples -> (1, 2, 3, 4)
print(combined)
```

## Checking for an Element

```python
fruits = ('apple', 'banana', 'cherry')

print('apple' in fruits)   # Check if 'apple' is in the tuple -> True
print('orange' in fruits)  # Check if 'orange' is in the tuple -> False
```

## Using Tuples for Multiple Return Values

```python
def get_coordinates():
    return (3, 4)  # Return multiple values as a tuple

x, y = get_coordinates()  # Unpack the returned tuple (x=3, y=4)
print(x, y)
```

## Why Use Tuples?

- Tuples are **faster** than lists.
- Tuples can be used as **dictionary keys** (lists cannot).
- Tuples are ideal when data **should not change**.