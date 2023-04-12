#!/bin/bash

read -p "Enter your file name: " file

if [ -f ${file} ]; then
    cat ${file}
    echo ""
else
    echo "no such file or directory"
fi
