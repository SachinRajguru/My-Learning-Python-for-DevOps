# GitHub–Jira Integration (Part 2)

This project automates Jira ticket creation directly from GitHub issue comments. When a developer comments `/CreateJira` on a GitHub issue, a Flask-based Python API automatically triggers and creates a corresponding Jira ticket.

---

## Project Overview

**Goal:** Automate communication between GitHub and Jira.  
**Flow:**  
1. GitHub sends an event (via Webhook) when someone comments on an issue.  
2. Flask API receives this JSON payload.  
3. If the comment is `/CreateJira`, the app makes a POST request to Jira's REST API to create a new ticket.  

---

## Requirements

- Python 3.x  
- Flask  
- Requests library  
- Jira Cloud account with API Token  
- GitHub repository (to configure webhook)

---

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install flask requests
   ```

2. **Set up Jira API credentials:**
   - Log in to your Atlassian account.
   - Go to **Account Settings → Security → API Tokens → Create Token.**
   - Save your **Email** and **Token** for authentication.

3. **Configure the Webhook in GitHub:**
   - Go to your repository → **Settings → Webhooks → Add webhook.**
   - Set **Payload URL** as `http://<your_ip>:5000/createJira`
   - Choose **Content type** → `application/json`
   - Select **Just the push event** (or issues/comments event).

---

## Folder Structure

```
python-for-devops/
└── Day-15/
    ├── examples/
    │   ├── 01-hello-world.py
    │   ├── 02-github-jira.py
    │   └── 03-github-jira-assignment.py
    └── README.md
```

---

## Example Code - Flask API (02-github-jira.py)

```python
from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    url = "https://<your-domain>.atlassian.net/rest/api/3/issue"
    API_TOKEN = "<your-api-token>"
    auth = HTTPBasicAuth("<your-email>", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "project": {"key": "DP"},
            "summary": "Example Jira Ticket",
            "description": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{
                        "text": "Automated Jira creation from GitHub comment.",
                        "type": "text"
                    }]
                }]
            },
            "issuetype": {"id": "10006"}
        }
    })

    response = requests.post(url, data=payload, headers=headers, auth=auth)
    return json.dumps(json.loads(response.text), indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

## Testing the API

1. Run the Flask app:
   ```bash
   python github-jira.py
   ```

2. Send a POST request to test manually:
   ```bash
   curl -X POST http://localhost:5000/createJira
   ```

3. Check your Jira board — a new ticket should appear.

---

## Assignment Ideas

- Trigger Jira creation only when comment == `/CreateJira`
- Add GitHub issue URL inside Jira ticket description
- Deploy Flask app on AWS EC2
- Add logging and error-handling

---

## References

- [Flask Official Docs](https://flask.palletsprojects.com/)
- [Jira Cloud REST API Docs](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [GitHub Webhooks Guide](https://docs.github.com/en/webhooks)

---