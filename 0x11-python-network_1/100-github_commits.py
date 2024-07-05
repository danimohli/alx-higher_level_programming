#!/usr/bin/python3
"""
This script lists the 10 most recent commits of a specified repository
by a specified owner
using the GitHub API. It prints each commit as: <sha>: <author name>.
"""
import requests
import sys


def list_commits(repo, owner):
    """
    Fetches and prints the 10 most recent commits of a
    specified repository by a specified owner.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'per_page': 10}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    else:
        print(f"Error code: {response.status_code}")


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    list_commits(repo, owner)
