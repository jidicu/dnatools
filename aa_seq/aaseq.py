import re

class AminoAcid:
    abbrev = ""
    codon = ""
    name = ""

    def __init__(abbrev, codon, name):
        self.abbrev = abbrev
        self.codon = codon
        self.name = name

# TODO Add polarity, charge, etc

def codons(rna_seq): # This method splits an input into a list of codons.
    return [ rna_seq[start:start+3] for start in range(0, len(rna_seq), 3) ]

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
print(codons(rna_seq))
