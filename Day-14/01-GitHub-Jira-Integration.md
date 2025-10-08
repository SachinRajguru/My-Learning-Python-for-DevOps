# Github-JIRA intergration (Automating Jira Ticket Creation from GitHub Issues - Part 1)

These notes summarize the key concepts, steps, and code from the session. The project focuses on a real-time DevOps automation: When a developer comments a trigger phrase (e.g., "/CreateJira") on a GitHub issue (after triaging QE-reported bugs), a webhook triggers a Python app to create a Jira ticket automatically. This bridges GitHub and Jira, reducing manual work.

**Learning Objectives**:
- Set up a free Jira instance and generate API tokens.
- Understand REST API basics for Jira (using documentation).
- Write Python scripts to interact with Jira APIs (list projects, create issues) using the `requests` module.
- Handle JSON responses and basic authentication.
- Prepare for Part 2: Flask app for webhooks, EC2 hosting, and GitHub integration.

**Why This Project?**
- DevOps engineers often manage multiple repos and tools (GitHub for issues, Jira for tracking).
- Automates triage: QE creates GitHub issues → Dev reviews → Comment trigger → Auto-create Jira ticket with details (summary, description, assignee).
- Teaches API integration, JSON parsing, and webhooks—core DevOps skills.
- No external libraries beyond `requests` (keeps it simple; no unstable Jira Python modules).

---

## 1. Project High-Level Architecture
- **Parties Involved**:
  - **GitHub**: Source of issues. Configure webhook to send JSON payload (issue details) on comments.
  - **Python App (Bridge)**: Hosted on EC2 (or local). Receives GitHub JSON → Extracts fields (e.g., title, description) → Calls Jira API.
  - **Jira**: Destination for tickets. Use REST API to create issues.
- **Flow**:
  1. Dev comments trigger on GitHub issue.
  2. GitHub webhook → POST JSON to your Python app URL (e.g., `http://ec2-ip:port/webhook`).
  3. App parses JSON → Creates Jira payload → POST to Jira API.
  4. Jira ticket created (e.g., with GitHub issue link for tracking).
- **Tools/Languages**:
  - Python (better than shell for cross-platform, dynamic APIs).
  - `requests` for HTTP calls.
  - JSON for data exchange.
  - Future: Flask for web server; EC2 for hosting.

**Problem Statement**:
- QE/Deps report bugs as GitHub issues (hundreds possible across repos).
- Devs triage: Close invalid; for valid bugs, manually create Jira tickets (login, copy-paste details)—tedious!
- Solution: Automate via webhook + API. Dev just comments trigger → Ticket auto-created.

---

## 2. Prerequisites
- **Environment**: Python 3.x (e.g., VS Code Spaces, local laptop, EC2).
- **Install Dependencies**: 
  ```bash
  pip install requests
  ```
- **Accounts**:
  - GitHub repo (yours or create one for testing).
  - Jira: Free Atlassian account (up to 10 users).
- **Knowledge Assumed**:
  - Python basics (imports, dicts/lists, loops).
  - JSON handling (from prior sessions).
  - Environment variables for secrets (e.g., API tokens).

---

## 3. Jira Setup Steps
1. **Sign Up**:
   - Go to [Atlassian Jira](https://www.atlassian.com/software/jira).
   - Click "Try Jira for free" → Sign in with email → Create account.
   - No credit card needed for <10 users.

2. **Create Project**:
   - Select "Jira Software" → "Get it free".
   - Site name: e.g., `your-jira-site` (URL becomes `https://your-jira-site.atlassian.net`).
   - Choose "Scrum" template (simple for bug tracking).
   - Project name: e.g., "DevOps Project" (key: auto-generated, e.g., `DP`—note this for API).
   - Skip quick start → Go to project board (backlog visible).

3. **Key Concepts**:
   - **Project Key**: Short code (e.g., `DP`) for API references. Visible in UI (e.g., issues like `DP-1`).
   - **Issue Types**: Story (`10001`), Bug (`10002`), etc. Get ID from project settings:
     - Project Settings → Issue Types → Click type (e.g., Story) → URL shows ID (e.g., `/issuetype/10001`).
   - **Fields**: Mandatory for creation: Project key, Issue Type ID, Summary. Optional: Description, Assignee, Labels.

---

## 4. API Token Creation (For Authentication)
- **Why?** APIs use tokens instead of passwords for security (revocable, per-service).
- **Steps**:
  1. In Jira: Profile (top-right) → "Manage account".
  2. Sidebar: "Security" → "Create and manage API tokens".
  3. Click "Create API token" → Label (e.g., "Python DevOps") → Copy token (e.g., `ATATT3xFfGF0...`).
- **Usage**: Pair with email for HTTP Basic Auth (like username:password).
- **Best Practice**: Store as env var (not hardcoded):
  ```python
  import os
  EMAIL = os.environ.get('JIRA_EMAIL')
  API_TOKEN = os.environ.get('JIRA_API_TOKEN')
  # Set in terminal: export JIRA_EMAIL=your@email.com; export JIRA_API_TOKEN=your-token
  ```
- **Security Note**: Tokens can be deleted anytime. Never commit to Git.

---

## 5. Understanding Jira API Documentation
- **Access**: Search "Jira API docs" → Official page: [developer.atlassian.com/cloud/jira/platform/rest/v3](https://developer.atlassian.com/cloud/jira/platform/rest/v3).
- **Why Jira is Beginner-Friendly**:
  - REST API (v3): Simple HTTP methods (GET/POST) with JSON.
  - Docs provide sample code in Python, Shell, Java, etc. (copy-paste ready).
  - Endpoints: `/rest/api/3/project` (list), `/rest/api/3/issue` (create), `/rest/api/3/search` (query issues).
- **Base URL**: `https://your-site.atlassian.net/rest/api/3/`.
- **Auth**: HTTP Basic (email + token).
- **Headers**: `Content-Type: application/json` for POST; `Accept: application/json` for responses.
- **Responses**: JSON (use `json.loads()` to parse into dict/list).
- **Common Errors**:
  - 401: Invalid auth.
  - 400: Missing mandatory fields (e.g., project key).
  - 404: Invalid project/issue type.
- **JSON Handling Tip**: Use online formatters (e.g., jsonlint.com) to debug raw responses.

**Example API Calls (from Docs)**:
- **GET All Projects**: `GET /rest/api/3/project` → Returns list of dicts (e.g., `[{"name": "DevOps Project", "key": "DP"}, ...]`).
- **POST Create Issue**: `POST /rest/api/3/issue` → Payload as JSON dict with `"fields"`.

---

## 6. Python Code Examples
The full scripts are in the `examples/` folder. Use `requests` for API calls. All scripts need: URL, auth, JSON import. The examples below are direct from the API docs, using `requests.request()` for flexibility.

### 6.1 List Projects (`list_projects.py`)
Lists all projects to verify setup and practice JSON parsing.

```python
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
```

- **Run**: `python list_projects.py`.
- **Output Example**:
  ```
  DevOps Project
  ```
- **Key Learning**: `response.json()` or `json.loads(response.text)` → Traverse list with loop (access `name`, `key`). Add error handling: `if response.status_code == 200:`.
- **Extensions**: Loop to print all: `for proj in output: print(f"- {proj['name']} (Key: {proj['key']})")`.

### 6.2 Create Jira Issue (`create_jira.py`)
Creates a minimal ticket. Customize payload for more fields.

```python
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
# 
# BEGINNER TIP: Same as above—requests for HTTP, auth for login, json for data.
# This is the POST version: Sends data to "create" a new ticket.

import requests
from requests.auth import HTTPBasicAuth
import json

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
```

- **Run**: `python create_jira.py` → Check Jira board for new ticket (e.g., `DP-14`).
- **Key Learning**:
  - POST with `json.dumps(payload)` for JSON body.
  - Description: Uses Atlassian Document Format (ADF)—simple text for now.
  - Add Fields: e.g., `"assignee": {"accountId": "your-id"}` (get ID via `/rest/api/3/myself`).
- **Extensions**:
  - List Issues: POST to `/search` with JQL (e.g., `{"jql": "project = DP", "maxResults": 10}`).

---

## 7. Key Python Concepts Reinforced
- **Imports**: `requests` (API calls), `HTTPBasicAuth` (auth), `json` (parse/dump).
- **HTTP Methods**: GET (read), POST (create).
- **JSON**: Strings → Dicts/Lists via `loads()`. Dicts → Strings via `dumps()`.
- **Error Handling**: Check `status_code` (200=OK, 201=Created).
- **Data Types**: API returns lists (projects/issues) → Loop with `for item in list:`.
- **Security**: Env vars > Hardcoding. Remove secrets before Git commit.

**Common Pitfalls**:
- Wrong URL/Key/ID → 400/404 errors.
- No `Content-Type` header → JSON parse fails.
- Rich descriptions: Start simple; advanced ADF for formatting.

---

## 8. Practice Exercises
1. Run both scripts—verify output in Jira UI.
2. Modify `create_jira.py`: Add a label (`"labels": ["bug", "qe"]`) or assignee.
3. List issues in your project: Adapt search

---

## 9. Next Steps (Part 2 Teaser)
- Convert script to Flask app: Handle POST from GitHub webhook (parse JSON for "/CreateJira" comment).
- Host on EC2: Use `gunicorn` or similar; expose port (e.g., 5000).
- GitHub Webhook Config: Repo Settings → Webhooks → Add URL (your EC2 app) → Events: "Issues" (comments).
- Enhancements: Filter for "/CreateJira" comment, link GitHub issue in Jira description, assign to user.
- Watch for: HTTP protocols, webhook JSON structure, error logging.

**Resources**:
- Jira API Docs: [developer.atlassian.com](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/).
- GitHub Webhooks: [docs.github.com/en/webhooks](https://docs.github.com/en/webhooks).
- Repo: Clone the series GitHub repo for full code.