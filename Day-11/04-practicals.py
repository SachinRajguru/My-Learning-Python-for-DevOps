# Server configurations dictionary
# Each server has its IP, port, and status
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Function to retrieve server status
# If server_name is not found, returns 'Server not found'
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

# Example usage
server_name = 'server2'  # Server to check
status = get_server_status(server_name)  # Retrieve status
print(f"{server_name} status: {status}")  # Output: server2 status: inactive