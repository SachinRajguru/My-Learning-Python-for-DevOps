# example_requests.py

# Import requests library to make HTTP requests
import requests

# Send a GET request to GitHub API
response = requests.get("https://api.github.com")

# Print the status code of the response
print("Status Code:", response.status_code)

# Print the response headers
print("Response Headers:", response.headers)