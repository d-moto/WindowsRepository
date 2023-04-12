#!/bin/bash

read -p "Enter your number: " num

flag=true
if [ $num -gt 2 ]; then
    for ((i=2; i<=$(echo "sqrt($num)" | bc); i++ ))
    do
        if [ $(($num % $i)) -eq 0 ]; then
            flag=false
            break
        fi
    done
    if $flag; then
        echo "${num} is sosuu"
    else
        echo "${num} is not sosuu"
    fi
else
    echo "${num} is not sosuu"
fi
