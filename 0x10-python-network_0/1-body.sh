#!/bin/bash
# script takes URL, sends a GET request, displays the body of a 200 status code
if [ "$(curl -s -o /dev/null -w '%{http_code}' "$1")" -eq 200 ]; then curl -s "$1"; fi
