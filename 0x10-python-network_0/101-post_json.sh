#!/bin/bash
# Bash script that sends a JSON POST request
curl -s -d "@$2" -H -X POST "$1"
