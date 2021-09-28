#!/bin/bash
# Hard Links
command -v hardlink >/dev/null 2>&1 || { echo >&2 "Failed, Try: apt-get install hardlink. Aborting."; exit 1; }
hardlink -v -c ./ ./
find ./ -name "*.hardlink-temporary" -type f -delete
