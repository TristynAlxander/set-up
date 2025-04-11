#!/bin/bash
for file in $(find ./ -type f); do
  if [[ "$file" == *.svg ]]; then
    new_file=$(echo "$file" | sed 's/svg/png/g')
    mkdir -p $(dirname $new_file)
    inkscape --export-type="png" --export-filename=$new_file $file
  fi
done