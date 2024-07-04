#!/bin/bash
# Use curl to get the size of the response body
echo "The size of the response body is $(curl -s -o /dev/null -w '%{size_download}' "$1") bytes."

