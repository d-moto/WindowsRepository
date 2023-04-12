#!/bin/bash

s="aaabbcvcccckdddfvvdsdddsllliieieiiiiiiiii"
echo $s | grep -o . | sort | uniq -c | sort -rn | head -1 | awk '{ print $2 }'