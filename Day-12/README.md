# File Operations for DevOps

## Overview

File operations are extremely important for DevOps engineers because you often need to read, write, or update files automatically. For example:

- Updating a server configuration file when a threshold is met.  
- Modifying an application properties file automatically.  
- Managing logs or configuration files across Linux and Windows environments.

Python makes these tasks easier because it works across platforms, unlike shell scripts (Linux) or PowerShell scripts (Windows), which need separate handling.

---

## Why Learn File Operations in Python?

- While shell scripts can handle file manipulations on Linux and PowerShell scripts on Windows, using Python allows you to automate tasks across **both Linux and Windows environments** without maintaining multiple scripts.
- Python provides **inbuilt functions** like `open()` to read, write, and update files efficiently.

---

## Common File Operations

Python provides built-in functions to handle files:

1. **Reading a file**
2. **Writing to a file**

### Syntax to Read a File

1. **Reading a file**

   ```python
   with open('/path/to/file', 'r') as file:
       content = file.readlines()
   ```

2. **Writing to a file**

   ```python
   with open('/path/to/file', 'w') as file:
       file.write("New content")
   ```

## Practical Example: Update Server Configuration Automatically

### Scenario:
Suppose you are managing server configurations (server.conf) like this:
```python
PORT = 8080
MAX_CONNECTIONS = 200
TIMEOUT = 30
SSL_ENABLED = true
LOG_LEVEL = INFO
```
Your task is to update the MAX_CONNECTIONS value automatically when a certain threshold is reached.

### Python Script: update_server.py

```python
# Function to update a specific configuration value in the server.conf file
def update_server_config(file_path, key, value):
    # Step 1: Read the existing content of the configuration file
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

    # Step 2: Open the file in write mode to overwrite with updated content
    with open(file_path, 'w') as file:
        for line in lines:
            # Check if the current line contains the key we want to update
            if key in line: # → updates if the key appears anywhere in the line.
                # if line.strip().startswith(key): → safer (only updates if the line begins with the key).
                # Update (Replace) the entire line with key=new_value
                file.write(key + "=" + value + "\n")
            else:
                # Otherwise, keep the existing line unchanged
                file.write(line)

# -------------------------------
# Example usage of the function
# -------------------------------

server_config_file = 'server.conf'  # Path to the server configuration file
key_to_update = 'MAX_CONNECTIONS'   # Configuration key to update
new_value = '500'                   # New value for MAX_CONNECTIONS

# Call the function to update the config file
update_server_config(server_config_file, key_to_update, new_value)

print(f"Configuration updated: {key_to_update} set to {new_value}")
```

---

## How the Script Works

- Opens the file in **read mode** and stores all lines in a list.
- Opens the file again in **write mode**.
- Iterates through each line:
    - If the line contains the key `(MAX_CONNECTIONS)`, it updates the value.
    - Otherwise, it writes the line unchanged.
- Saves the updated configuration automatically.

This approach ensures only the intended line is modified, keeping the rest of the file intact.

---

## Key Takeaways

- File operations (read and write) are core to automating DevOps tasks.
- Python's `open()` function simplifies file manipulations without needing additional packages.
- Writing a generic update function allows you to update any property in configuration files automatically.
- Automating file updates ensures cross-platform compatibility (Linux + Windows) without maintaining separate shell or PowerShell scripts.

---

## Summary

- File operations are critical for automating DevOps tasks.
- Python allows reading, writing, and updating files across Linux and Windows.
- With this approach, you can automatically update configuration files, logs, or other important files without manual intervention.

## Next Steps

- Practice updating different keys like `PORT` or `TIMEOUT` using the same function.
- Integrate this function into monitoring scripts to automate configuration updates when thresholds are met.