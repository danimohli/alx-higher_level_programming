#!/bin/bash
# Bash script that sends a JSON POST request
curl -s -X POST -H "Content-Type: application/json" "$1" -d "@$2"
