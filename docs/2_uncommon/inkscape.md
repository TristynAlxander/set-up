# Inkscape

    sudo apt install inkscape
    sudo apt install ffmpeg

inkscape > Edit > Preferences > Behaviour > Transforms > [deselect] "Scale stroke width" 

## Inkscape Command Line

inkscape --export-type="png" my_file.svg

inkscape --export-type="png" --export-filename=my_file.png my_file.svg 


for file in $(find ./ -type f); do
  if [[ "$file" == *.svg ]]; then
    inkscape --export-type="png" --export-filename="${file%.svg}.png" $file
  fi
done

!# 
for file in $(find ./ -type f); do
  if [[ "$file" == *.svg ]]; then
    new_file=$(echo "$file" | sed 's/svg/png/g')
    mkdir -p $(dirname $new_file)
    inkscape --export-type="png" --export-filename=$new_file $file
  fi
done
  

