#!/bin/bash
# Checks
command -v pdf2svg  >/dev/null 2>&1 || { echo >&2 "Failed, Try: apt-get install pdf2svg. Aborting.";      sleep 30; exit 1; }
command -v pdflatex >/dev/null 2>&1 || { echo >&2 "Failed, Try: apt-get install texlive-full. Aborting."; sleep 30; exit 1; }
command -v pdfcrop  >/dev/null 2>&1 || { echo >&2 "Failed, Try: apt-get install texlive-full. Aborting."; sleep 30; exit 1; }
# Create Temp Directory
if [ ! -d ./temp ]; then mkdir ./temp; fi
# Conversions
pdflatex --interaction=batchmode -jobname temp/latex.temp $1 > /dev/null
pdfcrop --margins 1 temp/latex.temp.pdf temp/crop.pdf > /dev/null
pdf2svg temp/crop.pdf $2  > /dev/null
# Delete Temp Directory
rm -r temp/
