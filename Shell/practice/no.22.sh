#!/bin/bash

fibonacci() {
    if [ $1 -le 0 ]; then
        echo 0
    elif [ $1 -eq 1 ]; then
        echo 1
    else
        a=0
        b=1
        for i in $(seq 2 $1)
        do
            c=$((a + b))
            a=$b
            b=$c
        done
        echo $b
    fi
}

read -p "Enter your number: " num
echo "The $num-th Fibonacci number is $(fibonacci $num)"
