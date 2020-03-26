#!/usr/bin/python3

'''
ECE 198: Special Problems in Electronics and Communications Engineering
DSP01 - A hybrid grapheme-to-phoneme and speech recognition system for automated phonetic transcription of speech data in Tagalog, Cebuano, and Hiligaynon
2014-06313 Aquino, Angelina A.
2014-06489 Tsang, Joshua Lijandro L.
'''

'''
< adapt-g2p-asr.py >
aligns G2P and ASR transcriptions, and makes permissible edits
'''

from g2p_parsing import *
from alignment import *

if __name__ == "__main__":

    g2p_list = "csv-test-files.txt"
    asr_list = "asr-output-files.txt"

    adapted_output = ""

    g2p_lookup = dict()
    asr_lookup = dict()

    sub_pairs = [   ['e','i'], ['i','e'], ['o','u'], ['u','o'], ['r','er'], \
                    ['er','r']                                              ]
    ins_pairs = [   [['*','V'], ['q','V']], \
                    [['V','*','V'], ['V','q','V']], \
                    [['V','*'], ['V','q']], \
                    [['ch','*'], ['t','i']], \
                    [['ch','*','*'], ['t','i','y']], \
                    [['sh','*'], ['s','i']], \
                    [['sh','*','*'], ['s','i','y']], \
                    [['jh','*'], ['d','i']], \
                    [['jh','*','*'], ['d','i','y']], \
                    [['ny','*','*'], ['n','i','y']], \
                    [['*','ch'], ['t','i']], \
                    [['*','*','ch'], ['t','i','y']], \
                    [['*','sh'], ['s','i']], \
                    [['*','*','sh'], ['s','i','y']], \
                    [['*','jh'], ['d','i']], \
                    [['*','*','jh'], ['d','i','y']], \
                    [['*','*','ny'], ['n','i','y']]                         ]

    with open(g2p_list, 'r') as g2p_list_file, \
    open(asr_list, 'r') as asr_list_file:

        for line in g2p_list_file:
            clean_csv(line.strip())
            g2p_lookup.update(trxn2phon(csv2trxn(line.strip())))

        for line in asr_list_file:
            asr_lookup.update(asr2phon(line.strip()))
            adapted_output = '.'.join(line.strip().split('.')[:-1]) + '.fin'

    with open(adapted_output, 'w') as adapted_output_file:

        for key in asr_lookup.keys():
            # if key not in g2p_lookup.keys():
            #     continue

            g2p_trxn = g2p_lookup[key]
            asr_trxn = asr_lookup[key]

            align_out = align_trxn(g2p_trxn, asr_trxn)

            g2p_aligned = align_out[0]
            asr_aligned = align_out[1]

            adapted = g2p_aligned   # default realization

            for i in range(len(g2p_aligned)):
                for sub in sub_pairs:
                    if (g2p_aligned[i] == sub[0]) and (asr_aligned[i] == sub[1]):
                        adapted[i] = asr_aligned[i]

                for ins in ins_pairs:
                    if (i + len(ins[0]) <= len(g2p_aligned)):
                        ins0 = ''.join(ins[0])
                        ins1 = ''.join(ins[1])
                        str0 = ''.join(g2p_aligned[i:i+len(ins[0])])
                        str1 = ''.join(asr_aligned[i:i+len(ins[0])])

                        if (ins0 == str0) and (ins1 == str1):
                            for j in range(len(ins[0])):
                                adapted[i+j] = asr_aligned[i+j]

                        # vowel adaptation
                        # reverse transform (t i y --> ch)

            while '*' in adapted:
                adapted.remove('*')

            adapted_output_file.write(key + ' ' + ' '.join(adapted) + '\n')
