# List Projects (`01-list-projects.py`)

#- Lists all projects to verify setup and practice JSON parsing.

# This code sample uses the 'requests' library:
# http://docs.python-requests.org
# 
# BEGINNER TIP: 'requests' is a Python library for making HTTP requests (like fetching web data).
# Install it: pip install requests
# This script is a direct copy from Jira's API docs—it's a simple GET request to list projects.

import requests  # Main library for HTTP requests (GET, POST, etc.)
from requests.auth import HTTPBasicAuth  # For "basic" authentication (email + token login)
import json  # Built-in Python module to handle JSON (text data from APIs, like structured dictionaries)

# URL: The full web address for Jira's "list projects" endpoint.
# Replace with your own (e.g., https://your-site.atlassian.net/rest/api/3/project).
# What is an endpoint? It's a specific path in the API (like a menu item) to get projects.
url = "https://your-site.atlassian.net/rest/api/3/project"  # Hardcoded for demo; make it a variable for flexibility.

# API_TOKEN: Your secure token from Jira (not a password—generate in Security settings).
# Replace the empty string. BETTER: Use env var (see tip below).
API_TOKEN = ""  # Replace with your token (e.g., "ATATT3xFfGF0...")

# Authentication: Pairs your email (username) with token (password) for secure access.
# Replace the empty string with your email (e.g., "your-email@example.com").
auth = HTTPBasicAuth("your-email@example.com", API_TOKEN)  # Replace email.

# Headers: Dictionary telling the server what to expect/send.
# - "Accept": Asks for JSON response (ensures clean data, not HTML).
# No "Content-Type" needed here (GET doesn't send data, just reads).
# Beginner Tip: Headers are like "instructions" for the request (e.g., "Give me JSON!").
headers = {
  "Accept": "application/json"  # Requests JSON back from Jira.
}

# Make the Request: Uses requests.request()—a general function for any HTTP method.
# - "GET": Read-only (fetches data, doesn't change anything).
# - headers: Attached to the request.
# - auth: Includes login info (sent securely).
response = requests.request(
   "GET",  # Method: GET for reading data.
   url,    # The endpoint URL.
   headers=headers,  # Our instructions (Accept JSON).
   auth=auth  # Login credentials.
)

# Parse Response: response.text is a JSON string (e.g., '[{"name": "Project1", ...}]').
# json.loads() converts it to a Python list of dictionaries (easy to access).
output = json.loads(response.text)  # Now 'output' is a list, like [project_dict1, project_dict2, ...]

# Access First Project: output[0] gets the first item (index 0) in the list—a dictionary.
# ["name"] gets the value for key "name" (like dict["key"]).
name = output[0]["name"]  # e.g., "Your Project Name" (assumes at least one project exists).

# Print the Result: Simple output.
print(name)  # Output: e.g., Your Project Name

# BEGINNER TIP: Add Error Handling (not in original, but recommended):
# Uncomment below to check if successful (200 = OK).
# if response.status_code == 200:
#     print("Success! First project:", name)
# else:
#     print(f"Error {response.status_code}: {response.text}")
# 
# Full Loop: Print all names.
# for proj in output:
#     print(f"- {proj['name']} (Key: {proj['key']})")
# 
# Security Upgrade: Use env vars instead of hardcoding.
# import os
# EMAIL = os.environ.get('JIRA_EMAIL', 'your-email')
# API_TOKEN = os.environ.get('JIRA_API_TOKEN', '')
# auth = HTTPBasicAuth(EMAIL, API_TOKEN)
# Set in terminal: export JIRA_EMAIL="your-email" && export JIRA_API_TOKEN="your-token"

# Run: python list_projects.py
# Expected: Prints your first project's name. If empty list or error, check auth/URL.