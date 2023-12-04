#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL,display size
curl -s "$1" | wc -c
