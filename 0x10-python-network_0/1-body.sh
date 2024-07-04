#!/bin/bash
# script takes URL, sends a GET request, displays the body of a 200 status code
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
