#!/bin/bash
for filename in ./*.mp4; do
  ffmpeg -i $filename -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 $(basename "$filename" .mp4).mp3
done
rm ./*.mp4