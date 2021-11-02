#!/bin/bash

# check $TEMPLATES is set

if [ '$1' == *.eqn.tex ]; then
  cp $TEMPLATES/template.eqn.tex ./$1
elif [ '$1' == *.graph.svg ]; then
  cp $TEMPLATES/template.graph.svg ./$1
elif [ '$1' == *.slide.svg ]; then
  cp $TEMPLATES/template.slide.svg ./$1
else
  touch $1
# 
# "$1" == *.eqn.svg
# 

# Copy from note templates
# Check if in notes
#
#
#

# maybe a command like help but for common grep,awk,sed commands?
