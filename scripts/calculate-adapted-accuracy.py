#!/usr/bin/python3

'''
ECE 198: Special Problems in Electronics and Communications Engineering
DSP01 - A hybrid grapheme-to-phoneme and speech recognition system for automated phonetic transcription of speech data in Tagalog, Cebuano, and Hiligaynon
2014-06313 Aquino, Angelina A.
2014-06489 Tsang, Joshua Lijandro L.
'''

'''
< calculate-adapted-accuracy.py >
compares the edit distance of adapted transcriptions against manually-verified transcriptions
'''

from g2p_parsing import *
from alignment import *

if __name__ == "__main__":

    test_list = "adapted-output-files.txt"
    ref_list = "csv-testref-files.txt"

    test_lookup = dict()
    ref_lookup = dict()

    total_ref_phones = 0
    total_edit_distance = 0

    with open(test_list, 'r') as test_list_file, \
    open(ref_list, 'r') as ref_list_file:

        for line in test_list_file:
            test_lookup.update(asr2phon(line.strip()))

        for line in ref_list_file:
            clean_csv(line.strip())
            ref_lookup.update(trxn2phon(csv2trxn(line.strip())))

        for key in test_lookup.keys():
            test_trxn = test_lookup[key]
            ref_trxn = ref_lookup[key]

            total_ref_phones += len(ref_trxn)

            align_out = align_trxn(test_trxn, ref_trxn)
            total_edit_distance += align_out[2]

    print('total phones in reference:', total_ref_phones)
    print('total edit distance:      ', total_edit_distance)
    print('phone error rate:         ', total_edit_distance / total_ref_phones)
