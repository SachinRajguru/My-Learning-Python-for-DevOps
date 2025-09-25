# Program to demonstrate integration with GitHub API
# Fetch details of users who created pull requests (active) 
# on the Kubernetes GitHub repository.

import requests

# URL to fetch pull requests from the GitHub API
url = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Make a GET request to fetch pull request data from GitHub
# For private repos or higher rate limits, add headers={'Authorization': 'token YOUR_TOKEN'}
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the JSON response into a Python dictionary (list of PRs)
    pull_requests = response.json()

    # Dictionary to store PR creators and their counts
    pr_creators = {}

    # Loop through each pull request
    for pull in pull_requests:
        creator = pull['user']['login']  # Get username of PR creator
        if creator in pr_creators:
            pr_creators[creator] += 1  # Increment count if already present
        else:
            pr_creators[creator] = 1   # Add new creator with count 1

    # Display PR creators and number of PRs they created
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")