#!/bin/bash

array=("apple" "banana" "grape" "aaa" "diifg")
sorted=($(echo ${array[@]} | tr ' ' '\n' | sort))
echo ${sorted[@]}
