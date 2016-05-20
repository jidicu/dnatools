def rna2dna(rna_seq):
    dna_seq = rna_seq.replace('U','T')
    print(dna_seq)

def dna2rna(dna_seq):
    rna_seq = dna_seq.replace('T','U')
    print(rna_seq)
# RNA sequence that you want to make into DNA:
rna2dna("AUGAUGCUC")

# DNA sequence you want to make into RNA:
dna2rna("ATCGCTAGCTAC")
