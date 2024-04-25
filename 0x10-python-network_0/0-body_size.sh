#!/bin/bash
# It sends a request to a URL and displays size of the response body
curl -s "$1" | wc -c
