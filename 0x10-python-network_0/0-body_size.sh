#!/bin/bash
# Use curl to get the size of the response body

SIZE=$(curl -s -o /dev/null -w "%{size_download}" "$URL")

echo "$SIZE"
