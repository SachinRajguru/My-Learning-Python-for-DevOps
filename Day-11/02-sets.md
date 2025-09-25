# Sets and Set Operations

## Overview
A **set** in Python is an **unordered collection of unique elements**.  
- Useful for **mathematical operations** like union, intersection, and difference.  
- Duplicate elements are automatically removed.  

---

## Creating a Set
```python
# Creating a set with numbers
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5} (order may vary)
```

## Adding and Removing Elements:
```python
# Adding an element to the set
my_set.add(6)
print(my_set)  # 6 is added

# Removing an element from the set
my_set.remove(3)
print(my_set)  # 3 is removed

# Note: using remove() on a non-existing element raises KeyError
# my_set.remove(10)  # X KeyError
```

## Set Operations:
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union: combine all elements without duplicates
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: elements common to both sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3, 4}

# Difference: elements in set1 but not in set2
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
```

## Subset and Superset:
```python
# Check if set1 is a subset of set2
is_subset = set1.issubset(set2)
print(is_subset)  # Output: False

# Check if set1 is a superset of set2
is_superset = set1.issuperset(set2)
print(is_superset)  # Output: False
```

## Practice Example: Managing Server Configurations

### Scenario:
You have a dictionary of server configurations and want to efficiently retrieve server statuses.

```python
# Dictionary storing server configurations
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
```

### Function for Retrieval:
```python
# Function to get status of a server
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')
```

### Example Usage:
```python
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")  # Output: server2 status: inactive
```