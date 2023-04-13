#!/bin/bash

a=1
b=2
c=3
array=(100 20 30 40)
str="111kdfa9d9f9aj2ojaf8i2"

echo $(( 2 + 2 ))
echo $(( a + b ))
echo $(( a + c / 2))
echo "(( 2 + 2 ))"
echo "$(( 2 + 2 ))"
echo $(( array ))
echo $array[@]
echo ${array[@]}
echo ${#array[@]}
echo ${#array}
echo ${#str}