#!/bin/bash

read -p "Enter your file name: " file

if [ -e ${file} ]; then
    echo "file exists."
else
    echo "file don't exist."
fi