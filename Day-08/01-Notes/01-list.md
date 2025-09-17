# Python Lists

A **list** in Python is an ordered, mutable collection that can hold elements of different data types.

## Characteristics of Lists

- Ordered (elements maintain insertion order).
- Mutable (elements can be changed).
- Allow duplicates.
- Elements can be of mixed types.

## Creating Lists

```python
# Creating a list with numbers
numbers = [1, 2, 3, 4, 5]  # List of integers

# Mixed data types
mixed = [10, "hello", 3.14, True]  # Integer, string, float, boolean
```

## Accessing Elements

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # Access first element -> "apple"
print(fruits[1])   # Access second element -> "banana"
print(fruits[-1])  # Access last element -> "cherry"
```

## Modifying Elements

```python
fruits[1] = "blueberry"   # Change "banana" to "blueberry"
print(fruits)             # Output: ['apple', 'blueberry', 'cherry']    
```

## Adding Elements

```python
fruits.append("orange")    # Add "orange" at the end
fruits.insert(1, "grape")  # Insert "grape" at index 1
print(fruits)              # Output: ['apple', 'grape', 'blueberry', 'cherry', 'orange']
```

## Removing Elements

```python
fruits.remove("apple")  # Remove element by value -> "apple"
fruits.pop(0)           # Remove element by index (0th element) -> first element
print(fruits)           # Output after removals
```

## Slicing a List

```python
my_list = [1, 2, 3, 4, 5, 6]

subset = my_list[1:4]  # Extract elements from index 1 to 3 -> [2, 3, 4]
print(subset)

subset2 = my_list[:3]  # First three elements -> [1, 2, 3]
subset3 = my_list[3:]  # Elements from index 3 to end -> [4, 5, 6]
```

## Concatenating Lists

```python
list1 = [1, 2]
list2 = [3, 4]

combined = list1 + list2  # Combine two lists -> [1, 2, 3, 4]
print(combined)
```

## Useful List Methods

```python
numbers = [4, 2, 8, 1]

numbers.sort()     # Sort list in ascending order -> [1, 2, 4, 8]
numbers.reverse()  # Reverse list -> [8, 4, 2, 1]

print(len(numbers))       # Get length of list -> 4
print(2 in numbers)       # Check if 2 is in the list -> True
print(10 in numbers)      # Check if 10 is in the list -> False
```