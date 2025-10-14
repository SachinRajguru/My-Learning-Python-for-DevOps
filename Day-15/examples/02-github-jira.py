# This code sample uses the 'requests' library:
# http://docs.python-requests.org
# The 'requests' library is a popular Python tool for making HTTP requests (like sending data to websites or APIs).
# It simplifies interacting with web services, such as posting data to Jira.
import requests
# Import HTTPBasicAuth from requests.auth. This is used for basic authentication (username/password or token-based auth)
# when making HTTP requests. Jira API uses this for secure access.
from requests.auth import HTTPBasicAuth
# Import the 'json' module, which helps work with JSON data (a common format for sending/receiving data over the web).
# JSON looks like a dictionary in Python but is text-based for APIs.
import json
# Import Flask to build a simple web application. Flask handles incoming web requests and sends responses.
from flask import Flask

# Create an instance (object) of the Flask application.
# '__name__' is a special Python variable that tells Flask the name of the current module (file).
# This helps Flask find resources like templates if needed.
app = Flask(__name__)

# Define a route (URL path) that handles incoming requests.
# '/createJira' is the endpoint (like http://yourapp.com/createJira).
# 'methods=['POST']' means this route only responds to POST requests (used for sending data, like creating something new).
# When someone sends a POST to this URL, Flask will call the function below.
@app.route('/createJira', methods=['POST'])
# Define the function that runs when the '/createJira' route is accessed via POST.
# This function will create a new issue (like a ticket or bug report) in Jira using their API.
def createJira():

    # Set the URL for the Jira REST API endpoint to create a new issue.
    # REST API is a way for programs to communicate with Jira over the web.
    # This specific URL is for Atlassian Jira Cloud (note: replace with your own Jira instance if different).
    url = "https://YOUR_JIRA_SITE.atlassian.net/rest/api/3/issue"

    # Define your API token here. This is a secret key from Jira that allows secure access to the API.
    # WARNING: In real code, never hardcode secrets like this—use environment variables or config files.
    # Get your token from Jira settings > Security > API tokens. Leave it empty for now, but fill it in to work.
    API_TOKEN=""

    # Create authentication object for basic auth.
    # Jira uses email as "username" and API token as "password".
    # Here, the email is empty—replace "" with your Jira email (e.g., "your.email@example.com").
    auth = HTTPBasicAuth("", API_TOKEN)

    # Define HTTP headers (extra info sent with the request).
    # "Accept": "application/json" tells the server we want JSON back.
    # "Content-Type": "application/json" tells the server we're sending JSON data.
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Prepare the data (payload) to send to Jira for creating the issue.
    # This is a Python dictionary that describes the new issue: summary, project, issue type, and description.
    # json.dumps() converts the dictionary to a JSON string (text format) that APIs expect.
    # The structure follows Jira's API format:
    # - "fields" contains details like summary, project key ("DP" is your project code), issue type ID (10006 might be "Bug"),
    #   and a rich description (using Atlassian's document format with paragraphs and text).
    # - "update" is empty here, but could be used for additional updates.
    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "DP"
        },
        "issuetype": {
            "id": "10006"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )

    # Make the HTTP POST request to the Jira API using the requests library.
    # - "POST" is the method for creating new resources.
    # - url: where to send it.
    # - data=payload: the JSON data to create the issue.
    # - headers: the metadata for the request.
    # - auth: the authentication credentials.
    # This will send the request and get a response from Jira (e.g., success or error).
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    # Return the response from Jira as a nicely formatted JSON string.
    # json.loads(response.text) parses the raw response text into a Python dictionary.
    # json.dumps() then converts it back to JSON with formatting: sorted keys, indentation for readability,
    # and specific separators for clean output.
    # This is what the web client (e.g., browser or tool sending POST) will see.
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

# This checks if the script is being run directly (not imported elsewhere).
# If you run 'python hello-world.py' in the terminal, '__name__' becomes '__main__', so the server starts.
if __name__ == '__main__':
    # Start the Flask development server.
    # host='0.0.0.0': Listen on all network interfaces (allows access from other devices, not just localhost).
    # port=5000: Run on port 5000 (default for Flask; change if needed).
    # To test: Run the script, then use a tool like curl or Postman to POST to http://localhost:5000/createJira.
    # Note: Fill in API_TOKEN and email first, or it won't work!
    app.run(host='0.0.0.0', port=5000)

# HOW TO RUN THIS CODE (Step-by-Step for Beginners):
# 1. Install required libraries: Open your terminal/command prompt and run:
#    pip install flask requests
#    (This installs Flask for the web app and requests for API calls.)
#
# 2. Set up your Jira credentials:
#    - Go to your Jira account (e.g., atlassian.net) > Account settings > Security > Create and manage API tokens.
#    - Create a new API token and copy it.
#    - In the code, replace the first "" in HTTPBasicAuth with your Jira email (e.g., "user@example.com").
#    - Replace API_TOKEN="" with your actual token (e.g., API_TOKEN="ATATT3xFfGF0...").
#    - Also, update the URL if it's not your Jira instance, and ensure "DP" is your project key and "10006" is a valid issue type ID.
#
# 3. Save the code: Save this as a file, e.g., 'hello-world.py' (or whatever name you prefer).
#
# 4. Run the script: In your terminal, navigate to the folder with the file and type:
#    python hello-world.py
#    (Or 'python3 hello-world.py' on some systems like macOS/Linux.)
#    You should see output like: "Running on all addresses (0.0.0.0)" and "Running on http://127.0.0.1:5000".
#    The server is now live! Press Ctrl+C in the terminal to stop it.
#
# 5. Test the endpoint:
#    - Use a tool like Postman, curl, or even Python's requests library to send a POST request to http://localhost:5000/createJira.
#    - Example with curl (in a new terminal): curl -X POST http://localhost:5000/createJira
#    - No body is needed for this endpoint since the payload is hardcoded inside the function.
#    - If successful, you'll see a JSON response with the new Jira issue details. If not (e.g., auth error), check the terminal for errors.
#
# Troubleshooting:
# - If port 5000 is busy, change 'port=5000' to another number like 5001.
# - Ensure your firewall allows the port.
# - For production, don't use the dev server—use a proper WSGI server like Gunicorn.
# - This is a basic example; in real apps, handle errors (e.g., if response.status_code != 201) and validate inputs.


# How to Run:
# 1. Save as 02-github-jira.py in a folder (e.g., day15-flask).
# 2. Replace placeholders: JIRA_SITE, EMAIL, API_TOKEN, key="DP", id="10006".
# 3. Install deps: pip install flask requests
# 4. Run: python 02-github-jira.py
#    - Output: * Running on all addresses (0.0.0.0):5000
#    - Press Ctrl+C to stop.
# 5. Test Local:
#    - curl -X POST http://localhost:5000/createJira -H "Content-Type: application/json" -d '{}'  # Empty JSON; creates hardcoded ticket.
#    - Expected Response: {"status": "success", "message": "Jira ticket created!", "issue_key": "DP-15"} (JSON).
# 6. Test on EC2:
#    - SSH to EC2, run script.
#    - Webhook URL: http://ec2-public-ip:5000/createJira
#    - Ensure security group allows inbound TCP 5000 from 0.0.0.0/0 (or GitHub IPs).
#    - GitHub Test: Add webhook (Events: Issue comments) → Comment anything → Ticket created (hardcoded).
# 7. Verify: Refresh Jira backlog → New ticket with demo details.
# Troubleshooting:
# - ImportError: pip install flask requests.
# - 405 Method Not Allowed: Use POST (not GET) in curl/webhook.
# - 404 Not Found: Wrong path (must be /createJira).
# - Jira 401 Unauthorized: Invalid EMAIL/API_TOKEN—regenerate token.
# - 400 Bad Request: Invalid project key/ID or JSON—check placeholders.
# - Webhook Ping Fail: Flask not running, port blocked, or use http:// (not https).
# - No Ticket: Print response.text in code for debug; check Jira logs.
# Pro Tip: For production, remove debug=True; use env vars (import os; API_TOKEN = os.getenv('JIRA_TOKEN')).
# Next: Use 03- for "CreateJira" check and dynamic GitHub data.