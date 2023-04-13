#!/bin/bash

file="no.00.sh"

lines=$(cat $file | wc -l)

echo "$lines lines"