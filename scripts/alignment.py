'''
ECE 198: Special Problems in Electronics and Communications Engineering
DSP01 - A hybrid grapheme-to-phoneme and speech recognition system for automated phonetic transcription of speech data in Tagalog, Cebuano, and Hiligaynon
2014-06313 Aquino, Angelina A.
2014-06489 Tsang, Joshua Lijandro L.
'''

def align_trxn(seqA, seqB):
    """Returns two aligned transcriptions (each a list of phones) and their edit distance given two unaligned transcriptions."""

    lenA = len(seqA)
    lenB = len(seqB)

    score_matrix        = [[0 for _ in range(lenB+1)] for _ in range(lenA+1)]
    traceback_matrix    = [[0 for _ in range(lenB+1)] for _ in range(lenA+1)]

    # define substitution scores and gap penalty
    match       = +1
    mismatch    = -1
    gap         = -1

    # initialize scoring matrix
    for i in range(lenA+1):
        score_matrix[i][0] = i*gap  # rows: seqA
    for j in range(lenB+1):
        score_matrix[0][j] = j*gap  # cols: seqB

    # fill scoring matrix
    for i in range(1, lenA+1):
        for j in range(1, lenB+1):
            if seqA[i-1] == seqB[j-1]:
                score = match
            else:
                score = mismatch

            # final score choices
            aligned     = score_matrix[i-1][j-1] + score
            deleted     = score_matrix[i-1][j  ] + gap
            inserted    = score_matrix[i  ][j-1] + gap

            score_matrix[i][j] = max(aligned, deleted, inserted)

            if score_matrix[i][j] == aligned:
                traceback_matrix[i][j] = 0  # phones i and j aligned
            elif score_matrix[i][j] == deleted:
                traceback_matrix[i][j] = 1  # gap in seqB
            elif score_matrix[i][j] == inserted:
                traceback_matrix[i][j] = -1 # gap in seqA

    # print(score_matrix)

    # get aligned sequences from traceback matrix
    i, j = lenA, lenB
    alnseqA, alnseqB = list(), list()
    edit_distance = 0

    while (i > 0 and j > 0):
        if traceback_matrix[i][j] == 0:
            alnseqA.append(seqA[i-1])
            alnseqB.append(seqB[j-1])
            if seqA[i-1] != seqB[j-1]:
                edit_distance += 1
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == 1:
            alnseqA.append(seqA[i-1])
            alnseqB.append('*')
            edit_distance += 1
            i -= 1
        elif traceback_matrix[i][j] == -1:
            alnseqA.append('*')
            alnseqB.append(seqB[j-1])
            edit_distance += 1
            j -= 1
    while i > 0:
        alnseqA.append(seqA[i-1])
        alnseqB.append('*')
        edit_distance += 1
        i -= 1
    while j > 0:
        alnseqA.append('*')
        alnseqB.append(seqB[j-1])
        edit_distance += 1
        j -= 1

    # reverse sequences to original orders
    alnseqA = alnseqA[::-1]
    alnseqB = alnseqB[::-1]

    # print(alnseqA)
    # print(alnseqB)
    # print('edit distance: ', edit_distance)
    return [alnseqA, alnseqB, edit_distance]
