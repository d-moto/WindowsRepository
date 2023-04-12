#!/bin/bash

array=(
    10
    20
    30
    90
    40
    33
    2
    409
    8
)

num=${#array[@]}
max=0

for ((i=0; i<${#array[@]}; i++))
do
    if [ ${max} -gt ${array[$i]} ]; then
        :
    else
        max=${array[i]}
    fi
done

echo $max