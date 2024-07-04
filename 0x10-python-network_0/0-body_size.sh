#!/bin/bash
# Use curl to get the size of the response body
echo $(curl -s -o /dev/null -w "%{size_download}" "$URL")
