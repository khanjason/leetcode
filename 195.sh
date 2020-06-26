#!/bin/bash
# Read from the file file.txt and output the tenth line to stdout.
input="file.txt"
COUNT=0
while IFS= read -r line
do
    ((COUNT=COUNT+1))
    if [ $COUNT == 10 ]; then
  echo "$line"
  fi
  
done < "$input"