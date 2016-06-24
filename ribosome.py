import re

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
        if amino_acid != '*': # Fix this to read through STOP
            peptide += amino_acid
        else:
            break

    return peptide

# User input prompt and verification
filename = raw_input("Enter the relative filepath: ")
sequence_file = open(filename,"r")
dna_seq = sequence_file.read()
sequence_file.close()
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
amino_acids = 'FFLLSSSSYY--CC-WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

peptide = translate(rna_seq)

peptide_text = open("peptide.txt","w")
peptide_text.write(peptide)
peptide_text.close()

print("RNA sequence: " + rna_seq + "\n" + "Amino acid sequence: " + peptide)
