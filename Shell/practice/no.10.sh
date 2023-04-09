#!/bin/bash

# read -p "Enter your number: " num

# if [ $n -eq 1 ]; then
#     echo "No"
# elif [ $n -eq 0 ]; then
#     echo "No"
# else
#     for i in {2..$((num - 1))}
#     do
#         result=$(($num % $i))
#         if [ $result -eq 0 ]; then
#             echo "No"
#             return 1
#         else
#             return 0
#         fi

#         ret=$?
#         if [ ${ret} -eq 1 ]; then
#             exit 1
#         fi
#     done
# fi

read -p "Enter your number: " num
flag=0

for ((i=2; i<=num-1; i++))
do
    if [ $(($num % $i)) -eq 0 ]; then
        flag=1
        break
    fi
done

if [ $flag -eq 0 ]; then
    echo "n is sosuu"
else
    echo "n is not sosuu"
fi


