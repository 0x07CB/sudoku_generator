#!/bin/bash

# Install requirements
# check if is into a virtual environment
if [[ $VIRTUAL_ENV == "" ]]
then
    echo "You are not into a virtual environment. Please activate it before running this script."
    exit 1
else
    python3 -m pip install -r requirements.txt
fi
