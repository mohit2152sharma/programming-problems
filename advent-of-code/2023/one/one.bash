#!/usr/bin/env bash

# read a file
sum=0
while read -r line; do
	first_number=$(echo "$line" | grep -oE "\d" | head -n 1)
	last_number=$(echo "$line" | grep -oE "\d" | tail -n 1)
	x="$first_number""$last_number"
	((sum += x))
done <lines.txt

echo $sum
