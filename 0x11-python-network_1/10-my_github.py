#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token)
and uses
the GitHub API to display your user ID. It uses Basic Authentication with the
personal access token.
"""
import requests
import sys

def get_github_user_id(username, token):
    """
    Uses the GitHub API to display the user ID of the given credentials.
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    
    if response.status_code == 200:
        user_info = response.json()
        print(user_info.get('id'))
    else:
        print(f"Error code: {response.status_code}")


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_user_id(username, token)
