import os  # Import os module to interact with the operating system

# Read environment variables PASSWORD and API_TOKEN
password = os.getenv("PASSWORD")
api_token = os.getenv("API_TOKEN")

# Print the values (will print None if the environment variable is not set)
print("Password:", password)
print("API Token:", api_token)