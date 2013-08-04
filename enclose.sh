#!/bin/bash

# a short script that puts all files of specified types in a specified directory into subdirectories with the name of that file
# usage: enclose.sh directory "ext" [ "ext" ... ]

EXTENSION=""
DIRNAME=""

if [ $# -lt 2 ]; then
    echo "usage: enclose.sh DIRNAME \"EXTENSION\" [ \"EXTENSION\" ... ]"
    echo " eg. $ enclose.sh /path/to/dir \"txt\" \"py\""
    exit 1    
fi

DIRNAME="$1"
shift

for EXTENSION in $@
do
    for FILE in `ls $DIRNAME`
    do
        # echo $FILE
        if [[ "${FILE##*.}" == "${EXTENSION}" ]]; then
            if [ ! -d "${DIRNAME}/${FILE%%.*}" ]; then
                mkdir "${DIRNAME}/${FILE%%.*}"
            fi
            mv "${DIRNAME}/${FILE}" "${DIRNAME}/${FILE%%.*}"
        fi
    done
done

exit 0