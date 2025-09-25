# Lists vs. Sets

## Lists

- **Ordered Collection**
  - Lists preserve the order of elements.
  - Elements can be accessed by their **index**.

  ```python
  my_list = [1, 2, 3, 4, 5]
  print(my_list[0])  # Access first element -> 1
  ```

- **Mutable:**
  - You can **modify elements** after creation.

  ```python
  my_list[1] = 10   # Change 2 to 10
  print(my_list)    # Output: [1, 10, 3, 4, 5]
  ```

- **Allows Duplicate Elements:**
  - Lists can contain duplicate elements.

  ```python
  my_list = [1, 2, 2, 3, 4]
  print(my_list)    # Output: [1, 2, 2, 3, 4]
  ```

- **Use Cases:**
  - Use lists when you need **ordered data** that can be changed or indexed.

---

## Sets

- **Unordered Collection:**
  - Sets do **not preserve order**.
  - Elements cannot be accessed by index.

  ```python
  my_set = {1, 2, 3, 4, 5}
  ```

- **Mutable:**
  - You can **add or remove elements**, but cannot change individual items.

  ```python
  my_set.add(6)
  print(my_set)  # 6 is added
  ```

- **No Duplicate Elements:**
  - Duplicates are automatically removed.

  ```python
  my_set = {1, 2, 2, 3, 4}  # Results in {1, 2, 3, 4}
  print(my_set)
  ```

- **Use Cases:**
  - Use sets when you need unique items and want to perform set operations like union, intersection, or difference.

### Common Operations:

- **Adding Elements:**
  - Lists use `append()` or `insert()` methods.
  - Sets use `add()` method.
    ```python
    # Lists
    my_list.append(6)

    # Sets
    my_set.add(6)
    ```

- **Removing Elements:**
  - Lists use `remove()`, `pop()`, or `del` statement.
  - Sets use `remove()` or `discard()` methods.
    ```python
    # Lists
    my_list.remove(3)
    my_list.pop(0)  # Remove first element

    # Sets
    my_set.remove(3)   # Raises error if 3 not present
    my_set.discard(3)  # Safe, does not raise error
    ```

- **Checking Membership:**
  - Lists use the `in` operator.
  - Sets use the `in` operator as well, which is more efficient for sets.

    ```python
    # Lists
    if 3 in my_list:
        print("3 is in the list")

    # Sets (more efficient)
    if 3 in my_set:
        print("3 is in the set")
    ```

### Choosing Between Lists and Sets

- **Use Lists When:**
  - You need to maintain the order of elements.
  - Duplicate elements are allowed.
  - You need to access elements by index (index-based access).

- **Use Sets When:**
  - Order doesn't matter.
  - You want to ensure **unique elements**.
  - You want to perform **set operations** like union, intersection, or difference.