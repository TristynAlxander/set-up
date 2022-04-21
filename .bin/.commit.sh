#!/bin/bash
# To-Do: Check USB Sticks
# To-Do: What about non-directory commits? 
sudo echo "..."
# Temporary Protein-Related Files
find . -name "*.pdb1"      -type f -delete
# Temporary Code-Related Files
find . -name "*.pyc"       -type f -delete
# Cache Directories
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name ".cache"      -type d -exec rm -rf {} +
# Temporary Directories
find . -name "temp"        -type d -exec rm -rf {} +
find . -name "*.temp.*"    -type d -exec rm -rf {} +
find . -name "*.temp"      -type d -exec rm -rf {} +
find . -name "*_temp"      -type d -exec rm -rf {} +
# Temporary Files
find . -name "*.temp.*"    -type f -delete
find . -name "*.temp"      -type f -delete
find . -name "*_temp"      -type f -delete
# Create .gitignore
cp $PREF_BIN/.gitignore .gitignore
# Ignore Symlinks
find . -type l >> .gitignore
# Git
git add -A
git commit -m "$(date +%Y_%m_%d_%H_%M_%S)"
git push origin
#if [ -d "/media/tristin/backup/repos/" ]; then sudo git push backup; fi
# Delete .gitignore
rm .gitignore