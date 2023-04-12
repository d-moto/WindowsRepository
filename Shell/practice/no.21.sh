#!/bin/bash

array=(22 9 123 78 5)

sorted_array=($(echo ${array[@]} | tr ' ' '\n' | sort -n))
sum=0
for ((i=1; i<${#sorted_array[@]}; i+=2))
do
    sum=$((sum + sorted_array[i]))
done
echo $sum

