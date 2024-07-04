#!/bin/bash
# Bash script that sends a JSON POST request
curl -s -X POST "$1" -d "@$2"
