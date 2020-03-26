#!/bin/bash

SEARCH_PATH="../data"

counter(){
    for file in "$1"/*
    do
        if [ -d "$file" ]
        then
            counter "$file"
        else
            if [ "${file: -4}" == ".log" ]
            then
                echo "$file"
                cp "$file" "../data/test"
            fi
        fi
    done
}

counter "$SEARCH_PATH" > log-files.txt
