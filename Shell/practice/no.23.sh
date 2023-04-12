#!/bin/bash

array=(1 2 3 4 5 6 7 8 5)

n=${#array[@]}
is_n=$(( n % 2 ))
if [ $is_n -eq 0 ]; then
    n_=$((${#array[@]} / 2))
    center_num=$(((${array[$n_]} + ${array[$(($n_ + 1))]}) / 2))
    echo $center_num
else
    echo "else"
fi