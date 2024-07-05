#!/usr/bin/python3
"""
This script takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter. It handles the response based on
the requirements.
"""
import requests
import sys


def search_user(letter):
    """
    Sends a POST request with the letter as a parameter and processes
    the response.
    """
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    search_user(letter)
