'''
ECE 198: Special Problems in Electronics and Communications Engineering
DSP01 - A hybrid grapheme-to-phoneme and speech recognition system for automated phonetic transcription of speech data in Tagalog, Cebuano, and Hiligaynon
2014-06313 Aquino, Angelina A.
2014-06489 Tsang, Joshua Lijandro L.
'''

def asr2phon(asr_address):
    """Extracts a dictionary of phone transcriptions (each defined as a list of phones) from a formatted Kaldi ASR output file."""
    phon_lookup = dict()

    with open(asr_address, 'r') as asr_file:
    
        for line in asr_file:
            split_line = line.strip().split(' ')
            
            if split_line[0].replace('.','').isdigit():
                phon = [x.lower() for x in split_line[1:]]
                phon_lookup[split_line[0]] = phon

    return phon_lookup

def trxn2phon(trxn_lookup):
    """Converts entries in a dictionary of utterance transcriptions (each defined as a list of words with space-separated phones) to a list of phones."""

    phon_lookup = dict()

    for key in trxn_lookup.keys():
        phon_str = ' '.join(trxn_lookup[key])
        phon = phon_str.strip().split(' ')
        phon_lookup[key] = phon

    return phon_lookup

def log2utt(log_address):
    """Creates a dictionary of utterances from a formatted .log file."""
    import re

    utt_lookup = dict()

    with open(log_address, 'r') as log_file:

        for line in log_file:
            split_line = line.strip().split(' ')
            if split_line[0][-4:] == '.wav':
                wav_file = split_line[0]
                # src_file = split_line[1]  ---> to fix: exception "Random Digit"

                str = ' '.join(split_line[1:])
                split_str = str.strip().split('\"')
                utt_trxn = ' '.join(split_str[3:])

                # wav_file: [\d\.]*\.wav    ---> remove .wav extension
                # utt_trxn: ".*"            ---> remove enclosing quotation marks
                utt_lookup[wav_file[:-4]] = utt_trxn

    return utt_lookup

def clean_utt(utt_lookup):
    """Normalizes text in a dictionary of utterances."""
    import unidecode    # remove accents from characters
    import re, string   # regex parsing

    for key in utt_lookup.keys():
        utt = utt_lookup[key]

        # convert to lowercase ASCII estimate
        utt = unidecode.unidecode(utt).lower()

        # remove parenthesized strings
        utt = re.sub('\(.*?\)', '', utt)

        # replace ampersands with 'and'
        utt = re.sub('&', 'and', utt)

        # remove non-alphanumerics except '-' and whitespace
        utt = re.sub('[^A-Za-z0-9\s-]+', '', utt)
        utt = re.sub('--+', '', utt)

        # replace consecutive whitespace with single space
        utt = re.sub('\s+', ' ', utt)

        utt_lookup[key] = [x.strip() for x in utt.strip().split(' ')]

    return utt_lookup

def utt2wlist(utt_lookup):
    """Creates a dictionary of words from a dictionary of utterances."""
    wlist = dict()

    for key in utt_lookup.keys():
        utt = utt_lookup[key]

        for word in utt:
            if not any(c.isdigit() for c in word):
                wlist[word] = ''

    return wlist

def utt2trxn(utt_lookup, wlist_g2p):
    """Creates a dictionary of utterance transcriptions (each defined as a list of words with space-separated phones) from a dictionary of utterances."""
    trxn_lookup = dict()

    for key in utt_lookup.keys():
        utt = utt_lookup[key]
        trxn = list()

        for i in range(len(utt)):
            if utt[i] in wlist_g2p:
                trxn.append(wlist_g2p[utt[i]])
            else:
                trxn.append('#')

        trxn_lookup[key] = trxn

    return trxn_lookup

def csv2trxn(csv_address):
    """Extracts a dictionary of utterance transcriptions (each defined as a list of words with space-separated phones) from a formatted CSV transcription file."""
    trxn_lookup = dict()

    with open(csv_address, 'r') as csv_file:

        for line in csv_file:
            split_line = line.strip().split(',')
            utt_id = '.'.join(split_line[1:4])

            trxn = [x.strip() for x in split_line[4].strip().split('_')]

            trxn_lookup[utt_id] = trxn

    return trxn_lookup

def trxn2csv(trxn_lookup, csv_address):
    """Creates a formatted CSV transcription file from a dictionary of utterance transcriptions."""
    with open(csv_address, 'w') as csv_file:

        add = '/'.join(csv_address.split('/')[:-1])
        spk_sess = '.'.join(csv_address.split('/')[-1].split('.')[:-1])

        for key in trxn_lookup.keys():
            key_ls = key.split('.')
            spk_id = key_ls[0]
            sess_id = '.'.join(key_ls[1:3])
            utt_id = key_ls[3]

            if spk_sess != (spk_id + '.' + sess_id):
                continue

            trxn = trxn_lookup[key]
            trxn_string = ' _ '.join(trxn)

            line = ','.join([add, spk_id, sess_id, utt_id, trxn_string])
            csv_file.write(line + '\n')

def clean_csv(csv_address):
    """Formats edited CSVs to restore speaker, session, and utterance IDs."""
    csv_file = csv_address.strip().split('/')[-1]
    csv_ids = csv_file.split('.')
    new_lines = list()

    with open(csv_address, 'r') as csv_file:
        print(csv_address)
        csv_lines = csv_file.readlines()

        for line in csv_lines:
            split_line = line.strip().split(',')
            split_line[1] = csv_ids[0]
            split_line[2] = '.'.join(csv_ids[1:3])
            split_line[3] = '0'*(4-len(split_line[3])) + split_line[3]

            new_lines.append(','.join(split_line))

    with open(csv_address, 'w') as csv_file:
        for line in new_lines:
            csv_file.write(line + '\n')
