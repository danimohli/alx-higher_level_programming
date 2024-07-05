#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using the requests
package.
"""
import requests


def fetch_status():
    """
    Fetches the status from the given URL and prints the response body.
    """
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")


if __name__ == "__main__":
    fetch_status()
