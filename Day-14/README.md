# GitHub–Jira Integration (Part 1)

## Overview

We build a **real-world DevOps automation** that connects **GitHub** and **Jira** using Python and REST APIs.  
Whenever a developer comments a trigger phrase (for example, `/CreateJira`) on a GitHub issue, a **webhook** automatically triggers a **Python script** that creates a **Jira ticket**.  

This automation eliminates manual steps, improves traceability, and demonstrates how DevOps engineers integrate multiple tools using APIs.

---

## Learning Objectives

- Understand how **REST APIs** work between GitHub and Jira.  
- Set up a **free Jira Cloud** account and generate an **API token**.  
- Use **Python + requests** to:
  - List Jira projects (`GET /project`)
  - Create Jira issues (`POST /issue`)
- Learn to authenticate with **HTTP Basic Auth** (email + token).  
- Parse and handle **JSON** responses.  
- Prepare for **Part 2** — building a Flask webhook app hosted on AWS EC2.

---

## Folder Contents

| File | Description |
|------|--------------|
| `01-list_projects.py` | Python script to list all Jira projects using the REST API. |
| `02-create_issue.py` | Python script to create a new Jira issue (ticket) with JSON payload. |
| `Day-14-GitHub-Jira-Integration.md` | Complete session notes and step-by-step explanation. |

---

## Architecture Summary

```
┌──────────┐       Webhook Event        ┌──────────────┐       REST API       ┌─────────┐
│ GitHub   │ ─────────────────────────▶ │ Python App   │ ───────────────────▶ │ Jira    │
│ (Issues) │   (trigger: /CreateJira)   │ (on EC2)     │   (create issue)    │ Cloud   │
└──────────┘                            └──────────────┘                     └─────────┘
```

**Flow**
1. Developer adds `/CreateJira` comment on a GitHub issue.  
2. GitHub webhook sends JSON payload to the Python app.  
3. The app extracts issue details and calls the Jira REST API.  
4. A new Jira ticket is created automatically and linked back to the GitHub issue.

---

## Prerequisites

- Python 3.x  
- Installed library:  
  ```bash
  pip install requests
  ```
- Jira Cloud account (<https://www.atlassian.com/software/jira>)  
- Generated API token (from “Manage Account → Security → API Tokens”).  
- GitHub repository for testing.  

---

## Environment Setup

1. Configure environment variables for credentials:
   ```bash
   export JIRA_EMAIL="your-email@example.com"
   export JIRA_API_TOKEN="your-generated-token"
   ```
   *(On Windows, use `set` instead of `export`.)*

2. Replace your Jira site URL in the Python scripts:
   ```python
   url = "https://your-site.atlassian.net/rest/api/3/project"
   ```

3. Run scripts to test connectivity:
   ```bash
   python 01-list_projects.py
   python 02-create_issue.py
   ```

---

## Key Takeaways

- Jira REST APIs use **simple JSON** structures — perfect for automation.  
- **requests** library is all you need for secure API calls.  
- Always check `response.status_code` for success (200/201).  
- Keep secrets in environment variables — **never** commit API tokens.  
- Mastering APIs builds the foundation for DevOps automation and toolchain integration.

---

## Next Steps (Part 2 Preview)

- Build a **Flask webhook app** to receive GitHub events.  
- Deploy it on **AWS EC2** and expose the endpoint publicly.  
- Configure GitHub Webhook → Python App → Jira automation pipeline.  
- Add logging, error handling, and notification enhancements.

---

## References

- Jira REST API Docs: <https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/>  
- GitHub Webhooks: <https://docs.github.com/en/webhooks>  
- requests Library: <https://requests.readthedocs.io/>