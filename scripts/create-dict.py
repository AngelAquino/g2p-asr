#!/usr/bin/python3

'''
ECE 198: Special Problems in Electronics and Communications Engineering
DSP01 - A hybrid grapheme-to-phoneme and speech recognition system for automated phonetic transcription of speech data in Tagalog, Cebuano, and Hiligaynon
2014-06313 Aquino, Angelina A.
2014-06489 Tsang, Joshua Lijandro L.
'''

'''
< create-dict.py >
creates a pronunciation dictionary using vocabulary from LOG files and corresponding transcriptions thereof from CSV files
'''

from g2p_parsing import *

if __name__ == "__main__":
    # import operator

    log_list = "log-train-files.txt"
    csv_list = "csv-train-files.txt"
    dict_name = "train.dict"

    utt_lookup = dict()
    trxn_lookup = dict()
    utt_trxn_set = set()
    utt_trxn_list = list()


    with open(log_list, 'r') as log_list_file, \
    open(csv_list, 'r') as csv_list_file, \
    open(dict_name, 'w') as dict_file:

        for line in log_list_file:
            utt_lookup.update(clean_utt(log2utt(line.strip())))
            # print(utt_lookup)
            pass

        for line in csv_list_file:
            clean_csv(line.strip())
            trxn_lookup.update(csv2trxn(line.strip()))
            # print(trxn_lookup)
            pass

        for key in trxn_lookup.keys():
            utt = utt_lookup[key]
            trxn = trxn_lookup[key]

            if len(utt) != len(trxn):
                print(key)
                print(len(utt), utt_lookup[key])
                print(len(trxn), trxn_lookup[key])
            else:
                for i in range(len(utt)):
                    utt_trxn_set.add((utt[i], trxn[i]))

        utt_trxn_list = list(utt_trxn_set)
        utt_trxn_list.sort()

        for (utt, trxn) in utt_trxn_list:
            dict_file.write(utt + '\t' + trxn + '\n')
