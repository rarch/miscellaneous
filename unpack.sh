#!/bin/bash

# a short script that unpacks a directory. the inverse to enclose.sh:
#   it takes all files in a directory that start with the same name as the directory,
#   moves these files to the enclosing directory, and removes the directory if it is empty
# usage: unpack.sh directory "ext" [ "ext" ... ]

if [ $# -lt 1 ]; then
    echo "usage: unpack.sh  directory [ directory ... ]"
    echo " eg. $ unpack.sh /path/to/dir /path/to/second/dir"
    exit 1    
fi

directories=( $@ )
COUNTER=0

for dir in "${directories[@]}"
do
    if [ -d "${dir}" ]; then
        dirname=$(basename "$dir")
        for file in $dir/*
        do
            filename=$(basename "$file")
            filename="${filename%.*}"
            if [ "$filename" = "$dirname" ]; then
                mv $file $dir/..
            fi
        done

        if [ ! "$(ls -A $dir)" ]; then
            rmdir $dir
        fi
    else
        echo invalid directory $dir
        COUNTER=$[$COUNTER +1]
    fi
done

exit $COUNTER