#!/bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
reset=`tput sgr0`

# Add environment variables
source my.env

echo "${yellow}Running question_example.py${reset}"
venv/bin/python question_example.py
echo "${green}Execution completed.${reset}"
echo "${yellow}Open the newly generated HTML files in your browser to view the different Question API states.${reset}"
