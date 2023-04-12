#!/bin/bash

read -p "Enter your number: " n

total=1
for ((i=1; i<=${n}; i++))
do
    total=$(($total * $i))
done
echo ${total}
