#!/bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
reset=`tput sgr0`

# Add environment variables
source my.env

echo "${yellow}Starting practice_api_python_pyramid${reset}"
echo "${yellow}Go to http://localhost:6543/responsive or http://localhost:6543/basic${reset}"
venv/bin/python practice_example.py