# Practice Exercises and Examples

## Example: Managing a Dictionary of Server Configurations and Optimizing Retrieval

### Scenario:
Suppose you are managing server configurations using a dictionary.

```python
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
```

### Function for Retrieval:
```python
def get_server_status(server_name):
    """
    Returns the status of the given server.
    If server_name is not found, returns 'Server not found'.
    """
    return server_config.get(server_name, {}).get('status', 'Server not found')
```

### Example Usage:
```python
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")  # Output: server2 status: inactive
```

### Explanation:
- The `get_server_status` function uses the `get` method to safely access the server dictionary.
- If the `server_name` does not exist in the dictionary, it returns a default value `'Server not found'`.
- This approach avoids `KeyError` and provides an optimized and safe retrieval method.