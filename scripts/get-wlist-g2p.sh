#!/bin/bash

MODEL_FILE="train/model.fst"
WLIST_FILE="test.wlist"
WLIST_G2P_FILE="wlist-g2p.txt"

phonetisaurus-apply --model "$MODEL_FILE" \
    --word_list "$WLIST_FILE" > "$WLIST_G2P_FILE"
