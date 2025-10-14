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