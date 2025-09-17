# Basic-Level List Answers

**Q1: What is a list in Python, and how is it used in DevOps?**  
**Answer:**  
A list in Python is a collection of **ordered and mutable elements**. In DevOps, lists are often used to manage and manipulate data, such as configurations, server names, and deployment targets. For example, you can use a list to store a collection of servers that need to be provisioned or configured.

**Q2: How do you create a list in Python, and can you provide an example related to DevOps?**  
**Answer:**  
In Python, you create a list using square brackets `[]`.  

```python
# List of servers in a DevOps environment
servers = ['web-server-01', 'db-server-01', 'app-server-01']
```

**Q3: What is the difference between a list and a tuple in Python, and when would you choose one over the other in a DevOps context?**  
**Answer:**  
- **List:** Mutable (elements can be changed). Use when data may change, e.g., list of active servers.  
- **Tuple:** Immutable (elements cannot be changed). Use when data should remain constant, e.g., deployment steps or fixed server configurations.

**Q4: How can you access elements in a list, and provide a DevOps-related example?**  
**Answer:**  
You can access elements by their **index**.  

```python
servers = ['web-server-01', 'db-server-01', 'app-server-01']
first_server = servers[0]  # Access the first server -> 'web-server-01'
```

**Q5: How do you add an element to the end of a list in Python? Provide a DevOps example.**  
**Answer:**  
Use the `append()` method to add elements to the end of a list.  

```python
servers = ['web-server-01', 'db-server-01']
servers.append('app-server-01')  # Adds a new server to the list
```

**Q6: How can you remove an element from a list in Python, and can you provide a DevOps use case?**  
**Answer:**  
Use the `remove()` method to delete a specific element by value.  

```python
servers = ['web-server-01', 'db-server-01', 'app-server-01']
servers.remove('db-server-01')  # Removes 'db-server-01' from the list
```