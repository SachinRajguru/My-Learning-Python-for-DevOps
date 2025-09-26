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
                # Replace the entire line with key=new_value
                file.write(key + "=" + value + "\n")
            else:
                # Otherwise, keep the existing line unchanged
                file.write(line)

# -------------------------------
# Example usage of the function
# -------------------------------

# Path to the server configuration file
server_config_file = 'server.conf'

# The configuration key we want to update
key_to_update = 'MAX_CONNECTIONS'

# The new value to set for this key
new_value = '600'  # Update maximum allowed client connections

# Call the function to update the config file
update_server_config(server_config_file, key_to_update, new_value)

print(f"Configuration updated: {key_to_update} set to {new_value}")
