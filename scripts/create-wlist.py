#!/usr/bin/python3

'''
ECE 198: Special Problems in Electronics and Communications Engineering
DSP01 - A hybrid grapheme-to-phoneme and speech recognition system for automated phonetic transcription of speech data in Tagalog, Cebuano, and Hiligaynon
2014-06313 Aquino, Angelina A.
2014-06489 Tsang, Joshua Lijandro L.
'''

'''
< create-wlist.py >
creates a wordlist file using vocabulary from LOG files
'''

from g2p_parsing import *

if __name__ == '__main__':

    log_test = "log-test-files.txt"
    wlist_name = "test.wlist"

    utt_lookup = dict()
    wlist = dict()

    with open(log_test, 'r') as log_test_file, \
    open(wlist_name, 'w') as wlist_file:

        for line in log_test_file:
            utt_lookup.update(clean_utt(log2utt(line.strip())))

        wlist.update(utt2wlist(utt_lookup))

        for word in wlist.keys():
            wlist_file.write(word + '\n')
