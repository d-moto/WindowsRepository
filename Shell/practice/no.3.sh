#!/bin/bash

read -p "Enter your number: " n

if [ $n -gt 0 ]; then
    echo "n is a even number."
elif [ $n -eq 0 ]; then
    echo "n is a zero."
elif [ $n -lt 0 ]; then
    echo "n is a odd number."
else
    echo "n is a not number"
fi