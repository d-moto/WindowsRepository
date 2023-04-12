#!/bin/bash

#read -p "Enter your string: " s

s="abff4c123d5ef45623456"
echo $(echo $s | grep -o "[0-9]" | head -1)
echo $(echo $s | grep -o "[0-9]")
