#!/bin/bash
# server say you've got me
curl -s -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "http://0.0.0.0:5000/catch_me"
