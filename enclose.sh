#!/bin/bash

# a short script that puts all files of specified types in a specified directory into subdirectories with the name of that file
# usage: enclose.sh directory ext [ ext ... ]

if [ $# -lt 2 ]; then
    echo "usage: enclose.sh directory extension [ extension ... ]"
    echo " eg. $ enclose.sh /path/to/dir txt py"
    exit 1    
fi

dir="$1"
shift
extensions=( $@ )

for file in $dir/*
do

    for i in "${extensions[@]}"
    do
        filename=$(basename "$file")
        ext="${filename##*.}"
        filename="${filename%.*}"
        if [ "$i" = $ext ] ; then
            # echo "$filename"
            if [ ! -d "${dir}/${filename%.*}" ]; then
                mkdir "${dir}/${filename%.*}"
            fi
            mv $file "${dir}/${filename%.*}"
        fi
    done
done

exit 0