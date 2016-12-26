import re

# test comment + commit

# class AminoAcid:
#     abbrev = ""
#     codon = ""
#     name = ""
#
#     def __init__(abbrev, codon, name):
#         self.abbrev = abbrev
#         self.codon = codon
#         self.name = name
#
# # TODO Add polarity, charge, etc

def translate(rna_seq):# Actual translation
    rna_seq = rna_seq.upper().replace('\n', '').replace(' ', '')
    peptide = ''

    for i in xrange(0, len(rna_seq), 3):
        codon = rna_seq[i: i+3]
        amino_acid = codon_table.get(codon, '*')
        if amino_acid != '*':
            peptide += amino_acid
        else:
            break

    return peptide

# User input prompt and verification
dna_seq = raw_input("Enter your sequence: ")
allowed_char = re.compile(r"a|c|t|g|u|A|T|C|G|U")
if not allowed_char.findall(dna_seq):
    print("You did not enter a valid sequence. Restart the program and try again.")
    raise SystemExit
if len(dna_seq)%3 != 0:
    print("You did not enter a sequence consisting only of codons. Restart the program and try again.")
    raise SystemExit
dna_seq = dna_seq.upper()
rna_seq = dna_seq.replace("T","U")

# Initialize codon dictionary
bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

peptide = translate(rna_seq)

print("RNA sequence: " + rna_seq + "\n" + "Amino acid sequence: " + peptide)
