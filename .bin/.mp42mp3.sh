#!/bin/bash

# Rename files with space in them
if compgen -G "*\ *" > /dev/null; then
    echo "Replacing Spaces in file names..."
    for f in *\ *; do mv "$f" "${f// /_}"; done
fi

# Proper Encoding for mp3s
# Some mp3s are actually m4as, you can look at the ffmpeg output that describes the input
for filename in ./*.mp3; do
  mv $filename $(basename "$filename" .mp3).m4a
done

# m4a conversions
for filename in ./*.m4a; do
  ffmpeg -i $filename -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 $(basename "$filename" .m4a).mp3
done
rm ./*.m4a

# Mp4 conversions
for filename in ./*.mp4; do
  ffmpeg -i $filename -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 $(basename "$filename" .mp4).mp3
done
rm ./*.mp4

# Mb4 conversions
for filename in ./*.mb4; do
  ffmpeg -i $filename -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 $(basename "$filename" .mb4).mp3
done
rm ./*.mb4

# wma conversions (needs to be checked)
for filename in ./*.wma; do
  ffmpeg -i $filename -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 $(basename "$filename" .wma).mp3
done
#rm ./*.wma






