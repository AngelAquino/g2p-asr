#!/bin/bash

SEARCH_PATH="../data"

counter(){
    for file in "$1"/*
    do
        if [ -d "$file" ]
        then
            counter "$file"
        else
            if [ "${file: -4}" == ".csv" ]
            then
                echo "$file"
            fi
        fi
    done
}

counter "$SEARCH_PATH" > csv-files.txt
