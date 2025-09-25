# Dictionaries

## Overview
A **dictionary** in Python is a data structure that stores **key-value pairs**.  
- Keys are unique and are used to retrieve corresponding values.  
- Similar to a **hashmap** or **associative array** in other languages.  
- Provides **fast access** to values based on their keys.

---

## Creating a Dictionary
```python
# Creating a dictionary with keys and values
my_dict = {
    'name': 'John',   # Key 'name' with value 'John'
    'age': 25,        # Key 'age' with value 25
    'city': 'New York' # Key 'city' with value 'New York'

print(my_dict)
# Output: {'name': 'John', 'age': 25, 'city': 'New York'}
}
```

## Accessing Values:
```python
# Access a value using its key
print(my_dict['name'])  # Output: John

# Trying to access a key that doesn't exist will raise a KeyError
# print(my_dict['country'])  # X KeyError
```

## Modifying and Adding Elements:
```python
# Modify an existing key's value
my_dict['age'] = 26
print(my_dict)  
# Output: {'name': 'John', 'age': 26, 'city': 'New York'}

# Add a new key-value pair
my_dict['occupation'] = 'Engineer'
print(my_dict)
# Output: {'name': 'John', 'age': 26, 'city': 'New York', 'occupation': 'Engineer'}
```

## Removing Elements:
```python
# Remove a key-value pair using `del`
del my_dict['city']
print(my_dict)
# Output: {'name': 'John', 'age': 26, 'occupation': 'Engineer'}

# Remove using `pop` and get the removed value
# removed_value = my_dict.pop('age')
# print(removed_value)  # Output: 26
# print(my_dict)        # Output: {'name': 'John', 'occupation': 'Engineer'}
```

## Checking Key Existence:
```python
# Check if a key exists in the dictionary
if 'age' in my_dict:
    print('Age is present')
else:
    print('Age is not present')
```

## Iterating Through Keys and Values:
```python
# Iterate through all key-value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# for key, value in my_dict.items():
#     print(key, value)

# Output:
# Key: name, Value: John
# Key: occupation, Value: Engineer
```