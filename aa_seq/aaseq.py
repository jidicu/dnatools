import re

class AminoAcid
    abbrev = ""
    codon = ""
    name = ""

    def __init__(abbrev, codon, name):
        self.abbrev = abbrev
        self.codon = codon
        self.name = name

# TODO Add polarity, charge, etc

dna_seq = raw_input("Enter your sequence.")
allowed_char = re.compile(r"a|c|t|g|u|A|T|C|G|U")
if not allowed_char.findall(dna_seq):
    print("You did not enter a valid sequence.")
dna_seq = dna_seq.upper()
rna_seq = dna_seq.replace("T","U")

def codons(rna_seq, 3):
    return [ rna_seq[start:start+3] for start in range(0, len(rna_seq), 3) ]
