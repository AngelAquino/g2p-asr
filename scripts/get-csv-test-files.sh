#!/bin/bash

SEARCH_PATH="../data/_small/test"

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

counter "$SEARCH_PATH" > csv-test-files.txt
