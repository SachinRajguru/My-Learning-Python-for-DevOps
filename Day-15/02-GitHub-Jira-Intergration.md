# GitHub-Jira Integration - Using Python and Flask (Automating Jira Ticket Creation from GitHub Issues - Part 2)

The project automates DevOps workflows: When a developer comments `/CreateJira` (a trigger keyword) on a GitHub issue, it auto-creates a matching ticket in Jira. No more manual copying—GitHub "talks" to your Python app, which "talks" to Jira.

**Why This Matters**: In real jobs, teams handle 100s of issues daily. This saves hours and shows automation skills (great for interviews). By the end, you'll have a working API on your laptop or EC2.

**Notes Structure**:
1. Project Overview
2. Key Concepts
3. Prerequisites and Setup
4. Folder Structure and Code Files (With Inline Comments)
5. How to Run and Test
6. Troubleshooting
7. Assignment and Extensions
8. Next Steps

---

## 1. Project Overview
### The Story Behind It
Imagine you're a developer: A user reports a bug on GitHub (an "issue"). You check it—if it's real, you want to track fixes in Jira (a project tool for tasks/bugs). But creating Jira tickets manually? Tedious! Solution: Automation.

- **Trigger**: Developer comments `/CreateJira` (slash + "slj" for "start linking Jira") on the GitHub issue.
- **Flow**:
  1. GitHub detects the comment and sends details (title, description, who commented) as JSON data via a "webhook" (auto-alert).
  2. Your Python Flask API receives this data (like a mailbox).
  3. API checks: Is the comment exactly `/CreateJira`? If yes, create a Jira ticket with the GitHub info. If no (e.g., "/abc" or "Need more info"), ignore it.
  4. Jira ticket appears in the backlog—done!
- **Day 14 Recap**: You set up Jira and wrote a basic script to create tickets. Today: Turn it into a web API for GitHub integration.
- **End Goal**: Refresh Jira after commenting `/CreateJira`—see the ticket with GitHub link for easy tracking.
- **Simple Diagram**:
  ```
  GitHub Issue + Comment (/CreateJira)
      ↓ (Webhook: Sends JSON data via POST)
  Your Python API (Flask on Port 5000)
      ↓ (If /CreateJira? → POST to Jira API)
  Jira Ticket Created (Auto-filled Details)
  ```

This uses **APIs** (app-to-app communication) instead of clicking buttons—core DevOps skill.

---

## 2. Key Concepts
Don't worry if terms are new—I'll use everyday examples.

### A. What is an API?
- **Definition**: API = "Application Programming Interface." It's a "bridge" for apps to share data without humans. Like ordering food via an app (API) instead of calling the restaurant (manual).
- **UI vs. API**:
  - **UI (User  Interface)**: Browser/mouse (e.g., GitHub's web page for reading issues). Human-friendly.
  - **API**: Code-only (e.g., `api.github.com/issues`). Fast for automation—GitHub sends data directly to your Python app.
- **HTTP Methods** (API "Actions"—Like Commands):
  - **GET**: Read/fetch (e.g., "Get issue details"). Like asking "What's on the menu?"
  - **POST**: Create/send (e.g., "Create a ticket"). Like submitting an order. *We use POST: GitHub POSTs to your API; your API POSTs to Jira.*
  - **PUT**: Update (e.g., edit ticket).
  - **DELETE**: Remove (e.g., close ticket).
- **JSON**: API's "language" (simple text format). Example: `{"name": "Bug", "details": "Login fails"}`. Like a structured note—easy for code to read/write.
- **Why APIs Here?** GitHub can't "log in" to your laptop and run a script. An API gives it a URL to "call" (e.g., `http://your-ip:5000/createJira`).

### B. Flask: Building Your API
- **What?** A Python "web toolkit" (lightweight framework). Install: `pip install flask`. Turns scripts into web services.
- **Core Ideas**:
  - **App Instance**: `app = Flask(__name__)`—Your API's "control center."
  - **Route/Decorator** (`@app.route`): `@` symbol + instructions. Example: `@app.route('/path', methods=['POST'])` means "If POST to /path, run this function."
    - Decorator = "Wrapper" that adds behavior (e.g., "Check URL before running code").
  - **Server**: `app.run()`—Starts a local web server (port 5000 = "door number"). For remote (EC2): `host='0.0.0.0'`.
- **Example**: In `hello-world.py`, a route returns "Hello!" on GET. In the project, a POST route processes GitHub data.

### C. GitHub Webhooks
- **What?** "Event listeners." GitHub says: "On comment, send JSON to this URL."
- **JSON Payload**: Data sent (e.g., comment body, issue title). View in GitHub: Repo > Settings > Webhooks > Recent Deliveries.
- **Setup**: Add webhook with your API URL. Select events (e.g., "Issue comments").
- **Security**: Add a "secret" (password) for verification (advanced—skip for beginners).

### D. Jira API
- **What?** Jira's automation backdoor. Use `requests` library to POST JSON and create tickets.
- **Auth**: Email + API Token (like a code password). Generate: Atlassian account > Security.
- **Endpoint**: `/rest/api/3/issue` (POST = create ticket).
- **Payload**: JSON with `project`, `summary`, `description`, `issuetype`.
- **Library**: `requests` (simple HTTP). Alternative: `jira` lib (easier, but `requests` teaches basics).

### E. The Assignment: Conditional Logic
- **What?** Add an `if` check: Only create ticket if comment body == `/CreateJira`.
- **Why?** Avoids fake tickets (e.g., casual comments). In code: Parse JSON, check `comment['body']`, skip if no match.
- **Pro Tip**: Use `.strip()` (remove spaces) and `.lower()` (case-insensitive) for robustness.

---

## 3. Prerequisites and Setup
- **Hardware/Software**:
  - Laptop with Python 3 (download from python.org).
  - GitHub account + repo (enable Issues).
  - Jira: Free account (atlassian.com). Create project (e.g., key "DP").
  - Optional: AWS EC2 (free tier) for remote testing.
- **Get Jira Credentials** (5 mins):
  1. Log in to id.atlassian.com.
  2. Security > Create API token (label: "GitHub Integration").
  3. Note: Site URL (e.g., `https://your-site.atlassian.atlassian.net`), email, token, project key, issue type ID (e.g., 10006=Task).
- **Install Tools** (Terminal/Command Prompt):
  ```bash
  pip install flask requests  # Flask=web API, requests=Jira calls
  ```
  - Linux/Mac: `pip3`. Virtual env? `python -m venv env; source env/bin/activate`.
- **Editor**: VS Code (free). It highlights errors and formats code.

---

## 4. Folder Structure and Code Files
Create `Day-15/examples/`. Each file builds on the last.

### Folder Creation
```bash
mkdir -p python-for-devops/Day-15/examples
cd python-for-devops/Day-15/examples
```
Files:
- `01-hello-world.py`: Basic Flask test.
- `02-github-jira.py`: Full API (includes assignment).
- `03-github-jira-assignment.py`: Standalone script to practice the `/CreateJira` check (no Flask/Jira).

### Code File 1: `01-hello-world.py` (Flask Basics)
Copy this into `examples/01-hello-world.py`. Comments explain every line.

```python
# 01-hello-world.py - Basic Flask API Example (Day 15: Step 1)
# Purpose: Learn Flask by creating a simple "Hello World" web endpoint.
# Beginner Explanation: This is your first API! It starts a server and responds to browser visits.
# No GitHub/Jira yet—just proves Flask works. Like saying "My phone is on" before calls.
# Run: python3 01-hello-world.py. Visit: http://localhost:5000/

from flask import Flask  # Import: Get Flask tool (like borrowing a hammer)

app = Flask(__name__)  # Create app: Your API's main object. __name__ = "this file"

@app.route('/', methods=['GET'])  # Route: If GET to '/', run hello_world(). @ = decorator (adds rules)
def hello_world():  # Function: What to do on visit
    return 'Hello, World! This is your first Flask API.'  # Response: Text sent back

if __name__ == '__main__':  # If run directly (not imported)
    app.run(host='0.0.0.0', port=5000, debug=True)  # Start server: All IPs, port 5000, debug=show errors
```

### Code File 2: `02-github-jira.py` (Full Integration)
Copy into `examples/02-github-jira.py`. This is the project core—handles webhook, check, Jira create.

```python
# 02-github-jira.py - GitHub-Jira Automation API (Day 15: Full Project)
# Purpose: Receive GitHub comment, check for '/CreateJira', create Jira ticket if match.
# Beginner Explanation: Builds on hello-world.py. Adds POST for data, JSON parsing, API call to Jira.
# Assignment Included: The if-check for '/CreateJira' (ignores other comments).
# Run: python3 02-github-jira.py. Webhook URL: http://localhost:5000/createJira
# Replace: EMAIL, API_TOKEN, etc., with your Jira details.

import json  # For JSON (data format)
import requests  # For calling Jira
from requests.auth import HTTPBasicAuth  # For Jira login
from flask import Flask, request, jsonify  # Flask tools

app = Flask(__name__)  # App instance

# Config: Your Jira settings (replace!)
JIRA_URL = "https://your-site.atlassian.net/rest/api/3/issue"
EMAIL = "your-email@example.com"
API_TOKEN = "your_token_here"
PROJECT_KEY = "DP"
ISSUE_TYPE_ID = "10006"

auth = HTTPBasicAuth(EMAIL, API_TOKEN)  # Login prep
headers = {"Accept": "application/json", "Content-Type": "application/json"}  # JSON instructions

@app.route('/createJira', methods=['POST'])  # POST route for GitHub
def create_jira():
    try:
        github_data = request.get_json()  # Get incoming JSON
        if not github_data:
            return jsonify({'error': 'No data'}), 400

        print("Payload:", json.dumps(github_data, indent=2))  # Debug print

        # Extract data safely
        comment_body = github_data.get('comment', {}).get('body', '').strip()
        issue_title = github_data.get('issue', {}).get('title', 'No Title')
        # ... (other extractions like commenter, repo)

        # Assignment: Conditional check
        if comment_body != '/CreateJira':
            return jsonify({'message': 'Ignored—not /CreateJira'}), 200

        # Build payload
        payload = {
            "fields": {
                "project": {"key": PROJECT_KEY},
                "summary": f"From GitHub: {issue_title}",
                "description": f"Issue: {issue_title}\nTriggered by /CreateJira",  # Add more details
                "issuetype": {"id": ISSUE_TYPE_ID}
            }
        }
        payload_json = json.dumps(payload)

        # Call Jira
        response = requests.post(JIRA_URL, data=payload_json, headers=headers, auth=auth)
        if response.status_code == 201:
            return jsonify({'success': 'Ticket created!'}), 201
        else:
            return jsonify({'error': response.text}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])  # Health check
def health():
    return jsonify({'status': 'Ready!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Code File 3: `03-github-jira-assignment.py` (Standalone Conditional Logic Practice)
Copy into `examples/03-github-jira-assignment.py`. This is a non-web script to practice the `/CreateJira` check. Run it to test JSON parsing without Flask/Jira.

```python
# 03-github-jira-assignment.py - Practice '/CreateJira' Conditional Logic (Day 15 Assignment)
# Purpose: Standalone script to parse GitHub-like JSON and check for '/CreateJira'.
# Beginner Explanation: No server/API—just Python basics (dicts, if-statements).
# This teaches the "brain" of the project: Extract comment, decide to "create ticket" or ignore.
# Run: python3 03-github-jira-assignment.py. It simulates GitHub data and prints results.
# Use: To understand JSON traversal before full API.

import json  # For handling JSON (like dicts)

# Simulate GitHub payload (what webhook sends)
sample_payload = {
    "comment": {
        "body": "/CreateJira",  # Change to "/abc" to test ignore
        "user": {"login": "dev-user"}
    },
    "issue": {
        "title": "Login Bug",
        "body": "Can't log in",
        "number": 42
    },
    "repository": {"name": "my-repo"}
}

# Function: Check comment and "simulate" ticket creation
def check_and_create(payload):
    # Extract comment body safely (no crash if missing)
    comment_body = payload.get('comment', {}).get('body', '').strip()
    issue_title = payload.get('issue', {}).get('title', 'No Title')

    print(f"Comment received: '{comment_body}'")
    print(f"Issue: {issue_title}")

    # Assignment Logic: If-Else for Conditional Handling
    if comment_body == '/CreateJira':  # Exact match (add .lower() for case-insensitivity)
        print("✓ Match! Would create Jira ticket here.")
        print(f"Ticket Summary: GitHub Issue - {issue_title}")
        # In full project: Call Jira API here
        return "Ticket Created"
    else:
        print("✗ Ignored: Not '/CreateJira'. No ticket.")
        return "Ignored"

# Run the check
result = check_and_create(sample_payload)
print(f"Result: {result}")

# Test Variations: Change sample_payload['comment']['body'] to "/abc" and run again.
# Output: Shows ignore. This is the core if-condition from the tutorial.
```

---

## 5. How to Run and Test
1. **01-hello-world.py** (Basics):
   - Run: `cd examples; python 01-hello-world.py`
   - Test: Browser `http://localhost:5000/` → "Hello, World!"
   - Curl: `curl http://localhost:5000/`

2. **03-github-jira-assignment.py** (Logic Practice):
   - Run: `python 03-github-jira-assignment.py`
   - Output: "Match! Would create..." (change body to "/abc" → "Ignored").
   - Why? Builds confidence in JSON/if before API.

3. **02-github-jira.py** (Full Project):
   - Update placeholders (email/token).
   - Run: `python 02-github-jira.py`
   - Health Test: `curl http://localhost:5000/` → {"status": "Ready!"}
   - Simulate Webhook:
     ```bash
     curl -X POST http://localhost:5000/createJira \
       -H "Content-Type: application/json" \
       -d '{"comment":{"body":"/CreateJira"},"issue":{"title":"Test Bug"}}'
     ```
     - Success: {"success": "Ticket created!"} + Jira ticket.
     - Ignore: Change "body" to "/abc" → {"message": "Ignored..."}
   - Full Test:
     - GitHub: Repo > Settings > Webhooks > Add (URL: `http://your-ip:5000/createJira`, Events: Issue comments).
     - Comment `/CreateJira` on issue → Terminal shows payload, Jira gets ticket.

For EC2: Replace `localhost` with public IP. Open port 5000.

---

## 6. Troubleshooting (Common Beginner Errors)
- **"No module named 'flask'"**: Run `pip install flask requests`.
- **IndentationError**: Python needs perfect spaces (4 per level). Use VS Code's auto-format.
- **Jira 401/403**: Wrong email/token. Regenerate token; test with Postman.
- **No Ticket (200 but ignored)**: Check comment body in terminal print. Ensure exact `/CreateJira`.
- **Webhook 404**: Wrong URL/port. Check GitHub deliveries tab.
- **Port Busy**: Change to 5001 in `app.run(port=5001)`.
- **JSON KeyError**: Use `.get()` (safe). Print payload to debug structure.
- **EC2 Access**: Security group: Allow inbound TCP 5000. Use public IP/DNS.

Debug Tip: Add `print("Step X")` everywhere—trace where it fails.

---

## 7. Assignment and Extensions
- **Core Assignment**: The `if comment_body != '/CreateJira'` in `github-jira.py` and `github-jira-assignment.py`. Test: 5 comments (3 ignore, 2 create).
- **Extensions** (Try After Basics):
  - Case-insensitive: `if comment_body.lower() != '/CreateJira'`.
  - Add webhook secret: Verify with `request.headers.get('X-Hub-Signature-256')`.
  - Link back: Update GitHub issue with Jira URL (use GitHub API).
  - Error Logging: Use `logging` module instead of `print`.
  - Deploy: `pip install gunicorn; gunicorn github_jira:app` + NGINX.

---

## Resources:
  - Flask Docs: flask.palletsprojects.com (tutorials).
  - GitHub Webhooks: docs.github.com/en/webhooks.
  - Jira API: developer.atlassian.com/cloud/jira/platform/rest/v3.