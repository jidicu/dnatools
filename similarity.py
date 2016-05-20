# Levenshtein edit distance
def levenshtein(source, target):
    if len(source) < len(target):
        return levenshtein(target, source)

    # So now we have len(source) >= len(target).
    if len(target) == 0:
        return len(source)

    # We call tuple() to force strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    source = np.array(tuple(source))
    target = np.array(tuple(target))

    # We use a dynamic programming algorithm, but with the
    # added optimization that we only need the last two rows
    # of the matrix.
    previous_row = np.arange(target.size + 1)
    for s in source:
        # Insertion (target grows longer than source):
        current_row = previous_row + 1

        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))

        # Deletion (target grows shorter than source):
        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)

        previous_row = current_row

    return previous_row[-1]

# Dice coefficient
""" duplicate bigrams in a word should be counted distinctly
(per discussion), otherwise 'AA' and 'AAAA' would have a
dice coefficient of 1...
"""
def dice_coefficient(seq1,seq2):
    if not len(seq1) or not len(seq2): return 0.0
    """ quick case for true duplicates """
    if seq1 == seq2: return 1.0
    """ if seq1 != seq2, and seq1 or seq2 are single chars, then they can't possibly match """
    if len(seq1) == 1 or len(seq2) == 1: return 0.0

    """ use python list comprehension, preferred over list.append() """
    seq1_bigram_list = [seq1[i:i+2] for i in range(len(seq1)-1)]
    seq2_bigram_list = [seq2[i:i+2] for i in range(len(seq2)-1)]

    seq1_bigram_list.sort()
    seq2_bigram_list.sort()

    # assignments to save function calls
    lenseq1 = len(seq1_bigram_list)
    lenseq2 = len(seq2_bigram_list)
    # initialize match counters
    matches = i = j = 0
    while (i < lenseq1 and j < lenseq2):
        if seq1_bigram_list[i] == seq2_bigram_list[j]:
            matches += 2
            i += 1
            j += 1
        elif seq1_bigram_list[i] < seq2_bigram_list[j]:
            i += 1
        else:
            j += 1

    score = float(matches)/float(lenseq1 + lenseq2)
    return score
