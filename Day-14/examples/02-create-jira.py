# Create Jira Issue (`02-create-jira.py`)

#- Creates a minimal ticket. Customize payload for more fields.

# This code sample uses the 'requests' library:
# http://docs.python-requests.org
# 
# BEGINNER TIP: Same as above—requests for HTTP, auth for login, json for data.
# This is the POST version: Sends data to "create" a new ticket.

import requests  # Main library for HTTP requests (GET, POST, etc.)
from requests.auth import HTTPBasicAuth  # For "basic" authentication (email + token login)
import json  # Built-in Python module to handle JSON (text data from APIs, like structured dictionaries)

# URL: Endpoint for creating issues (tickets).
# Replace with your own. /rest/api/3/issue is the standard path for POST.
url = "https://your-site.atlassian.net/rest/api/3/issue"

# API_TOKEN: Same as above—your Jira token.
API_TOKEN = ""  # Replace with your token (e.g., "ATATT3xFfGF0...").

# Authentication: Email + token.
# Replace the empty string with your email.
auth = HTTPBasicAuth("your-email@example.com", API_TOKEN)  # Replace email.

# Headers: Both Accept (response) and Content-Type (payload).
# - Content-Type: **MANDATORY**—tells Jira the data is JSON (prevents 400 errors).
# - Accept: Ensures JSON reply.
headers = {
  "Accept": "application/json",          # Request JSON response.
  "Content-Type": "application/json"     # **KEY**: Payload is JSON data.
}

# Payload: The data to create the ticket—converted to JSON string.
# json.dumps() turns the dict into a string (e.g., '{"fields": {...}}').
# Description: Uses ADF (Atlassian format)—simple paragraph here.
# Mandatory Fields: project key, issuetype id, summary.
# Project Key: "DP" (example—yours might be different).
# Issuetype ID: "10006" (example—get from your settings; e.g., 10001=Story, 10002=Bug).
payload = json.dumps({  # Outer dict for the whole request.
  "fields": {  # Jira expects issue details in "fields".
    "description": {  # Optional: Full details (ADF format).
      "content": [  # List of content blocks.
        {
          "content": [  # Nested: Text inside paragraph.
            {
              "text": "My first jira ticket",  # The actual text.
              "type": "text"  # Plain text type.
            }
          ],
          "type": "paragraph"  # Block type: A paragraph.
        }
      ],
      "type": "doc",     # Document type (ADF root).
      "version": 1       # Starts at 1 (for updates).
    },
    "project": {         # Mandatory: Which project?
      "key": "DP"        # Short key (e.g., "DP" from your project UI).
    },
    "issuetype": {       # Mandatory: Ticket type (e.g., Story/Bug).
      "id": "10006"      # Numeric ID (not name)—example value.
    },
    "summary": "First JIRA Ticket",  # Mandatory: Short title (headline).
  },
  "update": {}  # Empty: For future updates (not used here; can remove if simplifying).
})  # End json.dumps—now payload is a JSON string.

# Make the Request: POST to create the issue.
# - "POST": Sends data to create something new.
# - data=payload: The JSON body.
# - headers: Includes Content-Type (critical!).
# - auth: Login.
response = requests.request(
   "POST",      # Method: POST for creating.
   url,         # Endpoint.
   data=payload, # JSON data to send (the ticket details).
   headers=headers,  # Accept/Content-Type.
   auth=auth     # Credentials.
)

# Print Full Response: Parses JSON, then pretty-prints it (sorted, indented).
# json.loads(response.text): String → Python dict/list.
# json.dumps(..., sort_keys=True, indent=4): Pretty format for reading.
# Output: Full details of created issue (key, fields, etc.).
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

# BEGINNER TIP: Add Success Check (not in original):
# Uncomment for better handling.
# if response.status_code == 201:  # 201 = Created (success for POST).
#     print("Ticket Created! Check the JSON above for key (e.g., DP-14).")
#     print(f"View: {url.replace('/issue', f'/issue/{json.loads(response.text)['key']}')}")
# else:
#     print(f"Error {response.status_code}: {response.text}")
# 
# Simplify Payload: Remove "update": {} and extra ADF if not needed.
# Security: Use os.environ.get('JIRA_API_TOKEN', '') for token/email.
# import os
# EMAIL = os.environ.get('JIRA_EMAIL', '')
# API_TOKEN = os.environ.get('JIRA_API_TOKEN', '')
# auth = HTTPBasicAuth(EMAIL, API_TOKEN)
# 
# Shorthand Alternative: requests.post(url, json=dict_payload, ...) — auto-handles dumps/headers.

# Run: python create_jira.py
# Expected: Pretty JSON of new ticket (e.g., {"key": "DP-14", "fields": {...}}). Check Jira board!