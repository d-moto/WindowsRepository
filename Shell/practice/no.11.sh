#!/bin/bash

array=(
    "one"
    "two"
    "three"
)

for ((i=${#array[@]}-1; i>=0; i--))
do
    echo ${array[i]}
done