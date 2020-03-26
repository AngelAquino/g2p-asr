#!/bin/bash

SEARCH_PATH="../data/_small/adapt/ALL"

counter(){
    for file in "$1"/*
    do
        if [ -d "$file" ]
        then
            counter "$file"
        else
            if [ "${file: -4}" == ".fin" ]
            then
                echo "$file"
            fi
        fi
    done
}

counter "$SEARCH_PATH" > adapted-output-files.txt
