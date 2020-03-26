#!/usr/bin/python3

'''
ECE 198: Special Problems in Electronics and Communications Engineering
DSP01 - A hybrid grapheme-to-phoneme and speech recognition system for automated phonetic transcription of speech data in Tagalog, Cebuano, and Hiligaynon
2014-06313 Aquino, Angelina A.
2014-06489 Tsang, Joshua Lijandro L.
'''

'''
< create-trxn.py >
encodes CSV file transcriptions of utterances in LOG files using a dictionary containing words and G2P-generated pronunciations
'''

from g2p_parsing import *

if __name__ == '__main__':

    log_test = "log-test-files.txt"
    wlist_g2p_name = "wlist-g2p.txt"

    utt_lookup = dict()
    trxn_lookup = dict()
    wlist_g2p = dict()

    csv_files = list()

    with open(log_test, 'r') as log_test_file, \
    open(wlist_g2p_name, 'r') as wlist_g2p_file:

        for line in log_test_file:
            utt_lookup.update(clean_utt(log2utt(line.strip())))

            csv_files.append('.'.join(line.split('.')[:-1]) + '.csv')

        for line in wlist_g2p_file:
            pair = line.strip().split('\t')
            wlist_g2p[pair[0]] = pair[1]

        trxn_lookup.update(utt2trxn(utt_lookup, wlist_g2p))

        for csv_address in csv_files:
            trxn2csv(trxn_lookup, csv_address)
