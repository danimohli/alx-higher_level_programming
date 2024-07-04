#!/bin/bash
# Script to get the body size of a request
curl -Is "$1" | grep -i 'Content-Length' | awk '{print $2}'
