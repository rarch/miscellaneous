#!/bin/bash

# a short script that unpacks a directory. the inverse to enclose.sh:
#   it takes all files in a directory that start with the same name as the directory,
#   moves these files to the enclosing directory, and removes the directory if it is empty
# usage: unpack.sh directory "ext" [ "ext" ... ]

if [ $# -lt 1 ]; then
    echo "usage: unpack.sh  \"DIRECTORY\" [ \"DIRECTORY\" ... ]"
    echo " eg. $ unpack.sh /path/to/dir /path/to/second/dir"
    exit 1    
fi

for DIRNAME in $@
do
    # check for valid directory
    if [ -d "${DIRNAME}" ];
    then
        for FILE in `ls $DIRNAME`
        do
            # file name matches directory name, so remove file
            if [[ "${FILE%%.*}" == `basename $DIRNAME` ]]; then
                mv "${DIRNAME}/${FILE}" "${DIRNAME}/../${FILE}" 
            fi
        done

        # if directory is empty, delete it
        if [ ! "$(ls -A $DIRNAME)" ]; then
            rmdir $DIRNAME
        fi

    else
        echo invalid directory ${DIRNAME}
    fi 

done

exit 0